import subprocess

def baixar_video(url):
    print(f"Baixando: {url}")
    # O script tenta usar o yt-dlp que precisa estar instalado
    subprocess.run([
        "yt-dlp",
        "-f", "bestvideo+bestaudio",
        url
    ])

def baixar_lista(arquivo):
    try:
        with open(arquivo) as f:
            links = f.readlines()
        for link in links:
            link = link.strip()
            if link:
                baixar_video(link)
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado!")
