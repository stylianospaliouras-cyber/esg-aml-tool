import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Connect to Supabase using secrets
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON_KEY = st.secrets["SUPABASE_ANON_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

st.title("ESG & AML Tool")
st.write("✅ Streamlit is connected and ready for our project!")

# Fetch data from 'Entities' table
try:
    response = supabase.table("Entities").select("*").execute()
    data = response.data

    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No rows found in the 'Entities' table.")
except Exception as e:
    st.error(f"Error fetching data from Supabase: {e}")
import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Connect to Supabase using secrets
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON_KEY = st.secrets["SUPABASE_ANON_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

st.title("ESG & AML Tool")

st.write("✅ Streamlit is connected and ready for our project!")

# Fetch data from 'entities' table
try:
    response = supabase.table("Entities").select("*").execute()
    data = response.data

    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No rows found in the 'entities' table.")
except Exception as e:
    st.error(f"Error fetching data from Supabase: {e}")
import streamlit as st

st.title("ESG & AML Tool")
st.write("✅ Streamlit is connected and ready for our project!")

