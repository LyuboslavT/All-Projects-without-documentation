import random

fruits = ['🍋', '🍇', '🍑', '🍒']

balance = float(input('Enter your balance: '))

while balance > 0:
    print(f'Your current balance is: {balance:.2f}')

    bet = float(input('Place your bet: '))

    while bet > balance:
        print(f'Insufficient balance. Please place a bet within your balance.')

        bet = float(input('Place your bet: '))

    reel1 = random.choice(fruits)
    reel2 = random.choice(fruits)
    reel3 = random.choice(fruits)
    reel4 = random.choice(fruits)

    print(reel1, reel2, reel3, reel4)

    if reel1 == reel2 == reel3 == reel4:
        print(f'Congratulations! You have won the Jackpot - {bet * 10:.2f}')
        balance += bet * 10

    elif reel1 == reel2 == reel3 or reel1 == reel2 == reel4:
        print(f'You have won the amount of {bet * 5:.2f}')
        balance += bet * 5

    elif reel1 == reel2 or reel3 == reel4:
        print(f'You have won the amount of {bet * 2:.2f}')
        balance += bet * 2

    else:
        print('Sorry you lost! Try again!')
        balance -= bet

if balance <= 0:
    print(f'Game over! Your final balance is: {balance:.2f}')
