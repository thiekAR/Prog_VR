# ex. 8.7


def make_album(artist, title, tracks=0):

    if tracks != 0:
        return {'artist': artist, 'title': title, 'tracks': tracks}
    return {'artist': artist, 'title': title}


print(make_album('Bob', 'album1', 9))
print(make_album('Jack', 'album2', 1))
print(make_album('John', 'album3', 4))
print(make_album('Peter', 'album4', 14))


# ex. 8.8

def make_album(artist, title, tracks=0):

    if tracks != 0:
        return {'artist': artist, 'title': title, 'tracks': tracks}

    return {'artist': artist, 'title': title}

while True:
    print('Enter "q" any time to quit')

    artist = input('Enter the  of the artiste: ')

    if artist == 'q':
        break

    album = input('Enter the  of the album: ')

    if album == 'q':
        break

    print(make_album(artist, album))

