from sqlalchemy import Column, ForeignKey, Integer, String

from database import Base


class Pokemon_table(Base):
    __tablename__ = "pokemons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    #types
    hp = Column(Integer, unique=False, index=False, primary_key=False)
    attack = Column(Integer, unique=False, index=False, primary_key=False)
    weakness = Column(String)
    evolution_id = Column(Integer, unique=True, primary_key=False)
