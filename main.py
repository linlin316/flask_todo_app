from datetime import datetime
import db


def main(attendance_data="未設定",employee_id=0,attendance_status="未設定"):

    #現在の日付と時間を取得
    dt_now = datetime.now()

    # 週間の曜日
    weekdays = ["月","火","水","木","金","土","日"]

    # 年月日・曜日・時分を変数ごとに分ける
    format_date= dt_now.strftime("%Y年%m月%d日")
    weekday = weekdays[dt_now.weekday()]
    format_time = dt_now.strftime("%H時%M分")

    # 分けた変数をFstringを使って画面に表示する日時に修正
    format_date_time= f"{format_date} {weekday}曜日 \n     {format_time}"


    if attendance_status != "未設定":
        if attendance_status == "出勤":
            db.clock_in(format_date,format_time,employee_id)
            message = "出勤しました。"
            return message
        
        elif attendance_status == "退勤":
            db.clock_out(format_time,employee_id,format_date)
            message = "退勤しました。"
            return message
        

        else:
            return "勤怠データが追加・更新できません"
    
    
    if attendance_data != "未設定":
        if  attendance_data == "勤怠一覧":
            attendance_list = db.show_attendance_list()
            return attendance_list
        
        if  attendance_data == "社員別":
            attendance_list = db.show_attendance_by_employee(employee_id)
            return attendance_list

        else:
            return "勤怠データが見つかりません。"



    

if __name__=="__main__":
    main()