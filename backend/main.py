import os
from fastapi import FastAPI
from supabase import create_client

# Use environment variables for security
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://lhxmpxlbbrafjrpmkvov.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxoeG1weGxiYnJhZmpycG1rdm92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg5Nzg2ODgsImV4cCI6MjA3NDU1NDY4OH0.OMtBHEYF64x-FpBA8u42MAJ4yYrz0bZbbtb8INWsqbM")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize FastAPI
app = FastAPI(title="ESG / AML API")

# Root endpoint
@app.get("/")
def root():
    return {"message": "API is running!"}

# Entities endpoint
@app.get("/entities")
def get_entities():
    data = supabase.table("Entities").select("*").execute()
    return data.data

