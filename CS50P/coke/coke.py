'''bal = 50
coin_list = [5,10,25]
inserted_coin = int(input("Amount Due: 50" + "\n" + "Insert coin: "))
while bal > 0:
    if inserted_coin in coin_list:
        print("Amount Due: " + str(bal - inserted_coin))
        bal -= inserted_coin
        inserted_coin = int(input("Insert coin: "))
    elif inserted_coin not in coin_list:
        print("Amount Due: " + str(bal))
        inserted_coin = int(input("Insert coin: "))
    else:
        print("Changed Owed: 0")
        break'''

total = 50
coin_list = [5,10,25]

while total > 0:
    coin = int(input("Amount Due: " + str(total) + "\n" + "Insert coin: "))

    if coin in coin_list:
        total -= coin

print("Change Owed: " + str(abs(total)))

