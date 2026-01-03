from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class WorkHistory(BaseModel):
    company: str
    title: str
    start_date: datetime
    end_date: Optional[datetime]
    description: list[str]
    bullets: Optional[list[str]] = None


class SkillSet(BaseModel):
    category: str
    entries: list[str]


class Resume(BaseModel):
    history: list[WorkHistory]
