import streamlit as st
from supabase import create_client, Client

# Load secrets
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON_KEY = st.secrets["SUPABASE_ANON_KEY"]

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

st.title("ESG & AML Tool")
st.success("✅ Streamlit is connected and ready for our project!")

# Fetch entities
try:
    response = supabase.table("Entities").select("*").execute()
    entities = response.data if response.data else []
except Exception as e:
    st.error(f"Error fetching data from Supabase: {e}")
    entities = []

# Show entities
if entities:
    st.write("### Entities in database:")
    st.json(entities)
else:
    st.warning("⚠️ No rows found in the 'Entities' table.")

