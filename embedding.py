import base64
import json

with open("uploads/1781189610309_karuda-since-logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

with open("uploads/1781189610310_12c__1_.jpg", "rb") as f:
    black_dates_b64 = base64.b64encode(f.read()).decode()

with open("uploads/1781189610310_8d.jpg", "rb") as f:
    deseeded_b64 = base64.b64encode(f.read()).decode()

with open("uploads/1781189610311_10c__1_.jpg", "rb") as f:
    dates_pkt_b64 = base64.b64encode(f.read()).decode()

with open("uploads/1781189610312_IMG-20200627-WA0019.jpg", "rb") as f:
    mascot_b64 = base64.b64encode(f.read()).decode()

print("Images loaded:", len(logo_b64), len(mascot_b64))

data = {
    "logo": logo_b64,
    "black_dates": black_dates_b64,
    "deseeded": deseeded_b64,
    "dates_pkt": dates_pkt_b64,
    "mascot": mascot_b64
}

with open("img_data.json", "w") as f:
    json.dump(data, f)

print("Saved!")