word = "Bottles"
for milk_num in range(99,0,-1): 
    print(milk_num,word,"off milk on the wall.")
    print("Pass it around.")
    if milk_num == 1:
        print("No more bottles of milk on the wall.")
    else:
        new_num = milk_num - 1
        if new_num == 1:
            word = "milk"
        print(new_num,word, "of milk on the wall.")
        print()
