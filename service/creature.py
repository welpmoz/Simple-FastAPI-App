import os
from models.creature import Creature
if os.getenv("CRYPTID_UNIT_TEST"):
  from fake import creature as data
else:
  from data import creature as data

def get_all() -> list[Creature]:
  return data.get_all()

def get_one(name: str) -> Creature | None:
  return data.get_one(name)

def create(creature: Creature) -> Creature:
  return data.create(creature)

def replace(id: str, creature: Creature) -> Creature:
  return data.replace(id, creature)

def modify(id: str, creature: Creature) -> Creature:
  return data.modify(id, creature)

def delete(id: str, creature: Creature) -> bool:
  return data.delete(id)
