import random;

flag = 0
guess = 0
key = random.randint(1, 9);
chances = int(input("How many chances do you want? Don't pick over 5, loser.    "));
y = 1

while chances>5:
    print("Didn't I say DON'T PICK OVER 5!")
    chances = int(input("Choose BELOW 5.    "));

print (key);


while y <= chances:
    if(y == 1):
        guess = int(input("1st guess:    "));
        if(guess == key):
            print("You were right on your 1st try, noob. The answer is ", key);
            flag = 1;
            break
    elif(y == 2):
        guess = int(input("2nd guess:    "));
        if(guess == key):
            print("You were right on your 2nd try, noob. The answer is ", key);
            flag = 1;
            break
    elif(y == 3):
        guess = int(input("3rd guess:    "));
        if(guess == key):
            print("You were right on your 3rd try, noob. The answer is ", key);
            flag = 1;
            break
    else:
        guess = int(input("Lost Count. Count it yourself. Next guess:    "));
        if(guess == key):
            print("You were right on your ",y,"th try, noob. The answer is ", key);
            flag = 1;
            break
    y = y + 1;

if(flag == 0):
    print("Loser...")
