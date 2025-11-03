import os
import zipfile

# Create temporary folder
folder = "LiquidJane_temp"
os.makedirs(folder, exist_ok=True)

# HTML template for index.html and pages
index_html = """<!DOCTYPE html>https://chatgpt.com/c/6907c17b-37dc-8332-b538-3b510b18fce2
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LiquidJane</title>
<link rel="stylesheet" href="style.css">
<script src="config.js"></script>
<script src="script.js"></script>
</head>
<body onload="applyPageConfig('index')">
<h1 class="title" onclick="goHome()">🧜‍♀️ LIQUIDJANE 🧜‍♀️</h1>
<div class="page-buttons">
  <button class="page" onclick="openPage(1)">🐟</button>
  <button class="page" onclick="openPage(2)">🐠</button>
  <button class="page" onclick="openPage(3)">🐡</button>
  <button class="page" onclick="openPage(4)">🐬</button>
  <button class="page" onclick="openPage(5)">🦈</button>
  <button class="page" onclick="openPage(6)">🐳</button>
  <button class="page" onclick="openPage(7)">🐋</button>
</div>
<div class="instruments">🎷 🎹 🎺 🎸 🥁 🎤 🎻</div>
<div id="cursor">🧜‍♀️</div>
</body>
</html>
"""

page_html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LiquidJane Page {num}</title>
<link rel="stylesheet" href="style.css">
<script src="config.js"></script>
<script src="script.js"></script>
</head>
<body onload="applyPageConfig({num})">
<h1 class="title" onclick="goHome()">🧜‍♀️ LIQUIDJANE 🧜‍♀️</h1>
<div class="instruments">🎷 🎹 🎺 🎸 🥁 🎤 🎻</div>
<div id="cursor">💚</div>
<div class="page-buttons">
  <button class="page" onclick="openPage(1)">🐟</button>
  <button class="page" onclick="openPage(2)">🐠</button>
  <button class="page" onclick="openPage(3)">🐡</button>
  <button class="page" onclick="openPage(4)">🐬</button>
  <button class="page" onclick="openPage(5)">🦈</button>
  <button class="page" onclick="openPage(6)">🐳</button>
  <button class="page" onclick="openPage(7)">🐋</button>
</div>
</body>
</html>
"""

# CSS
style_css = """@import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');
body {
  margin:0;
  overflow:hidden;
  height:100vh;
  font-family:'Bangers','Impact','Arial Black',sans-serif;
  cursor:none;
  background: linear-gradient(180deg,#000033,#003399,#66ccff);
  background-size:400% 400%;
  animation: meltBack 6s ease-in-out infinite alternate-reverse;
}
@keyframes meltBack {
  0%{background-position:100% 100%;}
  100%{background-position:0% 0%;}
}
.title {
  position:absolute;
  top:40px;
  left:50%;
  transform:translateX(-50%);
  font-size:5em;
  font-weight:bold;
  cursor:pointer;
  z-index:10;
  color:#FFA500;
  text-shadow:0 0 20px pink,0 0 40px red;
  -webkit-text-stroke:2px red;
}
.instruments {
  position:absolute;
  bottom:20px;
  width:100%;
  text-align:center;
  font-size:2.5em;
  color:white;
}
.page-buttons {
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%, -50%);
}
.page {
  position:absolute;
  font-size:3em;
  background:none;
  border:none;
  cursor:pointer;
  animation:bob 2s ease-in-out infinite alternate;
}
@keyframes bob {
  0%{transform:translateY(0px);}
  100%{transform:translateY(-10px);}
}
#cursor {
  position:fixed;
  pointer-events:none;
  font-size:2em;
  transform:translate(-50%,-50%);
  z-index:1000;
}
"""

# JS
script_js = """const cursor=document.getElementById("cursor");
document.addEventListener("mousemove",e=>{cursor.style.left=e.pageX+"px";cursor.style.top=e.pageY+"px";});
function openPage(num){window.location.href=`page${num}.html`;}
function goHome(){window.location.href="index.html";}
function applyPageConfig(pageNum){if(!window.pageConfigs)return;const cfg=window.pageConfigs[pageNum];if(cfg){document.body.style.background=`linear-gradient(180deg,${cfg.bgStart},${cfg.bgEnd})`;const title=document.querySelector('.title');if(title){title.style.color=cfg.glow;title.style.textShadow=`0 0 20px ${cfg.glow},0 0 40px ${cfg.glow}`;}}}
// Circle moving fish
const title=document.querySelector('.title');
const buttons=document.querySelectorAll('.page');
let angle=0;
function moveFish(){
  const radius=150;
  angle+=0.02;
  buttons.forEach((btn,i)=>{
    const a=angle+(i*(Math.PI*2/buttons.length));
    btn.style.left=`${50+radius*Math.cos(a)}px`;
    btn.style.top=`${50+radius*Math.sin(a)}px`;
  });
  requestAnimationFrame(moveFish);
}
moveFish();
"""

# Config JS
config_js = """window.pageConfigs={ 'index': { bgStart:'#000033', bgEnd:'#66ccff', glow:'#FFA500' }, 1:{bgStart:'#003300',bgEnd:'#66ff99',glow:'#ff69b4'},2:{bgStart:'#004400',bgEnd:'#77ff88',glow:'#ff3399'},3:{bgStart:'#005500',bgEnd:'#88ff77',glow:'#ff66cc'},4:{bgStart:'#006600',bgEnd:'#99ff66',glow:'#ff33ff'},5:{bgStart:'#007700',bgEnd:'#aaee55',glow:'#ff66aa'},6:{bgStart:'#008800',bgEnd:'#bbff44',glow:'#ff3399'},7:{bgStart:'#009900',bgEnd:'#ccff33',glow:'#ff00ff'}};"""

# 404
html_404 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>404 - Page Not Found</title>
</head>
<body>
<h1>404 - Page Not Found</h1>
<a href="index.html">Go Home</a>
</body>
</html>"""

# Write files
with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

for i in range(1, 8):
    with open(os.path.join(folder, f"page{i}.html"), "w", encoding="utf-8") as f:
        f.write(page_html_template.format(num=i))

with open(os.path.join(folder, "style.css"), "w", encoding="utf-8") as f:
    f.write(style_css)
with open(os.path.join(folder, "script.js"), "w", encoding="utf-8") as f:
    f.write(script_js)
with open(os.path.join(folder, "config.js"), "w", encoding="utf-8") as f:
    f.write(config_js)
with open(os.path.join(folder, "404.html"), "w", encoding="utf-8") as f:
    f.write(html_404)

# Create ZIP
zip_filename = "LiquidJane.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for filename in os.listdir(folder):
        zipf.write(os.path.join(folder, filename), arcname=filename)

print(f"✅ {zip_filename} created! Ready to upload to GitHub.")
