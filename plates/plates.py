def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check for length requirement
    if len(s) < 2 or len(s) > 6:
        return False

    # Check for letter requirement at the start
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check for no punctuation, spaces, or periods
    if not s.isalnum():
        return False

    # Check for number requirement at the end
    encountered_digit = False
    for i in range(2, len(s)):
        if s[i].isalpha() and encountered_digit:
            return False
        elif s[i].isdigit():
            if s[i] == '0' and not encountered_digit:
                return False
            encountered_digit = True

    return True

main()
