from flask import Flask, request,render_template, redirect
from apps.todo_appdir.routes.todos import todo_bp
import main

app = Flask(__name__)
app.register_blueprint(todo_bp)

# URLを使ったときにトップページ
@app.route("/")
def attendance():

    return render_template("index.html")



#トップページから選択したアプリのページを取得
@app.route("/app",methods=["GET"])
def index():
    app_name = request.args.get("app_name")
    
    if app_name == "勤怠アプリ":
        return render_template("attendance.html")
    elif app_name == "ToDoアプリ":
        return redirect("/todo/")
    else:
        return "アプリ見つかりません"



# 勤怠アプリで選択した内容と社員番号を使ってデータベースにデータを追加・更新
@app.route("/clock",methods=["POST"])
def clock():
    employee_id = request.form.get("employee_id")
    attendance_status = request.form.get("attendance_status")

    if attendance_status is not None:
        message = main.main(employee_id = employee_id, attendance_status = attendance_status)
        return render_template("attendance.html",message=message)
    
    else:
        return "勤怠データが追加・更新できません"
    


# 勤怠アプリで勤怠の内容を見るためにデータベースに入っているデータを取得
@app.route("/data",methods=["GET"])
def attendance_data_page():
    attendance_data = request.args.get("attendance_data")
    employee_id = request.args.get("employee_id")

    if attendance_data is not None:
        attendance_list,total_attendance,result_total_working_hours= main.main(attendance_data = attendance_data, employee_id = employee_id)
        return render_template("attendance_result.html", attendance_list = attendance_list, employee_id = employee_id, total_attendance=total_attendance, result_total_working_hours=result_total_working_hours)
    
    else:
        return "勤怠データが見つかりません。"
    
    


        
# アプリを起動
if __name__=="__main__":
    app.run(debug=True)