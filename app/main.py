import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

class Pattern:
    DIGIT = "\d"
    ALNUM = "\w"

# A matcher that works recursively
def matcher(input_line, pattern):
    if not pattern:
        return True
    if not input_line:
        return False

    if pattern[0] == "[" and "]" in pattern:
        closing_idx = pattern.index("]")
        char_class = pattern[1:closing_idx]

        if char_class.startswith("^"):
            return input_line[0] not in char_class[1:] and matcher(input_line[1:], pattern[closing_idx + 1:])
        return input_line[0] in char_class and matcher(input_line[1:], pattern[closing_idx + 1:])
    
    # Handle `+` quantifier
    if len(pattern) > 1 and pattern[1] == "+":  
        char = pattern[0]
        if char == ".":  # If pattern starts with ., match any character
            i = 1
            while i < len(input_line):  # Consume as many chars as possible
                if matcher(input_line[i:], pattern[2:]):  
                    return True
                i += 1
            return False  # If no match found, fail
        
        if input_line[0] != char:  # If first char doesn't match, fail immediately
            return False
        
        i = 1
        while i < len(input_line) and input_line[i] == char:  # Consume multiple occurrences
            i += 1
        
        return matcher(input_line[i:], pattern[2:])  # Continue matching after `+` sequence

    
        # **Handle `?` (zero or one)**
    if len(pattern) > 1 and pattern[1] == "?":
        char = pattern[0]
        # Either skip the char or consume it once
        return matcher(input_line, pattern[2:]) or (input_line[0] == char and matcher(input_line[1:], pattern[2:]))

    # wildcard - '.'
    if pattern[0] == ".":
        return matcher(input_line[1:], pattern[1:])
    
    if pattern.startswith(Pattern.DIGIT):
        return input_line[0].isdigit() and matcher(input_line[1:], pattern[2:])
    
    if pattern.startswith(Pattern.ALNUM):
        return (input_line[0].isalnum() or input_line[0] == "_") and matcher(input_line[1:], pattern[2:])
    
    if pattern[0] == input_line[0]:
        return matcher(input_line[1:], pattern[1:])


    return False  # Do not attempt to shift input when `^` is used


def match_pattern(input_line, pattern):
    if not pattern:
        return True
    if not input_line:
        return False
    
    if pattern == "$":
        return input_line == ""

    if pattern[0] == "^":
        return matcher(input_line, pattern[1:])  # Start matching at beginning only

    if pattern[-1] == "$":
        return matcher(input_line, pattern[:-1]) and len(input_line) == len(pattern) - 1

    # Search for pattern match anywhere in input_line
    for i in range(len(input_line)):
        if matcher(input_line[i:], pattern):
            return True

    return False



def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
