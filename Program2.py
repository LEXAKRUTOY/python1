def reverse_words(words):
    return words[::-1]

def sort_words_by_length(words):
    return sorted(words, key=len)

user_words = input("Введите список слов: ")
words = user_words.split()
reversed_words = reverse_words(words)
sorted_words = sort_words_by_length(words)

user_menu = input("1 или 2: ")
if user_menu == "1":
    print(f"Слова в обратном порядке: {reversed_words}")
elif user_menu == "2":
    print(f"Сортировка слов по длине: {sorted_words}")
else:
    print("Я узбек")