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


# ホームページ
# 未完了のタスクを優先
# 期限が近いタスクを優先
def fetch_todos_sorted():
    # DB接続
    with get_conn() as conn:
        return conn.execute("""
            SELECT id, title, created_at, due_date, is_done
            FROM todos
            ORDER BY
              is_done ASC,
              CASE WHEN due_date IS NULL THEN 1 ELSE 0 END,
              due_date ASC,
              id DESC
        """).fetchall()


# タスク編集
def fetch_todo_with_journals(todo_id: int):
    # DB接続
    with get_conn() as conn:
        # 対象のTodoを取得
        todo = conn.execute(
            "SELECT id, title, due_date FROM todos WHERE id = ?",
            (todo_id,)
        ).fetchone()

        # 作業日誌を新しい順で取得
        journals = conn.execute("""
            SELECT id, content, created_at
            FROM todo_journals
            WHERE todo_id = ?
            ORDER BY id DESC
        """, (todo_id,)
        ).fetchall()
    
    return todo, journals


# todos テーブルが無ければ作る
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

        # todosテーブルの現在のカラム一覧を取得
        cols = [row["name"] for row in conn.execute(
            "PRAGMA table_info(todos)"
        ).fetchall()]

        if "due_date" not in cols:
            conn.execute("ALTER TABLE todos ADD COLUMN due_date TEXT")

        if "is_done" not in cols:
            conn.execute(
                "ALTER TABLE todos ADD COLUMN is_done INTEGER DEFAULT 0"
            )