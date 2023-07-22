#! /usr/bin/env python3


def display_title():
    print("Pig Latin Translator\n")


def get_text():
    return input("Enter text: ")


def convert_to_pig_latin(text):
    vowels = ["a", "e", "i", "o", "u", "y"]

    consonants = ["b", "c", "d", "f", "g", "h", "j",
                  "k", "l", "m", "n", "p", "q", "r",
                  "s", "t", "v", "w", "x", "y", "z"]

    words = text
    words = words.split()

    # If a word starts with a vowel, add way to the end of
    # the word.

    for i in range(len(vowels)):
        index = 0
        for word in words:
            if word.startswith(vowels[i]):
                if vowels[i] == "y":
                    break
                words[index] += "way"
            index += 1

    # If a word starts with a consonant, move all of the
    # consonants that appear before the first vowel to the
    # end of the word, then add ay to the end of the word.

    for j in range(len(consonants)):
        for v in range(len(vowels)):
            index = 0
            for word in words:
                if word.startswith(consonants[j]):
                    vowels_in_word = []
                    for char in word:
                        for i in range(len(vowels)):
                            if char == vowels[i]:
                                if char == "y" and word.startswith("y"):
                                    break
                                vowels_in_word.append(char)

                    if len(vowels_in_word) == 0:
                        return words

                    vowel_index = word.find(vowels_in_word[v])

                    if vowel_index == -1:
                        break

                    prefix = word[:vowel_index]
                    pig_latin_word = word[vowel_index:] + prefix + "ay"
                    words[index] = pig_latin_word

                    if len(words) == 1:
                        return words

                index += 1

    return words


def main():

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        # User input
        text = get_text()

        # Convert to lowercase before translating
        text = text.lower()

        # Remove any punctuation characters before translating
        punct_marks = ".?!',;:""-_[]{}()@/"

        for i in range(len(punct_marks)):
            for char in text:
                if char == punct_marks[i]:
                    text = text.replace(char, "")

        # Display English text
        print(f"English: \t{text}")

        # Convert the English text to Pig Latin
        words = convert_to_pig_latin(text)
        words = " ".join(words)

        # Display Pig Latin text
        print(f"Pig Latin:  {words}")

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
