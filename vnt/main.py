#IMPORTAÇÃO DO FASTAPI COM O Request
from fastapi import FastAPI, Request

#IMPORTAÇÃO JINJA2
from fastapi.templating import Jinja2Templates

#PARTE PYTHON INSTANCIANDO O JINJA2 EM VARIÁVEL templates
templates = Jinja2Templates(directory="templates")

#INICIO DA ATIVAÇÃO DO FastAPI
app = FastAPI()

#ROTA DA PAGINA INICIAL OU RAIZ
@app.get("/")

#APLICAÇÃO DO JINJA2 PARA QUE SEJA POSSÍVEL QUE O FastAPI LEIA ARQUIVOS HTML
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#FINAL DA ATIVAÇÃO DO FastAPI