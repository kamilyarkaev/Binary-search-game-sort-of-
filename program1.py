import random
my_list = [random.randint(1, 100) for _ in range(8)]
my_list.sort()
num = random.randint(1,8)
print (list) #just to see#1
answer = my_list[num]
print (answer) #just to see#2
ingame = True
print("This is a binary search game,try to guess using binary search")
while ingame == True:
    guess = int(input("Try to guess the random number \n"))
    if guess < answer:
        print("Wrong, your guess is smaller")
    elif guess > answer:
        print("Wrong, your guess is bigger")
    elif guess == answer:
        print("YOU GUESSED IT")
        ingame = False    
