from datetime import date
from typing import Optional, List
from sqlalchemy import String, Text, Date, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from infrastructure.persistence.database.base import BaseModel

class Patent(BaseModel):
    __tablename__ = "patents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    publication_number: Mapped[Optional[str]] = mapped_column(String(50))
    application_number: Mapped[Optional[str]] = mapped_column(String(50))
    filing_date: Mapped[Optional[date]] = mapped_column(Date)
    publication_date: Mapped[Optional[date]] = mapped_column(Date)
    examination_publication_date: Mapped[Optional[date]] = mapped_column(Date)
    title: Mapped[Optional[str]] = mapped_column(String(500))
    abstract: Mapped[Optional[str]] = mapped_column(Text)
    country: Mapped[Optional[str]] = mapped_column(String(5), default="BR")
    source: Mapped[Optional[str]] = mapped_column(String(50), default="INPI")
    national_phase_start_date: Mapped[Optional[date]] = mapped_column(Date)

    priorities: Mapped[List["Priority"]] = relationship("Priority", back_populates="patent", cascade="all, delete-orphan")
    classifications: Mapped[List["Classification"]] = relationship("Classification", back_populates="patent", cascade="all, delete-orphan")
    international_applications: Mapped[List["InternationalApplication"]] = relationship(
        "InternationalApplication", back_populates="patent", cascade="all, delete-orphan"
    )
    parties: Mapped[List["Party"]] = relationship("Party", back_populates="patent", cascade="all, delete-orphan")


class Priority(BaseModel):
    __tablename__ = "priorities"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patent_id: Mapped[int] = mapped_column(ForeignKey("patents.id"), nullable=False)
    number: Mapped[Optional[str]] = mapped_column(String(50))
    p_data: Mapped[Optional[date]] = mapped_column(Date)
    country: Mapped[Optional[str]] = mapped_column(String(5))

    patent: Mapped["Patent"] = relationship("Patent", back_populates="priorities")


class Classification(BaseModel):
    __tablename__ = "classifications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patent_id: Mapped[int] = mapped_column(ForeignKey("patents.id"), nullable=False)
    system: Mapped[Optional[str]] = mapped_column(String(50))
    code: Mapped[Optional[str]] = mapped_column(String(50))
    year: Mapped[Optional[str]] = mapped_column(String(10))
    description: Mapped[Optional[str]] = mapped_column(Text)

    patent: Mapped["Patent"] = relationship("Patent", back_populates="classifications")


class InternationalApplication(BaseModel):
    __tablename__ = "international_applications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patent_id: Mapped[int] = mapped_column(ForeignKey("patents.id"), nullable=False)
    application_type: Mapped[Optional[str]] = mapped_column(String(50))
    number: Mapped[Optional[str]] = mapped_column(String(50))
    ia_date: Mapped[Optional[date]] = mapped_column(Date)
    authority: Mapped[Optional[str]] = mapped_column(String(50))

    patent: Mapped["Patent"] = relationship("Patent", back_populates="international_applications")


class Party(BaseModel):
    __tablename__ = "parties"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patent_id: Mapped[int] = mapped_column(ForeignKey("patents.id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(200))
    country: Mapped[Optional[str]] = mapped_column(String(5))
    role: Mapped[Optional[str]] = mapped_column(String(50))

    patent: Mapped["Patent"] = relationship("Patent", back_populates="parties")

