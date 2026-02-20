import sqlite3
from datetime import datetime

def check_db(employee_id = 1):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # cursor.execute("PRAGMA table_info(attendance_list);")
    # rows = cursor.fetchall()
    # attendance_list = [row for row in rows]
    # print(attendance_list)
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT working_hours FROM attendance_list WHERE employee_id =?",
        (employee_id,)
    )
    total_working_hours_list = cursor.fetchall()


    total_minutes = 0
    # データベースから取得した勤務時間を1件ずつ取り取り出して合計勤務時間を表示する
    for row in total_working_hours_list:

        time_str = row[0]
        hour_str,minute_str = time_str.split(":")
        total_minutes += int(hour_str)*60 + int(minute_str)

    # 画面表示するためにデータを整える「hh:mm」
    hours = total_minutes // 60
    minutes = total_minutes % 60
    result_total_working_hours = f"{hours:02}:{minutes:02}"
    print(result_total_working_hours)
    

     

    
    

    conn.close()


if __name__=="__main__":
    check_db()