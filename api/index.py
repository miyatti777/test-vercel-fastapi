from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/test")
async def test():
    return {"status": "success", "message": "Test endpoint working"}

# Vercel用のハンドラー
def handler(request):
    return app 