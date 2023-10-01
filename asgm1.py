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

player1_choice = input("Player 1, choose rock, scissors, or paper: ").strip().lower()
player2_choice = input("Player 2, choose rock, scissors, or paper: ").strip().lower()

if player1_choice == "rock":
    player1_strategy = RockStrategy()
elif player1_choice == "scissors":
    player1_strategy = ScissorsStrategy()
else:
    player1_strategy = PaperStrategy()

if player2_choice == "rock":
    player2_strategy = RockStrategy()
elif player2_choice == "scissors":
    player2_strategy = ScissorsStrategy()
else:
    player2_strategy = PaperStrategy()

choice1 = player1_strategy.make_choice()
choice2 = player2_strategy.make_choice()

print(f"Player 1 chose: {choice1}")
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
