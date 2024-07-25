from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

