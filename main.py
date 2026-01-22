# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from multiprocessing.connection import deliver_challenge
import art
print(art.logo)

def highest_bid(bidding_dic):
    winner = ""
    high_bid = 0

    max(bidding_dic)

    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}! ")

user = {}
true = True
while true:
    name = input("Please enter your name : ")
    bid = int(input("Please write your Bid : $ "))
    user[name] = bid
    more = input("Anyone left who wants to bid ?. Print 'Yes'or 'No'").lower()
    if more == "no":
        true = False
        highest_bid(user)
    elif more == "yes":
        print("\n"*20)


def highest_bid(bidding_dic):
    winner = ""
    high_bid = 0

    max(bidding_dic)

    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}! ")