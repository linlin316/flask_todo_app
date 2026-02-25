from .core import get_conn


# ホームページ
def fetch_todos_sorted():
    # 未完了のタスクを優先
    # 期限が近い順
    # 同日の場合はID降順
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



# リストを削除
def delete_todo_with_journals(todo_id: int):
    with get_conn() as conn: 
        conn.execute("DELETE FROM todo_journals WHERE todo_id = ?", (todo_id,))
        conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))



# タスク完了
def toggle_todo_done(todo_id: int):
    with get_conn() as conn:
        # 対象のTodoを取得し、完了したタスクが下に移動
        conn.execute("""
            UPDATE todos SET is_done = 
            CASE is_done WHEN 1 THEN 0 ELSE 1 END
            WHERE id = ?
        """, (todo_id,))



# 記録削除
def insert_todo(title: str, due_date: str | None):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO todos (title, due_date) VALUES (?, ?)",
            (title, due_date or None))


# タスク編集
def update_todo(todo_id: int, title: str | None, due_date: str | None) -> None:
    with get_conn() as conn:
        conn.execute("""
            UPDATE todos
            SET title = ?, due_date = ?
            WHERE id = ?
        """, (title or None, due_date or None, todo_id))