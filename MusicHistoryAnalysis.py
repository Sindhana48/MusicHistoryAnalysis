import json
import itertools
import sys


def read_json_file(filename):
    try:
        with open(filename) as access_json:
            read_content = json.load(access_json)

        return read_content
    except:
        print("File not present. Give correct name and path")

def top_10_songs(read_content):
    songs_dict = {}
    for song in read_content:
        # print (song['title'])
        song_title = song['title'].replace("Watched ", "")
        songs_dict[song_title] = songs_dict.get(song_title, 0) + 1
    value_key_pairs = ((value, key) for (key, value) in songs_dict.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)

    top_10_list = []
    for i in range(0, 10):
        top_10_list.append(sorted_value_key_pairs[:10][i][1])

    return top_10_list


def least_popular(read_content):
    songs_dict = {}
    for song in read_content:
        # print (song['title'])
        song_title = song['title'].replace("Watched ", "")
        songs_dict[song_title] = songs_dict.get(song_title, 0) + 1
    value_key_pairs = ((value, key) for (key, value) in songs_dict.items())
    sorted_value_key_pairs = sorted(value_key_pairs)

    least_popular = []
    for i in range(0, 10):
        least_popular.append(sorted_value_key_pairs[:10][i][1])

    return least_popular



def main():
    #print(sys.argv[1])
    read_content = read_json_file(sys.argv[1])
    top_songs = top_10_songs(read_content)
    least_popular_songs = least_popular(read_content)
    print("----------------------")
    print("The top 10 songs are:")
    print("----------------------")

    [print(i) for i in top_songs]

    print("------------------------------")
    print("The least popular songs are:")
    print("------------------------------")

    for i in least_popular_songs:
        print(i)
    print("------------------------------")

if __name__ == '__main__':
    sys.exit(main())
