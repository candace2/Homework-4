print('Spelling Bee is one of a variety of puzzles found in The New York Times Magazine.'"\n")

#spellingBee is a variable hold the tuple of objects.  That is rules of the Spelling Bee game
spellingBee_rules = ('Below is a list of 7 letters called The Hive', 'Use letters in The Hive to spell common words of 5 or more letters',
'Every word spelled must use the letter N at least once', 'Letters may be used more than once in a word', 'At least one word will use all 7 letters',
'Proper nouns and hyphenated words are not allowed', 'Score 1 point for each word spelled with 5 or 6 letters and 3 points for each word that uses all 7 letters')

print('Rules of the Game')
for i in spellingBee_rules:
    print(*"*", i, "\n")

#variable the_hive hold the set of letters that can be used to play Spelling Bee
the_hive = {'A', 'C', 'H', 'N', 'I', 'T', 'Y'}
print('Letters in The Hive are:')
for i in the_hive:
    print(*"*", i,)



print(input('Use letters from The Hive to spell words with 5 or more letters. You must use the letter N.'"\n"))
response = input()


answers_def = {'Hyacinth:': '3 points', 'Antic:': '1 point', 'Attain:': '1 point', 'Cancan:': '1 point', 'Cantata:': '1 point',
'Cantina:': '1 point', 'Chain:' :'1 point', 'Chancy:': '1 point', 'Chant:': '1 point', 'Chianti:': '1 point', 'Cinch:': '1 point',
'Cynic:': '1 point', 'Inanity:': '1 point', 'Intact:': '1 point', 'Nanny:': '1 point', 'Natty:': '1 point', 'Niacin:': '1 point',
'Ninny:': '1 point', 'Ninth:': '1 point', 'Tactician:': '1 point', 'Tahini': '1 point', 'Taint:': '1 point', 'Tannic:': '1 point',
'Tannin:': '1 point', 'Tinny:': '1 point', 'Titan:': '1 point'}

def Diff(response, answers_def):
    return (list(set(response) & set(answers_def))) #returns words that are in The Hive
    return (list(set(answers_def) - set(response))) #returns words that are not in The Hive
print(('The following words you spelled are admissible:') , set(response) & set(answers_def))
print(('The following words you spelled are not admissible:'), set(answers_def) - set(response))
