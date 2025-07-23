# get number of inputs
N = int(input(""))

# get max cont
group_words = N

# open loop
for _ in range(N):

    # alphabet array to see if word has been used
    alphabet_tracker = {}
    # check if streak
    last_letter = 0

    # get word
    word = input("")

    # read word by letter
    for letter in word:
        # if 1) letter has been used and 2) letter is not on streak
        if letter in alphabet_tracker and last_letter != letter:
            # decrement from group_word
            group_words -= 1
            # move to next word
            break
        
        # if not update last_letter and move to next letter
        else:
            alphabet_tracker[letter] = 1
            last_letter = letter

# print result
print(group_words)