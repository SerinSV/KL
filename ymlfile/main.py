import sys
import yaml
import read_lines


def main():
    try:
        with open("config.yml", "r") as ymlfile:
            file_contents = yaml.safe_load(ymlfile)
    except FileNotFoundError:
        print("File not found")
        sys.exit()

    username = input("Enter username : ")
    password = input("Enter password : ")

    response = credential_verification(username, password)
    if response != "success":
        print(response)
        sys.exit()
    else:
        print("User credentials are verified")
        print("Login successful")
        print("\n")

    read_obj = read_lines.BookReading()
    name_of_file = file_contents.get("file_to_read")
    lines_to_read = file_contents.get("number_of_lines_to_read")
    if name_of_file:
        try:
            with open(f"Books/{name_of_file}", "r") as contents_of_log_file:
                file_content = read_obj.read_log_file(name_of_file, contents_of_log_file, lines_to_read)

        except Exception as e:
            print("file not found", str(e))


def credential_verification(username, password):
    expected_username = "serin"
    expected_password = "123"

    if expected_username != username and expected_password != password:
        return "invalid credentials, please try again"
    elif expected_username != username:
        return "invalid username, please try again"
    elif expected_password != password:
        return "invalid password, please try again"
    else:
        return "success"


if __name__ == '__main__':
    main()
