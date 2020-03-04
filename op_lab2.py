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
text2 = []
text3 = []
text4 = []
sred = []
spisok = []
name = csv.split(".csv")
my_file = open("D:\\files_for_lab\some.csv", "w+")
print(name)
for i in range(len(name) - 1):
    file = str(directory) + str(name[i] + ".csv")
    handle = open(file)
    text = parse_file(handle)
    for i in range(len(text)):
        text1 = text[i].split(',')
        text2.append(text1)
    for i in range(len(text2)):
        if text2[i][6] == 'FALSE\n':
            text2[i][6] = "FALSE"
            text3.append(text2[i])
for i in range(len(text3)):
    sum = str((int(text3[i][1]) + int(text3[i][2]) + int(text3[i][3]) + int(text3[i][4]) + int(
        text3[i][5])) / 5) + "\n"
    text3[i].append(sum)
