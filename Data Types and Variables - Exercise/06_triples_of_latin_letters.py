def generate_triples(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    triples = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                triple = alphabet[i] + alphabet[j] + alphabet[k]
                triples.append(triple)
    return triples

def main():
    N = int(input("Enter the value of N: "))
    triples = generate_triples(N)
    for triple in sorted(triples):
        print(triple)

if __name__ == "__main__":
    main()
