name = input("What is your name: ")
age = input("What is your age: ")
total_words = len(name.replace(" ", ""))

if(not name and not age):
    print('Sorry, you left fields blank')
else:
    print(f'Your name is {name}')
    print(f'Your inverted name is {name[::-1]}')
    if(' ' in name):
        print(f'Your name have space')
    else:
        print(f"Your name haven't space")
    print(f'Your name have {total_words} words')
    print(f'Your first word name is {name[0]}')
    print(f'Your last word name is {name[-1]}')
