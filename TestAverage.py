dTestscore1 = float(input("what is your test score\n"))
dTestscore2 = float(input("what is your second test score\n"))
dTestscore3 = float(input("what is your third test score\n"))
dTestaverage = float(dTestscore1 + dTestscore2 + dTestscore3 / 3)
if dTestaverage >= (90):
    print ("The letter grade of a 90 is equal to an A")
elif dTestaverage >= (80):
    print("The letter grade of a 80 is equal to a B")
elif dTestaverage >= (70):
    print ("The letter grade of a 70 is equal to a C")
elif dTestaverage >= (60):
    print ("The letter grade of a 60 is equal to a D")
elif dTestaverage <= 60:
    print("Any letter grade below 60 is an E")
