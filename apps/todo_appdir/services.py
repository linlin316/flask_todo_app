from datetime import datetime

# 時間を見やすくになる
def pretty_created_at(created_at_str: str, today_date):
    """
    DBの created_at を人間向け表示に変換
    例：
      今日 16:24
      昨日 09:10
      02/19 15:04
    """
    try:
        created_dt = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S")
        created_date = created_dt.date()

        if created_date == today_date:
            return f"今日 {created_dt.strftime('%H:%M')}"
        
        if (today_date - created_date).days == 1:
            return f"昨日 {created_dt.strftime('%H:%M')}"
        
        if created_date.year == today_date.year:
            return created_dt.strftime("%m/%d %H:%M")
        
        return created_dt.strftime("%Y/%m/%d %H:%M")
    
    except Exception:
        return created_at_str  # 壊れてたら元のまま