from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    # path('index2/<int:val1>/', views.index2),
    # path ('<int:bookId>/', views.viewbook),
  
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name="books.html5.links"),
 path('html/text/fromatting/', views.formatting, name="books.html5.text.formatting"),
 path('html5/listing/', views.listing, name="books.html5.listing"),
 path('html5/tables/', views.tables, name="books.html5.tables"),
 
]