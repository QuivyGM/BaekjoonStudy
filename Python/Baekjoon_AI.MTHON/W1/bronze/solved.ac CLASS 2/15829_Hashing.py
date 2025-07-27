word_len = int(input())
word_in = input()
word_out = 0
for i, letter in enumerate(word_in):
	word_out += (ord(letter)-96) * (31**i)
    
word_out %= 1234567891
print(word_out)