import os
from fastapi import FastAPI
from supabase import create_client
from fastapi.middleware.cors import CORSMiddleware

# --- Supabase setup ---
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://lhxmpxlbbrafjrpmkvov.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY", "YOUR_ANON_KEY_HERE")  # replace with your real anon key

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
import os
from fastapi import FastAPI
from supabase import create_client
from fastapi.middleware.cors import CORSMiddleware

# --- Supabase setup ---
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://lhxmpxlbbrafjrpmkvov.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxoeG1weGxiYnJhZmpycG1rdm92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg5Nzg2ODgsImV4cCI6MjA3NDU1NDY4OH0.OMtBHEYF64x-FpBA8u42MAJ4yYrz0bZbbtb8INWsqbM")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- FastAPI app ---
app = FastAPI()

# Allow CORS so frontend or Streamlit can access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/entities")
def get_entities():
    # Fetch all rows from Supabase table "Entities"
    response = supabase.table("Entities").select("*").execute()
    return response.data

