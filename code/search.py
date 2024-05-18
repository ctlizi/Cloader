from rich import print
import requests
import json
from rich.console import Console

console = Console()


# 搜索歌曲
def search_song(keyword):
    try:
        url = f'http://music.163.com/api/search/get/web?s={keyword}&type=1&offset=0&total=true&limit=100'
        response = requests.get(url)
        data = json.loads(response.text)
        for item in data['result']['songs']:
            if item['name'] in keyword or keyword in item['name']:
                console.print(item['name'] + ' - ' + "/".join(i['name'] for i in item['artists']), style="bold yellow")
                print("-----------")
                print("url:", "http://music.163.com/song/" + str(item['id']))
                print("online listen:", "http://music.163.com/song/media/outer/url?id=" + str(item['id']))
                print("id:", item['id'])
                print("-----------")
    except:
        console.print("No results found", style="bold red")


# 搜索歌手
def search_singer(keyword):
    try:
        url = f'http://music.163.com/api/search/get/web?s={keyword}&type=100&offset=0&total=true&limit=100'
        response = requests.get(url)
        data = json.loads(response.text)
        for item in data['result']['artists']:
            if item['name'] in keyword or keyword in item['name']:
                console.print(item['name'], style="bold yellow")
                print("-----------")
                print("url:", "http://music.163.com/artist/" + str(item['id']))
                print("id:", item['id'])
                print("-----------")
    except:
        console.print("No results found", style="bold red")
