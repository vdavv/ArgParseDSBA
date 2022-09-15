import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "-n", "--name", help="enter your name to proceed with healthy lifestyle index"
)
args = parser.parse_args()

if args.name:
    print(f"Hello, {args.name} and welcome to healthy lifestyle index test!\n")
else:
    print("Hello, dear user and welcome to healthy lifestyle index test!\n")

print("Choose your gender: male, female")
gender = input()
if not gender in ["male", "female"]:
    print("\nSorry, entered gender doesn't exist, please try again!")
    exit()

print("\nWrite your height (cm):")
height = int(input())

print("\nWrite your weight (kg);")
weight = int(input())

print("\nHow many hours do you usually sleep?")
# Less than 7 hours; 7-8 hours (1 point); More than 8 hours;
sleep = 1 if 7 <= int(input()) <= 8 else 0

print("\nHow many meals does your daily diet include?")
# 1 meal, 2-3 meals, 4-5 meals (1 point);
meals = 1 if 4 <= int(input()) <= 5 else 0

print("\nHow many grams of fresh fruits and vegetables do you eat during the day?")
# I do not eat these products regularly, Less than 500 grams, More than 500 grams (1 point);
frugetebles = 1 if int(input()) > 500 else 0

print("\nHow many steps do you walk on average per day?")
# Less than 5 thousand steps, 5-10 thousand steps, More than 10 thousand steps (1 point);
steps = 1 if float(input()) > 10000 else 0

print(
    "\nDo you monitor your health?: (1) No; (2) Yes, I have been undergoing medical examination in the last 3 years; (3) Yes, but I do not see a doctor;"
)
# Not; Yes, I have been undergoing medical examination in the last 3 years (1 point), Yes, but I do not see a doctor;
health = 1 if input() in ["2", "(2)"] else 0

print("\nWhat is your mood today?: Good, Neutral, Bad ")
# What is your mood today? Good (1 point), Neutral, Bad [choices];
mood = 1 if input() in ["Good", "good", "1"] else 0

print(
    "\nWhen was the last time you had a state of happiness?: (1) During the week; (2) During the month (1 point); (3) During the year."
)
# During the week (1 point), During the month (1 point), During the year.
happy = 1 if input() in ["1", "2", "(1)", "(2)"] else 0

# BMI (Body Mass Index) is calculated: BMI = body weight / height * height. BMI from 18.5 to 24.9 corresponds to 1 point.
bmi = 1 if 18.5 <= weight / ((height / 100) ** 2) <= 24.9 else 0


"""The maximum value of the healthy lifestyle index: 8 units. Depending on the result your python script should print out a message:

8 points Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!
[5-7] points Your health index is [5-7]/8, which means that you are on the right track!
[0-4] points Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!"""


indx = sleep + meals + frugetebles + steps + health + mood + happy + bmi
if indx == 8:
    print(
        "\nYour index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!"
    )
elif 5 <= indx <= 7:
    print(
        "\nYour health index is [5-7]/8, which means that you are on the right track!"
    )
else:
    print(
        "\nYour healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!"
    )
