from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     # return HttpResponse("Hello, world!")
#     name = request.GET.get("name") or "world!"
#     # return HttpResponse("Hello, "+name)
#     return render(request, "bookmodule/index.html", {"name": name})
# def index2(request, val1 = 0):
#     return HttpResponse("value1 = "+str(val1))
# def viewbook(request, bookId):
#     book1 = {
#         "id": 123,
#         "title": "continuous delivery",
#         "author": "J. Humble and D. Farley",
#     }
#     book2 = {
#         "id": 456,
#         "title": "Secret of Reverse Engineering",
#         "author": "E. Eilam",
#     }
#     targetBook = None
#     if book1["id"] == bookId:
#         targetBook = book1
#     if book2["id"] == bookId:
#         targetBook = book2
#     context = {"book": targetBook}
#     return render(request, "bookmodule/show.html", context)

#lab4
def index(request):
    return render(request, "bookmodule/index3.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

#lab5
def links (request):
    return render(request, "bookmodule/html5/links.html")

def formatting(request):
    return render(request, "bookmodule/html5/text/formatting.html")

def listing (request):
    return render(request, "bookmodule/html5/listing.html")

def tables (request):
    return render(request, "bookmodule/html5/tables.html")

#lab6
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained: newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, "bookmodule/search.html")
    
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

