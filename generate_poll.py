with open("tmp/logo_b64.txt") as f: logo_b64 = f.read().strip()
with open("tmp/black_dates_b64.txt") as f: black_dates_b64 = f.read().strip()
with open("tmp/deseeded_b64.txt") as f: deseeded_b64 = f.read().strip()
with open("tmp/dates_pkt_b64.txt") as f: dates_pkt_b64 = f.read().strip()
with open("tmp/mascot_b64.txt") as f: mascot_b64 = f.read().strip()

logo_ext = "png"
prod_ext = "jpeg"
mascot_ext = "jpeg"

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Karuda Dates – Consumer Poll</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --crimson: #9B1C1C;
  --crimson2: #C0392B;
  --gold: #C9960A;
  --gold-light: #F0C040;
  --gold-pale: #F5DFA0;
  --deep-red: #5E0A0A;
  --bg-dark: #100404;
  --bg-mid: #1E0808;
  --bg-card: rgba(255,255,255,0.045);
  --cream: #FFF8EC;
  --text-light: #FFF8EC;
  --text-muted: #C9966A;
  --border-gold: rgba(201,150,10,0.22);
}}

*,*::before,*::after {{ margin:0;padding:0;box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{
  font-family:'Poppins',sans-serif;
  background:var(--bg-dark);
  color:var(--text-light);
  min-height:100vh;
  overflow-x:hidden;
}}

/* ── LOADING ── */
#loader {{
  position:fixed;inset:0;z-index:9999;
  background:radial-gradient(ellipse at 40% 60%,#280808 0%,#0A0202 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  transition:opacity .9s ease,transform .9s ease;
}}
#loader.out {{ opacity:0;pointer-events:none;transform:scale(1.06); }}

.loader-particles {{ position:absolute;inset:0;overflow:hidden;pointer-events:none; }}
.lp {{
  position:absolute;border-radius:50% 50% 42% 42%;
  background:radial-gradient(ellipse,#7B3A10 0%,#3B1606 60%,transparent 80%);
  opacity:0;animation:lpFloat linear infinite;
}}
@keyframes lpFloat {{
  0%   {{ transform:translateY(110vh) rotate(0deg);opacity:0; }}
  8%   {{ opacity:.22; }}
  92%  {{ opacity:.22; }}
  100% {{ transform:translateY(-10vh) rotate(400deg);opacity:0; }}
}}

.loader-core {{ position:relative;z-index:2;text-align:center; }}
.loader-glow {{
  animation:lglow 2.2s ease-in-out infinite;
}}
@keyframes lglow {{
  0%,100% {{ filter:drop-shadow(0 0 18px rgba(201,150,10,.4)); transform:scale(1); }}
  50%      {{ filter:drop-shadow(0 0 44px rgba(201,150,10,.9)); transform:scale(1.04); }}
}}
.loader-core img {{ width:210px;height:auto; }}
.loader-tagline {{
  margin-top:14px;
  font-family:'Playfair Display',serif;font-style:italic;
  font-size:1rem;color:var(--gold-light);letter-spacing:4px;
  text-transform:uppercase;opacity:0;
  animation:fadeUp .8s .6s forwards;
}}
.loader-bar-wrap {{
  margin-top:32px;width:200px;height:3px;
  background:rgba(255,255,255,.08);border-radius:4px;overflow:hidden;
  position:relative;z-index:2;
}}
.loader-bar {{
  height:100%;width:0%;
  background:linear-gradient(90deg,var(--crimson),var(--gold-light));
  border-radius:4px;
  animation:lbar 2.6s cubic-bezier(.4,0,.2,1) forwards;
}}
@keyframes lbar {{ to {{ width:100%; }} }}

/* ── PAGE WRAPPER ── */
#page {{ opacity:0;transition:opacity .8s ease; }}
#page.on {{ opacity:1; }}

/* ── SHARED ANIMATIONS ── */
@keyframes fadeUp {{ from {{ transform:translateY(20px);opacity:0; }} to {{ transform:translateY(0);opacity:1; }} }}
@keyframes shimmer {{
  0%   {{ background-position:200% center; }}
  100% {{ background-position:-200% center; }}
}}

/* ── BRAND HERO ── */
#hero {{
  min-height:100vh;
  background:
    radial-gradient(ellipse 70% 50% at 15% 55%, rgba(155,28,28,.38) 0%,transparent 60%),
    radial-gradient(ellipse 60% 40% at 85% 45%, rgba(140,80,0,.22) 0%,transparent 60%),
    linear-gradient(160deg,#100404 0%,#1A0707 45%,#0D0303 100%);
  display:flex;flex-direction:column;align-items:center;
  padding:48px 20px 64px;
  position:relative;overflow:hidden;
}}

/* date-texture circles */
.hero-blob {{
  position:absolute;border-radius:50%;
  background:radial-gradient(ellipse,rgba(100,30,10,.25) 0%,transparent 70%);
  pointer-events:none;
}}

