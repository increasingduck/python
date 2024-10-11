def pap():
    choice1 = input("Player one enter r, p, or s")
    choice2 = input("Player two enter r, p, or s")

    if choice1 == "r" and choice2 =="p":
        print("Player two wins")
    if choice1 == "r" and choice2 == "s":
        print("Player one wins")
    if choice1 == "p" and choice2 == "s":
        print("Player two wins")
    
    def pap2():
        if choice1 == "p" and choice2 == "r":
            print("Player one wins")
        if choice1 == "s" and choice2 == "r":
            print("Player two wins")
        if choice1 == "s" and choice2 == "p":
            print("Player one wins")

if __name__ == "__main__":
    pap()
    pap2()