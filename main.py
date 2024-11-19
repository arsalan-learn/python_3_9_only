import sys
from parser import CustomJSONParser

def check_python_version():
    if not (sys.version_info.major == 3 and sys.version_info.minor == 9):
        raise RuntimeError("This project requires Python 3.9. Please use Python 3.9.x.")

def main():
    check_python_version()

    parser = CustomJSONParser()
    json_string = '{"name": "John", "age": 30}'
    print("Input JSON:", json_string)

    try:
        parsed_data = parser.parse(json_string)
        print("Parsed Data:", parsed_data)
    except ValueError as e:
        print("Error parsing JSON:", e)

if __name__ == "__main__":
    main()
