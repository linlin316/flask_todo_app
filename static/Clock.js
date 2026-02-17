// JavaScriptファイル または <script>タグ内に追加
function updateClock() {
    const now = new Date();

    // 日付と曜日の計算 
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // 1月は0から始まるので+1
    const date = String(now.getDate()).padStart(2, '0');
    const dayNames = ['日', '月', '火', '水', '木', '金', '土'];
    const day = dayNames[now.getDay()]; // 曜日を文字に変換

    // 画面に「〇〇年〇〇月〇〇日 〇曜日」を表示
    document.getElementById('date-display').textContent = `${year}年${month}月${date}日 ${day}曜日`;

    // デジタル時計の表示 
    document.getElementById('digital-time').textContent = now.toLocaleTimeString('ja-JP', {
        hour: '2-digit',
        minute: '2-digit'
    });
    
    // 現在の時刻を取得
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    
    // 各針の角度を計算
    const secondDegrees = (seconds / 60) * 360;
    const minuteDegrees = (minutes / 60) * 360 + (seconds / 60) * 6;
    const hourDegrees = (hours % 12 / 12) * 360 + (minutes / 60) * 30;
    
    // 針を回転させる
    document.querySelector('.second-hand').style.transform = 
        `rotate(${secondDegrees}deg)`;
    document.querySelector('.minute-hand').style.transform = 
        `rotate(${minuteDegrees}deg)`;
    document.querySelector('.hour-hand').style.transform = 
        `rotate(${hourDegrees}deg)`;

    // ここに追加：デジタル時計の文字を更新 
    document.getElementById('digital-time').textContent = now.toLocaleTimeString('ja-JP');
}

// 1秒ごとに時計を更新
setInterval(updateClock, 1000);

// ページ読み込み時に即座に表示
updateClock();
