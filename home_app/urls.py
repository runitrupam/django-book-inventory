from django.urls import path 
from home_app import views

urlpatterns = [
  
    path('',views.index,name='index'),  # list of books home page , add new book ,search for books , search in library 
    path('books/',views.index,name='index'), # list of books home page
    path('delete/<int:id>',views.delete,name='delete'), # delete a book
    path('update/<int:id>',views.update,name='update'), # UPDATE a book
    path('findBooks/',views.findBooks,name='findBooks'), # FIND books in inventory 
    path('listOfPublicBooks/',views.list_of_public_books,name='list_of_public_books'), # list all books world wide
    path('addBook/<str:id>',views.addBook,name='addBook'), # add a book after searching in the web using the google id
]
