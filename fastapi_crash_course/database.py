from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db",
)


new_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
