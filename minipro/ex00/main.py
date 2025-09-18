from checkmate import checkmate

def main():
    boards = [
"""\
R...
.K.....
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
""",

"""\
.k..
.P..
....
....\
"""
    ]

    for idx, b in enumerate(boards, start=1):
        print(f"\nTest case {idx}:")
        print(b)
        if checkmate(b) == "Error":
            print("Error")
        

if __name__ == "__main__":
    main()
