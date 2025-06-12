import os
import asyncio
from dotenv import load_dotenv
from datetime import datetime, timezone
from fastapi.responses import JSONResponse

load_dotenv()
IS_SHABBAT_LOCK_ON = bool(os.getenv("IS_SHABBAT_LOCK_ON", False))


def block_on_shabbat_logic():
    if IS_SHABBAT_LOCK_ON:
        now = datetime.now(timezone.utc)
        print(f'now day is: {now.weekday()}')
        if now.weekday() == 5:
            return JSONResponse(status_code=403, content={"error": "shabbat is breaking day"})
