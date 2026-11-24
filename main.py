from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="MAGONA AI VIDEO")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MAGONA AI VIDEO</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#090711;color:#fff;font-family:Arial,sans-serif}
header{padding:22px 7%;display:flex;justify-content:space-between;
align-items:center;border-bottom:1px solid #292037}
.logo{font-size:23px;font-weight:bold;color:#c084fc}
.online{color:#86efac;font-size:12px}
main{max-width:1050px;margin:35px auto;padding:20px}
h1{font-size:34px;color:#d8b4fe}
.subtitle{color:#aaa;margin-bottom:30px}
.panel{background:#151020;border:1px solid #352447;
padding:24px;border-radius:16px;margin-bottom:20px}
h2{font-size:18px;color:#d8b4fe;margin-top:0}
label{display:block;margin:15px 0 8px;color:#ddd;font-size:14px}
textarea,input,select{width:100%;padding:13px;background:#0c0913;
color:white;border:1px solid #49345f;border-radius:9px}
textarea{height:120px;resize:vertical}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
button{background:#9333ea;color:white;border:0;border-radius:9px;
padding:14px 20px;font-weight:bold;cursor:pointer}
button:hover{background:#7e22ce}
.generate{width:100%;font-size:17px;margin-top:18px}
.preview{max-width:100%;max-height:240px;display:none;margin-top:15px;
border-radius:10px}
.note{font-size:12px;color:#aaa;line-height:1.6}
#message{color:#c084fc;margin-top:15px}
footer{text-align:center;color:#777;padding:30px;font-size:12px}
@media(max-width:650px){.grid{grid-template-columns:1fr}main{padding:15px}
h1{font-size:27px}}
</style>
</head>
<body>
<header>
<div class="logo">MAGONA AI VIDEO</div>
<div class="online">● SYSTEM ONLINE</div>
</header>

<main>
<h1>Your AI Video Studio</h1>
<p class="subtitle">Create natural videos with multilingual voices.</p>

<section class="panel">
<h2>01 — Create Your Video</h2>
<label>Describe the video you want</label>
<textarea id="prompt" placeholder="Describe your video, scene, people, actions and dialogue..."></textarea>

<div class="grid">
<div>
<label>Video creation mode</label>
<select id="mode">
<option>Text to Video</option>
<option>Image to Video</option>
<option>Text + Image to Video</option>
</select>
</div>
<div>
<label>Video format</label>
<select id="format">
<option>16:9 — YouTube</option>
<option>9:16 — TikTok / Reels</option>
<option>1:1 — Instagram</option>
</select>
</div>
<div>
<label>Video quality</label>
<select id="quality">
<option>1080p — Full HD</option>
<option>4K — Ultra HD (if supported)</option>
</select>
</div>
<div>
<label>Video duration</label>
<select id="duration">
<option>5 seconds</option>
<option>10 seconds</option>
<option>15 seconds</option>
<option>30 seconds</option>
</select>
</div>
</div>

<label>Upload your image</label>
<input type="file" id="image" accept="image/*">
<img id="preview" class="preview">
</section>

<section class="panel">
<h2>02 — Natural Voice Studio</h2>
<div class="grid">
<div>
<label>Language</label>
<select id="language">
<option>Kiswahili</option>
<option>Kirundi</option>
<option>English</option>
<option>Français</option>
<option>Mandarin Chinese</option>
<option>Kinyarwanda</option>
<option>Arabic</option>
<option>Português</option>
<option>Español</option>
<option>Other languages</option>
</select>
</div>
<div>
<label>Voice type</label>
<select id="voice">
<option>Natural Female Voice</option>
<option>Natural Male Voice</option>
<option>My Own Voice (Authorized)</option>
<option>Multiple Speakers</option>
</select>
</div>
<div>
<label>Voice emotion</label>
<select id="emotion">
<option>Natural / Conversational</option>
<option>Happy</option>
<option>Emotional</option>
<option>Professional</option>
<option>Calm</option>
<option>Excited</option>
</select>
</div>
<div>
<label>Voice style</label>
<select id="accent">
<option>Natural accent</option>
<option>Tanzanian Swahili</option>
<option>Burundian Swahili</option>
<option>Kirundi accent</option>
<option>Other accent</option>
</select>
</div>
</div>

<label>Voice cloning — upload an authorized voice sample</label>
<input type="file" id="voiceFile" accept="audio/*">
<p class="note">Only upload a voice you own or have explicit permission to use.
Voice cloning will be activated after connecting a secure AI voice service.</p>
</section>

<section class="panel">
<h2>03 — Generate Your Video</h2>
<button class="generate" onclick="generate()">GENERATE VIDEO</button>
<p id="message"></p>
<p class="note">Video and voice generation engines will be connected in the next development stage.</p>
</section>
</main>

<footer>MAGONA AI VIDEO © 2026 — YOUR CREATIVE AI STUDIO</footer>

<script>
document.getElementById("image").addEventListener("change",function(){
 const file=this.files[0];
 const preview=document.getElementById("preview");
 if(file){
  preview.src=URL.createObjectURL(file);
  preview.style.display="block";
 }
});
function generate(){
 const prompt=document.getElementById("prompt").value.trim();
 if(!prompt){
  document.getElementById("message").textContent="Please describe your video first.";
  return;
 }
 document.getElementById("message").textContent=
 "Your project settings are ready. AI video generation engine is not connected yet.";
}
</script>
</body>
</html>
"""

@app.get("/health")
def health():
    return {"status": "healthy"}
