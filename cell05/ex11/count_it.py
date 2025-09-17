import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    params = sys.argv[1:]
    print("parameters:", len(params))
    for p in params:
        print(f"{p}: {len(p)}")

main()
