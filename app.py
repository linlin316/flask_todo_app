from flask import Flask, request,render_template
from datetime import datetime
import main

app = Flask(__name__)

@app.route("/")
def index():
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
    return render_template("index.html",date_time = format_date_time)



# 選択した内容と社員番号を使ってデータベースにデータを追加・更新
@app.route("/clock",methods=["POST"])
def clock():
    employee_id = request.form.get("employee_id")
    attendance_status = request.form.get("attendance_status")

    if attendance_status is not None:
        format_date_time,message = main.main(employee_id,attendance_status)
        return render_template("index.html",date_time = format_date_time,message=message)
    
    else:
        return "未対応の地域です。", 404
    


# 選択した内容と社員番号を使ってデータベースにデータを追加・更新
@app.route("/data",methods=["GET"])
def attendance_data_page():
    attendance = request.args.get("attendance")

    if attendance is not None:
        attendance_list = main.main()
        return render_template("result.html",attendance_list = attendance_list)
    
    else:
        return "未対応の地域です。", 404
    
    


        
# アプリを起動
if __name__=="__main__":
    app.run(debug=True)