import ipdb
class Anagram:

    def __init__(self, word="sets"):
        self.word = word

    def set_word(self):
        return self._word 
    
    def get_word(self, word):
        self._word = word

    word = property(set_word, get_word)

    def match(self, potential_anagrams):
        anagrams = []
        for potential_anagram in potential_anagrams:
            if sorted(list(potential_anagram)) == sorted(list(self._word)):
                anagrams.append(potential_anagram)
        return anagrams


sets = Anagram("sets")
print(sets.match(["sets" , "chicken", "etss"]))