from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

from external_api import search_vn, get_vn

app = FastAPI()
origins = [
    "http://127.0.0.1:5173",    
    "http://localhost:5173" 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,          
    allow_methods=["*"],              
    allow_headers=["*"],              
)


