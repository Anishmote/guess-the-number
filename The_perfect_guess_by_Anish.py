from random import randint
r = randint(1,100)
a = -1
guess = 0
print("HINT: The number is between 1 and 100.\n")
while (a != r):
    guess +=1
    a = int(input("🎯 Guess The Number Here..!:"))
    if r < a:
        print("🔽lower Number Please...")
    elif r > a :
        print("🔼Higher Number Please...")

print(f"\n✅ YEAH!! You guessed the right number: {r} in {guess} attempts! 🎉")