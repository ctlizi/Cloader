import requests
from tqdm.rich import trange
from rich import console

console = console.Console()

def download(url, filename):
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length'))//1024
        for _ in trange(total_size, unit='KB'):
            with open(filename, 'wb') as f:
                f.write(response.content)
    except Exception as e:
        console.print(f"Error downloading {url}: {e}", style="bold red")
