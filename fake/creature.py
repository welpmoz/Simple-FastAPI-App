from models.creature import Creature

_creatures = [
  Creature(name="Yeti",
            aka="Abominable Snowman",
            country="CN",
            area="Himalayas",
            description="Hirsute Himalayan"),
  Creature(name="Bigfoot",
            description="Yeti's Cousin Eddie",
            country="US",
            area="*",
            aka="Sasquatch"),
]

def get_all() -> list[Creature]:
  """Return all Creatures"""
  return _creatures

def get_one(name: str) -> Creature | None:
  for _creature in _creatures:
    if _creature.name == name:
      return _creature
  return None

def create(creature: Creature) -> Creature:
  """Add and Creature"""
  _creatures.append(creature)
  return creature

def modify(creature: Creature) -> Creature:
  """Partially modify an Creature"""
  return creature

def replace(creature: Creature) -> Creature:
  """Completely replace an Creature"""
  return creature

def delete(name: str) -> bool:
  """Delete an Creature, return None if it existed"""
  return None