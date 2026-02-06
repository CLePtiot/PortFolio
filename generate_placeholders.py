from PIL import Image, ImageDraw, ImageFont
import os

LOGOS = {
    "lycee-fulbert.png": ("Lycée Fulbert", "#e5e5e5", "#181818"),
    "lycee-sully.png": ("Lycée Sully", "#e5e5e5", "#181818"),
    "college-jean-monnet.png": ("Collège Jean Monnet", "#e5e5e5", "#181818"),
    "xls-optronic.png": ("XO XLS Optronic", "#181818", "#c9a962"),
    "xtrempro.png": ("XtremPro", "#181818", "#3b82f6"),
    "nuit-info.png": ("Nuit de l'Info", "#181818", "#c9a962")
}

os.makedirs("images/logos", exist_ok=True)

# Try to use a default font, otherwise load one
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

for filename, (text, bg, fg) in LOGOS.items():
    path = os.path.join("images/logos", filename)
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        print(f"Skipping {filename}, already exists and valid.")
        continue
    
    print(f"Generating {filename}...")
    img = Image.new('RGB', (200, 200), color=bg)
    d = ImageDraw.Draw(img)
    
    # Text wrapping (simple)
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        if len(" ".join(current_line)) > 15: # Arbitrary wrap
            lines.append(" ".join(current_line))
            current_line = []
    if current_line:
        lines.append(" ".join(current_line))
        
    y = 80
    for line in lines:
        # centered
        # bbox = d.textbbox((0, 0), line, font=font)
        # w = bbox[2] - bbox[0]
        # d.text((100 - w/2, y), line, fill=fg, font=font)
        d.text((10, y), line, fill=fg) # Simple left align for safety
        y += 20
        
    img.save(path)
