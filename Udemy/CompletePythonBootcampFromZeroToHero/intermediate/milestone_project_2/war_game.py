import random
from typing import Union

suits = ['HEARTS','DIAMONDS','SPADES','CLUBS']
ranks = ['TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING','ACE']
values = {x:(i+2) for i,x in enumerate(ranks)} #i.e 'TWO':2,'THREE':3,...so on so forth

class Card:
    #SUIT,RANK,VALUE
    def __init__(self,suit:str,rank:str) -> None:
        self.suit = suit.upper()
        self.rank = rank.upper()
        self.value = values[rank.upper()]
    def __str__(self):
        return self.rank+" of "+self.suit


class Deck:
    def __init__(self) -> None:
        self.all_cards = [Card(s,r) for s in suits for r in ranks]
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name:str) -> None:
        self.name = name
        self.all_cards:list[Card] = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards:Union[list[Card],Card]):
        if isinstance(new_cards,Card):
            self.all_cards.append(new_cards)
        elif type(new_cards) == type([]):
             self.all_cards.extend(new_cards)
    def __str__(self):
        return f"Player {self.name} has { len(self.all_cards) } cards."

    
###########################################
#  GAME SETUP
###########################################

def play_game():
    new_game = True
    cards_drawn_during_war = 5
    while new_game:
        print("Starting a new game!")
        game_on = True
        player_one = Player("One")
        player_two = Player("Two")
        deck = Deck()
        deck.shuffle()
        
        _ = input()
        print("Shuffling Deck...")

        while len(deck.all_cards) > 0:
            player_one.add_cards(deck.deal_one())
            player_two.add_cards(deck.deal_one())
        
        _ = input()
        print("Dealing cards to players...")

        player_one_pile:list[Card] = []
        player_two_pile:list[Card] = []
        
        print(f"Player One deck count: {len(player_one.all_cards)}  Cards in pile: {len(player_one_pile)}")
        print(f"Player Two deck count: {len(player_two.all_cards)}  Cards in pile: {len(player_two_pile)}")
        print()
        print("Gameplay start.")

        round_no = 0
        _ = input()
        while game_on:
            if len(player_one.all_cards) == 0 or len(player_two.all_cards) == 0:
                game_on = False
                break
            round_no += 1
            print()
            print(f"######## New Round ({round_no})#######")
            print(f"Player One deck count: {len(player_one.all_cards)}  Cards in pile: {len(player_one_pile)}")
            print(f"Player Two deck count: {len(player_two.all_cards)}  Cards in pile: {len(player_two_pile)}")
            print()
            print("Both players plays card...")
            print()
            player_one_card = player_one.remove_one()
            player_two_card = player_two.remove_one()

            player_one_pile.append(player_one_card)
            player_two_pile.append(player_two_card)

            print(f"[Player One card] | [Player Two card]")
            print(f"{player_one_card} | {player_two_card}")
            print("")
            print(f"Player One deck count: {len(player_one.all_cards)}  Cards in pile: {len(player_one_pile)}")
            print(f"Player Two deck count: {len(player_two.all_cards)}  Cards in pile: {len(player_two_pile)}")
            print("")

            #_ = input()
            if player_one_card.value > player_two_card.value:
                print(f"{player_one_card} > {player_two_card}")
                print()
                print(f"Player One wins.")
                print(f"Player One gains all cards in pile.")
                print()
                player_one.add_cards(player_one_pile + player_two_pile)
                player_one_pile.clear()
                player_two_pile.clear()

                print(f"Player One deck count: {len(player_one.all_cards)}  Cards in pile: {len(player_one_pile)}")
                print(f"Player Two deck count: {len(player_two.all_cards)}  Cards in pile: {len(player_two_pile)}")
            elif player_two_card.value > player_one_card.value:
                print(f"{player_one_card} < {player_two_card}")
                print()
                print(f"Player Two wins.")
                print(f"Player Two gains all cards in pile.")
                print()
                player_two.add_cards(player_two_pile + player_one_pile)
                player_one_pile.clear()
                player_two_pile.clear()
                
                print(f"Player One deck count: {len(player_one.all_cards)}  Cards in pile: {len(player_one_pile)}")
                print(f"Player Two deck count: {len(player_two.all_cards)}  Cards in pile: {len(player_two_pile)}")
            else: #EQUAL THEREFORE WAR
                print(f"{player_one_card} == {player_two_card} !!!")
                print()
                print("############# Entered War! ##############")
                print(f"# Each Player removes {cards_drawn_during_war} cards to pile #")
                print()
                
                print("# Removing cards...#")
                print()
                for _ in range(0,cards_drawn_during_war): # remove cards into deck
                    if len(player_one.all_cards) == 0 or len(player_two.all_cards) == 0:
                        game_on = False
                        break
                    player_one_pile.append(player_one.remove_one())
                    player_two_pile.append(player_two.remove_one())
                    print(f"Player One deck count: {len(player_one.all_cards)}  Cards in pile: {len(player_one_pile)}")
                    print(f"Player Two deck count: {len(player_two.all_cards)}  Cards in pile: {len(player_two_pile)}")
                    print("")

            _ = input()

        if len(player_one.all_cards) == 0 and len(player_two.all_cards) == 0:
            print(f"Both Player One and Player Two has no more cards left.")
            print(f"This game is a draw!")
        elif len(player_one.all_cards) == 0:
            print(f"Player One has no more cards left.")
            print(f"Player Two has won!")
        else:
            print(f"Player Two has no more cards left.")
            print(f"Player One has won!")
        
        print()
        player_input = ""
        while player_input not in ['Y','N']:
            player_input = input("New Game? (Y,N): ").upper()
        if player_input == 'N':
            new_game = False
            

play_game()