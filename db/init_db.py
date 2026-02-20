from .core import get_conn

# アプリ起動時に必要なテーブルを自動作成
def init_db():
    # DB接続
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

        # todosテーブルの現タスク一覧を取得
        cols = [row["name"] for row in conn.execute(
            "PRAGMA table_info(todos)"
        ).fetchall()]

        if "due_date" not in cols:
            conn.execute("ALTER TABLE todos ADD COLUMN due_date TEXT")

        if "is_done" not in cols:
            conn.execute(
                "ALTER TABLE todos ADD COLUMN is_done INTEGER DEFAULT 0"
            )