from flask import Flask, request,render_template
from datetime import datetime
import main

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")



# 選択した内容と社員番号を使ってデータベースにデータを追加・更新
@app.route("/clock",methods=["POST"])
def clock():
    employee_id = request.form.get("employee_id")
    attendance_status = request.form.get("attendance_status")

    if attendance_status is not None:
        message = main.main(employee_id,attendance_status)
        return render_template("index.html",message=message)
    
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