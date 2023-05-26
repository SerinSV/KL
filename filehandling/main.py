
log_file = open("serin.log", "r")
start = 0
end = y = int(input("Input the no of lines to read: "))
user_input = 1
while user_input:
    for i in range(start, end):
        print(log_file.readline())
        start = end
        end = end + y
    print("Enter 0 to stop or 1 to continue")
    user_input = (int(input()))
log_file.close()





import typer


def main():
    log_file = open("serin.log", "r")
    lines_of_file = log_file.readlines()
    log_file.close()
    length_of_log_file = len(lines_of_file)
    # print((length_of_log_file))
    # print(lines_of_file)

    start = 0
    no_of_lines_to_read = int(input("Input the no of lines to read: "))
    user_input = 1
    while start < length_of_log_file:
        line = lines_of_file[start:start + no_of_lines_to_read]
        print(line)
        user_input = (int(input("Enter 0 to stop or 1 to continue")))
        if user_input == 0:
            break
        start += no_of_lines_to_read


if __name__ == '__main__':
    typer.run(main)




import typer


def main():
    log_file = open("serin.log", "r")
    lines_of_file = log_file.readlines()
    log_file.close()
    length_of_log_file = len(lines_of_file)
    # print((length_of_log_file))
    # print(lines_of_file)

    start = 0
    end = no_of_lines_to_read = int(input("Input the no of lines to read: "))
    user_input = 1
    while user_input:
        for line in lines_of_file[start:start+end]:
            print(line)

        print("Enter 0 to stop or 1 to continue")
        user_input = (int(input()))


if __name__ == '__main__':
    typer.run(main)
