import sqlite3

def check_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(attendance_list);")
    rows = cursor.fetchall()
    attendance_list = [row for row in rows]
    print(attendance_list)

    attendance_status = input("出勤 or 退勤：").strip()

    if attendance_status == "出勤":
        # INSERT処理
        print("出勤処理")

    elif attendance_status == "退勤":
        # UPDATE処理
        print("退勤処理")

    conn.commit()
    conn.close()


if __name__=="__main__":
    check_db()