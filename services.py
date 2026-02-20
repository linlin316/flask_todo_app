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
        dt = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S")
        d = dt.date()

        if d == today_date:
            return f"今日 {dt.strftime('%H:%M')}"
        if (today_date - d).days == 1:
            return f"昨日 {dt.strftime('%H:%M')}"
        if d.year == today_date.year:
            return dt.strftime("%m/%d %H:%M")
        return dt.strftime("%Y/%m/%d %H:%M")
    except Exception:
        return created_at_str  # 壊れてたら元のまま