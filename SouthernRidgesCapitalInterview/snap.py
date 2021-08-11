import random
from typing import Union

suits = ['HEARTS','DIAMONDS','SPADES','CLUBS']
value = ['TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING','ACE']

class Card:
    #SUIT,RANK
    def __init__(self,suit:str,value:str) -> None:
        self.suit = suit.upper()
        self.value = value.upper()
    def __str__(self):
        return self.value+" of "+self.suit

class Deck:
    def __init__(self, n:int = 1) -> None:
        self.deck = [Card(s,v) for _ in range(n) for s in suits for v in value]
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop()
    def __len__ (self):
        return len(self.deck)
    def __str__(self):
        return "Cards: " + "  ".join(list(map(str,self.deck)))

class Player: #Two computer players
    def __init__(self, name:str) -> None:
        self.name = name
        self.cards:list[Card]= []
    def add_cards(self, new_cards:Union[list[Card],Card]):
        if isinstance(new_cards,Card):
            self.cards.append(new_cards)
        elif type(new_cards) == type([]):
            self.cards.extend(new_cards)
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return f"{self.name} Cards: " + "  ".join(list(map(str,self.cards)))



def match_value(card1:Card, card2:Card):
    return card1.value == card2.value
def match_suit(card1:Card, card2:Card):
    return card1.suit == card2.suit
def match_suit_value(card1:Card, card2:Card):
    return card1.suit == card2.suit and card1.value == card2.value

match_options = [match_value, match_suit, match_suit_value]

def get_user_input_deck_number():
    while(True):
        try:
            numOfDecks = int(input("Number Of Decks to use (>0): "))
        except:
            print("Invalid input. Please try again.")
        else:
            if numOfDecks > 0:
                return numOfDecks
            else:
                print("Invalid input. Please try again.")
        
def get_user_input_match_type():
    while(True):
        try:
            match_type = int(input("Match Type (0-by value, 1-by suit, 2-both value & suit): "))
        except:
            print("Invalid input. Please try again.")
        else:
            if match_type >= 0 and match_type<3:
                return match_type
            else:
                print("Invalid input. Please try again.")
     
def get_user_input_sim():
    while(True):
        try:
            autoplay = str(input("Would you like to autoplay? (Y/N): "))
            autoplay = autoplay.capitalize()
        except:
            print("Invalid input. Please try again.")
        else:
            if autoplay == 'Y' or autoplay == 'N':
                return autoplay
            else:
                print("Invalid input. Please try again.")

def play_snap():
    print('***********************************************************')
    print('***********           GAME OF SNAP!!!          ************')
    print('***********************************************************')

    numOfDecks = get_user_input_deck_number()
    match_index = get_user_input_match_type()
    autoplay = get_user_input_sim()

    deck = Deck(numOfDecks)
    player = [Player('Player_1'),Player('Player_2')]
    pile: list[Card] = []
    
    print('Card shuffling in progress...')
    deck.shuffle()
    print('\nGame Start!\n')
    if autoplay == 'N':
        _ = input('Press any key...')

    total_rounds = 0
    while(len(deck) > 0):
        total_rounds += 1
        print(f"\n================ Round number: {total_rounds} ================")
        print(f"{player[0].name}: {len(player[0])} cards")
        print(f"{player[1].name}: {len(player[1])} cards")

        card1 = deck.deal_one()
        card2 = deck.deal_one()
        
        pile.append(card1)
        pile.append(card2)

        print()
        print(f"{player[0].name} plays {card1}.")
        print(f"{player[1].name} plays {card2}.")
        print()
        if(match_options[match_index](card1, card2)): #if match according to the selected match type
            player_win = random.randint(0,1)
            print(f">>>>>>>>>>>>>>>>>>>>>>>>> {player[player_win].name} shouts SNAP!!! {player[player_win].name} wins!  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            #player gets to keep whatever is in the pile
            player[player_win].add_cards(pile)
            pile.clear()
            print()
            print(f"All cards in pile added to {player[player_win].name}'s hands.")
            print(f"{player[0].name}: {len(player[0])} cards")
            print(f"{player[1].name}: {len(player[1])} cards")
            
            if autoplay == 'N':
                _ = input('Press any key...')
        else:
            print(f'No one wins. Cards in pile are discarded.')
            pile.clear()
            if autoplay == 'N':
                _ = input('Press any key...')
    
    print()
    print("No more cards in deck! Calculating player's cards...")
    print(f"{player[0].name}: {len(player[0])} cards")
    print(f"{player[1].name}: {len(player[1])} cards")
    print()
    if(len(player[0]) > len(player[1])):
        print(f"{player[0].name} wins!!!")
    elif(len(player[0]) < len(player[1])):
        print(f"{player[1].name} wins!!!")
    else:
        print("It's a draw!")
    
    print("Game ends!")
    _ = input('Press any key...')

    

play_snap()