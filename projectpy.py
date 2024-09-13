from english_words import get_english_words_set
def insert_trie(root, word):

    temp = root
    for char in word:
        if char not in temp:
            temp[char] = {}
        temp = temp[char]
    temp['isEnd'] = True

def build_trie(words):
    trie_root = {}
    for word in words:
        insert_trie(trie_root, word)
    return trie_root

def print_suggestions(root, res, count=0):
    if count == 3:  # Stop when three suggestions have been printed
        return count
    if 'isEnd' in root:
        print(res, end=' ')
        count += 1  # Increment count when a suggestion is printed
        if count == 3:  # Check again after printing
            return count
    for char in root:
        if char != 'isEnd':
            res += char
            count = print_suggestions(root[char], res, count)
            res = res[:-1]
    return count
         

def check_spelling(trie_root, word):
    temp = trie_root
    incomplete_word=''
    if word[0] not in temp:
        print('No word staring with the letter in dicitionary')
        return False
    for char in word:
        if char not in temp:
            print("Incorrect spelling here are some Suggestions:")
            print_suggestions(temp, incomplete_word, 0)
            return False
        temp = temp[char]
        incomplete_word+=char
    if 'isEnd' in temp:
        return True
    print("Incorrect spelling here are some Suggestions:")
    print_suggestions(temp, word, 0)
    return False

'''def main():
    # Set up the dictionary trie
    english_words = get_english_words_set(['web2'], lower=True)
    trie = build_trie(english_words)

    # Continuously prompt for input until the user decides to stop
    while True:
        input_word = input("Enter a word (or type 'stop' to end): ").lower()

        # Check if the user wants to stop
        if input_word == 'stop':
            print("Exiting the spell checker.")
            break

        # Check the spelling
        if check_spelling(trie, input_word):
            print("The word is spelled correctly.")
        else:
            print('\nDo you want to add this word instead?')
            new_word = input("yes or no: ").lower()
            if new_word == 'yes': 
                insert_trie(trie, input_word)
                print("Word is added.")
            else:
                continue  # Continue to the next word if the user doesn't want to add it

        # Optionally, ask if the user wants to check another word immediately
        check_another = input("Do you want to check another word? (yes/no): ").lower()
        if check_another != 'yes':
            print("Exiting the spell checker.")
            break





if __name__ == "__main__":
    main()'''

def main():
    # Set up the dictionary trie
    english_words = get_english_words_set(['web2'], lower=True)
    trie = build_trie(english_words)
    
    # Continuously prompt for input until the user decides to stop
    while True:
        print("\nOptions:")
        print("1. Check spelling")
        print("2. Add word")
        print("3. Delete word")
        print("4. Stop")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            input_word = input("Enter a word to check spelling: ").lower()
            if check_spelling(trie, input_word):
                print("The word is spelled correctly.")
            else:
                print('\nDo you want to add this word instead?')
                new_word = input("yes or no: ").lower()
                if new_word == 'yes': 
                    insert_trie(trie, input_word)
                    print("Word is added.")
        elif choice == '2':
            input_word = input("Enter a word to add to the dictionary: ").lower()
            insert_trie(trie, input_word)
            print("Word is added.")
        elif choice == '3':
            word_to_delete = input("Enter the word to delete from the dictionary: ").lower()
            if word_to_delete in trie:
                # Delete the word from the trie
                del_word(trie, word_to_delete)
                print("Word has been deleted.")
            else:
                print("Word not found in the dictionary.")
        elif choice == '4':
            print("Exiting the spell checker.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def del_word(root, word):
    temp = root
    for char in word:
        if char not in temp:
            return
        temp = temp[char]
    if 'isEnd' in temp:
        del temp['isEnd']
    if len(temp) == 0:
        return True

if __name__ == "__main__":
    main()
