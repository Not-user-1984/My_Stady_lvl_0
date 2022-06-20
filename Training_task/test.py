def practicum():
    args = {
        0: 'Практикум',
        1: 'Яндекс',
    }
    args[0] = 'Яндекс'
    args[1] = 'Практикум'
    return [a for a in args.keys()]

print(practicum()) 