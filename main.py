from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Database imports
from database import schemas

app = FastAPI()

# Setup for templates
templates = Jinja2Templates(directory='templates')
# Setup for static files
app.mount('/static', StaticFiles(directory='static'), name='static')

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/translate', response_model=schemas.TranslateResponse)
def translate(request: schemas.TranslateRequest):
    return request