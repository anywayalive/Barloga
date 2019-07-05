def list_animals(animals):
    list = ''
    i = 0
    for a in animals:
        list += str(i + 1) + '. ' + animals[i] + '\n'
        i+=1
    return list