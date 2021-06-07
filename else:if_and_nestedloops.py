students = [("Jordan", ["ComputerScience", "Physics"]),
            ("John", ["Math", "English", "Stats"]),
            ("Patty", ["Biology", "Accounting", "Economics"]),
            ("Anonymous", ["EnvironmentalScience", "Accounting", "Economics", "Law"]),
            ("Claude", ["Sociology", "Economics", "Law", "Stats", "Music"])]

counter = 0
for (name, subjects) in students:
    for s in subjects:                 
        if s == "Law":
            counter += 1

ok=input("How many of you failed 'Law' this year? ")


if ok=="I don't Know":
    print("NO,IT'S",counter)
    print("and IT'S","ONE", "of", "YOU" * 10,"!!!")
    print("See you next year!")

elif ok=="2":
    print("you're correct!")
    
    


elif ok!="2":
    print("It was",counter, "that will have to retake it next year!")
    print("and IT'S","ONE", "of", "YOU" * 10,"!!!")
    print("See you next year!")
    
    
    
