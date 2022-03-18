from ast import Break
from english_words import english_words_lower_alpha_set
import turtle
import random

#Setting up all the pens for word display
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
curr_pen_height = 100
pengreen = turtle.Turtle()
pengreen.hideturtle()
pengreen.color("green")
pengreen.penup()
pengreen.goto(0, curr_pen_height)
penyellow = turtle.Turtle()
penyellow.hideturtle()
penyellow.color("yellow")
penyellow.penup()
penyellow.goto(0, curr_pen_height)
penwhite = turtle.Turtle()
penwhite.hideturtle()
penwhite.color("white")
penwhite.penup()
penwhite.goto(0, curr_pen_height)
penerror = turtle.Turtle()
penerror.hideturtle()
penerror.color("red")
penerror.penup()
penerror.goto(0, -300)

wn = turtle.Screen()
wn.title("Multi-wordle by Chance")
wn.bgcolor("black")
n = wn.textinput("request", "# of letters")
n = int(n)
Fulllist = list(english_words_lower_alpha_set)
Words = []
for word in Fulllist:
    if len(word) == n:
        Words.append(word)
Correct_word = random.choice(Words)
Avaliablewords = []
pen.clear()
pen.write(f"Letters: {len(Correct_word)}", align="center", font=("Courier New", 32, "normal"))
Total_guess = n + 1

Previous_guesses = list()

while Total_guess > 0:
    pen.clear()
    pen.write(f"Letters: {len(Correct_word)}", align="center", font=("Courier New", 32, "normal"))
    Guess = wn.textinput("Guess box", f"{n} letters")
    Guess = Guess.lower()
    if Guess == Correct_word:
        pengreen.write(f"{Guess}", align="center", font=("Courier New", 32, "normal"))
        pen.clear()
        Total_guess -= 10
    elif (len(Guess) == n and Guess in Words) and (not(Guess in Previous_guesses)):
        counter = 0
        Correct_word_modify = Correct_word
        (Temp_word_white, Temp_word_yellow, Temp_word_green) = ('', '', '')
        while counter < len(Guess):
            if Correct_word[counter] == Guess[counter]:
                Temp_word_white += ' ' 
                Temp_word_yellow += ' '
                Temp_word_green += Guess[counter]
                Correct_word_modify = Correct_word_modify[:counter] + Correct_word_modify[counter + 1:]
            elif Guess[counter] in Correct_word_modify:
                Temp_word_white += ' ' 
                Temp_word_yellow += Guess[counter]
                Temp_word_green += ' '
                Temp_finder = Correct_word_modify.index(Guess[counter])
                Correct_word_modify = Correct_word_modify[:Temp_finder] + Correct_word_modify[Temp_finder + 1:]
            else:
                Temp_word_white += Guess[counter]
                Temp_word_yellow += ' '
                Temp_word_green += ' '
            counter += 1
        penwhite.write(f"{Temp_word_white}", align="center", font=("Courier New", 32, "normal"))
        pengreen.write(f"{Temp_word_green}", align="center", font=("Courier New", 32, "normal"))
        penyellow.write(f"{Temp_word_yellow}", align="center", font=("Courier New", 32, "normal"))
        curr_pen_height -= 50
        pengreen.goto(0, curr_pen_height)
        penyellow.goto(0, curr_pen_height)
        penwhite.goto(0, curr_pen_height)
        Total_guess -= 1
        Previous_guesses.append(Guess)
        penerror.clear()
    else:
        pen.clear()
        penerror.write(f"Invalid Guess", align="center", font=("Courier New", 32, "normal"))


pen.clear()
pen.write(f"Game over, correct word: {Correct_word}", align="center", font=("Courier New", 32, "normal"))

wn.mainloop()