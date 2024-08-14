class Text:
    def __init__(self, text):
        # with open('words-list.txt', 'r') as file:
        # lines = file.readlines()
        data = open(text, 'r')
        text = data.read()
        self.text = text

    def frequency(self, word):
        word = word.lower()
        word_count = 0

        words_in_text = self.text.lower().split()
        word_count += words_in_text.count(word)
        
        if word_count > 0:
            return word_count
        else:
            return None
        
    def common(self):
        word_dict = {}
        words = self.text.lower().split()
        for word in words:
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        
        biggest_word = {'word': '', 'occurances': 0}

        for word in word_dict.keys():
            if word_dict[word] > biggest_word['occurances']:
                biggest_word['word'] = word
                biggest_word['occurances'] = word_dict[word]
        
        return biggest_word

    def all_words(self):
        words = set()
        words_in_text = self.text.lower().split()
        for word in words_in_text:
            words.add(word)

        return list(words)
                


stranger = Text('book.txt')
all_words = stranger.all_words()
common = stranger.common()
work = stranger.frequency('work')

print(len(all_words))
print(common)
print(work)