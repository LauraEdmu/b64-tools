import base64
import re
import mimetypes

def remove_prefix(base64_string):
    pattern = re.compile(r'data:[\w/]+;base64,')
    return pattern.sub('', base64_string)

def encode_file_to_base64(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        raise ValueError("Could not determine the file's MIME type.")
    
    with open(file_path, "rb") as file:
        base64_string = base64.b64encode(file.read()).decode('utf-8')
    return f"data:{mime_type};base64,{base64_string}"

def decode_base64_to_file(base64_string, output_path):
    base64_data = remove_prefix(base64_string)
    file_data = base64.b64decode(base64_data)
    with open(output_path, "wb") as file:
        file.write(file_data)

def main():
    action = input("Do you want to encode or decode? (Enter 'encode' or 'decode'): ").strip().lower()
    if action == 'encode':
        file_path = input("Enter the path to the file: ").strip()
        output_file = input("Enter the output file name for the text file: ").strip()
        base64_string = encode_file_to_base64(file_path)
        with open(output_file, "w") as text_file:
            text_file.write(base64_string)
        print("Base64 encoded string:")
        print(base64_string)
    elif action == 'decode':
        input_method = input("Do you want to paste the Base64 string or specify a file? (Enter 'paste' or 'file'): ").strip().lower()
        if input_method == 'paste':
            base64_string = input("Enter the Base64 encoded string: ").strip()
        elif input_method == 'file':
            base64_file = input("Enter the path to the file containing the Base64 string: ").strip()
            with open(base64_file, "r") as file:
                base64_string = file.read().strip()
        else:
            print("Invalid input method. Please enter 'paste' or 'file'.")
            return
        output_file = input("Enter the output file name for the file: ").strip()
        decode_base64_to_file(base64_string, output_file)
        print(f"File saved as {output_file}")
    else:
        print("Invalid action. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
