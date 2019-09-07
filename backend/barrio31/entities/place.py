import uuid
from datetime import datetime
from sqlalchemy import Column, String, JSON, DateTime
from database.data_base import DbEntity


class Place(DbEntity):
    __tablename__ = 'place'
    id = Column(String(100), primary_key=True)
    nombre = Column(String(200))
    coordenadas = Column(JSON)
    category = Column(String(200))
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, nombre, coordenadas, category="None"):
        self.id = str(uuid.uuid1())
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.category = category

    @classmethod
    def get(cls, id=None):
        filters = {'id': id} if id else None
        return DbEntity.find(Place, filters)

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'coordenadas': self.coordenadas,
            'creation_date': self.creation_date,
        }