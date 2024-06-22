from fastapi import FastAPI
import auth

app = FastAPI()

app.include_router(auth.router,prefix="/auth",tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


