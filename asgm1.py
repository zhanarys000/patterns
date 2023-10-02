class ChoiceStrategy:
    def make_choice(self):
        pass

class RockStrategy(ChoiceStrategy):
    def make_choice(self):
        return "rock"

class ScissorsStrategy(ChoiceStrategy):
    def make_choice(self):
        return "scissors"

class PaperStrategy(ChoiceStrategy):
    def make_choice(self):
        return "paper"

class Context:
    _strategy = None

    def setStrategy(self, choice):
        if choice == "rock":
            self._strategy = RockStrategy()
        elif choice == "scissors":
            self._strategy = ScissorsStrategy()
        else:
            self._strategy = PaperStrategy()

    def executeStrategy(self):
        return self._strategy.make_choice()
    


class main():
    a = Context()
    player1_choice = input("Player 1, choose rock, scissors, or paper: ").strip().lower()
    player2_choice = input("Player 2, choose rock, scissors, or paper: ").strip().lower()

    a.setStrategy(player1_choice)
    choice1 = a.executeStrategy()
    print(f"Player 1 chose: {choice1}")


    a.setStrategy(player2_choice)
    choice2 = a.executeStrategy()
    print(f"Player 2 chose: {choice2}")

    if choice1 == choice2:
        print("Draw!")
    elif (
        (choice1 == "rock" and choice2 == "scissors")
        or (choice1 == "scissors" and choice2 == "paper")
        or (choice1 == "paper" and choice2 == "rock")
    ):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
