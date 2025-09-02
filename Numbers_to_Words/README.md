
# Number to Words Converter

A Python project to convert integer numbers into their English word representation. It can handle numbers from 0 up to 999,999,999,999.

## Features

* Converts numbers from 0 to 999,999,999,999 into words.
* Handles numbers below 20, tens (20–90), hundreds, thousands, millions, and billions.
* Simple command-line interface for quick usage.
* Easily extensible by updating the `constants.py` file.

## Requirements

* Python 3.6+
* `constants.py` containing three dictionaries/lists:

```python
UNDER_20 = {0: "zero", 1: "one", ..., 19: "nineteen"}
TENS = {2: "twenty", 3: "thirty", ..., 9: "ninety"}
ABOVE_100 = {100: "hundred", 1_000: "thousand", 1_000_000: "million", 1_000_000_000: "billion"}
```

> Make sure the keys and values match the intended number-to-word mapping.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd number-to-words
```

2. Ensure `constants.py` is in the same directory as `num_to_word.py`.

## Usage

Run the script from the command line:

```bash
python num_to_word.py
```

You will be prompted to enter a number:

```
Enter a Number: 123
```

The script will print:

```
one hundred twenty three
```

### Example

```python
from num_to_word import num_to_word

print(num_to_word(56945781))
# Output: fifty six million nine hundred forty five thousand seven hundred eighty one
```

## Project Structure

```
number-to-words/
│
├── num_to_word.py       # Main script with conversion function
├── constants.py         # Number constants
└── README.md            # Project documentation
```

## License

This project is open-source and available under the MIT License.
