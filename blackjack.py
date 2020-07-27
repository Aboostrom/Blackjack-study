from deck import Deck
from dealer_hand import Dealer
from card import Card
import csv


def main():
    cards_to_try = Card().test_arr()
    for card in cards_to_try:
        card_run(card, 50000)

def card_run(card, ngames=1):
    winner_list = []
    data_dict = {}
    with open("data.csv", "a") as csvfile:
        fieldnames = ["win_percentage", "loss_percentage",
                  "player_hit_line", "dealer_card"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for num in range(21):
            for _ in range(ngames):
                dealer = Dealer(card)
                dealer_hand = dealer.hand
                shuffled_deck = dealer.deck
                player_hand = []
                player_split_hand = []
                player_split_count = []
                deal_cards(player_hand, shuffled_deck)

                player_count = count_hand(player_hand)
                dealer_count = count_hand(dealer_hand)

                card_decisions((num + 1), player_hand, player_count, player_split_hand,
                            player_split_count, dealer_hand, dealer_count, shuffled_deck)
                
                winner_list.append(
                    winner(dealer_count, player_count, player_hand, dealer_hand))
                if len(player_split_hand) > 0:
                    winner_list.append(
                        winner(dealer_count, player_split_count, player_split_hand, dealer_hand))
            win_percentage = (winner_list.count("Player") / len(winner_list)) * 100
            loss_percentage = (winner_list.count("Dealer") / len(winner_list)) * 100
            data_dict["win_percentage"] = win_percentage
            data_dict["loss_percentage"] = loss_percentage
            data_dict["player_hit_line"] = num + 1
            data_dict["dealer_card"] = card.split(" ")[0]
            writer.writerow(data_dict)
        
def deal_cards(hand_a, deck, hand_b=[],  num=2):
    for _ in range(num):
        hand_a.append(deck.pop())
        hand_b.append(deck.pop())

def card_decisions(hit_value, player_hand, player_count, player_split_hand, player_split_count, dealer_hand, dealer_count, shuffled_deck):
    player_decision = player_options(hit_value, player_hand, player_count, dealer_count)
    dealer_decision = dealer_options(dealer_hand, dealer_count)
    player_split_decision = ""
    while player_decision != "stay" or dealer_decision == "hit" or (len(player_split_hand) > 0 and player_split_decision == "hit"):
        if player_decision == "hit":
            hit_me(player_hand, shuffled_deck, player_count)
            player_decision = player_options(hit_value, player_hand, player_count, dealer_count, player_split_hand)
        elif player_decision == "split":
            player_split_hand.append(player_hand.pop())
            player_split_count.append(player_count.pop())
            player_decision = "hit"
            player_split_decision = "hit"
        if len(player_split_hand) > 0 and player_split_decision == "hit":
            hit_me(player_split_hand, shuffled_deck, player_split_count)
            player_split_decision = player_options(hit_value, player_split_hand, player_split_count, dealer_count, player_hand)
        if dealer_decision == "hit":
            hit_me(dealer_hand, shuffled_deck, dealer_count)
            dealer_decision = dealer_options(dealer_hand, dealer_count)        

def hit_me(hand, deck, count):
    hand.append(deck.pop())
    count.append(count_hand([hand[-1]])[0])
    if sum(count) > 21 and count[-1] == 11:
        count[-1] = 1
    elif sum(count) > 21 and 11 in count:
        for idx, num in enumerate(count):
            if num == 11:
                count[idx] = 1

def count_hand(hand):
    count = []
    for card in hand:
        card_arr = card.split()
        if card_arr[0].isdigit():
            count.append(int(card_arr[0]))
        elif card_arr[0] in ["J", "Q", "K"]:
            count.append(10)
        else:
            count.append(11)
    if sum(count) == 22:
        count[1] = 1
    return count

def player_options(hit_value, hand, count, opponent_count, split_hand=[]):
    if hand[0].split()[0] == hand[1].split()[0] and len(split_hand) == 0:
        return "split"
    elif sum(count) >= hit_value:
        return "stay"
    else:
        return "hit"

def dealer_options(hand, count):
    if sum(count) < 17:
        return "hit"
    else:
        return "stay"

def winner(dealer_count, player_count, player_hand, dealer_hand):
    winner = ""
    if (sum(dealer_count) > 21 and sum(player_count) > 21) or (sum(dealer_count) == sum(player_count)):
        winner = "Push"
        # print("It's a push! {0} and {1} counts with {2} and {3}".format(
        #     player_count, dealer_count, player_hand, dealer_hand))
    elif sum(player_count) > 21 or (sum(player_count) < sum(dealer_count) and sum(dealer_count) <= 21):
        winner = "Dealer"
        # print("Dealer wins! {0} and {1} counts with {2} and {3}".format(
        #     player_count, dealer_count, player_hand, dealer_hand))
    else:
        winner = "Player"
        # print("Player wins! {0} and {1} counts with {2} and {3}".format(
        #     player_count, dealer_count, player_hand, dealer_hand))
    return winner


main()
