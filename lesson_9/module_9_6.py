def all_variants(text):
    for l in range(len(text)):
        for i in range(len(text) - l):
            yield text[i: i + l + 1]


a = all_variants("abc")
for i in a:
    print(i)
