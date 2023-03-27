def cypher(data, offset, alphabet=None):
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z']
    offset = offset % len(alphabet)
    result = ""
    for i in range(len(data)):
        for j in alphabet:
            if data[i] == j:
                if alphabet.index(j)+5 > len(alphabet)-1:
                    result[i] += alphabet[alphabet.index(j) + offset - len(alphabet)]
                else:
                    result[i] += alphabet[alphabet.index(j + offset)]
    return data


print(cypher("lol", 5))
