given_file = open ('given_file.txt')
lines = given_file.readlines()

for line in lines:
    for c in line:
        if c.isdigit() == True:
            print('Integer found: {}'.format(c))

given_file.close()            