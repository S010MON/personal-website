import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


@app.get("/page_1", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('page_1.html', context={'request': request})


@app.get("/page_2", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('page_2.html', context={'request': request})

@app.get("/profile_pic")
async def profile(request: Request):
    return FileResponse("resources/profile_img.jpg")


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = num
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
