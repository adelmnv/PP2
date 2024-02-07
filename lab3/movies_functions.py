def imdb_score(movie):
    return movie["imdb"]>5.5

def movies_sublist_imdb(movies):
    sublist = []
    for movie in movies:
        if imdb_score(movie):
            sublist.append(movie)
    return sublist

def movies_sublist_category(movies,category):
    sublist = []
    for movie in movies:
        if movie["category"] == category:
            sublist.append(movie)
    return sublist

def av_imbd(movies):
    sum_imbd = sum(movie["imdb"] for movie in movies)
    return round(sum_imbd/len(movies),2)

def av_imbd_by_category(movies,category):
    sublist = movies_sublist_category(movies,category)
    return av_imbd(sublist)

def movies_print(movies):
    for movie in movies:
        print('{')
        print(f'"name": "{movie["name"]}",\n"imdb": {movie["imdb"]}\n"category": "{movie["category"]}"')
        print('},')
