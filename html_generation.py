import json

with open("img_data.json") as f:
    imgs = json.load(f)

logo = imgs["logo"]
black_dates = imgs["black_dates"]
deseeded = imgs["deseeded"]
dates_pkt = imgs["dates_pkt"]
mascot = imgs["mascot"]

# Google Apps Script URL from the uploaded file
GAS_URL = "https://script.google.com/macros/s/AKfycbzd4FN5woLzJM0NSPfByt4jV2IT8h_xeO9RkvB6RVecWaV9WH1d-wkEECXuTk4_FErOHg/exec"

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Karuda Dates — Consumer Poll</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* =========================================================
   BASE RESET & ROOT
========================================================= */
:root {
  --crimson:    #9B1C1C;
  --crimson2:   #C0392B;
  --gold:       #C9960A;
  --gold-light: #F0C040;
  --gold-pale:  #F5DFA0;
  --deep-red:   #5E0A0A;
  --bg:         #0D0303;
  --bg2:        #1A0707;
  --card:       rgba(255,255,255,0.045);
  --cream:      #FFF8EC;
  --muted:      #C0935A;
  --border:     rgba(201,150,10,0.22);
  --slide-h:    100dvh;
}
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
html, body {
  width:100%; height:100%;
  overflow:hidden;
  font-family:'Poppins', sans-serif;
  background:var(--bg);
  color:var(--cream);
  -webkit-font-smoothing:antialiased;
}

/* =========================================================
   SLIDE ENGINE — fullscreen, one slide visible at a time
========================================================= */
#deck {
  position:fixed; inset:0;
  display:flex; flex-direction:column;
}
.slide {
  position:absolute; inset:0;
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  opacity:0; pointer-events:none;
  transition:opacity 0.55s ease, transform 0.55s ease;
  transform:translateY(30px);
  overflow-y:auto; overflow-x:hidden;
  padding:0 0 env(safe-area-inset-bottom,0);
}
.slide.active {
  opacity:1; pointer-events:all;
  transform:translateY(0);
  z-index:10;
}
.slide.exit-up {
  opacity:0; transform:translateY(-30px); pointer-events:none; z-index:9;
}

/* =========================================================
   PROGRESS BAR (top of screen)
========================================================= */
#progress-bar {
  position:fixed; top:0; left:0; right:0;
  height:3px; z-index:999;
  background:rgba(255,255,255,0.07);
}
#progress-fill {
  height:100%;
  background:linear-gradient(90deg, var(--crimson), var(--gold-light));
  transition:width 0.5s ease;
  border-radius:0 2px 2px 0;
}

/* Step indicator dots */
#step-dots {
  position:fixed; bottom:20px; left:50%; transform:translateX(-50%);
  display:flex; gap:8px; z-index:999;
  pointer-events:none;
}
.step-dot {
  width:6px; height:6px; border-radius:50%;
  background:rgba(201,150,10,0.25);
  transition:all 0.3s;
}
.step-dot.lit {
  background:var(--gold-light);
  box-shadow:0 0 6px rgba(240,192,64,0.6);
  transform:scale(1.4);
}

/* =========================================================
   SHARED HELPERS
========================================================= */
@keyframes fadeUp   { from{transform:translateY(22px);opacity:0} to{transform:translateY(0);opacity:1} }
@keyframes shimmer  { 0%{background-position:200% center} 100%{background-position:-200% center} }
@keyframes pulsGlow { 0%,100%{filter:drop-shadow(0 0 16px rgba(201,150,10,.35)) } 50%{filter:drop-shadow(0 0 42px rgba(201,150,10,.8))} }
@keyframes float    { 0%,100%{transform:translateY(0px)} 50%{transform:translateY(-8px)} }
@keyframes spin     { to{transform:rotate(360deg)} }
@keyframes barLoad  { to{width:100%} }

