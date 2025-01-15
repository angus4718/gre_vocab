import pandas as pd
import random
import os

# Load the Excel file
file_path = "vocab_list.xlsm"
xls = pd.ExcelFile(file_path)

# List to store known words
known_words_file = "known_words.txt"

# Load known words from file
if os.path.exists(known_words_file):
    with open(known_words_file, 'r') as f:
        known_words = set(f.read().splitlines())
else:
    known_words = set()

# Function to get a random word
def get_random_word():
    all_words = []

    # Iterate over each sheet and collect words
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        words = df.dropna(subset=['Word']).to_dict('records')
        all_words.extend(words)

    # Filter out known words
    unknown_words = [word for word in all_words if word['Word'] not in known_words]

    if not unknown_words:
        print("You know all the words!")
        return None

    # Select a random word
    return random.choice(unknown_words), len(unknown_words)

# Function to mark a word as known
def mark_word_as_known(word):
    known_words.add(word)
    with open(known_words_file, 'w') as f:
        for w in known_words:
            f.write(f"{w}\n")

# Main loop
while True:
    result = get_random_word()
    if result is None:
        break

    word_data, remaining_count = result
    word = word_data['Word']
    print(f"\nDo you know this word? {word}")
    print(f"Vocabulary words remaining: {remaining_count}")

    while True:
        response = input("(1: yes / 2: no / 3: show definitions): ").strip()
        if response in ['1', '2', '3']:
            break
        print("Invalid input. Please enter '1', '2', or '3'.")

    if response == '1':
        mark_word_as_known(word)
    elif response == '2':
        print("No problem, it will appear again.")
    elif response == '3':
        print(f"\nDefinitions and Examples for {word}:")
        for i in range(1, 4):
            pos = word_data.get(f'POS{i}')
            definition = word_data.get(f'Definition{i}')
            example = word_data.get(f'Example{i}')
            if pos and definition:
                print(f"\nPart of Speech {i}: {pos}")
                print(f"Definition {i}: {definition}")
                if example:
                    print(f"Example {i}: {example}")

        # Ask again after showing definitions
        while True:
            final_response = input("Now, do you know this word? (1: yes / 2: no): ").strip()
            if final_response in ['1', '2']:
                break
            print("Invalid input. Please enter '1' or '2'.")

        if final_response == '1':
            mark_word_as_known(word)
        elif final_response == '2':
            print("No problem, it will appear again.")