#IMPORTAÇÃO DO FASTAPI COM O Request
from fastapi import FastAPI, Request

#IMPORTAÇÃO JINJA2
from fastapi.templating import Jinja2Templates

#IMPORTAÇÃO DA FUNÇÃO DE CAPTURA DE REDE CRIADA POR MIM NO ARQUIVO network_monitor.py
from network_monitor import monitor

from flask import render_template

#PARTE PYTHON INSTANCIANDO O JINJA2 EM VARIÁVEL templates
templates = Jinja2Templates(directory="templates")

#INICIO DA ATIVAÇÃO DO FastAPI
app = FastAPI()

#ROTA DA PAGINA INICIAL OU RAIZ
@app.get("/")

#APLICAÇÃO DO JINJA2 PARA QUE SEJA POSSÍVEL QUE O FastAPI LEIA ARQUIVOS HTML
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
async def dados_de_rede(request: Request):
    dados_rede = monitor()
    return templates.TemplateResponse("index.html", {"request": request, "dados_rede": dados_rede})

@app.get("/dados_rede")
async def dados_rede():
    dados = monitor
    return dados

#FINAL DA ATIVAÇÃO DO FastAPI