/* Floating date icons (SVG-drawn) */
.float-dates-wrap {{
  position:absolute;inset:0;pointer-events:none;overflow:hidden;
}}
.fd {{
  position:absolute;width:18px;height:28px;
  background:radial-gradient(ellipse at 40% 30%,#7B3A10,#2E1005);
  border-radius:50% 50% 44% 44%;
  opacity:0;
  animation:fdFloat linear infinite;
  box-shadow:inset 0 -2px 4px rgba(0,0,0,.4);
}}
@keyframes fdFloat {{
  0%   {{ transform:translateY(105vh) rotate(0deg);opacity:0; }}
  10%  {{ opacity:.18; }}
  90%  {{ opacity:.18; }}
  100% {{ transform:translateY(-8vh) rotate(360deg);opacity:0; }}
}}

/* palm leaf top decoration */
.hero-palm-bar {{
  width:100%;max-width:700px;
  display:flex;justify-content:center;align-items:center;gap:10px;
  margin-bottom:20px;position:relative;z-index:2;
  animation:fadeUp .7s .1s both;
}}
.palm-line {{ flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(201,150,10,.4),transparent); }}
.palm-label {{
  font-size:.68rem;letter-spacing:4px;color:rgba(201,150,10,.6);
  text-transform:uppercase;white-space:nowrap;
}}

.hero-logo {{
  position:relative;z-index:2;text-align:center;
  animation:fadeUp .7s .2s both;
}}
.hero-logo img {{
  width:clamp(160px,28vw,240px);height:auto;
  filter:drop-shadow(0 6px 32px rgba(201,150,10,.55));
}}

.hero-headline {{
  font-family:'Playfair Display',serif;
  font-size:clamp(1.7rem,5vw,3.2rem);
  font-weight:900;
  background:linear-gradient(135deg,#F5DFA0 0%,#F0C040 40%,#C9960A 70%,#F0C040 100%);
  background-size:200% auto;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:shimmer 4s linear infinite, fadeUp .7s .35s both;
  text-align:center;margin-top:12px;letter-spacing:2px;
}}
.hero-sub {{
  font-size:.78rem;color:var(--text-muted);letter-spacing:3px;
  text-transform:uppercase;margin-top:5px;
  animation:fadeUp .7s .45s both;
}}

.divider-gold {{
  width:110px;height:2px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  margin:20px auto;
}}

/* ── CAROUSEL ── */
.carousel-wrap {{
  width:100%;max-width:860px;
  position:relative;z-index:2;
  animation:fadeUp .7s .55s both;
}}
.carousel-eyebrow {{
  text-align:center;font-size:.68rem;letter-spacing:3px;
  color:var(--text-muted);text-transform:uppercase;margin-bottom:12px;
}}

.carousel-frame {{
  overflow:hidden;border-radius:18px;
  box-shadow:0 24px 64px rgba(0,0,0,.65),0 0 0 1px rgba(201,150,10,.18);
  position:relative;
}}
.carousel-track {{
  display:flex;
  transition:transform .72s cubic-bezier(.4,0,.2,1);
}}
.c-slide {{
  min-width:100%;position:relative;background:#160606;
}}
.c-slide img {{
  width:100%;max-height:400px;object-fit:contain;display:block;
  background:linear-gradient(135deg,#1a0808,#2c1010);
}}
.c-caption {{
  position:absolute;bottom:0;left:0;right:0;
  background:linear-gradient(transparent,rgba(0,0,0,.82));
  padding:32px 24px 16px;text-align:center;
}}
.c-caption strong {{
  font-family:'Playfair Display',serif;font-size:1.1rem;color:var(--gold-light);
}}
.c-caption small {{
  display:block;font-size:.68rem;color:rgba(255,248,236,.55);
  letter-spacing:2px;text-transform:uppercase;margin-top:2px;
}}
.c-dots {{
  display:flex;justify-content:center;gap:8px;margin-top:14px;
}}
.c-dot {{
  width:8px;height:8px;border-radius:50%;
  background:rgba(201,150,10,.25);cursor:pointer;
  transition:all .3s;border:none;outline:none;
}}
.c-dot.on {{
  background:var(--gold-light);transform:scale(1.4);
  box-shadow:0 0 8px rgba(240,192,64,.5);
}}

/* ── SCROLL HINT ── */
.scroll-hint {{
  position:relative;z-index:2;
  margin-top:28px;
  display:flex;flex-direction:column;align-items:center;gap:6px;
  animation:fadeUp .7s 1.1s both;
}}
.scroll-hint span {{
  font-size:.68rem;letter-spacing:3px;
  color:rgba(201,150,10,.45);text-transform:uppercase;
}}
.scroll-arrow {{
  width:20px;height:20px;
  border-right:2px solid rgba(201,150,10,.4);
  border-bottom:2px solid rgba(201,150,10,.4);
  transform:rotate(45deg);
  animation:arrowBob 1.4s ease-in-out infinite;
}}
@keyframes arrowBob {{
  0%,100% {{ transform:rotate(45deg) translateY(0); }}
  50%      {{ transform:rotate(45deg) translateY(5px); }}
}}

/* ── POLL SECTION ── */
#poll {{
  min-height:100vh;
  background:
    radial-gradient(ellipse 60% 40% at 50% 0%,rgba(155,28,28,.2) 0%,transparent 60%),
    linear-gradient(180deg,#0E0404 0%,#080101 100%);
  padding:64px 20px 80px;
  position:relative;overflow:hidden;
}}
#poll::before {{
  content:'';position:absolute;inset:0;pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cellipse cx='30' cy='30' rx='4' ry='6' fill='rgba(100,40,10,0.06)'/%3E%3C/svg%3E") repeat;
}}

.poll-inner {{
  max-width:660px;margin:0 auto;position:relative;z-index:2;
}}

.eyebrow {{
  text-align:center;font-size:.68rem;letter-spacing:4px;
  color:var(--gold);text-transform:uppercase;margin-bottom:8px;
}}
.section-title {{
  font-family:'Playfair Display',serif;
  font-size:clamp(1.5rem,4vw,2.2rem);font-weight:700;
  text-align:center;line-height:1.3;margin-bottom:6px;
  color:var(--text-light);
}}
.section-sub {{
  font-size:clamp(.82rem,2.3vw,.95rem);color:var(--text-muted);
  text-align:center;line-height:1.65;margin-bottom:30px;
  font-weight:300;
}}

