import os


def parse_file(text):
    result_list = []
    for line in text:
        result_list.append(line)
    return result_list

directory = 'D:\\files_for_lab\\'
files = os.listdir(directory)
csv = ''.join(filter(lambda x: x.endswith('.csv'), files))
file = str(directory) + str(csv)
handle = open(file)
text=parse_file(handle)
print(directory)
print(files)
print(file)
print(csv)
print(text)
