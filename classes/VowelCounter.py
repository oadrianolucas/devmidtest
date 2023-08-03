class VowelCounter:
    def count_vowels(sentence):
        vowels = "aeiouAEIOU"
        vowel_count = 0

        for char in sentence:
            if char in vowels:
                vowel_count += 1

        return vowel_count

    def main():
        sentence = input("Enter a sentence: ")
        num_vowels = VowelCouter.count_vowels(sentence)

        print(f"The sentence has {num_vowels} vowel(s).")


