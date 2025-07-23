if __name__ == "__main__":
    sentence = input().strip()
    
    if sentence == "":
        print(0)
    else:
        words = sentence.split()
        print(len(words))