def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

user_input = input('Enter a word')
output = most_frequent(user_input)

print(output)