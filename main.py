import tmdbsimple as tmdb
import urllib
import os
import string

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

if __name__ == "__main__":

    tmdb.API_KEY = 'x'
    search = tmdb.Movies()
    base = tmdb.Configuration().info().get("images").get("secure_base_url")
    genres = tmdb.Genres().list().get("genres");
    genre_map = {}

    total_pages = 100 #Maxiumum 284 for top_rated, 983 for popular

    #Directory of downloads to be saved. It should be same in reader
    path = "Data"
    if path != "":
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)

    for genre in genres:
        genre_map[genre.get('id')] = genre.get('name')

    for page in range (1,total_pages):
        print ("Page: " + page)
        list = search.top_rated(page=page).get('results') #search.popular() can also be used.
        for movie in list:
            id = movie.get("id")
            b_path = movie.get("backdrop_path")
            poster = movie.get("poster_path")
            genres = movie.get("genre_ids")
            title = movie.get("title")

            '''Title will be folder and filename, so it should not include any special chars.'''
            title = "".join(c for c in title if c in valid_chars)

            if not os.path.exists(title):
                os.makedirs(title)

            f = open(title + '/info.txt', 'w')
            f.write("ID:%s\n" % id)
            f.write("Title:%s\n" % title)
            f.write("Genres:")

            for g in genres:
                f.write(" %s" % genre_map.get(g))

            f.write("\n")
            f.close();

            urllib.urlretrieve(base + '/original' + poster, title +"/original.jpg")
            urllib.urlretrieve(base + '/w780' + poster, title + "/w780.jpg")
            urllib.urlretrieve(base + '/w342' + poster, title + "/w342.jpg")
