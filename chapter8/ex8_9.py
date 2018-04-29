def show_magicians(magicians):
    if magicians:
        for magician in magicians:
            print(magician.title())
    else:
        print("No magician in the list!")

def make_great(magicians):
    i = 0
    if magicians:
        for magician in magicians:
            magicians[i] = "The great " + magician
            i += 1
    else:
        print("No magician in the list!")
    return magicians
    
magicians = ['damon tan','alice gao']
show_magicians(magicians)

magicians_copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_copy)