/* lang toggle */
.lang-row {{
  display:flex;justify-content:center;gap:10px;margin-bottom:28px;
}}
.lang-btn {{
  background:rgba(255,255,255,.05);
  border:1px solid var(--border-gold);
  border-radius:50px;padding:6px 20px;
  font-family:'Poppins',sans-serif;font-size:.73rem;
  letter-spacing:1px;color:var(--text-muted);cursor:pointer;
  transition:all .25s;
}}
.lang-btn.on {{
  background:var(--gold);color:var(--bg-dark);
  border-color:var(--gold);font-weight:700;
  box-shadow:0 4px 18px rgba(201,150,10,.3);
}}

.ta-hidden {{ display:none; }}
.body-ta .en-only {{ display:none; }}
.body-ta .ta-only {{ display:block !important; }}

/* name card */
.name-card {{
  background:var(--bg-card);
  border:1px solid var(--border-gold);
  border-radius:16px;padding:26px 26px 22px;
  margin-bottom:24px;
  backdrop-filter:blur(12px);
}}
.field-label {{
  display:block;font-size:.7rem;letter-spacing:2px;
  color:var(--gold);text-transform:uppercase;margin-bottom:10px;
}}
.field-input {{
  width:100%;
  background:rgba(255,255,255,.055);
  border:1.5px solid rgba(201,150,10,.28);
  border-radius:10px;padding:13px 17px;
  font-family:'Poppins',sans-serif;font-size:.95rem;
  color:var(--text-light);outline:none;
  transition:border-color .3s,box-shadow .3s;
}}
.field-input:focus {{
  border-color:var(--gold-light);
  box-shadow:0 0 0 3px rgba(240,192,64,.12);
}}
.field-input::placeholder {{ color:rgba(255,248,236,.28); }}
.field-error {{
  color:#FF6B6B;font-size:.73rem;margin-top:8px;display:none;
}}

/* choices */
.choices {{ display:flex;flex-direction:column;gap:11px; }}
.choice {{
  display:flex;align-items:center;gap:14px;
  background:var(--bg-card);
  border:1.5px solid var(--border-gold);
  border-radius:13px;padding:16px 18px;
  cursor:pointer;
  transition:all .22s ease;
  position:relative;overflow:hidden;
}}
.choice::after {{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(201,150,10,.06),transparent);
  opacity:0;transition:opacity .22s;pointer-events:none;
}}
.choice:hover {{ border-color:rgba(201,150,10,.55);transform:translateX(5px); }}
.choice:hover::after {{ opacity:1; }}
.choice.picked {{
  background:linear-gradient(135deg,rgba(155,28,28,.28),rgba(201,150,10,.12));
  border-color:var(--gold-light);
  box-shadow:0 4px 24px rgba(201,150,10,.18),0 0 0 1px rgba(240,192,64,.15);
  transform:translateX(0);
}}
.choice input[type=radio] {{ display:none; }}
.radio-ring {{
  width:20px;height:20px;flex-shrink:0;
  border:2px solid rgba(201,150,10,.35);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  transition:all .22s;background:transparent;
}}
.choice.picked .radio-ring {{
  border-color:var(--gold-light);background:var(--gold-light);
}}
.radio-ring::after {{
  content:'';width:7px;height:7px;
  background:var(--bg-dark);border-radius:50%;
  opacity:0;transition:opacity .2s;
}}
.choice.picked .radio-ring::after {{ opacity:1; }}
.choice-text {{
  flex:1;font-size:clamp(.85rem,2.4vw,.97rem);
  font-weight:500;color:var(--text-light);line-height:1.4;
}}
.choice-num {{
  font-family:'Playfair Display',serif;font-size:1.3rem;
  font-weight:700;color:rgba(201,150,10,.25);
  transition:color .22s;min-width:26px;text-align:right;
}}
.choice.picked .choice-num {{ color:var(--gold); }}

/* submit */
.submit-row {{ margin-top:30px;text-align:center; }}
.choice-err {{
  color:#FF6B6B;font-size:.73rem;margin-bottom:12px;display:none;
}}
.btn-submit {{
  display:inline-block;cursor:pointer;
  background:linear-gradient(135deg,#A01E1E,#6E0E0E);
  color:var(--text-light);border:none;border-radius:50px;
  padding:15px 56px;
  font-family:'Poppins',sans-serif;font-size:.95rem;
  font-weight:700;letter-spacing:2.5px;text-transform:uppercase;
  position:relative;overflow:hidden;
  transition:all .28s;
  box-shadow:0 8px 28px rgba(155,28,28,.42);
}}
.btn-submit::before {{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(240,192,64,.28),transparent);
  opacity:0;transition:opacity .28s;
}}
.btn-submit:hover::before {{ opacity:1; }}
.btn-submit:hover {{ transform:translateY(-2px);box-shadow:0 14px 38px rgba(155,28,28,.52); }}
.btn-submit:active {{ transform:translateY(0); }}

/* ── THANK YOU ── */
#ty {{
  display:none;
  min-height:100vh;
  background:radial-gradient(ellipse 80% 60% at 50% 30%,rgba(155,28,28,.42) 0%,#080101 70%);
  flex-direction:column;align-items:center;justify-content:center;
  padding:60px 20px;text-align:center;
  position:relative;overflow:hidden;
}}
#ty.show {{ display:flex; }}

