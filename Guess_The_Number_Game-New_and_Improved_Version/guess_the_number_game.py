import random
import os

os.system('cls')

n = int(input("Enter the upper limit of range of the number you want to guess from (2 to ...) : "))

r_num = random.randrange(1,n)

hint_count=0
attempts=(12*n)//100

while attempts!=0:

	os.system('cls')

	print("You have got",attempts,"attempts to win the game! Choose your moves wisely!")

	num = int(input("\nGuess the number : "))

	if num==r_num:

		print("\nYou're Right!, the number was",r_num,"Looks like you've got some superpowers! You guessed the right number in just",10-attempts,"attempts,",end=" ")

		if hint_count==0:
			print("without using any hints!")
		elif hint_count==1:
			print("using only",hint_count,"hint!")
		else:
			print("using only",hint_count,"hints!")	

		print("\nYOU WON!")
		break

	else:

		attempts-=1
		print("\nUh oh! That's not the correct number! You gotta try again!")
		print("\nYou have",attempts,"attempts remaining...")

		if attempts>=2:
			print("\nDo you want a HINT? A HINT will cost you exhaustion of 1 attempt extra!")

			choice = input("Press 1 to get a HINT, else Press any other key to continue with hit and trial method... : ")

			if choice[0]=='1':			

				hint_count+=1
				attempts-=1

				if num<r_num:
					print("\nHINT -> Try entering a number which is a bit higher than",num)
				else:
					print("\nHINT -> Try entering a number which is a bit lower than",num)

		cont = input("\nPress any key to continue...")
else:
	print("\nAll 10 attempts exhausted! The number was",r_num,",Better luck next time!")
	print("\nYOU LOST")