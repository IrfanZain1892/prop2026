from flask import Flask, make_response
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SYSTEM BREACH</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #000;
      color: #ff0000;
      font-family: 'Share Tech Mono', 'Courier New', monospace;
      min-height: 100vh;
      overflow: hidden;
      cursor: none;
    }
    body::before {
      content: '';
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(255,0,0,0.03) 2px,
        rgba(255,0,0,0.03) 4px
      );
      pointer-events: none;
      z-index: 999;
    }
    body::after {
      content: '';
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.85) 100%);
      pointer-events: none;
      z-index: 998;
    }
    #skull {
      text-align: center;
      font-size: clamp(40px, 12vw, 80px);
      padding-top: 20px;
      animation: pulse 1s infinite;
      text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000;
    }
    #header {
      text-align: center;
      padding: 5px 10px;
      font-size: clamp(16px, 4.5vw, 28px);
      font-weight: bold;
      letter-spacing: 3px;
      text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
      animation: glitch 2s infinite;
    }
    #subheader {
      text-align: center;
      font-size: clamp(10px, 2.5vw, 13px);
      color: #ff4444;
      padding: 4px 20px 12px;
      letter-spacing: 1px;
    }
    #ip-box {
      text-align: center;
      font-size: clamp(10px, 2.5vw, 13px);
      color: #ff6600;
      margin-bottom: 10px;
      animation: flicker 3s infinite;
    }
    #log-box {
      margin: 0 15px;
      height: 38vh;
      overflow: hidden;
      border: 1px solid #330000;
      border-left: 3px solid #ff0000;
      padding: 8px 12px;
      font-size: clamp(9px, 2.3vw, 12px);
      line-height: 1.7;
      background: rgba(20,0,0,0.6);
      box-shadow: inset 0 0 20px rgba(255,0,0,0.1), 0 0 10px rgba(255,0,0,0.2);
    }
    .log-line { color: #cc0000; }
    .log-line.ok { color: #ff4400; }
    .log-line.warn { color: #ff0000; font-weight: bold; text-shadow: 0 0 5px #ff0000; }
    #progress-label {
      text-align: center;
      margin: 10px 0 4px;
      font-size: clamp(10px, 2.8vw, 13px);
      font-weight: bold;
      letter-spacing: 2px;
      text-shadow: 0 0 8px #ff0000;
    }
    #progress-track {
      margin: 0 15px;
      height: 18px;
      background: #0d0000;
      border: 1px solid #440000;
      box-shadow: 0 0 10px rgba(255,0,0,0.3);
    }
    #progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #660000, #ff0000);
      box-shadow: 0 0 10px #ff0000;
      transition: width 0.3s;
    }
    #footer {
      text-align: center;
      margin-top: 10px;
      font-size: clamp(8px, 2.2vw, 11px);
      color: #ff0000;
      letter-spacing: 1px;
      animation: flicker 1.5s infinite;
      text-shadow: 0 0 5px #ff0000;
    }
    #redirect-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: #000;
      z-index: 9999;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    #redirect-overlay.show { display: flex; }
    #gotcha {
      font-size: clamp(40px, 15vw, 90px);
      animation: pulse 0.5s infinite;
    }
    #gotcha-text {
      font-size: clamp(24px, 8vw, 52px);
      font-weight: bold;
      color: #ff0000;
      letter-spacing: 4px;
      text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000;
      margin: 10px 0;
      animation: glitch 0.5s infinite;
    }
    #gotcha-sub {
      font-size: clamp(12px, 3.5vw, 18px);
      color: #ff6600;
      margin-bottom: 20px;
      letter-spacing: 2px;
    }
    #follow-btn {
      display: inline-block;
      margin-top: 15px;
      padding: 14px 35px;
      background: transparent;
      border: 2px solid #ff0000;
      color: #ff0000;
      font-family: 'Share Tech Mono', monospace;
      font-size: clamp(14px, 4vw, 20px);
      letter-spacing: 3px;
      text-decoration: none;
      text-shadow: 0 0 10px #ff0000;
      box-shadow: 0 0 15px #ff0000, inset 0 0 15px rgba(255,0,0,0.1);
      animation: borderPulse 1s infinite;
      cursor: pointer;
    }
    #countdown-text {
      margin-top: 20px;
      font-size: clamp(10px, 2.5vw, 13px);
      color: #660000;
      letter-spacing: 1px;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.7; transform: scale(1.05); }
    }
    @keyframes flicker {
      0%, 100% { opacity: 1; }
      92% { opacity: 1; }
      93% { opacity: 0.3; }
      94% { opacity: 1; }
      96% { opacity: 0.5; }
      97% { opacity: 1; }
    }
    @keyframes glitch {
      0%, 100% { text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000; transform: translate(0); }
      92% { transform: translate(0); }
      93% { transform: translate(-3px, 1px); text-shadow: 3px 0 #ff4400, -3px 0 #cc0000; }
      94% { transform: translate(3px, -1px); }
      95% { transform: translate(0); }
    }
    @keyframes borderPulse {
      0%, 100% { box-shadow: 0 0 15px #ff0000, inset 0 0 15px rgba(255,0,0,0.1); }
      50% { box-shadow: 0 0 30px #ff0000, 0 0 50px #ff0000, inset 0 0 20px rgba(255,0,0,0.2); }
    }
  </style>
</head>
<body>

<div id="skull">💀</div>
<div id="header">⚠ SYSTEM BREACH DETECTED ⚠</div>
<div id="subheader">YOUR DEVICE HAS BEEN COMPROMISED</div>
<div id="ip-box">LOCATING YOUR IP ADDRESS...</div>
<div id="log-box"></div>
<div id="progress-label">ENCRYPTING FILES: 0%</div>
<div id="progress-track"><div id="progress-fill"></div></div>
<div id="footer">⚠ DO NOT CLOSE — DO NOT RESTART — DO NOT CALL POLICE ⚠</div>

<div id="redirect-overlay">
  <div id="gotcha">😈</div>
  <div id="gotcha-text">GOTCHA!</div>
  <div id="gotcha-sub">lu kena prank wkwkwk 😭🔥</div>
  <a id="follow-btn" href="https://www.instagram.com/irfanzain___/" target="_blank">
    FOLLOW ᮄᮁᮖᮔ᮪ ᮐᮄᮔ᮪ 😈
  </a>
  <div id="countdown-text">auto redirect dalam <span id="countdown">5</span> detik...</div>
</div>

<script>
const logs = [
  ["Initializing payload...", ""],
  ["Scanning device model... Android", "ok"],
  ["Bypassing Android security... [OK]", "ok"],
  ["Accessing /storage/emulated/0... [OK]", "ok"],
  ["Reading contacts list... 247 found [OK]", "ok"],
  ["Dumping WhatsApp messages... 3,847 msgs [OK]", "ok"],
  ["Stealing Instagram session... [OK]", "ok"],
  ["Stealing TikTok cookies... [OK]", "ok"],
  ["Accessing front camera... [OK]", "ok"],
  ["Accessing microphone... [OK]", "ok"],
  ["Screenshot captured... [OK]", "ok"],
  ["Extracting saved passwords... 34 found [OK]", "ok"],
  ["Reading SMS messages... [OK]", "ok"],
  ["Accessing location GPS... [OK]", "ok"],
  ["Location: Bandung, West Java, ID", "warn"],
  ["Uploading data to 45.142.212.100...", ""],
  ["Contacts uploaded... [OK]", "ok"],
  ["Photos uploaded... 2,341 files [OK]", "ok"],
  ["Installing persistent backdoor... [OK]", "ok"],
  ["Keylogger activated... [OK]", "ok"],
  ["WARNING: All files are being encrypted!", "warn"],
  ["Encrypting /WhatsApp/Media... [OK]", "ok"],
  ["Encrypting /DCIM/Camera... [OK]", "ok"],
  ["Encrypting /Downloads... [OK]", "ok"],
  ["Encrypting /Documents... [OK]", "ok"],
  ["Remote access granted to hacker...", "warn"],
  ["Bitcoin ransom: 0.05 BTC = ~$3,200", "warn"],
  ["Wallet: 1A2B3C4D5E6F7G8H9I0J", ""],
  ["DEVICE FULLY COMPROMISED 💀", "warn"],
  [">>> ENCRYPTION 100% COMPLETE <<<", "warn"],
];

const logBox = document.getElementById('log-box');
const progressFill = document.getElementById('progress-fill');
const progressLabel = document.getElementById('progress-label');
const header = document.getElementById('header');
const ipDisplay = document.getElementById('ip-box');
const overlay = document.getElementById('redirect-overlay');
const countdownEl = document.getElementById('countdown');

let progress = 0;
let logIndex = 0;

function fakeIP() {
  return `${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}.${Math.floor(Math.random()*255)}`;
}

setTimeout(() => {
  ipDisplay.textContent = `TARGET IP IDENTIFIED: ${fakeIP()} — LOCATION: INDONESIA`;
}, 1500);

function addLog(text, cls) {
  const line = document.createElement('div');
  line.className = 'log-line ' + cls;
  line.textContent = '> ' + text;
  logBox.appendChild(line);
  logBox.scrollTop = logBox.scrollHeight;
}

function updateProgress(val) {
  progressFill.style.width = val + '%';
  progressLabel.textContent = 'ENCRYPTING FILES: ' + val + '%';
}

function showGotcha() {
  overlay.classList.add('show');
  let sec = 5;
  const timer = setInterval(() => {
    sec--;
    countdownEl.textContent = sec;
    if (sec <= 0) {
      clearInterval(timer);
      window.location.href = 'https://www.instagram.com/irfanzain___/';
    }
  }, 1000);
}

function nextStep() {
  if (logIndex < logs.length) {
    addLog(logs[logIndex][0], logs[logIndex][1]);
    logIndex++;
  }

  progress += Math.floor(Math.random() * 4) + 1;
  if (progress > 100) progress = 100;
  updateProgress(progress);

  if (progress >= 100) {
    header.textContent = '💀 YOUR DEVICE IS OWNED 💀';
    setTimeout(showGotcha, 1500);
    return;
  }

  setTimeout(nextStep, Math.random() * 350 + 120);
}

window.onload = () => setTimeout(nextStep, 800);
</script>
</body>
</html>
"""

@app.route("/")
def index():
    resp = make_response(HTML)
    resp.headers['Content-Type'] = 'text/html'
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
