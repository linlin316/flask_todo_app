from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "todo.db"

# SQLite に接続するための共通関数
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# todos テーブルが無ければ作る
def init_db():
    with get_conn() as conn:
        # タスク本体
        conn.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now', '+9 hours')),
                due_date TEXT,
                is_done INTEGER DEFAULT 0
            )
        """)

        # タスクの作業記録
        conn.execute("""
            CREATE TABLE IF NOT EXISTS todo_journals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                todo_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now', '+9 hours')),
                FOREIGN KEY (todo_id) REFERENCES todos(id)
            )
        """)

        cols = [row["name"] for row in conn.execute(
            "PRAGMA table_info(todos)"
        ).fetchall()]

        if "due_date" not in cols:
            conn.execute("ALTER TABLE todos ADD COLUMN due_date TEXT")

        if "is_done" not in cols:
            conn.execute(
                "ALTER TABLE todos ADD COLUMN is_done INTEGER DEFAULT 0"
            )