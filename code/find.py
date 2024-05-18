from rich import print
from rich.console import Console
import requests
import json

console = Console()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def find_artist_songs(artist):
    try:
        url = f'http://music.163.com/api/search/get/web?s={artist}&type=1&offset=0&total=true&limit=100'
        response = requests.get(url)
        data = json.loads(response.text)
        for item in data['result']['songs']:
            if artist in [i["name"] for i in item["artists"]]:
                print(item['name']+' - '+"/".join(i['name'] for i in item['artists']))
                print("-----------")
                url = "http://music.163.com/song/"+str(item['id'])
                print("url:", url)
                print("online listen:", "http://music.163.com/song/media/outer/url?id=" + str(item['id']))
                print("id:", item['id'])
                print("-----------")
    except:
        console.print("No songs found for this artist", style="bold red")


def find_artist(artist_id):
    try:
        url = f'http://music.163.com/api/artist/albums/{artist_id}'
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        find_artist_songs(data['artist']['name'])
    except:
        console.print("No artist found with this id", style="bold red")
