from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Setup for templates
templates = Jinja2Templates(directory='templates')
# Setup for static files
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})