.gold-line {
  width:100px; height:2px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  margin:16px auto;
}
.eyebrow {
  font-size:0.68rem; letter-spacing:4px; text-transform:uppercase;
  color:var(--gold); margin-bottom:6px; text-align:center;
}
.slide-title {
  font-family:'Playfair Display',serif;
  font-size:clamp(1.6rem,5vw,2.4rem);
  font-weight:900; text-align:center; line-height:1.25;
}
.gold-shimmer {
  background:linear-gradient(135deg,#F5DFA0 0%,#F0C040 35%,#C9960A 65%,#F0C040 100%);
  background-size:200% auto;
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text;
  animation:shimmer 4s linear infinite;
}

/* =========================================================
   SLIDE 0 — LOADER
========================================================= */
#s-loader {
  background:radial-gradient(ellipse at 40% 55%, #250707 0%, #090101 100%);
  z-index:20;
}
.loader-particles { position:absolute;inset:0;pointer-events:none;overflow:hidden; }
.lp {
  position:absolute; border-radius:50% 50% 42% 42%;
  background:radial-gradient(ellipse,#7B3A10 0%,#3B1606 60%,transparent 80%);
  opacity:0; animation:lpFloat linear infinite;
}
@keyframes lpFloat {
  0%   { transform:translateY(110vh) rotate(0deg);opacity:0; }
  8%   { opacity:.22; }
  92%  { opacity:.22; }
  100% { transform:translateY(-10vh) rotate(400deg);opacity:0; }
}
.loader-logo { animation:pulsGlow 2.2s ease-in-out infinite; }
.loader-logo img { width:clamp(160px,35vw,220px); height:auto; display:block; }
.loader-tag {
  margin-top:12px; font-family:'Playfair Display',serif; font-style:italic;
  font-size:0.95rem; color:var(--gold-light); letter-spacing:4px;
  text-transform:uppercase; opacity:0;
  animation:fadeUp 0.8s 0.7s forwards;
}
.bar-wrap { margin-top:30px; width:190px; height:3px; background:rgba(255,255,255,.08); border-radius:4px; overflow:hidden; }
.bar-fill  { height:100%; width:0%; background:linear-gradient(90deg,var(--crimson),var(--gold-light)); border-radius:4px; animation:barLoad 2.6s cubic-bezier(.4,0,.2,1) forwards; }

/* =========================================================
   SLIDE 1 — BRAND HERO
========================================================= */
#s-brand {
  background:
    radial-gradient(ellipse 65% 50% at 15% 55%, rgba(155,28,28,.35) 0%,transparent 60%),
    radial-gradient(ellipse 55% 40% at 85% 45%, rgba(140,80,0,.2) 0%,transparent 60%),
    linear-gradient(155deg,#100404 0%,#1C0808 45%,#0C0202 100%);
}
.brand-wrap { width:100%; max-width:520px; padding:32px 20px 72px; text-align:center; position:relative; z-index:2; }
.brand-logo  { animation:pulsGlow 2.8s ease-in-out infinite, float 3.5s ease-in-out infinite; display:inline-block; }
.brand-logo img { width:clamp(150px,32vw,200px); height:auto; }
.brand-title { margin-top:14px; }
.brand-sub   { font-size:.75rem; color:var(--muted); letter-spacing:3px; text-transform:uppercase; margin-top:4px; }
.product-grid { display:flex; gap:12px; justify-content:center; margin-top:20px; flex-wrap:wrap; }
.prod-card {
  flex:1; min-width:90px; max-width:140px;
  background:rgba(255,255,255,0.04);
  border:1px solid var(--border);
  border-radius:14px; overflow:hidden;
  cursor:pointer; transition:all .3s;
  position:relative;
}
.prod-card:hover, .prod-card.active-prod {
  border-color:rgba(201,150,10,0.55);
  transform:translateY(-4px);
  box-shadow:0 12px 32px rgba(0,0,0,0.5), 0 0 0 1px rgba(201,150,10,0.3);
}
.prod-card img { width:100%; aspect-ratio:1; object-fit:contain; background:#1a0606; display:block; padding:8px; }
.prod-card-label { font-size:.65rem; letter-spacing:1px; text-transform:uppercase; color:var(--muted); padding:6px 4px; text-align:center; line-height:1.3; }

.brand-cta {
  margin-top:24px;
  background:none; border:1px solid var(--border);
  border-radius:50px; padding:11px 32px;
  font-family:'Poppins',sans-serif; font-size:.8rem;
  letter-spacing:2px; color:var(--gold-pale);
  cursor:pointer; text-transform:uppercase;
  transition:all .3s;
}
.brand-cta:hover { background:rgba(201,150,10,0.15); border-color:var(--gold); }

/* floating date background */
.fd-wrap { position:absolute;inset:0;pointer-events:none;overflow:hidden; }
.fd {
  position:absolute; border-radius:50% 50% 44% 44%;
  background:radial-gradient(ellipse at 40% 30%,#7B3A10,#2E1005);
  opacity:0; animation:lpFloat linear infinite;
  box-shadow:inset 0 -2px 4px rgba(0,0,0,.4);
}

/* =========================================================
   SLIDE 2 — NAME
========================================================= */
#s-name {
  background:
    radial-gradient(ellipse 70% 60% at 50% 20%, rgba(155,28,28,.22) 0%,transparent 65%),
    linear-gradient(180deg,#0E0404 0%,#080101 100%);
}
#s-name::before {
  content:''; position:absolute; inset:0; pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg width='56' height='56' xmlns='http://www.w3.org/2000/svg'%3E%3Cellipse cx='28' cy='28' rx='3.5' ry='5' fill='rgba(100,38,8,0.06)'/%3E%3C/svg%3E") repeat;
}
.name-card {
  width:100%; max-width:480px; padding:32px 20px 80px;
  position:relative; z-index:2; text-align:center;
}
.name-card .eyebrow { animation:fadeUp .6s .1s both; }
.name-card .slide-title { animation:fadeUp .6s .2s both; margin-bottom:8px; }
.name-card .section-sub { animation:fadeUp .6s .3s both; }
.section-sub {
  font-size:clamp(.8rem,2.4vw,.92rem); color:var(--muted);
  line-height:1.65; font-weight:300; margin-bottom:28px; text-align:center;
}
.input-wrap { position:relative; margin-top:8px; animation:fadeUp .6s .4s both; }
.input-icon {
  position:absolute; left:16px; top:50%; transform:translateY(-50%);
  font-size:1.1rem; pointer-events:none;
}
.name-input {
  width:100%; background:rgba(255,255,255,.06);
  border:1.5px solid var(--border); border-radius:14px;
  padding:15px 18px 15px 46px;
  font-family:'Poppins',sans-serif; font-size:1rem;
  color:var(--cream); outline:none;
  transition:border-color .3s, box-shadow .3s, background .3s;
}
.name-input:focus {
  border-color:var(--gold-light);
  background:rgba(255,255,255,.09);
  box-shadow:0 0 0 4px rgba(240,192,64,.12);
}
.name-input::placeholder { color:rgba(255,248,236,.28); }
.err-msg { color:#FF6B6B; font-size:.75rem; margin-top:8px; display:none; }

.btn-next {
  width:100%; margin-top:18px;
  background:linear-gradient(135deg, var(--crimson), #6E1010);
  border:none; border-radius:14px;
  padding:15px; font-family:'Poppins',sans-serif;
  font-size:.88rem; font-weight:600; letter-spacing:2px;
  text-transform:uppercase; color:var(--cream);
  cursor:pointer; position:relative; overflow:hidden;
  transition:all .3s;
  box-shadow:0 8px 28px rgba(155,28,28,.4);
  animation:fadeUp .6s .5s both;
}
.btn-next::after {
  content:''; position:absolute; inset:0;
  background:linear-gradient(135deg,rgba(240,192,64,.18),transparent);
  opacity:0; transition:opacity .3s;
}
.btn-next:hover::after { opacity:1; }
.btn-next:hover { transform:translateY(-2px); box-shadow:0 12px 36px rgba(155,28,28,.5); }
.btn-next:active { transform:translateY(0); }

/* language row */
.lang-row { display:flex; justify-content:center; gap:10px; margin-bottom:24px; animation:fadeUp .6s .0s both; }
.lang-btn {
  background:rgba(255,255,255,.05); border:1px solid var(--border);
  border-radius:50px; padding:5px 18px;
  font-family:'Poppins',sans-serif; font-size:.72rem; letter-spacing:1px;
  color:var(--muted); cursor:pointer; transition:all .25s;
}
.lang-btn.on { background:var(--gold); color:var(--bg); border-color:var(--gold); font-weight:600; }

/* =========================================================
   SLIDE 3 — POLL
========================================================= */
#s-poll {
  background:
    radial-gradient(ellipse 55% 35% at 50% 0%, rgba(100,20,20,.3) 0%,transparent 55%),
    linear-gradient(180deg,#0C0303 0%,#060000 100%);
  align-items:stretch; justify-content:flex-start;
  overflow-y:auto;
}
#s-poll::before {
  content:''; position:absolute; inset:0; pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg width='56' height='56' xmlns='http://www.w3.org/2000/svg'%3E%3Cellipse cx='28' cy='28' rx='3.5' ry='5' fill='rgba(100,38,8,0.06)'/%3E%3C/svg%3E") repeat;
}
.poll-inner {
  width:100%; max-width:580px; margin:0 auto;
  padding:40px 18px 100px;
  position:relative; z-index:2;
}
.poll-q-header { text-align:center; margin-bottom:24px; }
.voter-greeting {
  font-family:'Playfair Display',serif;
  font-size:clamp(1rem,3vw,1.25rem);
  color:var(--gold-pale); margin-bottom:4px;
}
.choices { display:flex; flex-direction:column; gap:10px; }
.choice {
  display:flex; align-items:center; gap:14px;
  background:rgba(255,255,255,0.04);
  border:1.5px solid rgba(201,150,10,0.16);
  border-radius:16px; padding:16px 18px;
  cursor:pointer; transition:all .25s; position:relative;
  overflow:hidden;
}
.choice::before {
  content:''; position:absolute; inset:0;
  background:linear-gradient(135deg,rgba(155,28,28,.12),rgba(201,150,10,.06));
  opacity:0; transition:opacity .25s;
}
.choice:hover::before, .choice.picked::before { opacity:1; }
.choice:hover { border-color:rgba(201,150,10,.4); transform:translateX(4px); }
.choice.picked {
  border-color:var(--gold-light);
  box-shadow:0 4px 24px rgba(201,150,10,.18), inset 0 0 0 1px rgba(240,192,64,.12);
}
.choice input[type=radio] { display:none; }
.radio-ring {
  width:22px; height:22px; flex-shrink:0; border-radius:50%;
  border:2px solid rgba(201,150,10,.35);
  display:flex; align-items:center; justify-content:center;
  transition:all .25s; position:relative; z-index:1;
}
.choice.picked .radio-ring { border-color:var(--gold-light); background:var(--gold-light); }
.radio-ring::after {
  content:''; width:8px; height:8px; border-radius:50%;
  background:var(--bg); opacity:0; transition:opacity .2s;
}
.choice.picked .radio-ring::after { opacity:1; }
.choice-text { flex:1; font-size:clamp(.85rem,2.4vw,.95rem); font-weight:500; line-height:1.4; position:relative; z-index:1; }
.choice-num {
  font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:700;
  color:rgba(201,150,10,.25); transition:color .25s;
  min-width:26px; text-align:right; position:relative; z-index:1;
}
.choice.picked .choice-num { color:var(--gold); }
.choice-err { color:#FF6B6B; font-size:.75rem; margin-top:10px; display:none; }
.submit-row { margin-top:20px; }

/* SUBMIT BUTTON — big and prominent */
.btn-submit {
  width:100%; background:linear-gradient(135deg,var(--crimson),#6E1010);
  border:none; border-radius:14px; padding:16px;
  font-family:'Poppins',sans-serif; font-size:.9rem;
  font-weight:700; letter-spacing:2.5px; text-transform:uppercase;
  color:var(--cream); cursor:pointer; position:relative; overflow:hidden;
  transition:all .3s; box-shadow:0 8px 28px rgba(155,28,28,.45);
}
.btn-submit::after { content:''; position:absolute; inset:0; background:linear-gradient(135deg,rgba(240,192,64,.2),transparent); opacity:0; transition:opacity .3s; }
.btn-submit:hover::after { opacity:1; }
.btn-submit:hover { transform:translateY(-2px); box-shadow:0 14px 40px rgba(155,28,28,.55); }
.btn-submit:disabled { opacity:.55; cursor:not-allowed; transform:none; }

/* submitting spinner */
.spinner {
  display:inline-block; width:16px; height:16px;
  border:2px solid rgba(255,255,255,.3);
  border-top-color:white; border-radius:50%;
  animation:spin .7s linear infinite; vertical-align:middle; margin-right:8px;
}

/* =========================================================
   SLIDE 4 — THANK YOU
========================================================= */
#s-ty {
  background:radial-gradient(ellipse at 50% 30%, rgba(155,28,28,.45) 0%, #080101 70%);
}
.ty-stars { position:absolute;inset:0;pointer-events:none; }
.ty-star {
  position:absolute; border-radius:50%;
  background:var(--gold-light); opacity:0;
  animation:twinkle ease-in-out infinite;
}
@keyframes twinkle { 0%,100%{opacity:0;transform:scale(.5)} 50%{opacity:.7;transform:scale(1.5)} }

.ty-inner { text-align:center; padding:32px 24px 80px; position:relative; z-index:2; max-width:520px; }
.ty-mascot { animation:mascotBounce 1s .3s both; display:inline-block; }
.ty-mascot img { width:clamp(90px,20vw,130px); height:auto; filter:drop-shadow(0 0 28px rgba(201,150,10,.5)); }
@keyframes mascotBounce { 0%{transform:translateY(40px);opacity:0} 60%{transform:translateY(-8px);opacity:1} 100%{transform:translateY(0);opacity:1} }
.ty-logo { margin-top:16px; animation:fadeUp .7s .7s both; }
.ty-logo img { width:clamp(120px,25vw,160px); height:auto; filter:drop-shadow(0 2px 14px rgba(201,150,10,.4)); }
.ty-title {
  font-family:'Playfair Display',serif;
  font-size:clamp(2rem,7vw,3.2rem); font-weight:900;
  color:var(--gold-light); margin-top:20px;
  animation:fadeUp .7s .9s both;
  text-shadow:0 4px 28px rgba(201,150,10,.35);
}
.ty-name { font-family:'Playfair Display',serif; font-size:clamp(1.1rem,3.5vw,1.6rem); color:var(--cream); margin-top:6px; animation:fadeUp .7s 1s both; }
.ty-msg { font-size:clamp(.82rem,2.3vw,.95rem); color:var(--muted); max-width:400px; margin:14px auto 0; line-height:1.7; animation:fadeUp .7s 1.1s both; }
.ty-msg-ta { font-size:clamp(.78rem,2.1vw,.9rem); color:rgba(192,147,90,.6); max-width:400px; margin:6px auto 0; animation:fadeUp .7s 1.15s both; }
.ty-choice-box {
  margin:22px auto 0; max-width:440px;
  background:rgba(255,255,255,.05); border:1px solid rgba(201,150,10,.22);
  border-radius:16px; padding:16px 24px;
  animation:fadeUp .7s 1.2s both;
}
.ty-choice-box p { font-size:.68rem; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin-bottom:7px; }
.ty-choice-box strong { font-family:'Playfair Display',serif; font-size:clamp(.95rem,2.5vw,1.1rem); color:var(--cream); }
.ty-tag { font-size:.68rem; letter-spacing:3px; text-transform:uppercase; color:rgba(201,150,10,.4); margin-top:28px; animation:fadeUp .7s 1.3s both; }

/* confetti */
.confetti { position:fixed; pointer-events:none; z-index:9998; border-radius:2px; animation:confettiFall linear forwards; }
@keyframes confettiFall { 0%{transform:translateY(-20px) rotate(0deg);opacity:1} 100%{transform:translateY(100vh) rotate(720deg);opacity:0} }

/* =========================================================
   ADMIN BUTTON + MODAL
========================================================= */
#admin-btn {
  position:fixed; bottom:env(safe-area-inset-bottom,0); right:0;
  padding:10px 16px 12px;
  background:transparent; border:none;
  font-size:.62rem; letter-spacing:1.5px; text-transform:uppercase;
  color:rgba(255,255,255,.13); cursor:pointer;
  transition:color .2s; z-index:200;
}
#admin-btn:hover { color:rgba(255,255,255,.45); }
#admin-modal {
  display:none; position:fixed; inset:0; z-index:9999;
  background:rgba(0,0,0,.88); align-items:center; justify-content:center;
  backdrop-filter:blur(10px);
}
#admin-modal.open { display:flex; }
.admin-box {
  background:linear-gradient(135deg,#180606,#2A0E0E);
  border:1px solid rgba(201,150,10,.28);
  border-radius:22px; padding:32px 28px;
  width:92%; max-width:620px;
  max-height:88vh; overflow-y:auto;
  position:relative;
}
.admin-box h2 { font-family:'Playfair Display',serif; color:var(--gold-light); font-size:1.4rem; text-align:center; margin-bottom:22px; }
.admin-close { position:absolute; top:14px; right:18px; background:none; border:none; color:rgba(255,255,255,.35); font-size:1.4rem; cursor:pointer; transition:color .2s; }
.admin-close:hover { color:white; }
.pw-input {
  width:100%; background:rgba(255,255,255,.06); border:1.5px solid var(--border);
  border-radius:12px; padding:13px 16px;
  font-family:'Poppins',sans-serif; font-size:.95rem; color:var(--cream); outline:none; margin-bottom:12px;
}
.pw-input:focus { border-color:var(--gold-light); box-shadow:0 0 0 3px rgba(240,192,64,.12); }
.btn-unlock {
  width:100%; background:linear-gradient(135deg,var(--crimson),#6E1010);
  color:white; border:none; border-radius:12px; padding:13px;
  font-family:'Poppins',sans-serif; font-size:.88rem; font-weight:600; letter-spacing:1.5px;
  cursor:pointer; transition:all .2s;
}
.btn-unlock:hover { opacity:.9; transform:translateY(-1px); }
.pw-err { color:#FF6B6B; font-size:.75rem; margin-top:7px; display:none; }
#admin-results { display:none; }
.res-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:18px; flex-wrap:wrap; gap:8px; }
.res-header h3 { font-family:'Playfair Display',serif; color:var(--gold-light); font-size:1.05rem; }
.btn-sm {
  border-radius:8px; padding:5px 13px; font-size:.7rem; letter-spacing:1px;
  cursor:pointer; text-transform:uppercase; transition:all .2s;
}
.btn-export { background:rgba(201,150,10,.18); border:1px solid var(--gold); color:var(--gold); }
.btn-export:hover { background:var(--gold); color:var(--bg); }
.btn-clear  { background:rgba(220,60,60,.12); border:1px solid rgba(220,60,60,.4); color:rgba(220,120,120,.9); margin-left:4px; }
.btn-clear:hover { background:rgba(220,60,60,.22); }
.res-bar-wrap { margin-bottom:13px; }
.res-bar-label { display:flex; justify-content:space-between; font-size:.78rem; margin-bottom:5px; color:var(--cream); }
.res-bar-label span:last-child { color:var(--gold); font-weight:600; }
.res-bar-bg { background:rgba(255,255,255,.07); border-radius:6px; height:9px; overflow:hidden; }
.res-bar-fill { height:100%; background:linear-gradient(90deg,var(--crimson),var(--gold)); border-radius:6px; transition:width .9s ease; }
.res-total { text-align:center; font-size:.8rem; color:var(--muted); margin-top:18px; padding-top:16px; border-top:1px solid rgba(255,255,255,.07); }
.voter-section h4 { font-size:.68rem; letter-spacing:2px; text-transform:uppercase; color:var(--gold); margin:18px 0 10px; }
.voter-row { display:flex; justify-content:space-between; align-items:center; padding:8px 10px; border-bottom:1px solid rgba(255,255,255,.05); font-size:.78rem; gap:8px; }
.voter-row:hover { background:rgba(255,255,255,.03); }
.vr-name { color:var(--cream); flex-shrink:0; max-width:30%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.vr-choice { color:var(--muted); font-size:.72rem; flex:1; text-align:center; }
.vr-time { color:rgba(255,255,255,.28); font-size:.68rem; flex-shrink:0; }

/* =========================================================
   ALREADY VOTED overlay
========================================================= */
.already-screen {
  text-align:center; padding:32px 24px 80px;
  max-width:460px; position:relative; z-index:2;
}
.already-screen h2 { font-family:'Playfair Display',serif; color:var(--gold-light); font-size:1.8rem; margin:14px 0 10px; }
.already-screen p { color:var(--muted); line-height:1.65; }

/* =========================================================
   MOBILE SAFE AREA
========================================================= */
@supports(padding: max(0px)) {
  .poll-inner, .name-card, .brand-wrap, .ty-inner {
    padding-bottom: max(80px, env(safe-area-inset-bottom) + 56px);
  }
}
</style>
</head>
<body>

<!-- PROGRESS BAR -->
<div id="progress-bar"><div id="progress-fill" style="width:0%"></div></div>

<!-- STEP DOTS -->
<div id="step-dots">
  <div class="step-dot" id="dot-0"></div>
  <div class="step-dot" id="dot-1"></div>
  <div class="step-dot" id="dot-2"></div>
  <div class="step-dot" id="dot-3"></div>
</div>

<!-- ════════════════════════════════
  DECK
════════════════════════════════ -->
<div id="deck">

  <!-- ── SLIDE 0: LOADER ── -->
  <div class="slide active" id="s-loader">
    <div class="loader-particles" id="lparts"></div>
    <div class="loader-logo"><img src="data:image/png;base64,''' + logo + '''" alt="Karuda Dates"></div>
    <div class="loader-tag">Since 1990 · Premium Quality</div>
    <div class="bar-wrap"><div class="bar-fill"></div></div>
  </div>

  <!-- ── SLIDE 1: BRAND HERO ── -->
  <div class="slide" id="s-brand">
    <div class="fd-wrap" id="fdWrap"></div>
    <!-- bg blobs -->
    <div style="position:absolute;width:500px;height:350px;top:5%;left:-120px;border-radius:50%;background:radial-gradient(ellipse,rgba(100,25,8,.22) 0%,transparent 70%);pointer-events:none;"></div>
    <div style="position:absolute;width:400px;height:300px;bottom:5%;right:-100px;border-radius:50%;background:radial-gradient(ellipse,rgba(80,40,5,.18) 0%,transparent 70%);pointer-events:none;"></div>

    <div class="brand-wrap">
      <!-- top ornament -->
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px;">
        <div style="flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(201,150,10,.35),transparent);"></div>
        <span style="font-size:.62rem;letter-spacing:4px;color:rgba(201,150,10,.55);text-transform:uppercase;white-space:nowrap;">Karuda Food Products</span>
        <div style="flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(201,150,10,.35),transparent);"></div>
      </div>

      <div class="brand-logo"><img src="data:image/png;base64,''' + logo + '''" alt="Karuda Dates Logo"></div>

      <div class="brand-title">
        <div class="slide-title gold-shimmer">Pure. Premium. Powerful.</div>
        <div class="brand-sub">Trusted Since 1990</div>
      </div>

      <div class="gold-line"></div>

      <!-- Product cards -->
      <div class="eyebrow" style="margin-top:4px;">Our Premium Range</div>
      <div class="product-grid">
        <div class="prod-card active-prod" onclick="activeProd(this,0)">
          <img src="data:image/jpeg;base64,''' + black_dates + '''" alt="Black Dates">
          <div class="prod-card-label">Black<br>Dates</div>
        </div>
        <div class="prod-card" onclick="activeProd(this,1)">
          <img src="data:image/jpeg;base64,''' + deseeded + '''" alt="Deseeded">
          <div class="prod-card-label">Deseeded<br>Dates</div>
        </div>
        <div class="prod-card" onclick="activeProd(this,2)">
          <img src="data:image/jpeg;base64,''' + dates_pkt + '''" alt="Natural Dates">
          <div class="prod-card-label">Natural<br>Dates</div>
        </div>
      </div>

      <button class="brand-cta" onclick="gotoSlide(2)">Share Your Voice →</button>
    </div>
  </div>

  <!-- ── SLIDE 2: NAME ── -->
  <div class="slide" id="s-name">
    <div class="name-card">
      <div class="lang-row">
        <button class="lang-btn on" onclick="setLang(\'en\')">English</button>
        <button class="lang-btn" onclick="setLang(\'ta\')">தமிழ்</button>
      </div>

      <div class="eyebrow en-only">Consumer Voice Poll</div>
      <div class="eyebrow ta-only ta-hidden">வாடிக்கையாளர் கருத்து வாக்கெடுப்பு</div>

      <h2 class="slide-title en-only">What\\\'s Your Name?</h2>
      <h2 class="slide-title ta-only ta-hidden">உங்கள் பெயர் என்ன?</h2>

      <div class="gold-line" style="margin:12px auto 18px;"></div>

      <p class="section-sub en-only">
        We\\\'d love to know who\\\'s sharing their voice with us.<br>
        <strong style="color:var(--gold-pale);">Your name is required to proceed.</strong>
      </p>
      <p class="section-sub ta-only ta-hidden">
        உங்கள் குரலை எங்களுடன் பகிர்வதற்கு நன்றி.<br>
        <strong style="color:var(--gold-pale);">தொடர உங்கள் பெயர் அவசியம்.</strong>
      </p>

      <div class="input-wrap">
        <span class="input-icon">👤</span>
        <input class="name-input" id="vName" type="text"
          placeholder="Enter your full name…" autocomplete="off"
          onkeydown="if(event.key===\'Enter\')goToPoll()">
      </div>
      <div class="err-msg" id="nameErr">⚠ Please enter your name to continue.</div>

      <button class="btn-next en-only" onclick="goToPoll()">Continue to Poll →</button>
      <button class="btn-next ta-only ta-hidden" onclick="goToPoll()">தொடர →</button>
    </div>
  </div>

  <!-- ── SLIDE 3: POLL ── -->
  <div class="slide" id="s-poll">
    <div class="poll-inner">
      <div class="poll-q-header">
        <div class="lang-row" style="margin-bottom:16px;">
          <button class="lang-btn on" onclick="setLang(\'en\')">English</button>
          <button class="lang-btn" onclick="setLang(\'ta\')">தமிழ்</button>
        </div>
        <div class="voter-greeting" id="voterGreeting"></div>
        <div class="eyebrow en-only" style="margin-top:6px;">Select Your Favourite</div>
        <div class="eyebrow ta-only ta-hidden" style="margin-top:6px;">உங்களுக்கு பிடித்ததை தேர்வு செய்யுங்கள்</div>
        <p class="section-sub en-only" style="margin-top:4px;margin-bottom:0;">
          The reasons why people should buy Karuda Dates are given below.<br>
          <strong style="color:var(--gold-pale);">Kindly select the one that you like the most.</strong>
        </p>
        <p class="section-sub ta-only ta-hidden" style="margin-top:4px;margin-bottom:0;">
          கருடா பேரிச்சம்பழத்தை மக்கள் ஏன் வாங்க வேண்டும் என்ற விளக்கங்கள் கீழே உள்ளது<br>
          <strong style="color:var(--gold-pale);">அதில் தங்களுக்கு பிடித்தது தயவு செய்து செலக்ட் செய்யுங்கள்</strong>
        </p>
      </div>

      <div class="gold-line" style="margin:14px auto 18px;"></div>

      <div class="choices" id="choiceList">
        <label class="choice" onclick="pick(this)">
          <input type="radio" name="poll" value="Karuda Dates - Never Slow Down">
          <div class="radio-ring"></div>
          <div class="choice-text">Karuda Dates — <strong>Never Slow Down</strong></div>
          <div class="choice-num">01</div>
        </label>
        <label class="choice" onclick="pick(this)">
          <input type="radio" name="poll" value="Karuda Dates - Strength Reloaded">
          <div class="radio-ring"></div>
          <div class="choice-text">Karuda Dates — <strong>Strength Reloaded</strong></div>
          <div class="choice-num">02</div>
        </label>
        <label class="choice" onclick="pick(this)">
          <input type="radio" name="poll" value="Karuda Dates - Stay Unstoppable">
          <div class="radio-ring"></div>
          <div class="choice-text">Karuda Dates — <strong>Stay Unstoppable</strong></div>
          <div class="choice-num">03</div>
        </label>
        <label class="choice" onclick="pick(this)">
          <input type="radio" name="poll" value="Karuda Dates - Instant Energy">
          <div class="radio-ring"></div>
          <div class="choice-text">Karuda Dates — <strong>Instant Energy</strong></div>
          <div class="choice-num">04</div>
        </label>
        <label class="choice" onclick="pick(this)">
          <input type="radio" name="poll" value="Karuda Dates - Instant Charging">
          <div class="radio-ring"></div>
          <div class="choice-text">Karuda Dates — <strong>Instant Charging</strong></div>
          <div class="choice-num">05</div>
        </label>
        <label class="choice" onclick="pick(this)">
          <input type="radio" name="poll" value="Karuda Dates - Fly Higher with Instant Charging">
          <div class="radio-ring"></div>
          <div class="choice-text">Karuda Dates — <strong>Fly Higher with Instant Charging</strong></div>
          <div class="choice-num">06</div>
        </label>
      </div>

      <div class="submit-row">
        <div class="choice-err" id="choiceErr">⚠ Please choose one option before submitting.</div>
        <button class="btn-submit en-only" id="submitBtn" onclick="doSubmit()">Submit My Vote</button>
        <button class="btn-submit ta-only ta-hidden" id="submitBtnTa" onclick="doSubmit()">வாக்களிக்கவும்</button>
      </div>
    </div>
  </div>

  <!-- ── SLIDE 4: THANK YOU ── -->
  <div class="slide" id="s-ty">
    <div class="ty-stars" id="tyStars"></div>
    <div class="ty-inner">
      <div class="ty-mascot"><img src="data:image/jpeg;base64,''' + mascot + '''" alt="Karuda Mascot"></div>
      <div class="ty-logo"><img src="data:image/png;base64,''' + logo + '''" alt="Karuda Logo"></div>
      <div class="ty-title">Thank You! 🙏</div>
      <div class="ty-name" id="tyName"></div>
      <p class="ty-msg">Your voice matters to us. Thank you for being part of the Karuda family and helping us grow stronger since 1990.</p>
      <p class="ty-msg-ta">நீங்கள் தேர்ந்தெடுத்தது எங்களுக்கு மிகவும் மகிழ்ச்சி. கருடா குடும்பத்தின் ஒரு அங்கமாக இருந்தமைக்கு நன்றி!</p>
      <div class="ty-choice-box">
        <p>Your Chosen Tagline</p>
        <strong id="tyChoice"></strong>
      </div>
      <div class="ty-tag">Karuda Dates · Since 1990 · Premium Quality · Pure Power</div>
    </div>
  </div>

</div><!-- /deck -->

<!-- ADMIN BUTTON -->
<button id="admin-btn" onclick="openAdmin()">Admin</button>

<!-- ADMIN MODAL -->
<div id="admin-modal">
  <div class="admin-box">
    <button class="admin-close" onclick="closeAdmin()">×</button>
    <h2>🔐 Admin Dashboard</h2>
    <div id="admin-pw">
      <input class="pw-input" type="password" id="pwInput" placeholder="Enter admin password…" onkeydown="if(event.key===\'Enter\')checkPw()">
      <button class="btn-unlock" onclick="checkPw()">Unlock Results</button>
      <div class="pw-err" id="pwErr">⚠ Incorrect password. Try again.</div>
    </div>
    <div id="admin-results">
      <div class="res-header">
        <h3>📊 Poll Results</h3>
        <div>
          <button class="btn-sm btn-export" onclick="exportCSV()">Export CSV</button>
          <button class="btn-sm btn-clear" onclick="clearData()">Clear All</button>
        </div>
      </div>
      <div id="resChart"></div>
      <div class="res-total" id="resTotal"></div>
      <div class="voter-section">
        <h4>Individual Responses</h4>
        <div id="voterList"></div>
      </div>
    </div>
  </div>
</div>

<script>
/* =========================================================
   CONFIG
========================================================= */
const ADMIN_PW   = 'KARUDA2024';
const GAS_URL    = '''' + GAS_URL + '''';
const STORE_KEY  = 'karuda_votes_v2';
const DEV_KEY    = 'karuda_dev_id';
const VOTED_KEY  = 'karuda_voted_';

const CHOICES = [
  'Karuda Dates - Never Slow Down',
  'Karuda Dates - Strength Reloaded',
  'Karuda Dates - Stay Unstoppable',
  'Karuda Dates - Instant Energy',
  'Karuda Dates - Instant Charging',
  'Karuda Dates - Fly Higher with Instant Charging'
];

/* =========================================================
   SLIDE ENGINE
========================================================= */
// Slides: 0=loader, 1=brand, 2=name, 3=poll, 4=ty
// Poll step dots correspond to slides 1–4 → dots 0–3
const SLIDE_IDS = ['s-loader','s-brand','s-name','s-poll','s-ty'];
let currentSlide = 0;

function gotoSlide(n){
  const prev = document.getElementById(SLIDE_IDS[currentSlide]);
  const next = document.getElementById(SLIDE_IDS[n]);
  if(!next || n === currentSlide) return;
  prev.classList.add('exit-up');
  prev.classList.remove('active');
  next.classList.add('active');
  setTimeout(()=> prev.classList.remove('exit-up'), 600);
  currentSlide = n;
  updateProgress(n);
}

function updateProgress(n){
  // progress covers slides 1-4
  const pct = n < 1 ? 0 : Math.round(((n-1)/3)*100);
  document.getElementById('progress-fill').style.width = pct + '%';
  // dots for slides 1-4
  for(let i=0;i<4;i++){
    const d = document.getElementById('dot-'+i);
    if(!d) continue;
    d.classList.toggle('lit', i < n);
  }
}

/* =========================================================
   STORAGE — localStorage (always works) + GAS (best effort)
========================================================= */
function devId(){
  let id = localStorage.getItem(DEV_KEY);
  if(!id){ id = Math.random().toString(36).slice(2)+Date.now().toString(36); localStorage.setItem(DEV_KEY,id); }
  return id;
}
function hasVoted(){ return !!localStorage.getItem(VOTED_KEY+devId()); }
function markVoted(){ localStorage.setItem(VOTED_KEY+devId(),'1'); }

function getVotes(){
  try{ return JSON.parse(localStorage.getItem(STORE_KEY)||'[]'); }
  catch{ return []; }
}
function saveVoteLocal(name, choice){
  const v = getVotes();
  v.push({name, choice, time: new Date().toLocaleString('en-IN')});
  localStorage.setItem(STORE_KEY, JSON.stringify(v));
}
function clearVotes(){ localStorage.removeItem(STORE_KEY); }

// Try to send to Google Sheet (fire-and-forget — never blocks UI)
async function sendToSheet(name, choice){
  try{
    await fetch(GAS_URL, {
      method:'POST',
      mode:'no-cors',          // avoids CORS error on Render
      headers:{'Content-Type':'text/plain'},
      body: JSON.stringify({name, choice, deviceId: devId()})
    });
  } catch(e){
    console.warn('GAS send failed (non-blocking):', e.message);
  }
}

/* =========================================================
   LOADER → BRAND
========================================================= */
(function(){
  const wrap = document.getElementById('lparts');
  for(let i=0;i<26;i++){
    const d = document.createElement('div'); d.className='lp';
    const w=8+Math.random()*20, h=w*1.7;
    d.style.cssText=`width:${w}px;height:${h}px;left:${Math.random()*100}%;`+
      `animation-duration:${7+Math.random()*11}s;animation-delay:${Math.random()*7}s;`;
    wrap.appendChild(d);
  }
})();

window.addEventListener('load', function(){
  setTimeout(function(){
    if(hasVoted()){
      // skip poll, show already-voted on brand slide
      gotoSlide(1);
      setTimeout(showAlreadyVoted, 400);
    } else {
      gotoSlide(1);
    }
    spawnFloatDates();
  }, 2800);
});

function showAlreadyVoted(){
  document.getElementById('s-name').innerHTML =
    `<div class="already-screen">
      <div style="font-size:3rem;margin-bottom:14px">🙏</div>
      <h2>Already Voted!</h2>
      <p>Thank you for participating in the Karuda poll! Your response has been recorded.</p>
      <p style="color:rgba(201,150,10,.45);font-size:.85rem;margin-top:8px">நீங்கள் ஏற்கனவே வாக்களித்துள்ளீர்கள். நன்றி!</p>
    </div>`;
}

function spawnFloatDates(){
  const w = document.getElementById('fdWrap');
  if(!w) return;
  for(let i=0;i<20;i++){
    const d=document.createElement('div'); d.className='fd';
    const sz=10+Math.random()*18;
    d.style.cssText=`width:${sz}px;height:${sz*1.72}px;left:${Math.random()*100}%;`+
      `animation-duration:${8+Math.random()*13}s;animation-delay:${Math.random()*9}s;`;
    w.appendChild(d);
  }
}

/* =========================================================
   PRODUCT CARD HIGHLIGHT
========================================================= */
function activeProd(el){ 
  document.querySelectorAll('.prod-card').forEach(c=>c.classList.remove('active-prod'));
  el.classList.add('active-prod');
}

/* =========================================================
   LANGUAGE
========================================================= */
function setLang(l){
  const isTa = l==='ta';
  document.querySelectorAll('.lang-btn').forEach((b,i)=>b.classList.toggle('on',(i===0&&!isTa)||(i===1&&isTa)));
  document.querySelectorAll('.en-only').forEach(el=>el.style.display=isTa?'none':'');
  document.querySelectorAll('.ta-only').forEach(el=>{
    el.style.display = isTa ? (el.tagName==='BUTTON'?'block':'block') : 'none';
    el.classList.toggle('ta-hidden',!isTa);
  });
}

/* =========================================================
   NAME → POLL
========================================================= */
function goToPoll(){
  const name = document.getElementById('vName').value.trim();
  if(!name){
    document.getElementById('nameErr').style.display='block';
    document.getElementById('vName').focus();
    return;
  }
  document.getElementById('nameErr').style.display='none';
  // personalise greeting
  document.getElementById('voterGreeting').textContent = 'Hello, '+name+' 👋';
  gotoSlide(3);
}

/* =========================================================
   POLL
========================================================= */
function pick(lbl){
  document.querySelectorAll('.choice').forEach(c=>c.classList.remove('picked'));
  lbl.classList.add('picked');
  lbl.querySelector('input').checked=true;
  document.getElementById('choiceErr').style.display='none';
}

async function doSubmit(){
  const name = document.getElementById('vName').value.trim();
  const sel  = document.querySelector('input[name=poll]:checked');

  if(!sel){ document.getElementById('choiceErr').style.display='block'; return; }
  document.getElementById('choiceErr').style.display='none';

  // Lock button & show spinner
  const btn = document.getElementById('submitBtn');
  const btnTa = document.getElementById('submitBtnTa');
  const origText = btn.innerHTML;
  btn.disabled = btnTa.disabled = true;
  btn.innerHTML = '<span class="spinner"></span>Submitting…';
  btnTa.innerHTML = '<span class="spinner"></span>சமர்ப்பிக்கிறது…';

  // 1. Save locally FIRST (never fails)
  saveVoteLocal(name, sel.value);
  markVoted();

  // 2. Try Google Sheet in background (non-blocking, no-cors)
  sendToSheet(name, sel.value);

  // Small artificial delay so spinner feels responsive
  await new Promise(r=>setTimeout(r,600));

  // Show thank you
  document.getElementById('tyName').textContent  = 'Dear '+name+' 🌟';
  document.getElementById('tyChoice').textContent = '✦ '+sel.value+' ✦';
  gotoSlide(4);
  spawnStars();
  launchConfetti();
}

/* =========================================================
   THANK YOU ANIMATIONS
========================================================= */
function spawnStars(){
  const c=document.getElementById('tyStars'); c.innerHTML='';
  for(let i=0;i<45;i++){
    const s=document.createElement('div'); s.className='ty-star';
    const sz=2+Math.random()*4;
    s.style.cssText=`left:${Math.random()*100}%;top:${Math.random()*100}%;`+
      `width:${sz}px;height:${sz}px;`+
      `animation-duration:${1.5+Math.random()*3}s;animation-delay:${Math.random()*2}s;`;
    c.appendChild(s);
  }
}
function launchConfetti(){
  const cols=['#C9960A','#F0C040','#9B1C1C','#fff','#FF6B35','#FFD700','#C0392B'];
  for(let i=0;i<70;i++){
    setTimeout(function(){
      const c=document.createElement('div'); c.className='confetti';
      c.style.cssText=`left:${Math.random()*100}vw;top:-12px;`+
        `background:${cols[Math.floor(Math.random()*cols.length)]};`+
        `width:${6+Math.random()*8}px;height:${6+Math.random()*8}px;`+
        `animation-duration:${1.5+Math.random()*2.2}s;`+
        `border-radius:${Math.random()>.5?'50%':'2px'};`;
      document.body.appendChild(c);
      setTimeout(()=>c.remove(),3600);
    },i*45);
  }
}

/* =========================================================
   ADMIN
========================================================= */
function openAdmin(){
  document.getElementById('admin-modal').classList.add('open');
  document.getElementById('pwInput').value='';
  document.getElementById('pwErr').style.display='none';
  document.getElementById('admin-pw').style.display='block';
  document.getElementById('admin-results').style.display='none';
  setTimeout(()=>document.getElementById('pwInput').focus(),120);
}
function closeAdmin(){ document.getElementById('admin-modal').classList.remove('open'); }
document.getElementById('admin-modal').addEventListener('click',e=>{ if(e.target===e.currentTarget)closeAdmin(); });

function checkPw(){
  if(document.getElementById('pwInput').value===ADMIN_PW){
    document.getElementById('admin-pw').style.display='none';
    document.getElementById('admin-results').style.display='block';
    renderAdmin();
  } else {
    document.getElementById('pwErr').style.display='block';
    document.getElementById('pwInput').value='';
    document.getElementById('pwInput').focus();
  }
}

function renderAdmin(){
  const votes=getVotes(); const total=votes.length;
  const counts={};
  CHOICES.forEach(c=>counts[c]=0);
  votes.forEach(v=>{ if(counts[v.choice]!==undefined)counts[v.choice]++; else counts[v.choice]=(counts[v.choice]||0)+1; });
  const sorted=CHOICES.slice().sort((a,b)=>counts[b]-counts[a]);
  let html='';
  sorted.forEach(ch=>{
    const pct=total>0?Math.round((counts[ch]/total)*100):0;
    html+=`<div class="res-bar-wrap">
      <div class="res-bar-label"><span>${ch}</span><span>${counts[ch]} votes (${pct}%)</span></div>
      <div class="res-bar-bg"><div class="res-bar-fill" style="width:${pct}%"></div></div>
    </div>`;
  });
  document.getElementById('resChart').innerHTML=html;
  document.getElementById('resTotal').innerHTML=total>0
    ?`<strong style="color:var(--gold-light)">${total}</strong> total votes &nbsp;·&nbsp; 🏆 Winner: <strong style="color:var(--gold-light)">${sorted[0].replace('Karuda Dates - ','')}</strong>`
    :`<span>No votes recorded yet.</span>`;
  let vhtml='';
  if(!votes.length) vhtml='<p style="color:rgba(255,255,255,.28);font-size:.78rem;text-align:center;padding:18px">No votes yet.</p>';
  else [...votes].reverse().forEach(v=>{
    vhtml+=`<div class="voter-row">
      <span class="vr-name">${v.name}</span>
      <span class="vr-choice">${v.choice.replace('Karuda Dates - ','')}</span>
      <span class="vr-time">${v.time}</span>
    </div>`;
  });
  document.getElementById('voterList').innerHTML=vhtml;
}

function exportCSV(){
  const v=getVotes();
  if(!v.length){alert('No votes to export yet.');return;}
  let csv='Name,Choice,Time\\n';
  v.forEach(r=>{ csv+=`"${r.name}","${r.choice}","${r.time}"\\n`; });
  const a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv'}));
  a.download='karuda_poll_results.csv'; a.click();
}
function clearData(){
  if(confirm('Delete ALL vote data? This cannot be undone.')){clearVotes();renderAdmin();}
}
</script>
</body>
</html>'''

with open("karuda_poll_v2.html", "w", encoding="utf-8") as f:
    f.write(html)

size = len(html)
print(f"HTML written! Size: {size:,} chars ({size//1024} KB)")