.ty-stars-layer {{ position:absolute;inset:0;pointer-events:none;overflow:hidden; }}
.ty-star {{
  position:absolute;border-radius:50%;
  background:var(--gold-light);opacity:0;
  animation:starTw ease-in-out infinite;
}}
@keyframes starTw {{
  0%,100% {{ opacity:0;transform:scale(.5); }}
  50%      {{ opacity:.6;transform:scale(1.6); }}
}}

.ty-mascot {{
  position:relative;z-index:2;
  animation:mascotIn .9s .3s both;
}}
@keyframes mascotIn {{
  0%   {{ transform:translateY(50px) scale(.85);opacity:0; }}
  65%  {{ transform:translateY(-12px) scale(1.04);opacity:1; }}
  100% {{ transform:translateY(0) scale(1);opacity:1; }}
}}
.ty-mascot img {{
  width:clamp(110px,20vw,160px);height:auto;
  filter:drop-shadow(0 0 28px rgba(201,150,10,.55));
}}

.ty-logo {{
  position:relative;z-index:2;margin-top:18px;
  animation:fadeUp .8s .7s both;
}}
.ty-logo img {{
  width:clamp(130px,24vw,180px);height:auto;
  filter:drop-shadow(0 2px 18px rgba(201,150,10,.4));
}}

.ty-big {{
  font-family:'Playfair Display',serif;
  font-size:clamp(2rem,6vw,3.6rem);
  font-weight:900;color:var(--gold-light);
  margin-top:20px;position:relative;z-index:2;
  animation:fadeUp .8s .9s both;
  text-shadow:0 4px 28px rgba(201,150,10,.4);
}}
.ty-name {{
  font-family:'Playfair Display',serif;
  font-size:clamp(1.2rem,3.5vw,1.8rem);
  color:var(--text-light);margin-top:6px;
  position:relative;z-index:2;
  animation:fadeUp .8s 1s both;
}}
.ty-msg {{
  font-size:clamp(.85rem,2.3vw,1rem);
  color:var(--text-muted);max-width:460px;
  margin:14px auto 0;line-height:1.7;
  position:relative;z-index:2;
  animation:fadeUp .8s 1.05s both;
}}
.ty-msg-ta {{
  font-size:clamp(.8rem,2.1vw,.9rem);
  color:rgba(201,150,10,.5);max-width:460px;
  margin:6px auto 0;position:relative;z-index:2;
  animation:fadeUp .8s 1.1s both;
}}
.ty-choice-box {{
  margin:22px auto 0;
  background:rgba(255,255,255,.045);
  border:1px solid rgba(201,150,10,.22);
  border-radius:14px;padding:16px 28px;
  max-width:460px;position:relative;z-index:2;
  animation:fadeUp .8s 1.15s both;
}}
.ty-choice-box p {{
  font-size:.68rem;color:var(--gold);
  letter-spacing:2px;text-transform:uppercase;margin-bottom:7px;
}}
.ty-choice-box strong {{
  font-family:'Playfair Display',serif;
  font-size:1.08rem;color:var(--text-light);
}}
.ty-footer {{
  font-size:.68rem;letter-spacing:3px;text-transform:uppercase;
  color:rgba(201,150,10,.38);margin-top:28px;
  position:relative;z-index:2;
  animation:fadeUp .8s 1.25s both;
}}

/* ── CONFETTI ── */
.cf {{
  position:fixed;pointer-events:none;z-index:9998;
  animation:cfFall linear forwards;border-radius:2px;
}}
@keyframes cfFall {{
  0%   {{ transform:translateY(-10px) rotate(0);opacity:1; }}
  100% {{ transform:translateY(100vh) rotate(720deg);opacity:0; }}
}}

/* ── ALREADY VOTED ── */
.already-voted {{
  text-align:center;padding:80px 20px;
}}

/* ── ADMIN BUTTON ── */
#admin-trigger {{
  position:fixed;bottom:18px;right:18px;z-index:200;
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.09);
  border-radius:8px;padding:7px 13px;
  font-size:.65rem;letter-spacing:1px;
  color:rgba(255,255,255,.18);cursor:pointer;
  text-transform:uppercase;transition:all .2s;
  font-family:'Poppins',sans-serif;
}}
#admin-trigger:hover {{ color:rgba(255,255,255,.45);border-color:rgba(255,255,255,.28); }}

