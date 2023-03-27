def cypher(data, offset, alphabet=None):
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z']
    offset = offset % len(alphabet)
    result = ""
    for i in data:
        for j in alphabet:
            if alphabet[alphabet.index(j) + offset] > len(alphabet):
                result += alphabet[alphabet.index(j) + offset - len(alphabet)]
            else:
                result += alphabet[alphabet.index(j + offset)]
        result += i
    return data


print(cypher("lol", 5))
