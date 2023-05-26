import sys
from time import sleep


class BookReading:
    def read_log_file(self, name_of_file, log_file, lines_to_read):
        lines_of_file = log_file.readlines()
        log_file.close()
        if not lines_of_file:
            print(f"Error: The file {name_of_file} is empty.")
            sys.exit()
        length_of_log_file = len(lines_of_file)
        start = 0
        no_of_lines_to_read = lines_to_read
        if no_of_lines_to_read:
            print(f"Initiating reading from {name_of_file}")
            print("\n")
            sleep(1)
            user_input = "yes"
            while user_input:
                for line in lines_of_file[start:start + no_of_lines_to_read]:
                    print(line)
                start += no_of_lines_to_read
                if start > length_of_log_file:
                    print(f"\nThe contents of {name_of_file} has ended")
                    sys.exit()
                user_input = input(f"Enter \'no\' to stop or \'yes\' to continue reading from {name_of_file}: ")
                print("\n")
                if user_input == "no":
                    break
                else:
                    print("invalid entry")
                    break
        else:
            for line in lines_of_file:
                print(line)
            sys.exit()
