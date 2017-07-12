import sys


def main():
    path = sys.argv[1]

    with open(path, 'r') as data:
        for d in data:
            print(d)
        # input = data.readlines()

        data.seek(0)
        input = [d.strip() for d in data.readlines()]

        dup_rem_data = set(input)

        print(input)

    with open(path, 'at') as new_data:
        new_data.write('new stuff here\n and more stuff here')


if __name__ == '__main__':
    main()
