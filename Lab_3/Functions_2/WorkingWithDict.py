def rating(movies):
    for x in movies:
        print(x["name"],end="")
        if x["imdb"] >= 5.5:
            print(" - true")
        else:
            print(" - false")

def goodfilms(movies):
    
    list = []
    for x in movies:
        if x["imdb"] >= 5.5:
            list.append(x["name"])
        else:
            continue
    print(list)

def find(movies):
    nm = str(input("What genre do you need? \n"))
    for x in movies:
        if x["category"] == nm:
            print(x["name"])

def filmimdb(movies):
    list = input("Введите фильмы через запятую + пробел\n").split(", ")
    cnt = 0
    points = 0.0
    for x in movies:
        for y in list:
            if x["name"] == y:
                cnt += 1
                points += x["imdb"]
    print(points / cnt)
    
def categoryimdb(movies):
    cat = str(input())
    cnt = 0
    pnts = 0.0
    for x in movies:
        if x["category"] == cat:
            cnt += 1
            pnts += x["imdb"]
    print(pnts / cnt)
            
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#rating(movies)
#goodfilms(movies)
#find(movies)
#filmimdb(movies)
categoryimdb(movies)