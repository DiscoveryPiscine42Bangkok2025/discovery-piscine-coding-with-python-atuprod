#!/usr/bin/env python3
from checkmate_bonus import is_checkmate, is_check

def main():
    boards = [
"""\
R...
.K..
..P.......
....\
""",

"""\
R..Q
.K..
..P.
....\
"""
    ]

    for idx, b in enumerate(boards, start=1):
        print(f"\nBoard {idx}:\n{b}")
        if is_checkmate(b) == True:
            print("Checkmate")
        elif is_checkmate(b) == "Error":
            print("Error")    
        elif is_check(b):
            print("Check")
        else:
            print("Safe")

if __name__ == "__main__":
    main()
