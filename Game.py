import tkinter as tk
import random


class GameWindow:
    def __init__(self, master):
        global PC_wins
        global player_wins
        global player_name
        global total_text

        """
        Define global variables and base values
        """

        PC_wins = 0
        player_wins = 0

        player_name = tk.StringVar()
        player_name.set("Player")

        total_text = tk.StringVar()
        total_text.set(f"PC - {PC_wins}:{player_wins} - {player_name.get()}")

        self.master = master
        master.title("Rock, paper, scissors")
        master.geometry("320x200")

        """
        Define labels and texts
        """

        pc_label = tk.Label(text="PC")
        pc_label.grid(row=0, column=0, columnspan=2)

        self.user_label = tk.Label(textvariable=player_name)
        self.user_label.grid(row=0, column=4, columnspan=2)

        self.pc_choice = tk.Text(master=master, width=10, height=4, padx=10, pady=10, bg='red')
        self.pc_choice.grid(row=1, column=0, columnspan=2, rowspan=2)

        self.user_choice = tk.Text(master=master, width=10, height=4, padx=10, pady=10, bg='blue')
        self.user_choice.grid(row=1, column=4, columnspan=2, rowspan=2)

        self.winner_label = tk.Label(text="Who is the winner?")
        self.winner_label.grid(row=1, column=2, columnspan=2)

        self.total_label = tk.Label(textvariable=total_text)
        self.total_label.grid(row=2, column=2, columnspan=2)

        """
        Define game buttons
        """

        rock_button = tk.Button(master=master, text="Rock", bg="green", width=10, height=2, padx=10,
                                pady=10, command=lambda: self.game('Rock'))
        rock_button.grid(row=4, column=0, columnspan=2)

        paper_button = tk.Button(master=master, text="Paper", bg="green", width=10, height=2, padx=10,
                                 pady=10, command=lambda: self.game('Paper'))
        paper_button.grid(row=4, column=2, columnspan=2)

        scissors_button = tk.Button(master=master, text="Scissors", bg="green", width=10, height=2, padx=10,
                                    pady=10, command=lambda: self.game('Scissors'))
        scissors_button.grid(row=4, column=4, columnspan=2)

        """
        Define menu buttons
        """

        score_reset_button = tk.Button(master=master, text="Restart", bg="grey", width=5, height=1,
                                       command=self.reset_score)
        score_reset_button.grid(row=5, column=0, columnspan=2)

        close_game_button = tk.Button(master=master, text="Close", bg="grey", width=5, height=1,
                                      command=master.destroy)
        close_game_button.grid(row=5, column=2, columnspan=2)

        set_name_button = tk.Button(text="Set player name", bg="grey", width=12, height=1,
                                    command=NameWindow)
        set_name_button.grid(row=5, column=4, columnspan=2)

        master.grid_rowconfigure(3, minsize=10)

    def game(self, choice):
        """
        Getting user choice
        Changing PC_choice, user_choice, total_text label and winner_label depend on result
        """

        global PC_wins
        global player_wins
        global player_name

        game_choice = random.randint(1, 3)
        if game_choice == 1:
            game_choice = "Rock"
        elif game_choice == 2:
            game_choice = "Paper"
        else:
            game_choice = "Scissors"

        if game_choice == choice:
            winner = "Draw"
        elif game_choice == "Rock" and choice == "Paper" or game_choice == "Paper" and choice == "Scissors" or \
                game_choice == "Scissors" and choice == "Rock":
            winner = player_name.get()
            player_wins += 1
        else:
            winner = "PC"
            PC_wins += 1

        self.user_choice.delete(1.0, "end")
        self.user_choice.insert(1.0, choice)
        self.pc_choice.delete(1.0, "end")
        self.pc_choice.insert(1.0, game_choice)

        if winner == "Draw":
            self.winner_label.configure(text=winner)
        else:
            self.winner_label.configure(text=f"{winner} win!")
        total_text.set(f"PC - {PC_wins}:{player_wins} - {player_name.get()}")

    def reset_score(self):
        """
        Button command, set PC_wins and player_wins value to 0, update total_tezt
        """
        global PC_wins
        global player_wins

        player_wins = 0
        PC_wins = 0
        total_text.set(f"PC - {PC_wins}:{player_wins} - {player_name.get()}")


class NameWindow(tk.Toplevel):
    """
    TopLevel to set player name
    """
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.title("Set player name")
        self.geometry("150x100")

        user_name_label = tk.Label(master=self, text="What is your name?")
        user_name_label.grid(column=0, row=0)

        self.user_name_entry = tk.Entry(self)
        self.user_name_entry.grid(column=0, row=1)
        self.user_name_entry.focus()

        ok_button = tk.Button(master=self, text="Ok", command=self.ok_command)
        ok_button.grid(column=0, row=2)

    def ok_command(self):
        """
        Update player_name and total_text in GameWindow
        :return:
        """
        global player_name
        global total_text
        global PC_wins
        global player_wins

        user_name = self.user_name_entry.get()
        player_name.set(user_name)
        total_text.set(f"PC - {PC_wins}:{player_wins} - {player_name.get()}")
        NameWindow.destroy(self)


def main():
    root = tk.Tk()
    app = GameWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
