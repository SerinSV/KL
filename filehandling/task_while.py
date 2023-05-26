import sys


def main():
    try:
        log_file = open("serin.log", "r")
    except FileNotFoundError:
        print("File not found")
        sys.exit()
    lines_of_file = log_file.readlines()
    log_file.close()
    if not lines_of_file:
        print("Empty File")
        sys.exit()
    length_of_log_file = len(lines_of_file)
    # print((length_of_log_file))
    # print(lines_of_file)
    start = 0
    no_of_lines_to_read = int(input("Input the no of lines to read: "))
    user_input = 1
    while start < length_of_log_file:
        line = lines_of_file[start:start + no_of_lines_to_read]
        print(*line, sep="\n")
        start += no_of_lines_to_read

        if start > length_of_log_file:
            print("The contents of file has ended")
            sys.exit()

        user_input = (int(input("Enter 0 to stop or 1 to continue")))
        if user_input == 0:
            break


if __name__ == '__main__':
    main()
