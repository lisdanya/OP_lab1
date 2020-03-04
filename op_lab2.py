import os


def parse_file(text):
    result_list = []
    for line in text:
        result_list.append(line)
    return result_list


def Shell(A):
    t = int(len(A) / 2)
    while t > 0:
        for i in range(len(A) - t):
            j = i
            while j >= 0 and A[j][7] < A[j + t][7]:
                A[j][7], A[j + t][7] = A[j + t][7], A[j][7]
                j -= 1
        t = int(t / 2)
    return A


directory = 'D:\\files_for_lab\\'
files = os.listdir(directory)
csv = ''.join(filter(lambda x: x.endswith('.csv'), files))
print(csv)
name = csv.split(".csv")
for i in range(len(name) - 1):
    file = str(directory) + str(name[i] + ".csv")
    print(file)
handle = open(file)
text = parse_file(handle)
print(files)
print(file)
print(text)

text2 = []
for i in range(len(text)):
    text1 = text[i].split(',')
    text2.append(text1)
print(text2)

print('\n')
text3 = []
for i in range(len(text2)):
    if text2[i][6] == 'FALSE\n':
        text2[i][6] = 'FALSE'
        text3.append(text2[i])
print(text3)

print('\n')
for i in range(len(text3)):
    sum = (int(text3[i][1]) + int(text3[i][2]) + int(text3[i][3]) + int(text3[i][4]) + int(
        text3[i][5])) / 5
    text3[i].append(sum)
print(text3)

print('\n')
b = Shell(text3)
print(b)

jopa = int(len(text3) * 0.4)

text4 = []
print('\n')
for i in range(jopa):
    text4.append(text3[i])
print(text4)

sred = []
for i in range(len(text4)):
    sred.append(text4[i][7])
print(sred)
print(min(sred))

spisok = []
print('\n')
for i in range(len(text4)):
    text5 = ''
    for j in range(8):
        text5 += str(text4[i][j]) + ','
    spisok.append(text5)
print(spisok)

my_file = open("D:\\files_for_lab\some.csv", "w")
for i in range(len(spisok)):
    my_file.write(spisok[i])
my_file.close()
