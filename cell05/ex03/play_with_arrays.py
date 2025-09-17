def main():
    x = [2, 8, 9, 48, 8, 22, -12, 2]
    result = [val + 2 for val in x if val > 5]
    result = list(dict.fromkeys(result))
    print(result)

main()
