def create_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def edit_file(filename, new_content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
