import sqlite3


def init_db():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance_list(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        work_date TEXT NOT NULL,
        clock_in TEXT NOT NULL,
        clock_out TEXT,
        working_hours TEXT,
        created_at TEXT NOT NULL        
    )                
    """)
    
    conn.commit()
    conn.close()

if __name__=="__main__":
    init_db()