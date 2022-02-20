import requests
search = "ravi"
book_ids = []
try:
    key = "AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg"
    #url = "https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg
    url = "https://www.googleapis.com/books/v1/volumes?q={}&startIndex=0&maxResults=30&key={}".format(search,key) # AIzaSyBC3ZEeDEa4uR5tmcQhc0l8gkR-mOst4Rg"
    response = requests.get(url).json()
    total_items =  len(response['items']) #response['totalItems']
    #print(total_items,len(response['items']))
    for i in range(total_items):
        
        #print(response['items'][i]['id'])
        book_ids.append(response['items'][i]['id'])
except Exception as err:
    print("connection failed")   
print(book_ids)     