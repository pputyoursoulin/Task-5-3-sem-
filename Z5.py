file = open('data.txt')

try:
    massiv = list(map(int, file.read().split()))

    if len(massiv) < 1:
         print('Error!!! The data in the file is incorrect!')
    else:
         value = massiv[0]
         if massiv.count(value) == len(massiv): print('The sequence consists of identical numbers\n-----')
         else: print('The sequence consists of different numbers\n-----')
except ValueError:
    print('Error!!! The data in the file is incorrect!')

file.close()