/* ── ADMIN MODAL ── */
#admin-modal {{
  display:none;position:fixed;inset:0;z-index:9999;
  background:rgba(0,0,0,.87);backdrop-filter:blur(8px);
  align-items:center;justify-content:center;
}}
#admin-modal.show {{ display:flex; }}
.admin-box {{
  background:linear-gradient(145deg,#1A0808,#2C1010);
  border:1px solid rgba(201,150,10,.3);
  border-radius:20px;padding:36px 30px;
  width:94%;max-width:640px;
  position:relative;max-height:90vh;overflow-y:auto;
}}
.admin-box h2 {{
  font-family:'Playfair Display',serif;
  color:var(--gold-light);font-size:1.4rem;
  margin-bottom:20px;text-align:center;
}}
.admin-close {{
  position:absolute;top:14px;right:18px;
  background:none;border:none;color:rgba(255,255,255,.35);
  font-size:1.5rem;cursor:pointer;transition:color .2s;
  font-family:'Poppins',sans-serif;
}}
.admin-close:hover {{ color:white; }}

#apw input {{
  width:100%;background:rgba(255,255,255,.06);
  border:1px solid rgba(201,150,10,.3);border-radius:10px;
  padding:12px 16px;font-family:'Poppins',sans-serif;
  font-size:.9rem;color:var(--text-light);outline:none;
  margin-bottom:12px;transition:border-color .3s;
}}
#apw input:focus {{ border-color:var(--gold-light); }}
.btn-login {{
  width:100%;background:linear-gradient(135deg,var(--crimson),#7A1515);
  color:white;border:none;border-radius:10px;
  padding:12px;font-family:'Poppins',sans-serif;
  font-size:.9rem;font-weight:600;cursor:pointer;
  letter-spacing:1px;transition:all .2s;
}}
.btn-login:hover {{ opacity:.88;transform:translateY(-1px); }}
.pw-err {{ color:#FF6B6B;font-size:.72rem;margin-top:6px;display:none; }}

#ares {{ display:none; }}
.res-header {{
  display:flex;justify-content:space-between;align-items:center;
  margin-bottom:18px;flex-wrap:wrap;gap:8px;
}}
.res-header h3 {{
  font-family:'Playfair Display',serif;
  color:var(--gold-light);font-size:1.05rem;
}}
.btn-export,.btn-clear {{
  border-radius:8px;padding:5px 13px;
  font-size:.7rem;letter-spacing:1px;cursor:pointer;
  text-transform:uppercase;transition:all .2s;font-family:'Poppins',sans-serif;
}}
.btn-export {{
  background:rgba(201,150,10,.15);border:1px solid var(--gold);
  color:var(--gold);
}}
.btn-export:hover {{ background:var(--gold);color:var(--bg-dark); }}
.btn-clear {{
  background:rgba(255,80,80,.1);border:1px solid rgba(255,80,80,.38);
  color:rgba(255,100,100,.8);
}}
.btn-clear:hover {{ background:rgba(255,80,80,.18); }}

.bar-wrap {{ margin-bottom:13px; }}
.bar-label {{
  display:flex;justify-content:space-between;
  font-size:.75rem;margin-bottom:5px;color:var(--text-light);
}}
.bar-label span:last-child {{ color:var(--gold);font-weight:600; }}
.bar-bg {{
  background:rgba(255,255,255,.07);border-radius:5px;
  height:9px;overflow:hidden;
}}
.bar-fill {{
  height:100%;
  background:linear-gradient(90deg,var(--crimson),var(--gold));
  border-radius:5px;transition:width .8s ease;
}}
.res-total {{
  text-align:center;font-size:.78rem;color:var(--text-muted);
  margin-top:18px;padding-top:14px;
  border-top:1px solid rgba(255,255,255,.07);
}}
.voter-section {{ margin-top:18px; }}
.voter-section h4 {{
  font-size:.68rem;letter-spacing:2px;text-transform:uppercase;
  color:var(--gold);margin-bottom:10px;
}}
.voter-row {{
  display:flex;justify-content:space-between;align-items:center;
  padding:8px 10px;border-bottom:1px solid rgba(255,255,255,.05);
  font-size:.77rem;
}}
.voter-row:hover {{ background:rgba(255,255,255,.03); }}
.vr-name {{ color:var(--text-light); }}
.vr-choice {{ color:var(--text-muted);font-size:.7rem;max-width:58%;text-align:right; }}
.vr-time {{ color:rgba(255,255,255,.26);font-size:.67rem; }}

/* ── RESPONSIVE ── */
@media(max-width:600px){{
  .hero-logo img {{ width:150px; }}
  .c-slide img {{ max-height:260px; }}
  .choice {{ padding:13px 14px; }}
  .admin-box {{ padding:22px 16px; }}
}}
</style>
</head>
<body>

<!-- ████ LOADER ████ -->
<div id="loader">
  <div class="loader-particles" id="lparts"></div>
  <div class="loader-core">
    <div class="loader-glow">
      <img src="data:image/{logo_ext};base64,{logo_b64}" alt="Karuda Dates">
    </div>
    <div class="loader-tagline">Since 1990 · Premium Quality</div>
  </div>
  <div class="loader-bar-wrap">
    <div class="loader-bar"></div>
  </div>
</div>

<!-- ████ MAIN PAGE ████ -->
<div id="page">

  <!-- ── HERO ── -->
  <section id="hero">
    <!-- background blobs -->
    <div class="hero-blob" style="width:500px;height:350px;top:-60px;left:-140px;"></div>
    <div class="hero-blob" style="width:380px;height:280px;bottom:60px;right:-100px;"></div>

    <!-- floating date particles -->
    <div class="float-dates-wrap" id="fdWrap"></div>

    <!-- palm bar -->
    <div class="hero-palm-bar">
      <div class="palm-line"></div>
      <span class="palm-label">🌴 Pure · Premium · Powerful 🌴</span>
      <div class="palm-line"></div>
    </div>

    <!-- logo -->
    <div class="hero-logo">
      <img src="data:image/{logo_ext};base64,{logo_b64}" alt="Karuda Dates Logo">
    </div>

    <!-- headline -->
    <div class="hero-headline">Nature's Finest Energy</div>
    <div class="hero-sub">Trusted Since 1990 · Karuda Food Products</div>
    <div class="divider-gold"></div>

    <!-- carousel -->
    <div class="carousel-wrap">
      <div class="carousel-eyebrow">Our Premium Products</div>
      <div class="carousel-frame">
        <div class="carousel-track" id="cTrack">
          <div class="c-slide">
            <img src="data:image/{prod_ext};base64,{black_dates_b64}" alt="Karuda Black Dates">
            <div class="c-caption">
              <strong>Black Dates</strong>
              <small>கருப்பு பேரிச்சம்பழம் · Premium Black Dates · 150g</small>
            </div>
          </div>
          <div class="c-slide">
            <img src="data:image/{prod_ext};base64,{deseeded_b64}" alt="Karuda Deseeded Dates">
            <div class="c-caption">
              <strong>Deseeded Dates</strong>
              <small>விதை நீக்கப்பட்ட பேரிச்சம்பழம் · Ready to Eat</small>
            </div>
          </div>
          <div class="c-slide">
            <img src="data:image/{prod_ext};base64,{dates_pkt_b64}" alt="Karuda Natural Dates">
            <div class="c-caption">
              <strong>Natural Dates</strong>
              <small>பேரிச்சம்பழம் · 100% Natural · 180g</small>
            </div>
          </div>
        </div>
      </div>
      <div class="c-dots">
        <button class="c-dot on" onclick="goSlide(0)"></button>
        <button class="c-dot" onclick="goSlide(1)"></button>
        <button class="c-dot" onclick="goSlide(2)"></button>
      </div>
    </div>

    <div class="divider-gold" style="margin-top:28px;"></div>
    <div class="scroll-hint">
      <span>Share Your Voice ↓</span>
      <div class="scroll-arrow"></div>
    </div>
  </section>

  <!-- ── POLL ── -->
  <section id="poll">
    <div class="poll-inner">

      <!-- language toggle -->
      <div class="lang-row">
        <button class="lang-btn on" onclick="setLang('en')">English</button>
        <button class="lang-btn" onclick="setLang('ta')">தமிழ்</button>
      </div>

      <div class="eyebrow en-only">Consumer Voice Poll</div>
      <div class="eyebrow ta-only ta-hidden">வாடிக்கையாளர் கருத்து வாக்கெடுப்பு</div>

      <h2 class="section-title en-only">Which tagline speaks to you the most?</h2>
      <h2 class="section-title ta-only ta-hidden">உங்களுக்கு மிகவும் பிடித்த வரிசையை தேர்வு செய்யுங்கள்</h2>

      <p class="section-sub en-only">
        The reasons why people should buy Karuda Dates are given below.<br>
        <strong>Kindly select the one that you like the most.</strong>
      </p>
      <p class="section-sub ta-only ta-hidden">
        கருடா பேரிச்சம்பழத்தை மக்கள் ஏன் வாங்க வேண்டும் என்ற விளக்கங்கள் கீழே உள்ளது<br>
        <strong>அதில் தங்களுக்கு பிடித்தது தயவு செய்து செலக்ட் செய்யுங்கள்</strong>
      </p>

      <!-- name -->
      <div class="name-card">
        <label class="field-label en-only">Your Name <span style="color:#FF6B6B">*</span></label>
        <label class="field-label ta-only ta-hidden">உங்கள் பெயர் <span style="color:#FF6B6B">*</span></label>
        <input class="field-input" type="text" id="vName"
               placeholder="Enter your full name…" autocomplete="off">
        <div class="field-error" id="nameErr">⚠ Please enter your name to continue.</div>
      </div>

      <!-- choices -->
      <div class="choices" id="choices">
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
        <button class="btn-submit en-only" onclick="doSubmit()">Submit My Vote</button>
        <button class="btn-submit ta-only ta-hidden" onclick="doSubmit()">வாக்களிக்கவும்</button>
      </div>

    </div>
  </section>

  <!-- ── THANK YOU ── -->
  <section id="ty">
    <div class="ty-stars-layer" id="tyStars"></div>

    <div class="ty-mascot">
      <img src="data:image/{mascot_ext};base64,{mascot_b64}" alt="Karuda Mascot">
    </div>
    <div class="ty-logo">
      <img src="data:image/{logo_ext};base64,{logo_b64}" alt="Karuda Dates">
    </div>

    <div class="ty-big">Thank You! 🙏</div>
    <div class="ty-name" id="tyName"></div>
    <p class="ty-msg">Your voice matters to us. Thank you for being part of the Karuda family and helping us grow stronger since 1990.</p>
    <p class="ty-msg-ta">நீங்கள் தேர்ந்தெடுத்தது எங்களுக்கு மிகவும் மகிழ்ச்சி. கருடா குடும்பத்தின் ஒரு அங்கமாக இருந்தமைக்கு நன்றி!</p>
    <div class="ty-choice-box">
      <p>Your Chosen Tagline</p>
      <strong id="tyChoice"></strong>
    </div>
    <div class="ty-footer">Karuda Food Products · Since 1990 · Premium Quality · Pure Power</div>
  </section>

</div><!-- /page -->

<!-- ── ADMIN BUTTON ── -->
<button id="admin-trigger" onclick="openAdmin()">Admin</button>

<!-- ── ADMIN MODAL ── -->
<div id="admin-modal">
  <div class="admin-box">
    <button class="admin-close" onclick="closeAdmin()">✕</button>
    <h2>🔐 Admin Dashboard</h2>

    <div id="apw">
      <input type="password" id="apwIn" placeholder="Enter admin password…"
             onkeydown="if(event.key==='Enter')tryLogin()">
      <button class="btn-login" onclick="tryLogin()">Unlock Results</button>
      <div class="pw-err" id="pwErr">⚠ Wrong password. Try again.</div>
    </div>

    <div id="ares">
      <div class="res-header">
        <h3>📊 Poll Results</h3>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="btn-export" onclick="exportCSV()">Export CSV</button>
          <button class="btn-clear" onclick="clearData()">Clear All</button>
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
/* ═══════════════════════════════════════════════
   CONFIG
═══════════════════════════════════════════════ */
const ADMIN_PW  = 'KARUDA2024';
const STORE_KEY = 'kd_votes_v1';
const DEV_KEY   = 'kd_dev_id';
const VOTED_PFX = 'kd_voted_';

const CHOICES = [
  'Karuda Dates - Never Slow Down',
  'Karuda Dates - Strength Reloaded',
  'Karuda Dates - Stay Unstoppable',
  'Karuda Dates - Instant Energy',
  'Karuda Dates - Instant Charging',
  'Karuda Dates - Fly Higher with Instant Charging'
];

/* ═══════════════════════════════════════════════
   STORAGE
═══════════════════════════════════════════════ */
function getVotes(){{
  try{{ return JSON.parse(localStorage.getItem(STORE_KEY)||'[]'); }}
  catch{{return[];}}
}}
function pushVote(name,choice){{
  const v=getVotes();
  v.push({{name,choice,time:new Date().toLocaleString('en-IN')}});
  localStorage.setItem(STORE_KEY,JSON.stringify(v));
}}
function clearVotes(){{ localStorage.removeItem(STORE_KEY); }}

function devId(){{
  let id=localStorage.getItem(DEV_KEY);
  if(!id){{ id=Math.random().toString(36).slice(2)+Date.now().toString(36); localStorage.setItem(DEV_KEY,id); }}
  return id;
}}
function hasVoted(){{ return !!localStorage.getItem(VOTED_PFX+devId()); }}
function markVoted(){{ localStorage.setItem(VOTED_PFX+devId(),'1'); }}

/* ═══════════════════════════════════════════════
   LOADER
═══════════════════════════════════════════════ */
(function(){{
  const wrap=document.getElementById('lparts');
  for(let i=0;i<24;i++){{
    const d=document.createElement('div');
    d.className='lp';
    const w=8+Math.random()*18, h=w*1.7;
    d.style.cssText=`width:${{w}}px;height:${{h}}px;left:${{Math.random()*100}}%;`+
      `animation-duration:${{7+Math.random()*11}}s;animation-delay:${{Math.random()*7}}s;`;
    wrap.appendChild(d);
  }}
}})();

window.addEventListener('load',function(){{
  setTimeout(function(){{
    document.getElementById('loader').classList.add('out');
    document.getElementById('page').classList.add('on');
    spawnFloatDates();
    if(hasVoted()) setTimeout(showAlreadyVoted,800);
  }},2800);
}});

function showAlreadyVoted(){{
  document.getElementById('poll').innerHTML=`
    <div class="already-voted">
      <div style="font-size:3rem;margin-bottom:14px">🙏</div>
      <h2 style="font-family:'Playfair Display',serif;color:var(--gold-light);font-size:2rem;margin-bottom:10px">Already Voted!</h2>
      <p style="color:var(--text-muted);max-width:400px;margin:0 auto;line-height:1.65">Thank you for participating in the Karuda poll! Your response has been recorded.</p>
      <p style="color:rgba(201,150,10,.45);font-size:.85rem;margin-top:8px">நீங்கள் ஏற்கனவே வாக்களித்துள்ளீர்கள். நன்றி!</p>
    </div>`;
}}

function spawnFloatDates(){{
  const w=document.getElementById('fdWrap');
  for(let i=0;i<18;i++){{
    const d=document.createElement('div');
    d.className='fd';
    const sz=10+Math.random()*16;
    d.style.cssText=`width:${{sz}}px;height:${{sz*1.72}}px;left:${{Math.random()*100}}%;`+
      `animation-duration:${{8+Math.random()*12}}s;animation-delay:${{Math.random()*8}}s;`;
    w.appendChild(d);
  }}
}}

/* ═══════════════════════════════════════════════
   CAROUSEL
═══════════════════════════════════════════════ */
let cIdx=0;
const cTotal=3;
function goSlide(n){{
  cIdx=n;
  document.getElementById('cTrack').style.transform=`translateX(-${{n*100}}%)`;
  document.querySelectorAll('.c-dot').forEach((d,i)=>d.classList.toggle('on',i===n));
}}
setInterval(()=>goSlide((cIdx+1)%cTotal),3800);

/* ═══════════════════════════════════════════════
   LANGUAGE
═══════════════════════════════════════════════ */
function setLang(l){{
  const isTa=l==='ta';
  document.querySelectorAll('.lang-btn').forEach((b,i)=>b.classList.toggle('on',(i===0&&!isTa)||(i===1&&isTa)));
  document.querySelectorAll('.en-only').forEach(el=>el.style.display=isTa?'none':'');
  document.querySelectorAll('.ta-only').forEach(el=>el.style.display=isTa?'block':'none');
}}

/* ═══════════════════════════════════════════════
   POLL
═══════════════════════════════════════════════ */
function pick(lbl){{
  document.querySelectorAll('.choice').forEach(c=>c.classList.remove('picked'));
  lbl.classList.add('picked');
  lbl.querySelector('input').checked=true;
  document.getElementById('choiceErr').style.display='none';
}}

function doSubmit(){{
  const name=document.getElementById('vName').value.trim();
  const sel=document.querySelector('input[name=poll]:checked');
  let ok=true;
  if(!name){{ document.getElementById('nameErr').style.display='block'; document.getElementById('vName').focus(); ok=false; }}
  else document.getElementById('nameErr').style.display='none';
  if(!sel){{ document.getElementById('choiceErr').style.display='block'; ok=false; }}
  else document.getElementById('choiceErr').style.display='none';
  if(!ok) return;

  pushVote(name,sel.value);
  markVoted();

  document.getElementById('poll').style.display='none';
  const ty=document.getElementById('ty');
  ty.classList.add('show');

  document.getElementById('tyName').textContent='Dear '+name+' 🌟';
  document.getElementById('tyChoice').textContent='✦ '+sel.value+' ✦';

  window.scrollTo({{top:0,behavior:'smooth'}});
  spawnStars();
  confetti();
}}

function spawnStars(){{
  const c=document.getElementById('tyStars');c.innerHTML='';
  for(let i=0;i<44;i++){{
    const s=document.createElement('div');s.className='ty-star';
    const sz=2+Math.random()*4;
    s.style.cssText=`left:${{Math.random()*100}}%;top:${{Math.random()*100}}%;`+
      `width:${{sz}}px;height:${{sz}}px;`+
      `animation-duration:${{1.4+Math.random()*3}}s;animation-delay:${{Math.random()*2}}s;`;
    c.appendChild(s);
  }}
}}

function confetti(){{
  const cols=['#C9960A','#F0C040','#9B1C1C','#ffffff','#FF6B35','#FFD700','#FF4500'];
  for(let i=0;i<70;i++){{
    setTimeout(()=>{{
      const el=document.createElement('div');el.className='cf';
      const sz=6+Math.random()*8;
      el.style.cssText=`left:${{Math.random()*100}}vw;top:-12px;`+
        `width:${{sz}}px;height:${{sz}}px;`+
        `background:${{cols[Math.floor(Math.random()*cols.length)]}};`+
        `animation-duration:${{1.6+Math.random()*2}}s;`+
        `border-radius:${{Math.random()>.5?'50%':'2px'}};`;
      document.body.appendChild(el);
      setTimeout(()=>el.remove(),3600);
    }},i*48);
  }}
}}

/* ═══════════════════════════════════════════════
   ADMIN
═══════════════════════════════════════════════ */
function openAdmin(){{
  const m=document.getElementById('admin-modal');
  m.classList.add('show');
  document.getElementById('apw').style.display='block';
  document.getElementById('ares').style.display='none';
  document.getElementById('apwIn').value='';
  document.getElementById('pwErr').style.display='none';
  setTimeout(()=>document.getElementById('apwIn').focus(),120);
}}
function closeAdmin(){{ document.getElementById('admin-modal').classList.remove('show'); }}
document.getElementById('admin-modal').addEventListener('click',function(e){{if(e.target===this)closeAdmin();}});

function tryLogin(){{
  if(document.getElementById('apwIn').value===ADMIN_PW){{
    document.getElementById('apw').style.display='none';
    document.getElementById('ares').style.display='block';
    renderAdmin();
  }} else {{
    document.getElementById('pwErr').style.display='block';
    document.getElementById('apwIn').value='';
    document.getElementById('apwIn').focus();
  }}
}}

function renderAdmin(){{
  const votes=getVotes();
  const total=votes.length;
  const counts={{}};
  CHOICES.forEach(c=>counts[c]=0);
  votes.forEach(v=>{{ if(counts[v.choice]!==undefined) counts[v.choice]++; else counts[v.choice]=1; }});
  const sorted=CHOICES.slice().sort((a,b)=>counts[b]-counts[a]);

  let html='';
  sorted.forEach(ch=>{{
    const pct=total>0?Math.round(counts[ch]/total*100):0;
    html+=`<div class="bar-wrap">
      <div class="bar-label"><span>${{ch}}</span><span>${{counts[ch]}} votes (${{pct}}%)</span></div>
      <div class="bar-bg"><div class="bar-fill" style="width:${{pct}}%"></div></div>
    </div>`;
  }});
  document.getElementById('resChart').innerHTML=html;
  document.getElementById('resTotal').innerHTML=
    `<strong style="color:var(--gold-light)">${{total}}</strong> total votes`+
    (total>0?` · Winner: <strong style="color:var(--gold-light)">${{sorted[0].replace('Karuda Dates - ','')}}</strong>`:'');

  let vhtml='';
  if(!votes.length) vhtml='<p style="color:rgba(255,255,255,.28);font-size:.78rem;text-align:center;padding:18px">No votes yet.</p>';
  else [...votes].reverse().forEach(v=>{{
    vhtml+=`<div class="voter-row">
      <span class="vr-name">${{v.name}}</span>
      <span class="vr-choice">${{v.choice.replace('Karuda Dates - ','')}}</span>
      <span class="vr-time">${{v.time}}</span>
    </div>`;
  }});
  document.getElementById('voterList').innerHTML=vhtml;
}}

function exportCSV(){{
  const v=getVotes();
  if(!v.length){{alert('No votes to export yet.');return;}}
  let csv='Name,Choice,Time\\n';
  v.forEach(r=>{{ csv+=`"${{r.name}}","${{r.choice}}","${{r.time}}"\\n`; }});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([csv],{{type:'text/csv'}}));
  a.download='karuda_poll_results.csv';a.click();
}}

function clearData(){{
  if(confirm('Delete ALL vote data? This cannot be undone.')){{
    clearVotes();renderAdmin();
  }}
}}
</script>
</body>
</html>"""

with open("karuda_poll.html","w",encoding="utf-8") as f:
    f.write(html)

print(f"Done! Size: {{len(html):,}} chars / {{len(html)//1024}} KB")