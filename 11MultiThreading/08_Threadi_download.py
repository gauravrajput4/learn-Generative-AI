import threading
import time
import requests

def download(url):
    print(f"Downloading {url}...")
    response = requests.get(url)
    print(f"Downloading {url} done..., size: {len(response.content)} bytes")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpg",
    "https://httpbin.org/image/svg"
]

start = time.time()
threads=[]

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
end = time.time()
print(f"All Download done in {end - start:.2f} seconds")