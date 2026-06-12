# getLyrics

getLyrics é uma ferramenta em Python para transcrever letras de músicas localmente utilizando modelos Whisper através do Faster-Whisper e, opcionalmente, corrigir e traduzir as letras para português brasileiro usando Ollama.

O projeto foi desenvolvido para funcionar totalmente offline após o download inicial dos modelos, sem depender de APIs pagas.

## Funcionalidades

* Transcrição automática de músicas em áudio.
* Suporte a diferentes níveis de qualidade.
* Correção opcional de transcrições usando IA local.
* Tradução opcional para português brasileiro.
* Suporte a músicas multilíngues.
* Modo avançado para músicas mais difíceis (metal, vocais agressivos, gravações complexas).
* Exportação em TXT e JSON.

## Requisitos

* Python 3.10+
* FFmpeg
* Ollama (opcional)
* Linux, Windows ou macOS

## Instalação

### Clonar o repositório

```bash
git clone git@github.com:mateus-macciel/getLyrics.git
cd getLyrics
```

### Criar ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Instalar FFmpeg

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Verificar instalação:

```bash
ffmpeg -version
```

## Instalação do Ollama (Opcional)

O Ollama é utilizado para:

* Corrigir erros da transcrição.
* Melhorar músicas multilíngues.
* Traduzir letras para português brasileiro.

Instalação:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Baixar modelo recomendado:

```bash
ollama pull qwen2.5:3b
```

Iniciar o serviço:

```bash
ollama serve
```

## Estrutura do Projeto

```text
getLyrics/
│
├── input/
├── output/
│
├── src/
│   ├── audio.py
│   ├── transcriber.py
│   ├── translator.py
│   └── exporter.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Modos de Uso

### Fast

Mais rápido, menor consumo de memória.

Utiliza:

```text
Whisper Small
```

Comando:

```bash
python main.py input/musica.mp3 fast
```

Indicado para:

* Testes rápidos
* Músicas simples
* Máquinas com pouca memória

---

### Quality

Modo recomendado.

Utiliza:

```text
Whisper Medium
```

Comando:

```bash
python main.py input/musica.mp3 quality
```

Indicado para:

* Uso diário
* Melhor equilíbrio entre velocidade e precisão

---

### Extreme

Modo de máxima qualidade.

Fluxo:

```text
Demucs
↓
Whisper Large-v3
↓
Correção com IA
↓
Tradução
```

Comando:

```bash
python main.py input/musica.mp3 extreme
```

Indicado para:

* Metal
* Deathcore
* Metalcore
* Black Metal
* Gravações ao vivo
* Áudios difíceis

## Arquivos Gerados

Após o processamento, os resultados são salvos na pasta:

```text
output/
```

Arquivos:

```text
lyrics_original.txt
lyrics_original.json

lyrics_fixed.txt
lyrics_fixed.json

lyrics_ptbr.txt
lyrics_ptbr.json
```

### Descrição

| Arquivo         | Descrição                          |
| --------------- | ---------------------------------- |
| lyrics_original | Saída bruta do Whisper             |
| lyrics_fixed    | Letra corrigida pela IA            |
| lyrics_ptbr     | Tradução para português brasileiro |

## Exemplos

Transcrição rápida:

```bash
python main.py input/teste.mp3 fast
```

Transcrição recomendada:

```bash
python main.py input/teste.mp3 quality
```

Máxima qualidade:

```bash
python main.py input/teste.mp3 extreme
```

## Limitações

O projeto realiza uma transcrição do áudio utilizando modelos de reconhecimento de fala.

A qualidade dos resultados depende de fatores como:

* Clareza dos vocais.
* Qualidade da gravação.
* Idiomas presentes na música.
* Intensidade dos instrumentos.
* Tipo de vocal utilizado.

Mesmo utilizando os melhores modelos disponíveis, músicas com vocais extremamente distorcidos ou guturais podem apresentar erros de reconhecimento.
