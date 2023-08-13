bids = {}
biding_finished = False


def find_highest_bider(biding_record):
    highest_bid_amount = 0
    for bidder in biding_record:
        amount = biding_record[bidder]
        if amount > highest_bid_amount:
            highest_bid_amount = amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid_amount}")


while not biding_finished:
    name = input("enter the name of the bider: ")
    bid_amount = int(input('Enter the bid amount: '))
    bids[name] = bid_amount
    should_continue = input('Are there any bidder to bid? types YES or NO').lower()
    if should_continue == 'no':
        biding_finished = True
        find_highest_bider(bids)

