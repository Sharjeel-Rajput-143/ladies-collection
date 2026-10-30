from PIL import Image, ImageDraw, ImageFont
import random, os

W, H = 1200, 1600

GOLD_LIGHT = (214, 180, 120)
INK_LINE = (110, 86, 48)

PALETTES = {
    "lawn":  [(250, 240, 224), (233, 210, 176)],
    "kurti": [(247, 231, 227), (224, 189, 180)],
    "abaya": [(45, 43, 41), (22, 21, 20)],
    "dress": [(58, 24, 30), (94, 30, 40)],
}

def font(size, bold=True):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

def vgradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        base.putpixel((0, y), (r, g, b))
    return base.resize((w, h))

def silhouette(draw, cx, top_y, bottom_y, shoulder_w, waist_w, hem_w, color, width, neckline="round", sleeves=True, dupatta=False):
    body_top = top_y + 90
    pts_right = [
        (cx + shoulder_w * 0.5, body_top),
        (cx + waist_w * 0.5, top_y + (bottom_y - top_y) * 0.45),
        (cx + hem_w * 0.5, bottom_y),
    ]
    left_mirror = [(2 * cx - x, y) for x, y in pts_right]
    outline = [(cx - shoulder_w * 0.5, body_top)] + pts_right + [(cx + hem_w * 0.5, bottom_y), (cx - hem_w * 0.5, bottom_y)] + list(reversed(left_mirror))
    draw.line(outline + [outline[0]], fill=color, width=width, joint="curve")

    if neckline == "round":
        draw.arc([cx - 70, top_y + 55, cx + 70, top_y + 140], start=20, end=160, fill=color, width=width)
    elif neckline == "v":
        draw.line([(cx - 55, top_y + 70), (cx, top_y + 150), (cx + 55, top_y + 70)], fill=color, width=width, joint="curve")

    if sleeves:
        draw.line([(cx - shoulder_w * 0.5, body_top), (cx - shoulder_w * 0.5 - 60, body_top + 140)], fill=color, width=width)
        draw.line([(cx + shoulder_w * 0.5, body_top), (cx + shoulder_w * 0.5 + 60, body_top + 140)], fill=color, width=width)

    if dupatta:
        draw.line([(cx - shoulder_w * 0.5 - 10, body_top + 10), (cx - shoulder_w * 1.05, bottom_y - 260)], fill=color, width=max(width - 8, 2))
        draw.line([(cx + shoulder_w * 0.5 + 10, body_top + 10), (cx + shoulder_w * 1.05, bottom_y - 260)], fill=color, width=max(width - 8, 2))

def embroidery_dots(draw, cx, top_y, color, n=14, spread=150, seed=42):
    rnd = random.Random(seed)
    for _ in range(n):
        x = cx + rnd.uniform(-spread, spread)
        y = top_y + 90 + rnd.uniform(20, 160)
        r = rnd.uniform(3, 6)
        draw.ellipse([x - r, y - r, x + r, y + r], outline=color, width=2)

def make_placeholder(path, category, label, embroidered=False, seed=1):
    top, bottom = PALETTES[category]
    im = vgradient((W, H), top, bottom).convert("RGB")
    d = ImageDraw.Draw(im)

    line_color = INK_LINE if category in ("lawn", "kurti") else GOLD_LIGHT
    cx = W / 2
    top_y = 260
    bottom_y = H - 260

    if category == "lawn":
        silhouette(d, cx, top_y, bottom_y, 420, 300, 520, line_color, 7, "round", sleeves=True, dupatta=True)
    elif category == "kurti":
        silhouette(d, cx, top_y, bottom_y - 140, 360, 260, 360, line_color, 7, "round", sleeves=True, dupatta=False)
    elif category == "abaya":
        silhouette(d, cx, top_y - 60, bottom_y + 60, 380, 260, 560, line_color, 7, "v", sleeves=True, dupatta=False)
    elif category == "dress":
        silhouette(d, cx, top_y, bottom_y, 320, 170, 480, line_color, 7, "v", sleeves=False, dupatta=False)

    if embroidered:
        embroidery_dots(d, cx, top_y, line_color, seed=seed)

    m = 48
    frame_color = (214, 180, 120) if category in ("abaya", "dress") else (150, 120, 70)
    d.rectangle([m, m, W - m, H - m], outline=frame_color, width=3)

    f = font(52)
    text_color = (235, 220, 190) if category in ("abaya", "dress") else (90, 68, 36)
    bbox = d.textbbox((0, 0), label, font=f)
    tw = bbox[2] - bbox[0]
    d.text(((W - tw) / 2 - bbox[0], H - 150), label, font=f, fill=text_color)

    im.save(path, quality=88)


ITEMS = [
    ("LWN-101", "lawn", "Lawn . Embroidered", True, 1),
    ("LWN-102", "lawn", "Lawn . Digital Print", False, 2),
    ("LWN-103", "lawn", "Lawn . Festive", True, 3),
    ("LWN-104", "lawn", "Lawn . Pastel", False, 4),
    ("LWN-105", "lawn", "Lawn . Stitched", True, 5),
    ("LWN-106", "lawn", "Lawn . Stitched", False, 6),
    ("LWN-107", "lawn", "Lawn . Schiffli", True, 7),
    ("LWN-108", "lawn", "Lawn . Karandi", True, 8),
    ("KUR-201", "kurti", "Kurti . A-Line", True, 9),
    ("KUR-202", "kurti", "Kurti . Straight", False, 10),
    ("KUR-203", "kurti", "Kurti . Printed", False, 11),
    ("KUR-204", "kurti", "Kurti . Unstitched", False, 12),
    ("KUR-205", "kurti", "Kurti . Cambric", True, 13),
    ("ABY-301", "abaya", "Abaya . Classic", False, 14),
    ("ABY-302", "abaya", "Abaya . Front Open", True, 15),
    ("ABY-303", "abaya", "Abaya . Butterfly", False, 16),
    ("ABY-304", "abaya", "Abaya . Chiffon", True, 17),
    ("DRS-401", "dress", "Dress . Embellished", True, 18),
    ("DRS-402", "dress", "Dress . Chiffon Maxi", False, 19),
    ("DRS-403", "dress", "Dress . Velvet", True, 20),
    ("DRS-404", "dress", "Dress . Organza", True, 21),
]

out_dir = "public/products"
os.makedirs(out_dir, exist_ok=True)
for pid, cat, label, emb, seed in ITEMS:
    fname = f"{pid.lower()}.jpg"
    make_placeholder(os.path.join(out_dir, fname), cat, label, emb, seed)
    print("made", fname)
