## Requirements 
- [x] Django , Heroku , Python , HTML CSS
- [X] DB = SQLITE
- [X] A book is unique based on the google id(volume id obtained using the google API) used in the table BOOKS .
- [X] On adding same book again increase the Quantity 
	 


# Book Browse

A Django app which uses the Google Books API to allow a to user search for and see information about books and store the books in your inventoy.


## Running locally

To install:

* clone this repo
* in your terminal, run:
  
``` 
> brew install python3 #if you don't already have python3
> python3 -m pip install -r requirements.txt
```

To run locally:

``` 
> python3 manage.py runserver
```

## BEFORE USING THE GOOGLE API:
	- [ ] read here - https://developers.google.com/books/docs/v1/using
	- [ ] create google book api key - https://console.developers.google.com/home


## Features Added 
- [x] Home page ; shows search bar to find books , Also shows all the books available .
	  GET : https://book-inventory-library.herokuapp.com/

- [x] Search by title # gives 1st 40 latest results
		GET : https://book-inventory-library.herokuapp.com/listOfPublicBooks/?search_text=Eternals
		url = "https://www.googleapis.com/books/v1/volumes?q=intitle:{}&orderBy=newest&startIndex=0&maxResults=40&key={}".format(search_text,key)
           	response = requests.get(url).json()
		
```
Add the books you want
POST : addBook/<str:GOOGLE_id> 
url = https://www.googleapis.com/books/v1/volumes/zyTCAlFPjgYC
response = requests.get(url).json()](url)
```
- [x] Search by title in library which matches only if book.google_id is same as the google_id of book 
		
		POST: https://book-inventory-library.herokuapp.com/findBooks/    CAN BE CHANGED TO GET 
- [x]  Manually add a book to your inventory 	
			post : localhost:8000/
- [x]  Update a book of your inventory 	(like name , description ,quantity available , author name )	
		GET : https://book-inventory-library.herokuapp.com/update/2
		POST :https://book-inventory-library.herokuapp.com/update/2
- [x]  Delete a book from your inventory 		
		GET:  /delete/<int:id>    html doesn't allow DELETE method 

## Features I'd like to add
- [ ] get a list of 1000 books 
- [ ] Problem : Now  supose the search fetches me only 40 books , and the book I am searching for is not present that is an issue , or if not found in inventory.
- [ ] Search by author
- [ ] Search by genre
- [ ] Filter / sort functionality



