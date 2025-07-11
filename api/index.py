from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/test")
async def test():
    return {"status": "success", "message": "Test endpoint working"}

@app.get("/test")
async def test_simple():
    return {"status": "success", "message": "Simple test endpoint"}

# Vercel用のハンドラー
handler = app 