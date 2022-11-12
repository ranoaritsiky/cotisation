import uvicorn

# from dotenv import load_dotenv
# from src.config import CONFIG
from src import create_app

app = create_app()

if __name__ == "__main__":
    # load_dotenv()
    uvicorn.run(
        app="main:app",
        reload=True,
        port=8002,
        host="0.0.0.0",
        workers=1,
    )