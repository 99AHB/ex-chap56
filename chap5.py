#chap 5-1
song = """when an eel grabs your arm,
And it causes great harm
That's - a moray"""
song = song.replace('m', 'M')
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

# chap5-3
print("""My kitty cat likes %s
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s.""" % ('roast beef', 'ham', 'head', 'clam'))


