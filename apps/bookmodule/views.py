from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Book
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student, Address, Publisher, Author
from django.utils import timezone
from django.db.models import F, FloatField, ExpressionWrapper
from .form import BookForm

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

#lab7
def add_books(request):
    Book.objects.create(
        title="java concepts",
        author="michael cohen",
        price=54,
        edition=4
    )

    Book.objects.create(
        title="programming concepts",
        author="prof. khan",
        price=87,
        edition=5
    )

    return HttpResponse("Books added successfully!")

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='Learning')

    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index3.html')

# lab 8: 
def task1(request):
    books = Book1.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8/task1.html', {'books': books})

def task2(request):
    books = Book1.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task2.html', {'books': books})

def task3(request):
    books = Book1.objects.filter(
        Q(edition__lte=3) & 
        ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task3.html', {'books': books})

def task4(request):
    books = Book1.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8/task4.html', {'books': books})

def task5(request):
    data = Book1.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        avg=Avg('price'),
        max=Max('price'),
        min=Min('price')
    )
    return render(request, 'bookmodule/lab8/task5.html', {'data': data})

def task7(request):
    # create data:
    # if Student.objects.count() == 0:
    #     addr1 = Address.objects.create(city="Qassim")
    #     addr2 = Address.objects.create(city="Riyadh")
    #     addr3 = Address.objects.create(city="Jeddah")

    #     Student.objects.create(name="Rawan", age=20, address=addr1)
    #     Student.objects.create(name="Sara", age=21, address=addr1)
    #     Student.objects.create(name="Lama", age=22, address=addr2)
    #     Student.objects.create(name="Maha", age=23, address=addr2)
    #     Student.objects.create(name="Nour", age=24, address=addr3)
    #     Student.objects.create(name="Reem", age=25, address=addr3)

    data = Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'bookmodule/lab8/task7.html', {'data': data})

#lab9:
#task1
def task1(request):
    # if Book.objects.count() == 0:
    #     p1 = Publisher.objects.create(name="OReilly", location="USA")
    #     p2 = Publisher.objects.create(name="Pearson", location="UK")

    #     a1 = Author.objects.create(name="Author1")
    #     a2 = Author.objects.create(name="Author2")

    #     b1 = Book.objects.create(
    #         title="Django Basics",
    #         price=100,
    #         quantity=5,
    #         pubdate=timezone.now(),
    #         rating=4,
    #         publisher=p1
    #     )
    #     b1.authors.add(a1)

    #     b2 = Book.objects.create(
    #         title="Python Advanced",
    #         price=150,
    #         quantity=10,
    #         pubdate=timezone.now(),
    #         rating=5,
    #         publisher=p2
    #     )
    #     b2.authors.add(a2)

    # total_books = Book.objects.aggregate(total=Sum('quantity'))['total']

    # books = Book.objects.annotate(
    #     percentage=(F('quantity') * 100.0) / total_books
    # )
    total_books = Book.objects.aggregate(total=Sum('quantity'))['total']

    books = Book.objects.annotate(
        percentage=ExpressionWrapper(
            (F('quantity') * 100.0) / total_books,
            output_field=FloatField()
        )
    )


    return render(request, 'bookmodule/lab9/task1.html', {'books': books})
#task2
def task2(request):
    data = Publisher.objects.annotate(total_books=Sum('book__quantity'))

    return render(request, 'bookmodule/lab9/task2.html', {'data': data})
#task3
def task3(request):
    data = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))

    return render(request, 'bookmodule/lab9/task3.html', {'data': data})
#task4
def task4(request):
    data = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )

    return render(request, 'bookmodule/lab9/task4.html', {'data': data})
# task5
def task5(request):
    data = Publisher.objects.annotate(
        high_rated=Count('book', filter=Q(book__rating__gte=4))
    )

    return render(request, 'bookmodule/lab9/task5.html', {'data': data})
#task6
def task6(request):
    data = Publisher.objects.annotate(
        filtered_books=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )

    return render(request, 'bookmodule/lab9/task6.html', {'data': data})

#lab10
#task1
def list_books_lab9(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1/listbooks.html', {'books': books})

#task2
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            price=price,
            quantity=1,
            rating=1,
            pubdate=timezone.now()
        )

        return redirect('/books/lab9_part1/listbooks/')

    return render(request, 'bookmodule/lab9_part1/addbook.html')
#task3
def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.save()

        return redirect('/books/lab9_part1/listbooks/')

    return render(request, 'bookmodule/lab9_part1/editbook.html', {'book': book})
#task4
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part1/listbooks/')

#part2:
def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2/listbooks.html', {'books': books})

def add_book_form(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks/')

    return render(request, 'bookmodule/lab9_part2/addbook.html', {'form': form})

def edit_book_form(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks/')

    return render(request, 'bookmodule/lab9_part2/editbook.html', {'form': form})

def delete_book_form(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part2/listbooks/')
