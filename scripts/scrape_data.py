import json
import requests

url = "https://raw.githubusercontent.com/labnol/saregama-carvaan/master/artistes/songs.md"

def extract_url(text):
    return text[text.find("(")+1:text.find(")")]


scrape_data = requests.get(url, stream=True)

songs_data = []

for song_detail in scrape_data.iter_lines():
    data = {}
    if song_detail:
        # print(type(song_detail))
        itr = str(song_detail).split("|")
        data["cover_art"] = extract_url(itr[0])
        data["url"] = extract_url(itr[1])
        data["movie"] = extract_url(itr[2])
        data["artiste"] = extract_url(itr[3])

    songs_data.append(data)

songs_data = songs_data[2:]
# print(songs_data[59])

dump_data = []

for pk in range(1,len(songs_data)+1):
    record = {}
    record["model"] = "songs.Song"
    record["pk"] = pk
    
    cover_art= songs_data[pk-1]["cover_art"]
    url= songs_data[pk-1]["url"]
    movie= songs_data[pk-1]["movie"]
    artiste= songs_data[pk-1]["artiste"]

    record["fields"] = { "cover_art": cover_art, "title": url, "movie":movie, "artiste":artiste  }

    dump_data.append(record)

with open('dump_data_song.json', 'w') as outfile:
    json.dump(dump_data, outfile)
