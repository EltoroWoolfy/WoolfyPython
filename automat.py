type = int(input('hello, some coffee? '))
types = ['-', 'espresso', 'mokka', 'kappuchino']
cash = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
esp = 100
mok = 200
kap = 150
if type == 1:
    print('you choose ' + types[1] + ', push 100r')
    insert1 = int(input())
    if insert1 < cash[10]:
        insert2= int(input('Count: ' + str(insert1) + '. not enough money, insert more '))
        scesp = insert1 + insert2
        if scesp == cash[10]:
            print(types[1] + ' is coming')
        elif scesp < cash[10]:
            insert3 = int(input('Count: ' + str(scesp) + '. not enough money, insert more '))
            third = scesp + insert3
            if third == cash[10]:
                print('espresso is coming')
            elif third < cash[10]:
                insert4 = int(input('Count: ' + str(third) + '. not enough money, insert more'))
                fourth = third + insert4
                if fourth == cash[10]:
                    print(types[1] + ' is coming')
                elif fourth < cash[10]:
                    insert5 = int(input('Count: ' + str(fourth) + '. not enough money, insert more'))
                    five = fourth + insert5
                    print(five)
    elif insert1 == cash[10]:
        print(types[1] + ' is comming')
