from checkmate import checkmate

def main():
    boards = [
"""\
R...
.K..
..P.
....\
""", 

"""\
..
.K\
""",

"""\
B...
.K..
....
....\
""",  

"""\
Q...
.K..
....
....\
""",

"""\
....
.P..
.K..
....\
""",

"""\
....
.P..
K...
....\
"""
    ]

    for idx, b in enumerate(boards, start=1):
        print(f"\nTest case {idx}:")
        print(b)
        checkmate(b)

if __name__ == "__main__":
    main()
