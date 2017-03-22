import os

if __name__ == "__main__":

    path = "Data"
    if path != "":
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)


    list = []

    for subdir, dirs, files in os.walk(os.path.abspath(path)):
        for dir in dirs:
            print dir
            movie_map = {}
            f = open(subdir + "/" + dir + '/info.txt', 'r')
            id = f.readline()
            title = f.readline()
            genres = f.readline()
            genres = genres[genres.index(":")+1:].strip().split()
            f.close()

            movie_map['id'] = id
            movie_map['title'] = title
            movie_map['genre'] = genres

            movie_map['original'] = ""
            movie_map['w342'] = ""
            movie_map['w780'] = ""

            if os.path.isfile(subdir + "\\" + dir + '\original.jpg'):
                movie_map['original'] = subdir + "\\" + dir + '\\original.jpg'

            if os.path.isfile(subdir + "\\" + dir + '\\w342.jpg'):
                movie_map['w342'] = subdir + "\\" + dir + '\\w342.jpg'

            if os.path.isfile(subdir + "\\" + dir + '\\w780.jpg'):
                movie_map['w780'] = subdir + "\\" + dir + '\\w780.jpg'
            list.append(movie_map)


