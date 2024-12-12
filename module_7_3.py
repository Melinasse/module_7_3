import re

class WordsFinder:
    def __init__(self, *file_names: str):
        self.word = None # Дабавил в itit после метода find, т.к. данный атрибут реализовывается позже
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                box = file.read()
                clear_txt = re.sub(r'[^\w\s-]', '', box.lower()) # 1.По шаблону удаляем знаки препинания, 2.заменяем на пробел, 3.Объект метода (с методом нижнего регистра)
                words = clear_txt.split() #Разделение строки на одинарный отступ (пробел)
            all_words[file_name] = words
        return all_words

    def find(self, word: str):
        self.word = {}
        word = word.lower()
        box_dict = self.get_all_words()
        for file_name, words in box_dict.items():
            for i, w in enumerate(words):
                if w == word:
                    if file_name not in self.word:
                        self.word[file_name] = i + 1
        return self.word
    
    
    def count(self, word: str):
        self.word = {}
        word = word.lower()
        box_dict = self.get_all_words()
        for file_name, words in box_dict.items():
            for w in words:
                if w == word:
                    self.word[file_name] = words.count(w)
        return self.word
        

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

#По результату вывода метода find у 'Rudyard Kipling - If.txt': 107' , вместо 109.
#Не совсем понял почему. Хотя в остальных случаях работает прекрасно.
