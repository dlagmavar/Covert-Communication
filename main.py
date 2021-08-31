with open('Welcome to CSEC47 Covert Communications.txt', 'r') as file:
    data = file.readlines()

    for line in data:
        tmp = line.replace('\t', '1')
        tmp = tmp.replace(' ', '0')
        tmp = tmp[-8:-1]
        if tmp.isnumeric():
            decimal_representation = int(tmp, 2)
            asc = chr(decimal_representation)
            print(asc)

