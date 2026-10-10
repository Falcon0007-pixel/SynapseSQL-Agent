from sqlalchemy import create_engine, inspect
from pathlib import Path
def read_schema (url:str) -> str:
    """Read tables, columns and foreign keys from any SQL database."""
    insp = inspect(create_engine(url))
    lines = []
    for table in insp.get_table_names():
        col =", ".join(f"{c["name"]} {c["type"]}" for c in insp.get_columns(table))
        lines.append(f"TABLE {table} ({col})")
        for fk in insp.get_foreign_keys(table):
            for src, dst in zip(fk["constrained_columns"], fk["referred_columns"]):
                lines.append(f'  {table}.{src} -> {fk["referred_table"]}.{dst}')
    return "\n".join(lines)


if __name__ == "__main__":
    db_file = Path(__file__).resolve().parent.parent /"Data" /"shop.db"
    print(read_schema(f"sqlite:///{db_file.as_posix()}"))
