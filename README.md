# Custom Regex Engine

## Overview
This project implements a lightweight custom grep-like utility with its own regex engine in Python that supports basic pattern matching without using built-in `re` module. The matcher works recursively to process input strings against a defined pattern.

## Features
The engine currently supports:
- **Literal Character Matching**: Matches characters in the pattern exactly.
- **Character Classes**: Supports character sets like `[abc]` and negated sets like `[^abc]`.
- **Wildcard (`.`)**: Matches any single character.
- **Digit (`\d`) and Alphanumeric (`\w`) Shortcuts**:
  - `\d` matches any numeric digit (0-9).
  - `\w` matches any alphanumeric character (a-z, A-Z, 0-9, and `_`).
- **Anchors (`^` and `$`)**:
  - `^` matches the beginning of the string.
  - `$` matches the end of the string.
- **Quantifiers**:
  - `+` (one or more occurrences of a character)
  - `?` (zero or one occurrence of a character)
- **Pattern Searching**: If no `^` anchor is used, the pattern can match anywhere in the string.

## Usage
To use this regex engine, run the script with the following command:
```sh
python script.py -E "pattern"
```
Where:
- `script.py` is the name of your Python file.
- `-E` is required as the first argument.
- `"pattern"` is the regex pattern to match against input from `stdin`.

### Example:
#### Command:
```sh
echo "hello123" | python script.py -E "\w+"
```
#### Output:
Returns exit code `0` (match found) or `1` (no match).

## Updates and Planned Improvements
### Current Focus:
- **Multiple and Nested Backreferences**: Allow references to previously captured groups in patterns (e.g., `(\w+) and \1` should match `word and word`).
- **Group Capturing and Alternation (`|`)**: Implement support for capturing groups `( ... )` and alternatives using `|`.
- **Advanced Character Classes**: Extend support for predefined classes like `\s` (whitespace) and `\b` (word boundaries).
- **Better Error Handling**: Improve handling of malformed patterns (e.g., unmatched brackets or parentheses).

### Future Enhancements:
- **Lookahead and Lookbehind Support**: Enable checking for patterns before or after the current match without consuming characters.
- **Optimized Matching Algorithm**: Improve performance for large strings and complex patterns.
- **Support for `{min,max}` Quantifiers**: Extend quantifier functionality beyond `+` and `?`.

## Contributing
If you’d like to contribute, feel free to submit an issue or pull request.