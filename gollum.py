# This program asks Gollum's riddles and the user provides answers.
# If the answer is correct, the user procedes to the next question.
# If the answer is wrong, the user is given another chance to answer the question.
# The program ends when all riddles are solved.

while True:
    riddle1 = "What has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows?"
    print(riddle1)
    line1 = input(">")
    if line1.startswith("mount") or line1.startswith("Mount"):
        print()
        print(line1, "precious! She gots it! But we will get her on the next one:\n")
        break
    else:
        print("\nNo, that is not it my love. Gollum, Gollum.\n")
        print("Try again.\n")
while True:
    riddle2 = "Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters."
    print(riddle2)
    line2 = input(">")
    if line2 == "wind" or line2 == "Wind":
        print()
        print(line2 + "!", "Trixy she is, my love! Lets try another one:\n")
        break
    else:
        print("\nA dumb, fat hobbit she is, precious!\n")
while True:
    riddle3 = ("It cannot be seen, cannot be felt,\nCannot be heard, cannot be smelt.\nIt lies behind stars and under hills,\nAnd empty holes it fills.\nIt comes out first and follows after,\nEnd life, kills laughter.")
    print(riddle3)
    line3 = input(">")
    if line3.startswith("dark") or line3.startswith("Dark"):
        print()
        print(line3 + ",", "she knows it well! Too well, precious.\n")
        break
    else:
        print("\nHe he he heeee!! She is ours now, my love!\n")
while True:
    riddle4 = "Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail, never clinking."
    print(riddle4)
    line4 = input(">")
    if line4 == "fish" or line4 == "Fish":
        print("\nHrmmhpp! Stinky fish! She will never get the last one, my love.\n")
        break
    else:
        print("\nWe got her at last, precious! Now what should we do with her?\n")
while True:
    riddle5 = "This thing all things devour;\nBirds, beasts, trees, flowers;\nGnaws iron, bites steel;\nGrinds hard stones to meal;\nSlays kings, ruins towns,\nAnd beats mountains down."
    print(riddle5)
    line5 = input(">")
    if line5 == "Time" or line5 == "time":
        print("\nOh no, precious! She has done it! She beats us!\n")
        break
    else:
        print("\nBeaten her we have, precious. Now its time we EATS her!\n")
