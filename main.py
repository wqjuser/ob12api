"""OB1 2API launcher."""
import os
import uvicorn

from src.core.config import HOST, PORT

if __name__ == "__main__":
    reload_enabled = os.getenv("OB12API_RELOAD", "").lower() in {"1", "true", "yes"}
    uvicorn.run("src.main:app", host=HOST, port=PORT, reload=reload_enabled)
