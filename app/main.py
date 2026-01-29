from fastapi import FastAPI

app = FastAPI(title="FreshTrack API")

@app.get("/")
def root():
    return {"status": "Backend running"}