def book_on_shelf(book_name):
    if book_name in book_list:
        return True
    else:
        return False


def valid_index(index):
    if 0 <= index < len(book_list):
        return True
    else:
        return False

def print_books():
    print(", ".join(book_list))

book_list = input().split("&")

while True:
    command = input().split(" | ")
    command_type = command[0]
    if len(command) > 1:
        book_name = command[1]
    if command_type == "Add Book":
        if not book_on_shelf(book_name):
            book_list.insert(0, book_name)
    elif command_type == "Take Book":
        if book_on_shelf(book_name):
            book_list.remove(book_name)
    elif command_type == "Swap Books":
        first_book = command[1]
        second_book = command[2]
        if book_on_shelf(first_book) and book_on_shelf(second_book):
            first_book_index = book_list.index(first_book)
            second_book_index = book_list.index(second_book)
            book_list[first_book_index], book_list[second_book_index] =\
                book_list[second_book_index], book_list[first_book_index]
    elif command_type == "Insert Book":
        if not book_on_shelf(book_name):
            book_list.append(book_name)
    elif command_type == "Check Book":
        index = int(command[1])
        if valid_index(index):
            print(book_list[index])
    elif command_type == "Done":
        print_books()
        break
