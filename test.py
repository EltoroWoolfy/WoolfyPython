print('hello, choose your coffee')
bank = 0
while bank < 100:
    print('Insert coin')
    insert = int(input())
    bank = bank + insert
    print('Count:' + str(bank))
print('your cofeee')