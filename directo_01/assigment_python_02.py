# ex. 8.7


def make_album(artist_name, title_name, tracks = 0):

    if tracks != 0:
        return {'artist': artist_name, 'title': title_name, 'tracks': tracks}
    return {'artist': artist_name, 'title': title_name}


print(make_album('Bob', 'album1', 9))
print(make_album('Jack', 'album2', 1))
print(make_album('John', 'album3', 4))
print(make_album('Peter', 'album4', 14))


# ex. 8.8

def make_album(artist_name, title_name, tracks = 0):

    if tracks != 0:
        return {'artist': artist_name, 'title': title_name, 'tracks': tracks}

    return {'artist': artist_name, 'title': title_name}

while True:
    print('Enter "q" any time to quit')

    artist_name = input('Enter the  of the artiste: ')

    if artist_name == 'q':
        break

    album = input('Enter the  of the album: ')

    if album == 'q':
        break

    print(make_album(artist_name, album))