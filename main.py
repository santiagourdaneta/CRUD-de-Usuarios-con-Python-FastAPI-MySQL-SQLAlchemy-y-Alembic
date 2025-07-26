from fastapi import FastAPI
from app.database.session import Base, engine
from app.api.routes.routes_user import router


app = FastAPI()

if __name__ == "__main__":
    # La variable 'engine' se usa aquí
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

@app.get("/")
async def read_root():
    return {"message": "Welcome to your API!"}

app.include_router(router)

