# bookbot

def get_book_text(path):
    # Open the file and return its contents
    with open(path) as f:
        return f.read()

def main():
    # Call get_book_text with the path and print the contents
    path = "books/frankenstein.txt"  # Relative path to the book
    text = get_book_text(path)
    print(text)

# Call the main function
main()
