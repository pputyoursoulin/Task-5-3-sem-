file = open('data.txt')



try:
    chislo = list(map(int, file.readline().split()))

    if (len(chislo) < 2) or (chislo[0] <= 0):
         print('Error!!! The data in the file is incorrect!')
    else:
        count = 0
        for i in range(len(chislo)):
            if (chislo[i] < 0) or (chislo[i] > 9):
                count += 1
        if count == 0:
            print('Start number: ')
            for i in range(len(chislo)):
                print(chislo[i],end = '')
            print('\n')
            a = int(input('Enter the operation:\n1 - "+1"\n2 - "-1"\n\n'))
            if a == 1:
                chislo[-1] += 1
                for i in range(len(chislo) -1, -1, -1):
                    if chislo[i] == 10:
                        if i == 0:
                            chislo[i] = 0
                            chislo.insert(0, 1)
                        else:
                            chislo[i] = 0
                            chislo[i-1] += 1
                for i in range(len(chislo)):
                    print(chislo[i],end = '')
            else:
                if a == 2:
                    chislo[-1] -= 1
                    for i in range(len(chislo) -1, -1, -1):
                        if chislo[i] == -1:
                            chislo[i] = 9
                            chislo[i-1] -= 1
                    if chislo[0] == 0:
                        chislo.pop(0)
                    for i in range(len(chislo)):
                        print(chislo[i],end = '')
                else:
                    print('Operation entered incorrectly')
        else:
            print('Error!!! The data in the file is incorrect!')
   

    print('\n')
except ValueError:
    print('Error!!! The data in the file is incorrect!')

file.close()