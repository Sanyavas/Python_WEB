import time
from ipaddress import ip_address
from typing import Callable

import redis.asyncio as redis
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi_limiter import FastAPILimiter
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.conf.config import settings
from src.database.db import get_db
from src.routes import contacts, auth, users

from src.routes.contacts import get_contacts

app = FastAPI()
contacts_router = contacts.router
app.include_router(contacts_router, prefix="/api")
app.include_router(auth.router, prefix='/api')
app.include_router(users.router, prefix='/api')

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

banned_ips = [ip_address("192.168.1.1"), ip_address("192.168.1.2")]


# Виставляти ліміт на запити
@app.on_event("startup")
async def startup():
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, password=settings.redis_password, db=0)
    await FastAPILimiter.init(r)


# Видача дозволів
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:5500', "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# бан хостів
@app.middleware("http")
async def ban_ips(request: Request, call_next: Callable):
    ip = ip_address(request.client.host)
    if ip in banned_ips:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": "You are banned"})
    response = await call_next(request)
    return response


# ЮзерАгент показує з якого пристрою зайшов
@app.middleware("http")
async def user_agent_ban_middleware(request: Request, call_next: Callable):
    user_agent = request.headers.get("user-agent")
    print('----------------------------')
    print(user_agent)
    print('----------------------------')
    response = await call_next(request)
    return response


# Простий приклад міделваре
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, form=Depends(get_contacts)):
    return templates.TemplateResponse('index.html', {'request': request, "contacts": form})


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")
