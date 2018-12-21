import random

cash = 2000

def create_winning_numbers():
    winning_numbers = set()
    while len(winning_numbers) < 6:
        winning_numbers.add(random.randint(1,49))
    return winning_numbers

def buy_lottery_ticket():
    entered_numbers=input('Enter 6 numbers ( 1 to 49): ')
    entered_numbers_list = entered_numbers.split(',')
    if len(entered_numbers_list) >6:
        return 'Do not enter more than 6 numbers!!!'
    elif len(entered_numbers_list) <6:
        global cash
        cash=cash-50
        entered_numbers_list.add(random.randint(1,49))
        ticket_numbers = {int(n) for n in entered_numbers_list}
    return ticket_numbers


def drawing_result(ticket_numbers, winning_numbers):
    print('Winning numbers are {} '.format(winning_numbers))
    numbers_matched = ticket_numbers.intersection(winning_numbers)
    prizes=[0,0,0,400,2000,40000,100000000]
    prize = prizes[len(numbers_matched)]
    if prize > 0:
        global cash
        cash += prize
        return 'You matched {} numbers, and you just won {} NTD!!'.format(len(numbers_matched),prize)
    else:
        return 'Better luck next time!!'

def run():
    while True:
        cmd = input('welcome to Lottery store.\nDo you [b]uy, [c]heck balance or [l]eave? ')
        if cmd == 'b':
            ticket_numbers =  buy_lottery_ticket()
            winning_numbers = create_winning_numbers()
            msg = drawing_result(ticket_numbers, winning_numbers)
            print(msg)
        elif cmd== 'c':
            print (cash)
        elif cmd == 'l':
            break

run()