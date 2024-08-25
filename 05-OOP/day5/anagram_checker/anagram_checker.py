class AnagramChecker:
    def __init__(self):
        self.words =  []
        with open('words.txt', 'r') as f:
            for word in f.readlines():
                self.words.append(word.strip())

    def is_valid_word(self, word):
        if word in self.words:
            return True
        else:
            return False
        

    def word_dict(self, word):
        my_word = {}
        for letter in word:
            if letter in my_word:
                my_word[letter] += 1
            else:
                my_word[letter] = 1
        
        return my_word
    
        # If word is 'apple'
        # will return {'a': 1, 'p':2, 'l':1, 'e':1}

    def is_anagram(self, word1, word2):
        word1_dict = self.word_dict(word1)
        word2_dict = self.word_dict(word2)

        if word1_dict == word2_dict:
            return True
        else:
            return False

        # my_word1 = {}
        # for letter in word1:
        #     if letter in my_word1:
        #         my_word1[letter] += 1
        #     else:
        #         my_word1[letter] = 1

        # my_word2 = {}
        # for letter in word2:
        #     if letter in my_word2:
        #         my_word2[letter] += 1
        #     else:
        #         my_word2[letter] = 1

    def get_anagrams(self, word_to_check):
        word_to_check = word_to_check.upper()
        anagrams = []
        for word in self.words:
            if self.is_anagram(word, word_to_check):
                anagrams.append(word)

        return anagrams
