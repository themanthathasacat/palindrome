if __name__ == '__main__':
    # Find a palindrom in the list
    words = ["cat", "mom", "tacocat", "dued", "HannaH"]
    for x in words:
        reversed = x[::-1]
        if x == reversed:
           print(x)

