class WordsFinder:
    """  Класс для поиска слов в текстовых файлах   """

    def __init__(self, *files):
        self.file_names = [f for f in files]

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            all_words[file_name] = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for simbol_for_del in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(simbol_for_del, '')
                    all_words[file_name].extend(line.lower().split())
        return all_words

    def find(self, word):
        all_words = {}
        for name, words in self.get_all_words().items():
            all_words[name] = words.index(word.lower()) + 1
        return all_words

    def count(self, word):
        all_words = {}
        for name, words in self.get_all_words().items():
            all_words[name] = words.count(word.lower())
        return all_words


if __name__ == '__main__':
    # finder2 = WordsFinder('test_file.txt')
    # print(finder2.get_all_words())  # Все слова
    # print(finder2.find('TEXT'))  # 3 слово по счёту
    # print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
