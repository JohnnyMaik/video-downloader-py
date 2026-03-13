# 📥 Python Video Downloader

Um automatizador de linha de comando para baixar vídeos em alta resolução. Este projeto gerencia automaticamente a criação de pastas e a união de áudio/vídeo em alta qualidade.

## 🚀 Como usar o programa (Executável)
Para rodar sem precisar instalar o Python:
1. Vá na aba **Releases** deste projeto e baixe o arquivo `main.exe` e o `ffmpeg.exe`.
2. Coloque os dois arquivos na **mesma pasta**.
3. Execute o `main.exe`, cole a URL do vídeo e pronto! O vídeo aparecerá na pasta `/downloads`.

## 🛠️ Requisitos para Desenvolvedores
Se for rodar o código `main.py`:
- Instale a biblioteca: `pip install yt-dlp`
- Tenha o `ffmpeg.exe` na pasta do script.
  
### 🛠️ Pré-requisitos Obrigatórios

Para que o download funcione em alta qualidade (unindo áudio e vídeo), você **precisa** do FFmpeg:

1. **Baixe o FFmpeg aqui:** [Download Direto (Essentials)](https://www.gyan.dev)
2. Extraia o arquivo e procure por `ffmpeg.exe` dentro da pasta `bin`.
3. **Mova o `ffmpeg.exe`** para a mesma pasta onde está o seu `main.exe` (ou `main.py`).

## 📁 Estrutura do Projeto
- `main.py`: Código fonte principal.
- `main.exe`: Versão executável para Windows.
- `ffmpeg.exe`: Motor de processamento de vídeo (essencial para 1080p/4K).


