from sys import argv

script, name = argv

print(f"hellow {name}, I hear you are having a rough day! well lets make it better!")

print("Hit 1. to make it better and hit 2. if you want use to leave you alone.")

answer = input("> ")

if answer == "1":
    print("ok you are about to go on an adventure! Also my name is Gandalf nice to meet you!")
    print("I am going to give you some choices of adventures!!")
    print("Enter 1 if you want to go to the Mountains!")
    print("Enter 2 if you want to go to the Ocean!")
    print("Enter 3 if you want to go to the Desert!")


elif answer == "2":
    print("well luckily for you we don't take no for an answer.! Also my name is Gandalf nice to meet you!")
    print("I am going to give you some choices of adventures!!")
    print("Enter 1 if you want to go to the Mountains!")
    print("Enter 2 if you want to go to the Ocean!")
    print("Enter 3 if you want to go to the Desert!")
else:
    print("that was not the answer i asked for but we will try again!")
    print("I am going to give you some choices of adventures!!")
    print("Enter 1 if you want to go to the Mountains!")
    print("Enter 2 if you want to go to the Ocean!")
    print("Enter 3 if you want to go to the Desert!")
adventure = input("> " )

if adventure == "1":
    print("Well the moutains are very high up lets get on this here drago and go!")

elif adventure == "2":
    print("Alright, well step through my teleporter to get on the submarine!")

elif adventure == "3":
    print("Alright, lets get in my Viking longship and go!!")

else:
    print("Hmmm that is not what i asked we are done here")
    quit()
    