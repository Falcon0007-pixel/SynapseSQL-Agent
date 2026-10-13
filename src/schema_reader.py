from sqlalchemy import create_engine, inspect , text
from pathlib import Path
def read_schema (url:str) -> str:
    """Read tables, columns and foreign keys from any SQL database."""
    engine = create_engine(url)
    insp = inspect(engine)
    lines = []
    for table in insp.get_table_names():
        col =", ".join(f"{c["name"]} {c["type"]}" for c in insp.get_columns(table))
        lines.append(f"TABLE {table} ({col})")
        with engine.connect() as conn:
            for c in insp.get_columns(table):
                result = conn.execute(text(f'SELECT DISTINCT {c["name"]} FROM "{table}" LIMIT 3'))
                for r in result:
                    lines.append(f"{c["name"]}: {r[0]} ")
        for fk in insp.get_foreign_keys(table):
            for src, dst in zip(fk["constrained_columns"], fk["referred_columns"]):
                lines.append(f'  {table}.{src} -> {fk["referred_table"]}.{dst}')
    return "\n".join(lines)

db_file = Path(__file__).resolve().parent.parent /"Data" /"shop.db"
if __name__ == "__main__":
   #db_file = Path(__file__).resolve().parent.parent /"Data" /"shop.db"
    print(read_schema(f"sqlite:///{db_file.as_posix()}"))
