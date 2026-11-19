# Short Library Manager - saves books to books.txt

def load():
    try:
        return [line.strip().split("|") for line in open("books.txt") if line.strip()]
    except FileNotFoundError:
        return []

def save(books):
    with open("books.txt", "w") as f:
        for b in books:
            f.write("|".join(b) + "\n")

def show(books):
    for i, (title, author, status) in enumerate(books, 1):
        print(f"{i}. {title} by {author} ({status})")
    if not books:
        print("No books yet.")

books = load()
while True:
    choice = input("\n1.Add 2.Show 3.Search 4.Update status 5.Delete 6.Quit: ")
    if choice == "1":
        books.append([input("Title: "), input("Author: "), input("Status (want/reading/read): ")])
    elif choice == "2":
        show(books)
    elif choice == "3":
        word = input("Search: ").lower()
        for b in books:
            if word in b[0].lower() or word in b[1].lower():
                print(" - ".join(b))
    elif choice in ("4", "5"):
        show(books)
        n = input("Book number: ")
        if n.isdigit() and 1 <= int(n) <= len(books):
            if choice == "4":
                books[int(n) - 1][2] = input("New status: ")
            else:
                books.pop(int(n) - 1)
        else:
            print("Invalid number.")
    elif choice == "6":
        break
    save(books)
