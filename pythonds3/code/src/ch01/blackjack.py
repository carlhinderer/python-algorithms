import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s%s' % (self.suit, self.rank)


class Deck:
    SUITS = ['C', 'D', 'H', 'S']
    RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(s, r) for s in self.SUITS for r in self.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def deal_cards(self, num):
        return [self.deal_card() for i in range(num)]


class BlackjackHand:
    def __init__(self, hand=[]):
        self.cards = hand

    def add_card(self, card):
        self.cards.append(card)

    def natural_blackjack(self):
        return len(self.cards) == 2

    def print_hand(self):
        print(*self.cards, sep=' ')


class Game:
    NUM_HANDS_PER_DECK = 3

    def __init__(self):
        self.hands_used_in_deck = 0
        self.get_new_shuffled_deck()
        self.last_winner = None

    def play_game(self):
        print('Blackjack Is Fun!!!!!\n')
        while True:
            still_playing = input('Would you like to play a hand? Y/N\n')
            if still_playing == 'N':
                print("You'll be back!")
                break
            self.play_hand()

    def play_hand(self):
        print('Playing A Hand...\n')
        self.update_deck()

        winner = None

        player_cards = self.current_deck.deal_cards(2)
        player_hand = BlackjackHand(player_cards)

        dealer_cards = self.current_deck.deal_cards(1)
        dealer_hand = BlackjackHand(dealer_cards)

        print('Player: ')
        player_hand.print_hand()
        print('Dealer: ')
        dealer_hand.print_hand()

        if player_hand.natural_blackjack():
            second_dealer_card = self.current_deck.deal_card()
            dealer_hand.add_card(second_dealer_card)
            if dealer_hand.natural_blackjack():
                winner = 'Tie'
            else:
                winner = 'Player'

        print(winner)

    def update_deck(self):
        if self.hands_used_in_deck >= self.NUM_HANDS_PER_DECK:
            self.get_new_shuffled_deck()
        self.hands_used_in_deck += 1

    def get_new_shuffled_deck(self):
        self.current_deck = Deck()
        self.current_deck.shuffle()


if __name__ == '__main__':
    g = Game()
    g.play_game()
