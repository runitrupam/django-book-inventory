# Book Browse

A Django app which uses the Google Books API to allow a to user search for and see information about books.


## Running locally

To install:

* clone this repo
* in your terminal, run:
  
``` 
> brew install python3 #if you don't already have python3
> python3 -m pip install -r requirements.txt
```

To run locally:

  ``` sh
  > python3 manage.py runserver
  ```

## Features Added 
- [ ] Home page ; shows search bar to find books , Also shows all the books available .
	  GET : https://book-inventory-library.herokuapp.com/

- [ ] Search by title , gives 1st 40 latest results
		GET : https://book-inventory-library.herokuapp.com/listOfPublicBooks/?search_text=Eternals
		--> Add the books you want
		POST : addBook/<str:GOOGLE_id> 
- [ ] Search by title in library which matches only if book.google_id is same as the google_id of book 
		Problem : supose the search fetches me only 50 books , and the book I am searching for is not present .
		POST: https://book-inventory-library.herokuapp.com/findBooks/    CAN BE CHANGED TO GET 
_ [ ] Manually add a book to your inventory 	
			post : localhost:8000/
_ [ ] Update a book of your inventory 	(like name , description ,quantity available , author name )	
		GET : https://book-inventory-library.herokuapp.com/update/2
		POST :https://book-inventory-library.herokuapp.com/update/2
_ [ ] Delete a book from your inventory 		
		GET:  /delete/<int:id>    html doesn't allow DELETE method 

## Features I'd like to add
- [ ] get a list of 1000 books 
- [ ] Search by author
- [ ] Search by genre
- [ ] Filter / sort functionality



