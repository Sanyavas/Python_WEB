from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(prefix="", tags=["pages_auth"])
templates = Jinja2Templates(directory="templates")


@router.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    return templates.TemplateResponse('logout.html', {'request': request})


@router.get("/login", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@router.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse('signup.html', {'request': request})
