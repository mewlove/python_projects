import random
#from typing import Union

suits = ['HEARTS','DIAMONDS','SPADES','CLUBS']
ranks = ['TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING','ACE']
values:dict[str,int] = {'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9,
'TEN':10,'JACK':10,'QUEEN':10,'KING':10,'ACE':11}

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
        self.deck = [Card(s,r) for s in suits for r in ranks]
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop()

class Hand:
    def __init__(self, name:str) -> None:
        self.name = name
        self.cards:list[Card]= []
        self.base_value = 0
        self.aces = 0  
    def add_card(self,card:Card):
        self.cards.append(card)
        self.base_value += values[card.rank]
        if card.rank == "ACE":
            self.aces += 1
    def return_value(self):
        temp_value = self.base_value
        for _ in range(0,self.aces):
            if temp_value > 21:
                temp_value -= 10
            else:
                break
        return temp_value
    def show_partial_hand(self):
        return f"{self.name} Cards: [Hidden card]  " + "  ".join([str(x) for x in self.cards[1:]])
    def __str__(self):
        return f"{self.name} Cards: " + "  ".join(list(map(str,self.cards))) +"\nValue: "+ str(self.return_value())
            

class Chips:
    def __init__(self, balance:int) -> None:
        self.balance = balance
    def add_to_balance(self, amount:int):
        self.balance += amount
    def __str__(self):
        return f"Balance: {self.balance}"

def ask_for_player_balance():
    player_choice = -1
    while(True):
        try:
            player_choice = int(input("Please input player balance: "))
        except:
            print("Invalid input. Please try again.")
        else:
            if player_choice > 0:
                break
            else:
                print("Invalid input. Please try again.")

    return player_choice

def ask_for_player_bet(remaining_balance:int):
    player_choice = -1
    while(True):
        try:
            player_choice = int(input(f"How much would you like to bet? (Balance: {remaining_balance}): "))
        except:
            print("Invalid input. Please try again.")
        else:
            if player_choice > 0 and player_choice <= remaining_balance:
                break
            else:
                print("Invalid input. Please try again.")

    return player_choice

def hit_or_stand():
    player_choice = ""
    while player_choice not in ["0","1"]:
        player_choice = input("Hit or Stand? (0,1): ")
    return player_choice

def yes_or_no(message:str):
    player_choice = ""
    while player_choice not in ["Y","N"]:
        player_choice = input(f"{message} (Y,N): ").upper()
    return player_choice

def play_blackjack():
    play_new_game = True

    while play_new_game:
        print()
        print("New Game Start.")
        player_balance = Chips(ask_for_player_balance())

        round_no = 0
        play_new_round = True        
        while play_new_round:
            round_no += 1
            print()
            print(f"Round no: {round_no}: ")
            print()
            deck = Deck()
            deck.shuffle()

            # deals 2 cards to dealer
            print("Deal 2 cards to dealer...")
            dealer = Hand("Dealer")
            for _ in range(0,2):
                dealer.add_card(deck.deal_one())
            print(dealer.show_partial_hand())
            print()

            # deals 2 cards to player
            print("Deal 2 cards to player...")
            player = Hand("Player")
            for _ in range(0,2):
                player.add_card(deck.deal_one())
            print(player)
            print()

            player_bet = ask_for_player_bet(player_balance.balance)
            player_balance.add_to_balance(-player_bet)

            #asks player if they want to hit or stand (hit to take another card, stand to stop taking cards)
            stand = False
            player_choice = hit_or_stand()
            if player_choice == "1":  #stand
                stand = True
            
            # while player hits 
            dealer_plays = True
            while not stand:
                print("Player hits. A card is dealt to the player...")
                player.add_card(deck.deal_one())
                print(player)
                print()

                if player.return_value() >= 21:
                    dealer_plays = False
                    break

                player_choice = hit_or_stand()
                if player_choice == "1":  #stand
                    stand = True
                    print("Player Stands. Dealer's turn.")
                    break
            
            while dealer_plays:
                if dealer.return_value() < 17:
                    dealer.add_card(deck.deal_one())
                    print(f"Dealer hits.")
                    print(dealer)
                    print()
                else:
                    dealer_plays = False

            
            if player.return_value() == 21:
                print("Blackjack! Player wins!")
                player_balance.add_to_balance(player_bet*2)
            elif player.return_value() > 21:
                print("Player exceeds 21, Player busts!")
            else:
                if dealer.return_value() > 21 or dealer.return_value() < player.return_value():
                    print("Dealer exceeds 21, Dealer busts! Player wins!")
                    player_balance.add_to_balance(player_bet*2)
                elif dealer.return_value() == player.return_value():
                    print("Its a draw.")
                    player_balance.add_to_balance(player_bet)
                else:
                    print("Dealer wins!")
            
            print()
            if player_balance.balance > 0:
                print(player_balance)
                player_choice = yes_or_no("Play another round? ")
                if player_choice == "N":
                    play_new_round = False
            else:
                print(f"Player balance not sufficient: {player_balance.balance}")
                play_new_round = False

        print(player_balance)
        player_choice = yes_or_no("Play a new game?")
        if player_choice == "N":
            play_new_game = False
                


play_blackjack()