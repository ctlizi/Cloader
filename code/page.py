from rich import print
from rich.console import Console
import download
import search
import find
import os

console = Console()


def page_main():
    if not os.path.exists("./music"):
        os.mkdir("./music")
    console.rule("[bold red]Cloader[/bold red]", style="bold red")
    print("[1] 网易云音乐[bold yellow]链接[/bold yellow]下载")
    print("[2] 网易云音乐[bold yellow]ID[/bold yellow]下载")
    print("[3] 搜索[bold yellow]歌曲[/bold yellow]")
    print("[4] 搜索[bold yellow]歌手[/bold yellow]")
    print("[5] 查询[bold yellow]歌手歌曲[/bold yellow]")
    print("[6] 获取[bold yellow]本地音乐文件夹[/bold yellow]路径")
    print("[7] 输出[bold yellow]本地音乐[/bold yellow]")
    print("[8] 文件资源管理器打开[bold yellow]本地音乐文件夹[/bold yellow]")
    print("[9] [bold yellow]清屏[/bold yellow]")
    n = console.input("[green]请输入选项：[/green]")
    return n

def page_link():
    link = console.input("[purple]请输入[/purple]网易云[bold yellow]音乐链接[/bold yellow]：")
    path = "./music"
    name = console.input("[purple]请输入[/purple][bold yellow]文件名[/bold yellow](任意扩展名)：")
    name = path + "/" + name
    """链接解析"""
    link = link.replace("/#/song?id=", "/song/media/outer/url?id=")
    return link, name
    
def page_id():
    id = console.input("[purple]请输入[/purple]网易云[bold yellow]音乐ID[/bold yellow]：")
    path = "./music"
    name = console.input("[purple]请输入[/purple][bold yellow]文件名[/bold yellow](任意扩展名)：")
    name = path + "/" + name
    """ID解析成链接"""
    id = "https://music.163.com/song/media/outer/url?id=" + id
    return id, name

def page_search():
    keyword = console.input("[purple]请输入[/purple]搜索[bold yellow]关键字[/bold yellow]：")
    return keyword

def start():
    while True:
        n = page_main()
        if n == "1":
            link, name = page_link()
            download.download(link, name)
        elif n == "2":
            link, name = page_id()
            download.download(link, name)
        elif n == "3":
            keyword = page_search()
            search.search_song(keyword)
        elif n == "4":
            keyword = page_search()
            search.search_singer(keyword)
        elif n == "5":
            singer = console.input("[purple]请输入[/purple][bold yellow]歌手id[/bold yellow]：")
            find.find_artist(singer)
        elif n == "6":
            print("[bold yellow]本地音乐文件夹[/bold yellow]路径：", end=" ")
            console.print(os.getcwd() + "\\music", style="bold blue")
        elif n == "7":
            for file in os.listdir("./music"):
                console.print(file, style="bold yellow")
                print("文件路径：", end=" ")
                console.print(os.getcwd() + "\\music\\" + file, style="bold blue")
                print("-------------")
        elif n == "8":
            os.startfile(os.getcwd() + "\\music")
        elif n == "9":
            console.clear()
        else:
            print("ERROR: 输入错误", style="bold red")
