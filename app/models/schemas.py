# app/models/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ConversionMetadata(BaseModel):
    originalFileName: str
    convertedAt: str

class ConversionResponse(BaseModel):
    markdown: str
    metadata: Optional[ConversionMetadata] = None