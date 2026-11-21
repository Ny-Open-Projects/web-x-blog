try:
    from contextlib import asynccontextmanager
    from typing import AsyncIterator
    from sqlalchemy import text
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
except ImportError:
    print("pip install sqlalchemy aiosqlite fastapi httpx 后再运行")
    raise SystemExit(0)
try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

engine = create_async_engine("sqlite+aiosqlite://")  # 生产用 postgresql+asyncpg 并配池参数
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session

app = FastAPI()

@app.get("/ok")
async def ok(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SELECT 1"))
    return {"first": result.scalar()}

with TestClient(app) as c:
    print(c.get("/ok").json())
