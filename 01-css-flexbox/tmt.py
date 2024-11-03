tm_class = {
    "jacob" : {"grade": 4, "hair": "brown", "game": "an upsidedown character jumps down instead of up"},
    "ben" : {"grade": 5, "hair": "brown", "game": "a cat runs away from dogs"},
    "aviad" : {"grade": 4, "hair": "brown", "game": "mario runs around"},
    "matan" : {"grade": 4, "hair": "blonde", "game": "there are multiple levels"},
    "zeev" : {"grade": 3, "hair": "brown" , "game": "there are lots of hearts"},
    "nehorai" : {"grade": 5, "hair": "blonde", "game": "I don't know"},
    "yael" : {"grade": 5, "hair": "blonde", "game": "doesn't work"},
    "kira" : {"grade": 5, "hair": "dark blonde", "game": "with kira written in blocks"},
    "shira" : {"grade": 3, "hair": "dark brown", "game": "a cat jumps and collects things"},
}

res_list = ['great', 'good', 'bad']

res = input("Hey! How's it going? [great/good/bad]")

if res == "great":
    print("Wonderful!")
elif res == "good":
    print("cool cool")
elif res == "bad":
    print("Oh no! I hope things get better")
else:
    print("Uh ok.")

name = input("Who am I talking to? What's your name?")
name = name.lower()
grade = tm_class[name]["grade"]
hair = tm_class[name]["hair"]
game = tm_class[name]["game"]
print(f"Oh I know {name}!!!")
print(f"You're kid in grade {grade} with {hair} hair!")

input("Do you know what?")
print()

print(f"I also know you have a cool game where {game}.")
