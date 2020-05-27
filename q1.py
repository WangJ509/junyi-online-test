def reverse_word(w):
    return w[::-1]

def reverse_sentence_by_word(s):
    s = s.split(' ')
    ans = []
    for w in s:
        ans.append(reverse_word(w))
    return ' '.join(ans)


s1 = input('Please enter a word: ')
print (reverse_word(s1))

s2 = input('Please enter a sentence: ')
print (reverse_sentence_by_word(s2))
