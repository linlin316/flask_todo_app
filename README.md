# Flask Todo App

シンプルな Todo 管理アプリです。  
Flask + SQLite を使用し、タスク管理と作業日誌の記録ができます。

本プロジェクトでは、Blueprint構成およびDBレイヤー分離を意識した設計を行っています。

---

## 主な機能

- Todo の追加 / 編集 / 削除
- 完了ステータス切替
- 期限管理（残り日数表示）
- 作業日誌の記録・削除
- Flask Blueprint 構成
- レイヤー分離構成（routes / db / services）

---

## 使用技術

- Python 3.14
- Flask
- SQLite3
- Jinja2
- HTML / CSS

---

## アーキテクチャ概要

- **routes**：HTTPリクエスト処理
- **services**：表示用ロジック処理
- **db**：データベース操作（SQL分離）
- **templates**：UI表示
- **static**：CSSなどの静的ファイル

## ディレクトリ構成

```text
flask_app/
├── app.py                # Flaskアプリのエントリーポイント
├── services.py           # 表示用ロジック層（日時整形など）
├── requirements.txt
├── README.md
│
├── db/                   # データベース関連モジュール
│   ├── __init__.py       # DBパッケージ定義
│   ├── core.py           # SQLite接続管理 (get_conn)
│   ├── init_db.py        # テーブル初期化処理
│   ├── todos_db.py       # todosテーブル操作
│   ├── journals_db.py    # todo_journalsテーブル操作
│   └── todo.db           # SQLiteデータベースファイル
│
├── routes/
│   ├── __init__.py
│   └── todos.py          # Todo関連のBlueprintルート
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css

```
## 起動手順

```bash
git clone <このリポジトリURL>
cd flask_app

# 仮想環境作成
python -m venv .venv

# 仮想環境有効化（Windows PowerShell）
.\.venv\Scripts\Activate.ps1

# 依存関係インストール
pip install -r requirements.txt

# アプリ起動
python app.py

#ブラウザで以下にアクセス
http://127.0.0.1:5000

---

## 補足

初回起動時に SQLite データベースが自動生成されます。

開発用サーバーのため、本番環境では WSGI サーバーの使用を推奨します。
