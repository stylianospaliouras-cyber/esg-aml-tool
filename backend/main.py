import os
from fastapi import FastAPI
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://lhxmpxlbbrafjrpmkvov.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxoeG1weGxiYnJhZmpycG1rdm92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg5Nzg2ODgsImV4cCI6MjA3NDU1NDY4OH0.OMtBHEYF64x-FpBA8u42MAJ4yYrz0bZbbtb8INWsqbM")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/entities")
def get_entities():
    data = supabase.table("entities").select("*").execute()
    return data.data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for React frontend
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/entities")
def read_entities():
    return [{"id": 1, "name": "Sample Entity"}]
from fastapi import FastAPI

app = FastAPI()

@app.get("/entities")
def read_entities():
    return [{"id": 1, "name": "Sample Entity"}]

