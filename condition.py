import math
import random
def ClumpDiagnosis():
    M_a = input("marginal adhesion (0-6): ")
    if int(M_a) >3:
        B_n = input("bare nuclei (0-8): ")
        if int(B_n) > 4:
            print("The clump is cancer")
        else: print("The clump is benign")
    else:
        C_t = input("clump thickness (0-6): ")
        if int(C_t) >3:
            U_c = input("uniformity of cell shape (0-4): ")
            if int(U_c) > 2:
                print("The clump is cancer")
        else: print("The clump is benign")
    # print(M_a[len(M_a)-1])
def GuessNumber():
    ans = random.randint(1,100)
    inp = -1
    time_count = 0
    while(inp != ans):
        inp = int(input("guess an integer between 1 and 100: "))
        if inp > ans:
            print("The true number is smaller")
        elif inp <ans:
            print("The true number is bigger")
        time_count += 1
        # print(inp)
    print("You get it!")
    print("It takes you {0:d} times to nail the number.".format(time_count))
    # print(s)
def DiceGame():
    t = input("enter to throw three dices")
    your = 0
    banker = 0
    for i in range(3):
        your += random.randint(1,6)
        banker += random.randint(1,6)
    print("Your dice sum is {0:d} .".format(your))
    print("Banker's dice sum is {0:d} .".format(banker))
    # print(your,banker)
    if(your%10 > banker%10):
        print("You win!")
    elif(your%10 <banker%10):
        print("Banker win!")
    else:print("It is a draw")

# GuessNumber()
# ClumpDiagnosis()
DiceGame()
