from .core import get_conn

# 記録追加
def create_todo_journal(todo_id: int, content: str) -> None:
    with get_conn() as conn:
            conn.execute("""
                INSERT INTO todo_journals (todo_id, content)
                VALUES (?, ?)
            """, (todo_id, content))



# 記録削除
# 削除後のリダイレクト先取得のため、先に todo_id を取得
def delete_todo_journal_and_get_todo_id(journal_id: int) -> int | None:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT todo_id FROM todo_journals WHERE id = ?",
            (journal_id,)
        ).fetchone()

        if row is None:
            return None

        todo_id = row["todo_id"]
        conn.execute("DELETE FROM todo_journals WHERE id = ?", (journal_id,))
        return todo_id