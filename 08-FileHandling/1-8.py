def read_from_file(filename):
    with open(filename) as file:
        content=file.read()
    return content

file_content=read_from_file("pets.txt")
words=file_content.split()
print(words)
total=len(words)
print(f"Number of words is: {total}")