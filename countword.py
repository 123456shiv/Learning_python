text = "apple banana apple cherry banana apple"
words = text.lower().split()
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)