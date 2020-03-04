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
my_file.close()
