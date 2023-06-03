def dictComp(stop, step):
    dictionary = {}
    for i in range(stop // step):
        key = "items-{}".format(i)
        values = list(range(i * step, (i + 1) * step))
        dictionary[key] = values
    return dictionary
print(dictComp(10, 4))