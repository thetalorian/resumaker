from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class WorkHistoryDescription(BaseModel):
    paragraphs: Optional[list[str]] = None
    bullets: Optional[list[str]] = None


class WorkHistory(BaseModel):
    company: str
    title: str
    start_date: datetime
    end_date: Optional[datetime]
    description: WorkHistoryDescription


class SkillSet(BaseModel):
    category: str
    entries: list[str]


class Resume(BaseModel):
    history: list[WorkHistory]
    skills: list[SkillSet]
