from datetime import datetime
import db


def main(attendance_data="未設定",employee_id=0,attendance_status="未設定"):

    # 現在の日付と時間を取得
    dt_now = datetime.now()

    # 週間の曜日
    weekdays = ["月","火","水","木","金","土","日"]

    # 年月日・曜日・時分を変数ごとに分ける
    format_date= dt_now.strftime("%Y-%m-%d")
    weekday = weekdays[dt_now.weekday()]
    format_time = dt_now.strftime("%H:%M")


    # attendance_statusを確認して、「出勤」の場合は出勤時間を登録し、「退勤」の場合は退勤時間を更新する
    if attendance_status != "未設定":
        if attendance_status == "出勤":
            db.clock_in(format_date,format_time,employee_id)
            # 登録したことを勤務一覧ページにメッセージに表示する
            message = "出勤しました。"
            return message
        
        elif attendance_status == "退勤":
            db.clock_out(format_time,employee_id,format_date)
            # 更新したことを勤務一覧ページにメッセージに表示する
            message = "退勤しました。"
            return message
        
        else:
            return "勤怠データが追加・更新できません"
    


     # attendance_statusを確認して、「勤怠一覧」の場合は全社員のデータを取得、「社員別」の場合は入力した社員番号のデータを取得
    if attendance_data != "未設定":
        if  attendance_data == "勤怠一覧":
            attendance_list = db.show_attendance_list()
            total_attendance = None
            result_total_working_hours = None
            return attendance_list,total_attendance,result_total_working_hours
        
        if  attendance_data == "社員別":
            attendance_list, total_attendance, result_total_working_hours = db.show_attendance_by_employee(employee_id)
            return attendance_list,total_attendance,result_total_working_hours

        else:
            return "勤怠データが見つかりません。"



    

if __name__=="__main__":
    main()