from django.shortcuts import render, redirect

def home(request, anything=None):
    return render(request, "home.html")

def writers(request, anything=None):
    writer = request.GET.get("writers")
    year = request.GET.get("year")

    if writer and year:
        books = []

        for place, book in top_books.items():
            if (
                writer == "Hemingway"
                and book["author"] == "Эрнест Хемингуэй"
                and book["year"] == int(year)
            ):
                books.append((place, book))

            elif (
                writer == "Shakespeare"
                and book["author"] == "Уильям Шекспир"
                and book["year"] == int(year)
            ):
                books.append((place, book))

        if books:
            return render(request, "writers/books_by_year.html", {
                "books": books,
                "writer": writer,
                "year": year,
            })

        if writer == "Hemingway":
            return redirect("Hemingway")

        if writer == "Shakespeare":
            return redirect("Shakespeare")

    return render(request, "writers.html")

def writers_hemingway(request):
    return render(request, "writers/writers_hemingway.html")

def writers_shakespeare(request):
    return render(request, "writers/writers_shakespeare.html")

def books(request):
    print("BOOKS VIEW")
    return render(request, "books.html", {"top_books": top_books})

top_books = {
    1: {
        "slug": "The_Old_Man_and_the_Sea",
        "title": "Старик и море",
        "author": "Эрнест Хемингуэй",
        "year": 1952
    },

    2: {
        "slug": "Hamlet",
        "title": "Гамлет",
        "author": "Уильям Шекспир",
        "year": 1601
    },

    3: {
        "slug": "For_Whom_the_Bell_Tolls",
        "title": "По ком звонит колокол",
        "author": "Эрнест Хемингуэй",
        "year": 1940
    },

    4: {
        "slug": "Macbeth",
        "title": "Макбет",
        "author": "Уильям Шекспир",
        "year": 1606
    },

    5: {
        "slug": "A_Farewell_to_Arms",
        "title": "Прощай, оружие!",
        "author": "Эрнест Хемингуэй",
        "year": 1929
    },

    6: {
        "slug": "King_Lear",
        "title": "Король Лир",
        "author": "Уильям Шекспир",
        "year": 1605
    },

    7: {
        "slug": "Othello",
        "title": "Отелло",
        "author": "Уильям Шекспир",
        "year": 1604
    },

    8: {
        "slug": "The_Sun_Also_Rises",
        "title": "И восходит солнце",
        "author": "Эрнест Хемингуэй", 
        "year": 1926
    },

    9: {
        "slug": "Romeo_and_Juliet",
        "title": "Ромео и Джульетта",
        "author": "Уильям Шекспир",
        "year": 1595
    },

    10: {
        "slug": "The_Merchant_of_Venice",
        "title": "Венецианский купец",
        "author": "Уильям Шекспир",
        "year": 1596
    }    
}

def book_place(request, place):
    if place not in top_books:
        return redirect("books")

    return render(request, "books/book_place.html", {
        "place": place,
        "book": top_books[place]
    })

def writers_hemingway(request):
    hemingway_books = []

    for book in top_books.values():
        if book["author"] == "Эрнест Хемингуэй":
            hemingway_books.append(book)

    return render(request, "writers/writers_hemingway.html", {
        "books": hemingway_books
    })

def hemingway_books(request, slug):
    for place, book in top_books.items():
        if book["author"] == "Эрнест Хемингуэй" and book["slug"] == slug:
            return render(request, "books/book_place.html", {"place": place, "book": book})

    return redirect("Hemingway")

def writers_shakespeare(request):
    shakespeare_books = []

    for book in top_books.values():
        if book["author"] == "Уильям Шекспир":
            shakespeare_books.append(book)

    return render(request, "writers/writers_shakespeare.html", {
        "books": shakespeare_books
    })

def shakespeare_books(request, slug):
    for place, book in top_books.items():
        if book["author"] == "Уильям Шекспир" and book["slug"] == slug:
            return render(request, "books/book_place.html", {"place": place, "book": book})

    return redirect("Shakespeare")