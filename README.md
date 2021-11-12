# Translate
Command-line interface to translation pipelines, powered by Huggingface transformers.
This tool can download translation models, and then using them to translate sentences offline.
By default, tries using models from `Helsinki-NLP` (each model is about 300MB large).

## Install

```bash
$ git clone https://github.com/Teuze/translate
$ cd translate
$ pip3 install --user -r requirements.py
```
If you want to be able to use this script from anywhere in your system, you can symlink or copy the  `translate` script file into  one of your path folders, like for example `$HOME/.local/bin`.

## Usage

Listing available and installed translation models :

```bash
$ # Also available on https://huggingface.co/models
$ ./translate model list online | less
$ ./translate model list local | less
```

Downloading models :

```bash
$ ./translate download model "Helsinki-NLP/opus-mt-en-es"
$ ./translate download model "Helsinki-NLP/opus-mt-fr-en"
```

Using models to translate from CLI arguments or from standard input :

```bash
$ ./translate text -e "Helsinki-NLP/opus-mt-en-es" "Hello World!"
¡Hola Mundo!
$ echo "Ceci est une phrase d'exemple simple" | ./translate text -s fr -t en
This is a simple example sentence
```