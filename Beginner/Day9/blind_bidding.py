
def find_highest_bidder(bids):
    max_bid = 0.0
    winner = ""
    for name in bids:
        if bids[name] > max_bid:
            max_bid = bids[name]
            winner = name
    
    print(f"Winner is {winner} with ${max_bid}")

def start_bidding():
    bids = {}

    print("Welcome to the secret auction program.")

    more_bidders = True
    while more_bidders:
        name = input("What is your name?\t")
        bid_amount = float(input("What's your bid?\t $"))
        cont = input("Are there any other bidders? ('yes' or 'no')\t").lower()

        bids[name] = bid_amount
        if cont == "no":
            more_bidders = False

    find_highest_bidder(bids)

start_bidding()
