def write_file(file_name, file_content):
    formatted_file_name = file_name.with_suffix(".txt")
    with open(formatted_file_name, mode = 'w', encoding="utf-8") as text_file:
        text_file.write(file_content)


def append_file(file_name, append_content):
    formatted_file_name = file_name.with_suffix(".txt")
    with open(formatted_file_name, mode = 'a', encoding="utf-8") as text_file:
        text_file.write(append_content)

def read_file(file_name):
    formatted_file_name = file_name.with_suffix(".txt")
    with open(formatted_file_name, mode = 'r', encoding="utf-8") as text_file:
        return text_file.read()

