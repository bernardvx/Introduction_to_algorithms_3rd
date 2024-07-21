#!/bin/sh

# Start FastAPI
uvicorn FastApi.main:app --host=0.0.0.0 --port=8000 --reload &

# Start Streamlit
streamlit run FastApi/stream_lit.py --server.port=8501

# Keep the container running
tail -f /dev/null
