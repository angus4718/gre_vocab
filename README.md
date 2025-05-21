# GRE Vocabulary Memorization Tool

This tool is designed to help students preparing for the **GRE** master vocabulary efficiently. It randomly selects words from an Excel file containing your vocabulary list, tracks your progress, and displays helpful definitions and examples to aid memorization.

## Features

- **Random Word Selection**: Picks words randomly from a GRE vocabulary list stored in an Excel file.
- **Track Known Words**: Saves the words you’ve already mastered in a separate file so they don’t appear again.
- **Definitions and Examples**: Shows up to three definitions, parts of speech, and example sentences for each word (if provided in the Excel file).
- **Interactive Learning**: Prompts you to indicate whether you’ve learned a word, ensuring an engaging and personalized experience.

---

## Setup and Requirements

### Prerequisites

1. **Python** (version 3.6 or higher).
2. Required Python libraries:
   - `pandas`
   - `openpyxl` (for handling `.xlsm` Excel files).

Install the required libraries using pip:

```bash
pip install pandas openpyxl
```

### Files Needed

1. **`vocab_list.xlsm`**: The Excel file containing your GRE vocabulary list. Each sheet in the file should include the following columns:
   - `Word` (required): The vocabulary word.
   - `POS1`, `POS2`, `POS3` (optional): The parts of speech for the word.
   - `Definition1`, `Definition2`, `Definition3` (optional): The definitions of the word.
   - `Example1`, `Example2`, `Example3` (optional): Example sentences using the word.

   Example structure:

   | Word       | POS1    | Definition1                          | Example1                       |
   |------------|---------|--------------------------------------|--------------------------------|
   | Abate      | Verb    | To reduce in intensity or amount.    | The storm abated after a day. |
   | Cacophony  | Noun    | Harsh, jarring noise.                | The cacophony of the city...  |

2. **`known_words.txt`** (optional): A text file used to store the words you’ve already learned. If it doesn’t exist, it will be created automatically by the program.

---

## How to Use

1. **Prepare the Vocabulary List**:
   - Ensure your vocabulary list is saved as `vocab_list.xlsm` and placed in the same directory as the script.
   - If you want, you can modify the file name or path in the script by updating the `file_path` variable.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Run the script with:

     ```bash
     python vocab_learning_tool.py
     ```

3. **Interact with the Program**:
   - A random word from the vocabulary list will be displayed, along with the number of unknown words remaining.
   - Choose one of the following options:
     - `1`: Mark the word as "known."
     - `2`: Indicate you don't know the word yet (it will appear again later).
     - `3`: Show definitions and examples for the word (if available).

   After reviewing definitions, you will be asked again if you now recognize the word.

4. **Progress Tracking**:
   - Words marked as "known" are stored in the `known_words.txt` file.
   - The program skips known words when selecting new ones.

---

## Example Usage

### Initial Prompt

```plaintext
Do you know this word? Abate
Vocabulary words remaining: 25
(1: yes / 2: no / 3: show definitions):
```

### If You Select `3` (Show Definitions)

```plaintext
Definitions and Examples for Abate:

Part of Speech 1: Verb
Definition 1: To reduce in intensity or amount.
Example 1: The storm abated after a day.

Now, do you know this word? (1: yes / 2: no):
```

---

## Customizing the Tool

- **Change Vocabulary File**: Update the `file_path` variable to use a different Excel file.
- **Change Progress File**: Update the `known_words_file` variable to save progress to a different file.

---

## Notes

- If you see the message **"You know all the words!"**, congratulations! You’ve mastered every word in your list.
- Ensure your Excel file has a proper `Word` column. Other columns (e.g., `POS`, `Definition`, `Example`) are optional but enhance the learning experience.

---

## License

This tool is free and open-source. Feel free to modify it to suit your needs or contribute improvements!
