import os


def parse_file(text):
    result_list = []
    for line in text:
        result_list.append(line)
    return result_list

directory = 'D:\\files_for_lab\\'
files = os.listdir(directory)
csv=''.join(filter(lambda x: x.endswith('.csv'), files))
print(csv)
name=csv.split(".csv")
for i in range(len(name)-1):
    file = str(directory) + str(name[i]+".csv")
    print(file)
handle = open(file)
# text=parse_file(handle)
print(files)
# print(file)
print(csv)
# print(text)
