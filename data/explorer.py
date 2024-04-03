from data import conn, curs, IntegrityError
from models.explorer import Explorer
from error import Missing, Duplicate

# DB_NAME = "cryptid.db"
# conn = sqlite3.connect(DB_NAME)
# curs = conn.cursor()

curs.execute("""create table if not exists explorer(
  name text primary key,
  country text,
  description text)""")

# def init():
#   curs.execute("create table creature(name, description, country, area, aka)")

def row_to_model(row: tuple) -> Explorer:
  return Explorer(name=row[0], country=row[1], description=row[2])

def model_to_dict(explorer: Explorer) -> dict | None:
  return explorer.model_dump() if explorer else None

def get_one(name: str) -> Explorer:
  qry = "select * from explorer where name=:name"
  params = {"name": name}
  curs.execute(qry, params)
  row = curs.fetchone()
  if row:
    return row_to_model(row)
  else:
    raise Missing(msg=f"Explorer {name} not found")

def get_all() -> list[Explorer]:
  qry = "select * from explorer"
  curs.execute(qry)
  return [row_to_model(row) for row in curs.fetchall()]

def create(explorer: Explorer):
  if not explorer: return None
  qry = """insert into explorer values
          (:name, :country, :description)"""
  params = model_to_dict(explorer)
  try:
    curs.execute(qry, params)
  except IntegrityError:
    raise Duplicate(msg=f"Explorer {explorer.name} already exists")
  return get_one(explorer.name)
  
def modify(name: str, explorer: Explorer) -> Explorer:
  if not (name and explorer): return None
  qry = """update explorer
          set country=:country,
          name=:name,
          description=:description
          where name=:name_orig"""
  params = model_to_dict(explorer)
  params["name_orig"] = name
  curs.execute(qry, params)
  if curs.rowcount == 1:
    return get_one(explorer.name)
  else:
    raise Missing(msg=f"Explorer {name} not found")

def delete(name: str) -> bool:
  if not name: return False
  qry = "delete from creature where name = :name"
  params = {"name": name}
  curs.execute(qry, params)
  if curs.rowcount != 1:
    raise Missing(msg=f"Explorer {name} not found")
