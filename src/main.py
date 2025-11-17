from decouple import config

def print_author():
    author = config('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()
