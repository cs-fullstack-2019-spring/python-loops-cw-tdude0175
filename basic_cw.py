def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    FIZZBUZZ()

'''
Print -20 to and including 50. 
Use any loop you want.
'''
# how would you do with while loop?
# while(start != 51)
def problem1():
    for num in range(-20,51):
        print(num)

'''
Create a loop that prints even numbers from 0 to and including 20.
'''
# how to do it with while equaling true?
def problem2():
    start =0
    while(start !=21):
        print(start)
        start+=1

'''
Prompt the user for 3 numbers. 
Then print the 3 numbers along with their average after the 3rd number is entered. 
Refer to example below 
replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.
'''

def problem3():
    num1 = int(input("gimme a number."))
    num2 = int(input("gimme ANOTHER ONE."))
    num3 = int(input("GIMME ONE MOAR."))
    average = (num1+num2+num3/3)
    print(str(num1 + num2 + num3) + " is the sum of " + str(num1) + " " + str(num2) + " " + str(num3) + " and " + str(average) + " is the average." )

'''
Password Checker - Ask the user to enter a password. Ask them to confirm the password. If it's not equal, keep asking until it's correct or they enter 'Q' to quit.
'''

def problem4():
    secretPassword = "C0d3Cr3w"
    userInput = input("what is the password")

    while(True):
        if userInput == secretPassword:
            break
        elif userInput == "Q":
            break
        elif userInput !=secretPassword:
            print("ERROR WRONG PASSWORD Q TO QUIT.")
        userInput = input()

'''
FIZZBUZZ is the classic Programmer's challenge often used as part of job interviews:

Prompt the User for the ending value (e.g. 100)

Your code should start at 1 and then iterate each number up to the ending value entered by the user

If the current number is evenly divisible by 3 you should print FIZZ and the number

If the current number is evenly divisible by 5 you should print BUZZ and the number

If the current number is evenly divisible by both 3 and 5 you should print FIZZBUZZ and the number to the screen

Otherwise, just print the original number
'''

def FIZZBUZZ():
    endvalue = int(input("enter the ending number"))
    startvalue =1
    while(startvalue <= endvalue):
        if(startvalue%3 == 0 and startvalue%5 == 0):
            print("FIZZBUZZ")
        elif(startvalue%5 == 0):
            print("BUZZ")
        elif(startvalue%3 == 0):
            print("FIZZ")
        else:
            print(startvalue)
        startvalue+=1

if __name__=='__main__':
    main()