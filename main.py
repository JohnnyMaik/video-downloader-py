import os
import sys
import subprocess

def baixar_video(url):
    # Pega a pasta onde o .exe está localizado
    diretorio_do_exe = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
    
    # Define a pasta de downloads um nível acima (fora da dist) ou na pasta atual
    # Se você quer que a pasta 'downloads' fique na raiz do projeto 'MeuDownloader':
    pasta_raiz = os.path.dirname(diretorio_do_exe) if "dist" in diretorio_do_exe else diretorio_do_exe
    pasta_destino = os.path.join(pasta_raiz, "downloads")
    
    # O FFmpeg deve estar na mesma pasta que o .exe para funcionar
    ffmpeg_path = os.path.join(diretorio_do_exe, "ffmpeg.exe")

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)


    # Cria a pasta se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    print(f"\n[INFO] Salvando em: {pasta_destino}")

    # Comando configurado para usar o ffmpeg local
    comando = [
        "yt-dlp",
        "--ffmpeg-location", ffmpeg_path,
        "-f", "bestvideo+bestaudio/best",
        "-o", f"{pasta_destino}/%(title)s.%(ext)s",
        url
    ]

    try:
        subprocess.run(comando, check=True)
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um problema: {e}")
        input("Pressione Enter para fechar...")

def menu():
    print("\n" + "="*25)
    print("   VIDEO DOWNLOADER CLI")
    print("="*25)
    print("1 - Baixar um vídeo")
    print("2 - Sair")

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("\nEscolha: ")
        if opcao == "1":
            url = input("URL: ")
            baixar_video(url)
        elif opcao == "2":
            break
