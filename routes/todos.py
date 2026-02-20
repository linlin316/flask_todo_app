from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime, timedelta, timezone

from db import get_conn, fetch_todos_sorted, fetch_todo_with_journals
from services import pretty_created_at

todo_bp = Blueprint("todo", __name__)

JST = timezone(timedelta(hours=9))

# ホームページ
@todo_bp.route("/")   #http://127.0.0.1:5000/の意味
def home():
    rows = fetch_todos_sorted()

    # 現在の時間を文字列と数字になる(日本時間)
    today_date = datetime.now(JST).date()
    today_str  = today_date.isoformat()

    # 表示用のTodoリストを作成
    todos = []
    for r in rows:
        d = dict(r)
        d["created_at_pretty"] = pretty_created_at(d["created_at"], today_date)
        d["days_left"] = None # 残り日数の初期値（期限なしの場合はNoneのまま）

        # 期限が設定されている場合のみ残り日数を計算
        if d.get("due_date"):
            try:
                due = datetime.strptime(d["due_date"], "%Y-%m-%d").date()
                d["days_left"] = (due - today_date).days
            except ValueError:
                d["days_left"] = None  # 形式がおかしい場合は表示しない

        todos.append(d)

    return render_template("index.html", todos=todos, today=today_str)

# 追加タスク
@todo_bp.route("/add", methods=["POST"])
def add():
    title = (request.form.get("title") or "").strip()  #.strip()文字列の前後の空白を削除
    due_date = (request.form.get("due_date") or "").strip()

    # タイトル未入力の場合は登録しない
    if title:
        with get_conn() as conn: # DBに接続してTodoを新規追加
            conn.execute(
                "INSERT INTO todos (title, due_date) VALUES (?, ?)",
                (title, due_date or None)
            )
    return redirect(url_for("todo.home"))

# タスク削除
@todo_bp.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    with get_conn() as conn: # DBに接続してTodoを削除
        conn.execute("DELETE FROM todo_journals WHERE todo_id = ?", (todo_id,))
        conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    return redirect(url_for("todo.home"))

# タスク完了
@todo_bp.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    with get_conn() as conn:
        conn.execute("""
            UPDATE todos
            SET is_done = CASE is_done WHEN 1 THEN 0 ELSE 1 END
            WHERE id = ?
        """, (todo_id,))
    return redirect(url_for("todo.home"))

# タスク編集
@todo_bp.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    if request.method == "POST":
        # 編集対象をもらう
        title = (request.form.get("title") or "").strip()
        due_date = (request.form.get("due_date") or "").strip()

        # 編集ページで未変更の場合は登録しない
        if title:
            with get_conn() as conn:
                conn.execute("""
                    UPDATE todos
                    SET title = ?, due_date = ?
                    WHERE id = ?
                """, (title or None, due_date or None, todo_id))

        return redirect(url_for("todo.home"))
    # GET時dbからもらう
    todo, journals = fetch_todo_with_journals(todo_id)

    today_str = datetime.now(JST).date().isoformat()

    if todo is None:
        return "Not Found", 404

    return render_template("edit.html", todo=todo, journals=journals, today=today_str)

# 記録、メモ追加
@todo_bp.route("/journal/add/<int:todo_id>", methods=["POST"])
def add_journal(todo_id):
    content = (request.form.get("content") or "").strip()

    # 記録未入力の場合は登録しない
    if content:
        with get_conn() as conn:
            conn.execute("""
                INSERT INTO todo_journals (todo_id, content)
                VALUES (?, ?)
            """, (todo_id, content or None))

    return redirect(url_for("todo.edit", todo_id=todo_id))

# 記録、メモ削除
@todo_bp.route("/journal/delete/<int:journal_id>", methods=["POST"])
def delete_journal(journal_id):
    with get_conn() as conn:
        
        # 削除対象の日誌が紐づく todo_id を取得（削除後のリダイレクトに必要）
        row = conn.execute(
            "SELECT todo_id FROM todo_journals WHERE id = ?",
            (journal_id,)
        ).fetchone()

        if row is None:
            return "Not Found", 404

        todo_id = row["todo_id"]

        # 日誌を削除
        conn.execute("DELETE FROM todo_journals WHERE id = ?", (journal_id,))

    return redirect(url_for("todo.edit", todo_id=todo_id))