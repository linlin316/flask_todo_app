import sqlite3
from datetime import datetime

def check_db(employee_id = 5,format_date="2026-02-19",clock_out="18:10"):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # cursor.execute("PRAGMA table_info(attendance_list);")
    # rows = cursor.fetchall()
    # attendance_list = [row for row in rows]
    # print(attendance_list)
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
            SELECT clock_in
            FROM attendance_list
            WHERE employee_id = ? AND work_date = ?
            """,(employee_id,format_date)    
    )
    clock_in_list = cursor.fetchone()
    clock_in = clock_in_list[0]
    today = datetime.today().strftime("%Y-%m-%d")
    clock_in_dataTime = f"{today} {clock_in}"
    clock_in_time = datetime.strptime(clock_in,"%H:%M")

    clock_out_dataTime = f"{today} {clock_out}"
    clock_out_time = datetime.strptime(clock_out,"%H:%M")
    working_hours = clock_out_time - clock_in_time

    # clock_in_data_time = datetime.strptime(clock_in_dataTime, "%Y-%m-%d %H:%M")
    conn.close()


if __name__=="__main__":
    check_db()