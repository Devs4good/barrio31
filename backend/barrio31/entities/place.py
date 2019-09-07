import uuid
from datetime import datetime
from sqlalchemy import Column, String, Sequence, JSON, Float, Integer, ForeignKey, DateTime
from backend.barrio31.database.data_base import DbEntity


class Place(DbEntity):
    __tablename__ = 'models'
    id = Column(String(100), primary_key=True)
    name = Column(String(200))
    coordenates = Column(JSON)
    category = Column(String(200))
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    @classmethod
    def get(cls, id=None):
        filters = {'id': id} if id else None
        return DbEntity.find(Place, filters)
