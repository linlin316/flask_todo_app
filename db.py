import sqlite3

# 出勤のデータを追加する。
def clock_in(format_date,format_time,employee_id):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO attendance_list 
        (employee_id ,work_date ,clock_in ,created_at ) 
        VALUES(?,?,?,?)
        """,(employee_id,format_date,format_time,format_date)
    )

    conn.commit()
    conn.close()



# 退勤のデータを追加してデータ更新
def clock_out(format_time,employee_id,format_date):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
            UPDATE attendance_list 
            SET clock_out = ?
            WHERE employee_id = ? AND work_date = ? AND clock_out IS NULL
            """,(format_time,employee_id,format_date)    
    )

    conn.commit()
    conn.close()



#　勤怠のデータを取得
def show_attendance_list():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    # DBから取得した勤怠一覧（タプル）を、文字列のリストに変換する
    cursor.execute("SELECT * FROM attendance_list")
    attendance_list  = cursor.fetchall()
        
    conn.close()

    return attendance_list



#　社員別に勤怠のデータを取得
def show_attendance_by_employee(employee_id):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    # DBから取得した勤怠一覧（タプル）を、文字列のリストに変換する
    cursor.execute("SELECT * FROM attendance_list WHERE employee_id =?",
        (employee_id,)
    )
    attendance_list  = cursor.fetchall()
        
    conn.close()

    return attendance_list