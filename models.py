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


class University(BaseModel):
    name: str
    start: int
    end: int
    major: str


class Education(BaseModel):
    universities: Optional[list[University]] = None
    certifications: Optional[list[str]] = None


class Resume(BaseModel):
    history: list[WorkHistory]
    skills: list[SkillSet]
    education: Education
