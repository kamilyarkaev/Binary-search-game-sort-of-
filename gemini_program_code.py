import random
my_list = random.sample(range(1, 1000), 128)
my_list.sort()
answer = random.choice(my_list)
print(f"I generated 128 unique numbers between {my_list[0]} and {my_list[-1]}.")
print("This is a binary search game. Try to guess using binary search!")
ingame = True
while ingame:  
    guess = int(input("Try to guess the random number:\n"))
    
     if guess < answer:
        print("Wrong, your guess is too small. Aim higher!")
    elif guess > answer:
        print("Wrong, your guess is too big. Aim lower!")
    elif guess == answer:
        print("YOU GOT IT!")
        ingame = False  
