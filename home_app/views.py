from django.shortcuts import render , HttpResponse ,redirect 
from datetime import datetime
from home_app.models import Book
from django.contrib import messages
import requests

#add a book using google id
def addBook(request,id):
    if request.method == 'POST': 
        try:
            #GET https://www.googleapis.com/books/v1/volumes/zyTCAlFPjgYC
            try:#objects.get  throws error if not found 
                book_ob = Book.objects.get(google_id=id )
                book_ob.qty = book_ob.qty + 1
            except:
                
                url = "https://www.googleapis.com/books/v1/volumes/"+str(id)
                
                response = requests.get(url).json()
                name = response["volumeInfo"]["title"]
                author_name = response["volumeInfo"]["authors"][0]
                desc = response["volumeInfo"]["description"]
                publish_date = response["volumeInfo"]["publishedDate"]
                price = 100
                qty = 1
                google_id = id
                
                book_ob = Book(name=name,author_name=author_name,qty=qty, desc=desc,price=price,date=publish_date,google_id = google_id)
            
            book_ob.save()
            messages.success(request,"Your details are saved")
            
            return redirect("/") # to go to home
        except Exception as err:
            # needed as if requests.get fails
            return HttpResponse("unable to add book ")
    return redirect("/") # to go to home
    
# find books all over world
def list_of_public_books(request):
    #return HttpResponse("search page")
    if request.method == "GET":
        
        total_items = 0
        book_ids = []
        try:
            search = request.GET.get('search_text')
            key = "AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg"
            #url = "https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg
            url = "https://www.googleapis.com/books/v1/volumes?q=intitle:{}&orderBy=newest&startIndex=0&maxResults=40&key={}".format(search,key) # AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg"
            response = requests.get(url).json()
            total_items =  len(response['items'])

            for i in range(total_items):
                try:
                    g_id = response['items'][i]['id']
                    name = response['items'][i]['volumeInfo']["title"]
                    author_name = response['items'][i]['volumeInfo']['authors'][0]
                    d = dict()
                    d["google_id"] =  g_id
                    d["name"] =  name
                    d["author_name"] =  author_name
                    book_ids.append(d)
                except Exception as e:
                    pass   
        except Exception as err:
            print("connection failed",err)        
        return render(request,'list_of_public_books.html',{'all_books':book_ids})
    return redirect("/") # to go to home

# find books in my library
# called from index.html search in inventory search button
def findBooks(request):
    #return HttpResponse("search page")
    if request.method == "POST":
         
        total_items = 0
        book_ids = []
        try:
            search = request.POST.get('search')
            key = "AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg"
            #url = "https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg
            url = "https://www.googleapis.com/books/v1/volumes?q=intitle:{}&orderBy=newest&startIndex=0&maxResults=40&key={}".format(search,key) # AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg"
            response = requests.get(url).json()
            total_items =  len(response['items'])
            for i in range(total_items):
                try:#objects.get  throws error if not found 
                    ob = Book.objects.get(google_id= response['items'][i]['id'] )
                    book_ids.append(ob)
                except:
                    pass    
               
        except Exception as err:
            print("connection failed",err)
        book_ids = set(book_ids)
        return render(request,'findBooks_in_inventory.html',{'all_books':book_ids})
    return redirect("/") # to go to home
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author_name = request.POST.get('author_name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        google_id = request.POST.get('google_id')
        try:#objects.get  throws error if not found 
            book_ob = Book.objects.get(google_id=google_id )
            book_ob.qty = book_ob.qty + 1
        except:    
            book_ob = Book(name=name,author_name=author_name,qty=qty, desc=desc,price=price,date=datetime.today(),google_id=google_id)
        book_ob.save()
        messages.success(request,"Your details are saved")
    messages.success(request,"Your index page")
    
    allBooks = Book.objects.all()
    book_list = []
  

    for i in allBooks:
        i.desc = i.desc[:30] + "....."
        book_list.append(i)
        #book_list.append([i.id,i.name,i.author_name ,i.desc[:3]+"...", i.price,i.date])
        #print(i.id,i.name,i.author_name , i.price,i.desc[:3]+"...",i.date ) 
    #print(allBooks)   
    #return HttpResponse("home app page")
    # return render(request,'library/viewissuedbook.html',{'li':li})
    return render(request,'index.html',{'all_books':book_list})
def delete(request,id):
    #html doesn't allow DEPETE method only POst and get is allowed 
    if True:
        Book.objects.filter(id=id).delete()
        return redirect("/")
    else:
        return HttpResponse("unable to delete ")

def update(request,id):
    #html doesn't allow DEPETE method only POst and get is allowed 
    if request.method == 'POST':
        name = request.POST.get('name')
        author_name = request.POST.get('author_name')
        desc = request.POST.get('desc')
        # if desc is None:
        #     desc = ''
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        google_id = request.POST.get('google_id')
        book  = Book.objects.get(id=id) 
        book.name = name
        book.author_name = author_name
        book.desc = desc
        book.price = price
        book.qty = qty
        book.google_id = google_id
        book.date=datetime.today()
        book.save()
        return redirect("/")
    book_ob  = Book.objects.get(id=id) 
    #print(book_ob,book_ob.name , book_ob.price)
    return render(request,'update.html',{'book':book_ob})


