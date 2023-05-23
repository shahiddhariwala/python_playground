import os
auction_bid_art = '''
                __
               (_()  \\
          \__/  ||    \  \__/
          (oo)  /)       (oo)
         //~~\\//       //~~\\
         \\__/\/   _____\\__//_____
          |/\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|_______

'''

print(auction_bid_art)

auction_ledger = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?\n")
    bid = int(input("What is your bid $"))
    auction_ledger[name] = bid
    if "no" in input(
            "Are there any other bidders, type 'Yes' or 'No'\n").lower().strip():
        continue_bidding = False
    else:
        os.system("clear")

winner = ""
winning_bid = 0
for bidder in auction_ledger:
    if winning_bid < auction_ledger[bidder]:
        winning_bid = auction_ledger[bidder]
        winner = bidder

print(f"Winner is {winner} with bid of ${winning_bid}")
