def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.lower().count(root_word.lower()) or word.lower() in root_word.lower():
            same_words.append(word)
    return  same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
# Вывод на консоль:['richiest', 'orichalcum', 'richies']
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
# Вывод на консоль:['Able', 'Disable']
print(single_root_words('123_AbC', '123_', '023_abc', '0123_abcd', '123_abd', '_abc'))
# Вывод на консоль:['123_', '0123_abcd', '_abc']