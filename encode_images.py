import base64
import os

images = {
    "logo.png": "logo_b64.txt",
    "black_dates.jpg": "black_dates_b64.txt",
    "deseeded.jpg": "deseeded_b64.txt",
    "dates_packet.jpg": "dates_pkt_b64.txt",
    "mascot.jpg": "mascot_b64.txt"
}

os.makedirs("tmp", exist_ok=True)

for image, output in images.items():
    with open(f"images/{image}", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    with open(f"tmp/{output}", "w") as f:
        f.write(encoded)

    print(f"{image} encoded successfully")

print("All images converted!")