
# 勤怠管理アプリ

## 概要
出勤・退勤の記録と勤怠履歴を表示できるシンプルな勤怠管理アプリです。  
社内メンバーが使用することを想定しています。

---


## 機能
・社員番号を入力して出勤  
・社員番号を入力して退勤  
・勤怠履歴の表示  

※ 出勤時はデータを新規登録し、退勤時は該当データを更新します。

---


## 使用技術
・Python  
・Flask  
・SQLite  
・HTML / CSS  

---


## フォルダー構成
```
attendance-app/
├── app.py          # Flaskアプリのエントリーポイント
├── main.py         # アプリのメイン処理
├── init_db.py      # データベース初期化用スクリプト
├── db.py           # データベース接続・操作処理
├── check_db.py     # データベース確認用スクリプト
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html  # 出勤・退勤画面
│   └── result.html # 勤怠結果表示画面
└── static/
    └── style.css   # CSSファイル
```


---


## 起動方法

### 1. 必要なライブラリをインストール
```bash
uv pip install -r requirements.txt
```

### 2. データベースを初期化
```bash
uv run init_db.py
```

### 3. アプリを起動
```bash
uv run app.py
```

### 4. ブラウザでアクセス

アプリ起動後、以下のURLにアクセスしてください。

http://127.0.0.1:5000


※ 本アプリでは uv を使用して実行しています。
※ 仮想環境の作成方法については説明を省略しています。