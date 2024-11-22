import uvicorn
from fastapi import FastAPI
from API.User.view import router as user_router


app = FastAPI()
app.include_router(router=user_router, prefix="")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)