import sys


def main(start=0, previous_count=0):
    log_file = open("serin.log", "r")
    lines_of_file = log_file.readlines()
    log_file.close()
    length_of_log_file = len(lines_of_file)
    no_of_lines_to_read = int(input("Input the no of lines to read: "))
    if previous_count + no_of_lines_to_read > length_of_log_file:
        print("Error:index out of range")
        sys.exit()
    no_of_lines_to_read = previous_count + no_of_lines_to_read
    while start < no_of_lines_to_read:
        line = lines_of_file[start]
        print(line)
        start += 1
    user_input = (int(input("Enter 0 to stop or 1 to continue")))
    if user_input == 0:
        sys.exit()
    else:
        main(start=start, previous_count=no_of_lines_to_read)


if __name__ == '__main__':
    main()
