from anagram_checker import AnagramChecker

def main():
    while True:
        print("""
Welcome to the Anagram Checker!
Type in a word to find its anagram!!!
[type 1 to quit]
            """)
        
        word = input(">>> ")
        if word == '1':
            break
        ana = AnagramChecker()
        anagrams = ana.get_anagrams(word)
        print(anagrams)


if __name__ == '__main__':
    main()