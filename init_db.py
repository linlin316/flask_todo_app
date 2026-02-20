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

    cursor.execute("""
        INSERT INTO attendance_list 
        (employee_id, work_date, clock_in, clock_out, working_hours, created_at ) 
        VALUES(?,?,?,?,?,?)
        """,(1,"2026-02-21","11:50", "11:55", "00:05", "2026-02-21")
    )

    cursor.execute("""
        INSERT INTO attendance_list 
        (employee_id, work_date, clock_in, clock_out, working_hours, created_at ) 
        VALUES(?,?,?,?,?,?)
        """,(1,"2026-02-22","11:50", "11:55", "00:05", "2026-02-22")
    )
    
    
    cursor.execute("""
        INSERT INTO attendance_list 
        (employee_id, work_date, clock_in, clock_out, working_hours, created_at ) 
        VALUES(?,?,?,?,?,?)
        """,(1,"2026-02-23","11:50", "11:55", "00:05", "2026-02-23")
    )
    
    conn.commit()
    conn.close()

if __name__=="__main__":
    init_db()