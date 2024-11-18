import sys


def add(num1, num2):
    try:
        print(num1 + num2)
    except Exception as e:
        print(e)

def read_file(file_name):
    try:
        file = open(file_name[1])
        for line in file:
            try:
                split = line.split()
                print(float(split[0]) + float(split[1]))
            except ValueError as e:
                print(e)
        file.close()
    except FileNotFoundError as e:
        print(e)
        exit()
if __name__ == '__main__':
    print(sys.argv)
    read_file(sys.argv)
