import uuid
import uvicorn
from fastapi import FastAPI
from loguru import logger

from tweegen.log import log
from tweegen.config import PROJECT_NAME, VERSION, LOG_LEVEL, PORT
from tweegen.service import load_model, generate, upload


app = FastAPI(title=PROJECT_NAME, version=VERSION)


@app.on_event("startup")
def startup_event():
    load_model()


@app.get("/health", tags=["sanity"])
@log("Health check")
def health():
    return {"status_code": 200, "response": "ok"}


@app.get(
    "/tweet",
    tags=["services"],
    summary="Generates bunch of tweets",
)
@log("Tweet generated text")
async def tweet():
    """Generate tweets and upload them to environment user drafts"""
    with logger.contextualize(request_id=str(uuid.uuid4())):
        tweets = generate()
        upload(tweets)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, log_level=LOG_LEVEL)
