# This program asks Gollum's riddles and the user provides answers.
# If the answer is correct, the user procedes to the next question.
# If the answer is wrong, the user is given another chance to answer the question.
# The program ends when all riddles are solved.

while True:
    print("What has roots as nobody sees,")
    print("Is taller than trees,")
    print("Up, up it goes,")
    print("And yet never grows?")
    line1 = input(">")
    if line1.startswith("mount") or line1.startswith("Mount"):
        print()
        print(line1, "precious! She gots it! But we will get her on the next one:")
        print()
        break
    else:
        print()
        print("No, that is not it my love. Gollum, Gollum.")
        print()
        print("Try again.")
        print()
while True:
    print("Voiceless it cries,")
    print("Wingless flutters,")
    print("Toothless bites,")
    print("Mouthless mutters.")
    line2 = input(">")
    if line2 == "wind" or line2 == "Wind":
        print()
        print(line2 + "!", "Trixy she is, my love! Lets try another one:")
        print()
        break
    else:
        print()
        print("A dumb, fat hobbit she is, precious!")
        print()
while True:
    print("It cannot be seen, cannot be felt,")
    print("Cannot be heard, cannot be smelt.")
    print("It lies behind stars and under hills,")
    print("And empty holes it fills.")
    print("It comes out first and follows after,")
    print("End life, kills laughter.")
    line3 = input(">")
    if line3.startswith("dark") or line3.startswith("Dark"):
        print()
        print(line3 + ",", "she knows it well! Too well, precious.")
        print()
        break
    else:
        print()
        print("He he he heeee!! She is ours now, my love!")
        print()
while True:
    print("Alive without breath,")
    print("As cold as death;")
    print("Never thirsty, ever drinking,")
    print("All in mail, never clinking.")
    line4 = input(">")
    if line4 == "fish" or line4 == "Fish":
        print()
        print("Hrmmhpp! Stinky fish! She will never get the last one, my love.")
        print()
        break
    else:
        print()
        print("We got her at last, precious! Now what should we do with her?")
        print()
while True:
    print("This thing all things devour;")
    print("Birds, beasts, trees, flowers;")
    print("Gnaws iron, bites steel;")
    print("Grinds hard stones to meal;")
    print("Slays kings, ruins towns,")
    print("And beats mountains down.")
    line5 = input(">")
    if line5 == "Time" or line5 == "time":
        print()
        print("Oh no, precious! She has done it! She beats us!")
        print()
        break
    else:
        print()
        print("Beaten her we have, precious. Now its time we EATS her!")
        print()
