print("Hello, whats your name?")
name = str(input())
king = str("arthur")
king.lower().find('arthur')
if name == king:
    print("My lord forgive me, I did not recognise you!")
else:
    print("Hi Sir", name.capitalize(), "it's very nice to meet you!")