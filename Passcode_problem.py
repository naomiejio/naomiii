def enter_word():
    word = input("Enter a word: ")
    word = word.upper()
    return word


def space(word):
    space_in_word = word.find(" ")
    return space_in_word


def words(space_in_word, word):
    word1 = word[0:space_in_word]
    word2 = word[space_in_word + 1:]
    return word1, word2



def check_vowels(pass_code, vowels, word):
      
    count = 0
    for each in word:
        if each == " ":
            count = -1
        elif each in vowels:
            pass_code = pass_code + str(count)
        count = count + 1

    return pass_code


def main():
    passcode = ""
    word = enter_word()
    vowels = "A" "E" "I" "O" "U"
    #space_in_word = space(word)
    #word1, word2 = words(space_in_word, word)
    pass_code = check_vowels(passcode, vowels, word)
    #pass_code = check_vowels(pass_code, vowels, word2)
    print(f"Your passcode is {pass_code}")


main()