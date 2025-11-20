
import random

x = random.randint(1,10)
y = random.randint(1,10)

while True:
    print("1.main")
    print("2.quit")
    cois = int(input("= "))

    if cois == 1:
        print("---level---")
        print("1.easy")
        print("2.medium")
        print("3.hard")
        print("4.extreme")
        play = int(input("="))

        if play == 1:
            print("level easy")
            print(x, "+", y)
            ans = int(input("= "))
            if ans == x + y:
                print("the answer is", x + y)
                print("anjay bener")
                break
            else:
                print("try again!")

        elif play == 2:
            print("level medium")
            print(x, "*", y)
            ans = int(input("= "))
            if ans == x * y:
                print("the answer is", x * y)
                print("hoki aja")
                break
            else:
                print("ya salah lawak")

        elif play == 3:
            print("level hard")
            print(x, "/", y)
            ans = float(input("= "))  # pembagian hasilnya desimal
            if ans == x / y:
                print("the answer is", x / y)
                print("boleh lah")
                break
            else:
                print("try again!")

        elif play == 4:
            print("level extreme")
            print(x, "**", y)
            ans = int(input("= "))
            if ans == x ** y:
                print("the answer is", x ** y)
                print("nyontek aja bangga")
                break
            else:
                print("try again!")

    else:
        print("thanks for playing")
        break