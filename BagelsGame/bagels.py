import random

NUM_DIGITS = 3    #未知数的位数
MAX_GYESSES = 10  #可用猜测次数


# 创建未知数
def getSecnum():
    num = list('0123456789')   #创建列表，存放每个位置的未知数
    random.shuffle(num)        #打乱列表

    secnum = ''
    for i in range(NUM_DIGITS):
        secnum += str(num[i])
    return secnum

# 用于鉴定
def getClues(guess,secnum):   #传入猜测数guess和未知数secnum
    #  猜对
    if guess == secnum:
        return 'you got it'

    clues = []

    for i in range(len(secnum)):
        # Fermi 的情况
        if guess[i] == secnum[i]:
            clues.append('Fermi')
        # Pico 的情况
        if guess[i] in secnum:
            clues.append('Pico')
    # Bagels 的情况
    if len(clues) == 0:
        return 'Bagels'
    else:
        return ''.join(clues)


# 主函数，用来运行
def main():
    print('''rules:
        Pico  : One digit is correct but in the wrong position.
        Fermi : One digit is correct and in the right position.
        Bagels: No digit is correct.
    ''')
    while True:
        secnum = getSecnum()     #获取未知数
        print('you have {} guesses to get the secnum'.format(MAX_GYESSES))

        #开始猜数
        numGuesses = 1
        while numGuesses < MAX_GYESSES:
            guess = ''
            # 检测所猜测的数的位数是否与未知数相同，猜测数中是否都是十进制数
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess,secnum)
            print(clues)
            numGuesses += 1



if __name__ == '__main__':
    main()