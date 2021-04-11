answer = input("Hey Kid!")
prompt = "WHAT?!"
while True:
    if answer == "GOODBYE!":
        answer = input("LEAVING SO SOON?")
        if answer == "GOODBYE!":
            print("LATER, SKATER!")
            break
    if not answer.isupper():
        prompt = "SPEAK UP, KID!"
    elif answer.isupper():
        prompt = "NO, NOT SINCE 1946!"
    answer = input(prompt)
