class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().lower().replace(",", "").replace(".", "").replace("=", "").replace("!", "").replace("?", "").replace(";", "").replace(":", "").replace(" - ", "")
                words = content.split()
                all_words[filename] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        positions = {}
        for filename, words in all_words.items():
            positions[filename] = words.index(word) + 1
        return positions

    def count(self, word):
        all_words = self.get_all_words()
        counts = {}
        for filename, words in all_words.items():
            counts[filename] = words.count(word.lower())
        return counts

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('text')) # 3 слова text в тексте всего