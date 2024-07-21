def single_root_words(root_word, *other_words):
    same_words = []
    a = str(root_word.lower())
    other_list = list(other_words)
    other_list = [user.lower() for user in other_list]
    for i in other_list:
        if i.count(a):
            same_words.append(i)
    return same_words


print(single_root_words('Лес', 'Лесопилка', 'Трава', 'Лесополоса', 'Пес'))
