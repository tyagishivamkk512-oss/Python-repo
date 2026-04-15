questions = ("1. Which keyword is used to define a function in Python?",
             "2. What is the capital of India?",
             "3. Which planet is known as the Red Planet?",
             "4. What is the national animal of India?")


options = (("a.def","b.function","c.define","d.func"),
           ("a.Delhi","b.Mumbai","c.Kolkata","d.Muzaffarnagar"),
           ("a.earth","b.venus","c.mars","d.jupiter"),
           ("a.lion","b.tiger","c.dog","d.cat"),)

ans = ("a","a","c","b")
i=0
guesses = []

for ques in questions:
    print("---------------")
    print(ques)
    
    for opt in options[i]:
        print(opt)

    guess = input("Enter option: ")
    #guesses.append(guess)
    if guess == ans[i]:
        print("Correct!!")
    else:
        print("Incorrect!!")
        print(f"{ans[i]} is correct")
    i+=1

    print()