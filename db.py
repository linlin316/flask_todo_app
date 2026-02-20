import sqlite3
from datetime import datetime

# 出勤のデータを追加する。
def clock_in(format_date,format_time,employee_id):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()


    # 社員番号・日付・出勤時間・作成日をテーブルにデータを追加
    cursor.execute("""
        INSERT INTO attendance_list 
        (employee_id ,work_date ,clock_in ,created_at ) 
        VALUES(?,?,?,?)
        """,(employee_id,format_date,format_time,format_date)
    )

    conn.commit()
    conn.close()



# 退勤のデータを追加してデータ更新を行う
# 勤務時間を計算し、勤務時間のデータ追加してデータ更新を行う
def clock_out(format_time,employee_id,format_date):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()


    # 社員番号と日付を使ってデータを検索し、退勤時間を追加
    cursor.execute("""
            UPDATE attendance_list 
            SET clock_out = ?
            WHERE employee_id = ? AND work_date = ? AND clock_out IS NULL
            """,(format_time,employee_id,format_date)    
    )


    # 社員番号と日付を使ってデータを検索し、出勤時間を取得
    cursor.execute("""
            SELECT clock_in
            FROM attendance_list
            WHERE employee_id = ? AND work_date = ?
            """,(employee_id,format_date)    
    )
    clock_in_list = cursor.fetchone()
    clock_in = clock_in_list[0]


    # 出勤・退勤から出勤時間を計算
    clock_in_time = datetime.strptime(clock_in,"%H:%M")
    clock_out_time = datetime.strptime(format_time,"%H:%M")
    working_hours = clock_out_time - clock_in_time


    # 勤務時間をテーブルに追加するためにデータを整える
    base_time = datetime(1900, 1, 1)
    temp_datetime = base_time + working_hours
    result_working_hours = temp_datetime.strftime("%H:%M")


    # 社員番号と日付を使ってデータを検索し、退勤時間を追加
    cursor.execute("""
        UPDATE attendance_list 
        SET working_hours = ?
        WHERE employee_id = ? AND work_date = ? AND clock_out = ? AND working_hours IS NULL
        """,(result_working_hours,employee_id,format_date,format_time)    
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


    #　DBから社員別の出勤数を取得
    cursor.execute("SELECT COUNT(*) FROM attendance_list WHERE employee_id =?",
        (employee_id,)
    )
    total_attendance_list = cursor.fetchone()
    total_attendance = total_attendance_list[0]

    conn.close()

    return attendance_list,total_attendance