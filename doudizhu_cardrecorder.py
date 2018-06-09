

def getcards() -> list:
    lst = [4]*14
    lst[0] = 2 # 大小王

    return lst


def getprintnames():
    names = [0]*20
    names[0] = '大小王'
    names[1] = 'A'
    names[2] = '二'
    names[13] = 'K'
    names[12] = 'Q'
    names[11] = 'J'
    for i in range(3,11):
        names[i] = str(i)

    return names


def getleftcards(curcards: list, outcards: list):
    for item in outcards:
        curcards[item] -= 1

    return curcards


def printcards(curcards, printnames):



    print("大小王:\t", max(curcards[0], 0))

    print("2:\t", max(curcards[2], 0))

    print("A:\t", max(curcards[1], 0))

    for i in range(13,2,-1):
        print(printnames[i]+':\t', max(curcards[i], 0))






def main():
    curcards = getcards()
    names = getprintnames()

    printcards(curcards,names)


    while True:
        lst = input("outcards：")
        if not lst:
            continue
        lst = lst.split(' ')
        for i in range(len(lst)):
            lst[i] = int (lst[i])

        outcards = lst[:]
        if outcards and outcards[0] == -1:
            string = input("restart a game? :")
            if string and string[0] == 'n':
                break
            else:
                curcards = getcards()
        else:
            leftcards = getleftcards(curcards,outcards)
            printcards(leftcards, names)



if __name__ == '__main__':
    main()
