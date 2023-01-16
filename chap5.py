#chap 5-1
song = """when an eel grabs your arm,
And it causes great harm
That's - a moray"""
song = song.replace(' m', ' M')
print(song)

#chap 5-2
questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]
print(f'Q:{questions[0]}')
print(f'A:{answers[0]}')
print(f'Q:{questions[1]}')
print(f'A:{answers[1]}')
print(f'Q:{questions[2]}')
print(f'A:{answers[2]}')

# chap 5-3
print("""My kitty cat likes %s
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s.""" % ('roast beef', 'ham', 'head', 'clam'))

# chpa 5-4

letter = """
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near any
{animals}.

    Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {procent}% less llikely to have {verbed}

    Thank you for your support.
    Sincerly
    {spokesman}
    {job_title}"""

#chap 5-5
print(format(letter))



