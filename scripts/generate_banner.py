#!/usr/bin/env python3
"""
High-Precision SVG Hero Generator for Meghana Kotambari's GitHub Profile
Theme: Futuristic Developer OS / Terminal (term://meghana.os/profile.sh --live)
Matches Reference Image 1 Layout & Color Palette with Dithered Avatar & Particle SMIL
"""

import json
import math
import os
import random
import html
import numpy as np
from PIL import Image, ImageEnhance, ImageOps, ImageDraw

def escape_xml(text):
    return html.escape(str(text), quote=True)


def generate_logo_points(logo_type, num_points=900, width=280, height=300, offset_x=30, offset_y=60):
    """
    Generate clean, geometrically exact particle points for technical logos
    normalized to the (offset_x, offset_y, width, height) viewport.
    """
    points = []
    cx = offset_x + width / 2.0
    cy = offset_y + height / 2.0
    
    if logo_type == "react":
        # React Logo: 1 nucleus circle + 3 rotated ellipses
        n_nucleus = int(num_points * 0.20)
        for i in range(n_nucleus):
            r = math.sqrt(random.random()) * 20
            theta = random.random() * 2 * math.pi
            points.append((cx + r * math.cos(theta), cy + r * math.sin(theta)))
            
        n_ellipse = (num_points - len(points)) // 3
        angles = [0, math.pi / 3, 2 * math.pi / 3]
        a, b = 95, 36
        
        for rot in angles:
            for i in range(n_ellipse):
                t = (2 * math.pi * i) / n_ellipse + (random.random() - 0.5) * 0.05
                ex = a * math.cos(t)
                ey = b * math.sin(t)
                rx = ex * math.cos(rot) - ey * math.sin(rot)
                ry = ex * math.sin(rot) + ey * math.cos(rot)
                points.append((cx + rx, cy + ry))
                
    elif logo_type == "nodejs":
        # Node.js Logo: Hexagon outline + inner structure
        radius = 95
        n_hex = int(num_points * 0.55)
        for i in range(n_hex):
            side = random.randint(0, 5)
            t = random.random()
            a1 = side * math.pi / 3 - math.pi / 6
            a2 = (side + 1) * math.pi / 3 - math.pi / 6
            x1, y1 = cx + radius * math.cos(a1), cy + radius * math.sin(a1)
            x2, y2 = cx + radius * math.cos(a2), cy + radius * math.sin(a2)
            px = x1 + t * (x2 - x1)
            py = y1 + t * (y2 - y1)
            points.append((px, py))
            
        n_inner = num_points - len(points)
        for i in range(n_inner):
            sub = random.random()
            if sub < 0.33:
                points.append((cx - 40, cy - 50 + random.random() * 100))
            elif sub < 0.66:
                points.append((cx + 40, cy - 50 + random.random() * 100))
            else:
                points.append((cx - 40 + random.random() * 80, cy - 50 + random.random() * 100))

    elif logo_type == "typescript":
        # TypeScript Logo: Rounded square badge + 'TS' letters
        badge_points = int(num_points * 0.45)
        s = 85
        for i in range(badge_points):
            side = random.randint(0, 3)
            t = (random.random() - 0.5) * 2 * s
            if side == 0:
                points.append((cx + t, cy - s))
            elif side == 1:
                points.append((cx + s, cy + t))
            elif side == 2:
                points.append((cx + t, cy + s))
            else:
                points.append((cx - s, cy + t))
                
        n_t = int((num_points - len(points)) * 0.45)
        for i in range(n_t):
            if random.random() < 0.5:
                points.append((cx - 65 + random.random() * 45, cy - 25))
            else:
                points.append((cx - 42.5, cy - 25 + random.random() * 65))
                
        n_s = num_points - len(points)
        for i in range(n_s):
            t = random.random()
            if t < 0.25:
                points.append((cx + 5 + random.random() * 35, cy - 25))
            elif t < 0.5:
                points.append((cx + 5, cy - 25 + random.random() * 32))
            elif t < 0.75:
                points.append((cx + 5 + random.random() * 35, cy + 7))
            elif t < 0.9:
                points.append((cx + 40, cy + 7 + random.random() * 32))
            else:
                points.append((cx + 5 + random.random() * 35, cy + 39))

    while len(points) < num_points:
        points.append((cx + (random.random() - 0.5) * 100, cy + (random.random() - 0.5) * 100))
    return points[:num_points]


def match_points_nearest(source_pts, target_pts):
    unassigned = list(range(len(target_pts)))
    target_arr = np.array(target_pts)
    matched_target = []
    
    for sx, sy in source_pts:
        if not unassigned:
            break
        remaining_targets = target_arr[unassigned]
        dists = np.sum((remaining_targets - np.array([sx, sy])) ** 2, axis=1)
        best_idx_in_remaining = np.argmin(dists)
        best_target_idx = unassigned[best_idx_in_remaining]
        matched_target.append(target_pts[best_target_idx])
        unassigned.pop(best_idx_in_remaining)
        
    return matched_target


def generate_dithered_portrait_matrix(width=280, height=310, offset_x=30, offset_y=60):
    """
    Generate an engineered 1-bit Floyd-Steinberg dithered head-and-shoulders
    monochrome portrait point matrix (~15,000 dots) directly from Meghana's 4th image.
    """
    photo_path = "assets/portrait.jpg" if os.path.exists("assets/portrait.jpg") else "data/portrait.jpg"
    
    if os.path.exists(photo_path):
        img = Image.open(photo_path).convert("L")
        img = ImageOps.autocontrast(img, cutoff=2)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.4)
        
        w, h = img.size
        target_ratio = width / height
        current_ratio = w / h
        
        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            img = img.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_ratio)
            top = int((h - new_h) * 0.12)
            img = img.crop((0, top, w, min(h, top + new_h)))
            
        img = img.resize((width, height), Image.Resampling.LANCZOS)
    else:
        img = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(img)
        cx = width // 2
        for y in range(height):
            v = int(20 + 35 * (1 - y / height))
            draw.line([(0, y), (width, y)], fill=v)
        draw.ellipse([cx - 100, height - 120, cx + 100, height + 100], fill=180)
        draw.rectangle([cx - 24, height - 145, cx + 24, height - 90], fill=195)
        draw.ellipse([cx - 52, height - 235, cx + 52, height - 125], fill=220)
    
    # Floyd-Steinberg dithering with serpentine scan
    arr = np.array(img, dtype=float)
    h, w = arr.shape
    dots = []
    
    for y in range(0, h, 2):
        row_range = range(0, w, 2) if (y // 2) % 2 == 0 else range(w - 2, -1, -2)
        for x in row_range:
            old_val = arr[y, x]
            new_val = 255 if old_val > 124 else 0
            err = old_val - new_val
            
            if new_val == 255:
                dots.append((offset_x + x, offset_y + y))
                
            if x + 1 < w:
                arr[y, x + 1] += err * 7 / 16
            if y + 1 < h:
                if x - 1 >= 0:
                    arr[y + 1, x - 1] += err * 3 / 16
                arr[y + 1, x] += err * 5 / 16
                if x + 1 < w:
                    arr[y + 1, x + 1] += err * 1 / 16

    grouped_dots = [[] for _ in range(60)]
    for i, (dx, dy) in enumerate(dots):
        group_id = int((dx * 73856093 ^ dy * 19349663 ^ i * 83492791) % 60)
        drift_x = math.sin(dy * 0.08) * 12 + (random.random() - 0.5) * 8
        drift_y = math.cos(dx * 0.08) * 8 + (random.random() - 0.5) * 6
        grouped_dots[group_id].append((int(dx), int(dy), round(drift_x, 1), round(drift_y, 1)))

    return grouped_dots, len(dots)


def generate_svg(theme="dark", profile_data=None):
    if profile_data is None:
        with open("data/profile_data.json", "r") as f:
            profile_data = json.load(f)
            
    is_dark = (theme == "dark")
    
    if is_dark:
        bg_color = "#0A101F"
        card_bg = "#070D19"
        chrome_color = "#22D3EE"        # Cyan Neon
        chrome_secondary = "#0891B2"    # Deep Cyan
        accent_emerald = "#10B981"      # Emerald Glow
        accent_purple = "#A78BFA"       # Light Purple
        text_primary = "#F8FAFC"        # Pure White
        text_secondary = "#94A3B8"      # Silver Muted
        border_color = "#1E293B"
        portrait_hue = "#38BDF8"        # Sky Blue for Meghana face
        traveller_hue = "#22D3EE"       # Cyan morph particles
        live_glow = "#10B981"
        header_bar = "#0F172A"
        pill_bg = "#0F172A"
    else:
        bg_color = "#F8FAFC"
        card_bg = "#FFFFFF"
        chrome_color = "#0284C7"
        chrome_secondary = "#0369A1"
        accent_emerald = "#059669"
        accent_purple = "#7C3AED"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        border_color = "#E2E8F0"
        portrait_hue = "#0284C7"
        traveller_hue = "#7C3AED"
        live_glow = "#059669"
        header_bar = "#E2E8F0"
        pill_bg = "#FFFFFF"

    # Compute Portrait Matrix (Layer 1)
    portrait_groups, total_dense_dots = generate_dithered_portrait_matrix()
    
    # Compute Traveller Morphs (Layer 2: 900 dots)
    p_portrait = []
    for g in portrait_groups:
        for dx, dy, _, _ in g:
            p_portrait.append((dx, dy))
            if len(p_portrait) >= 900:
                break
        if len(p_portrait) >= 900:
            break
    while len(p_portrait) < 900:
        p_portrait.append((170 + (random.random()-0.5)*100, 200 + (random.random()-0.5)*100))
        
    p_react = generate_logo_points("react", num_points=900)
    p_node = generate_logo_points("nodejs", num_points=900)
    p_ts = generate_logo_points("typescript", num_points=900)
    
    p_react_matched = match_points_nearest(p_portrait, p_react)
    p_node_matched = match_points_nearest(p_react_matched, p_node)
    p_ts_matched = match_points_nearest(p_node_matched, p_ts)
    p_return_matched = match_points_nearest(p_ts_matched, p_portrait)

    # Build SVG
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 450" width="100%" height="100%" style="background-color: {bg_color}; border-radius: 12px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append(f'    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.5" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append(f'    <filter id="glow-emerald" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <clipPath id="portrait-clip"><rect x="25" y="65" width="290" height="340" rx="8" /></clipPath>')
    svg.append('  </defs>')

    # Master Window Frame
    svg.append(f'  <rect x="1" y="1" width="938" height="448" rx="12" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5" />')
    
    # Window Top Bar
    svg.append(f'  <rect x="1" y="1" width="938" height="40" rx="12" fill="{header_bar}" />')
    svg.append(f'  <path d="M1 28 L1 40 L939 40 L939 28 Z" fill="{header_bar}" />')
    svg.append(f'  <line x1="1" y1="40" x2="939" y2="40" stroke="{border_color}" stroke-width="1" />')

    # Window Controls (Red, Amber, Green)
    svg.append(f'  <circle cx="22" cy="20" r="5.5" fill="#EF4444" />')
    svg.append(f'  <circle cx="40" cy="20" r="5.5" fill="#F59E0B" />')
    svg.append(f'  <circle cx="58" cy="20" r="5.5" fill="#10B981" />')

    # Terminal prompt title
    svg.append(f'  <text x="82" y="25" fill="{chrome_color}" font-size="13" font-weight="600" letter-spacing="0.5">term://meghana.os/profile.sh <tspan fill="{text_secondary}">--live</tspan></text>')

    # Top Right Handle Pill
    svg.append(f'  <g transform="translate(680, 10)">')
    svg.append(f'    <rect x="0" y="0" width="140" height="22" rx="11" fill="{pill_bg}" stroke="{chrome_secondary}" stroke-width="1" />')
    svg.append(f'    <text x="70" y="15.5" fill="{chrome_color}" font-size="11" font-weight="600" text-anchor="middle">@{escape_xml(profile_data["github"])}</text>')
    svg.append(f'  </g>')

    # Top Right Pulsing LIVE Indicator
    svg.append(f'  <g transform="translate(850, 20)">')
    svg.append(f'    <circle cx="0" cy="0" r="4.5" fill="{live_glow}" filter="url(#glow-emerald)">')
    svg.append(f'      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />')
    svg.append(f'    </circle>')
    svg.append(f'    <text x="10" y="4.5" fill="{live_glow}" font-size="11.5" font-weight="700" letter-spacing="1">LIVE</text>')
    svg.append(f'  </g>')

    # 2. Left Panel: [ VISUAL.MAP ]
    svg.append(f'  <!-- Left Panel: VISUAL.MAP -->')
    svg.append(f'  <rect x="18" y="52" width="310" height="382" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <rect x="18" y="52" width="310" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'  <path d="M18 66 L18 78 L328 78 L328 66 Z" fill="{header_bar}" />')
    svg.append(f'  <line x1="18" y1="78" x2="328" y2="78" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <text x="28" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ VISUAL.MAP ]</text>')
    svg.append(f'  <text x="318" y="70" fill="{text_secondary}" font-size="9.5" font-weight="600" text-anchor="end">300x340 // DITHER.FS</text>')

    # Layer 1: Dense Portrait Matrix (Meghana's 4th Image Avatar)
    svg.append(f'  <g clip-path="url(#portrait-clip)">')
    for group_idx, dots in enumerate(portrait_groups):
        if not dots:
            continue
        path_data = " ".join([f"M{int(dx)},{int(dy)}h1" for dx, dy, _, _ in dots])
        drift_data = " ".join([f"M{int(round(dx+drx))},{int(round(dy+dry))}h1" for dx, dy, drx, dry in dots])
        
        svg.append(f'    <path d="{path_data}" stroke="{portrait_hue}" stroke-width="1.6" stroke-linecap="round" opacity="0">')
        svg.append(f'      <animate attributeName="opacity" values="0;0.9;0.9;0;0;0;0;0.9;0.9" keyTimes="0;0.08;0.34;0.40;0.55;0.72;0.88;0.94;1" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="d" values="{path_data};{path_data};{drift_data};{drift_data};{path_data}" keyTimes="0;0.30;0.39;0.90;1" dur="14s" repeatCount="indefinite" />')
        svg.append(f'    </path>')
    svg.append(f'  </g>')

    # Layer 2: Traveller Morph Particles (~900 Points)
    svg.append(f'  <g clip-path="url(#portrait-clip)">')
    for i in range(min(len(p_portrait), 900)):
        x0, y0 = round(p_portrait[i][0], 1), round(p_portrait[i][1], 1)
        x1, y1 = round(p_react_matched[i][0], 1), round(p_react_matched[i][1], 1)
        x2, y2 = round(p_node_matched[i][0], 1), round(p_node_matched[i][1], 1)
        x3, y3 = round(p_ts_matched[i][0], 1), round(p_ts_matched[i][1], 1)
        
        svg.append(f'    <circle cx="{x0:g}" cy="{y0:g}" r="1.3" fill="{traveller_hue}">')
        key_times = "0;0.34;0.44;0.56;0.62;0.72;0.78;0.88;0.94;1"
        cx_vals = f"{x0:g};{x0:g};{x1:g};{x1:g};{x2:g};{x2:g};{x3:g};{x3:g};{x0:g};{x0:g}"
        cy_vals = f"{y0:g};{y0:g};{y1:g};{y1:g};{y2:g};{y2:g};{y3:g};{y3:g};{y0:g};{y0:g}"
        svg.append(f'      <animate attributeName="cx" values="{cx_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="cy" values="{cy_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="opacity" values="0;0;0.95;0.95;0.95;0.95;0.95;0.95;0;0" keyTimes="0;0.34;0.40;0.56;0.60;0.72;0.76;0.88;0.94;1" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="fill" values="{traveller_hue};{traveller_hue};{chrome_color};{chrome_color};{accent_emerald};{accent_emerald};{chrome_color};{chrome_color};{traveller_hue};{traveller_hue}" keyTimes="0;0.34;0.42;0.56;0.62;0.72;0.78;0.88;0.94;1" dur="14s" repeatCount="indefinite" />')
        svg.append(f'    </circle>')
    svg.append(f'  </g>')

    # Bottom Mode Indicator Pill on Visual Map
    svg.append(f'  <g transform="translate(28, 412)">')
    svg.append(f'    <rect x="0" y="0" width="290" height="18" rx="4" fill="{header_bar}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <rect x="0" y="0" width="46" height="18" rx="4" fill="{chrome_secondary}" />')
    svg.append(f'    <text x="23" y="13" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">MODE</text>')
    svg.append(f'    <text x="56" y="13" fill="{accent_emerald}" font-size="9" font-weight="600" letter-spacing="0.5">PARTICLE.MORPH [REACT ➔ NODE ➔ TS]</text>')
    svg.append(f'  </g>')

    # 3. Right Panel: [ SYSTEM.INFO ]
    svg.append(f'  <!-- Right Panel: SYSTEM.INFO -->')
    svg.append(f'  <rect x="340" y="52" width="582" height="382" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <rect x="340" y="52" width="582" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'  <path d="M340 66 L340 78 L922 78 L922 66 Z" fill="{header_bar}" />')
    svg.append(f'  <line x1="340" y1="78" x2="922" y2="78" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <text x="352" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ SYSTEM.INFO ]</text>')
    svg.append(f'  <text x="910" y="70" fill="{accent_emerald}" font-size="9.5" font-weight="600" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')

    # Top Info Block with exact dotted leaders
    info_fields_top = [
        ("Subject", profile_data["name"]),
        ("Role", profile_data["role"]),
        ("Origin", profile_data["origin"]),
        ("Status", profile_data["status"]),
        ("ToolChain", profile_data["tools"])
    ]

    cur_y = 102
    for label, val in info_fields_top:
        svg.append(f'  <g transform="translate(356, {cur_y})">')
        svg.append(f'    <text x="0" y="0" fill="{text_secondary}" font-size="11.5" font-weight="600">{escape_xml(label)}</text>')
        svg.append(f'    <text x="85" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_emerald if label in ["Status"] else (chrome_color if label in ["Subject", "Role"] else text_primary)
        val_weight = "700" if label in ["Subject", "Status"] else "500"
        svg.append(f'    <text x="550" y="0" fill="{val_color}" font-size="11.5" font-weight="{val_weight}" text-anchor="end">{escape_xml(val)}</text>')
        svg.append(f'  </g>')
        cur_y += 24

    # Divider
    svg.append(f'  <line x1="356" y1="{cur_y + 2}" x2="906" y2="{cur_y + 2}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 22

    # Core Stacks Block
    info_fields_core = [
        ("Core.Lang", profile_data["core_languages"]),
        ("Core.Frontend", profile_data["core_frontend"]),
        ("Core.Backend", profile_data["core_backend"]),
        ("Core.Database", profile_data["core_database"]),
        ("Core.Infra", profile_data["core_infra"])
    ]

    for label, val in info_fields_core:
        svg.append(f'  <g transform="translate(356, {cur_y})">')
        svg.append(f'    <text x="0" y="0" fill="{text_secondary}" font-size="11" font-weight="600">{escape_xml(label)}</text>')
        svg.append(f'    <text x="100" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        svg.append(f'    <text x="550" y="0" fill="{chrome_color}" font-size="11" font-weight="500" text-anchor="end">{escape_xml(val)}</text>')
        svg.append(f'  </g>')
        cur_y += 22

    # Divider
    svg.append(f'  <line x1="356" y1="{cur_y + 2}" x2="906" y2="{cur_y + 2}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 22

    # Grid Links Block
    grid_fields = [
        ("Grid.Mail", profile_data["email"]),
        ("Grid.Portfolio", profile_data["portfolio"]),
        ("Grid.LinkedIn", "linkedin.com/in/meghana-kotambari-58a4332b0"),
        ("Grid.GitHub", f"github.com/{profile_data['github']}")
    ]

    for label, val in grid_fields:
        svg.append(f'  <g transform="translate(356, {cur_y})">')
        svg.append(f'    <text x="0" y="0" fill="{text_secondary}" font-size="10.5" font-weight="600">{escape_xml(label)}</text>')
        svg.append(f'    <text x="95" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_purple if "GitHub" in label else (accent_emerald if "Portfolio" in label else text_primary)
        svg.append(f'    <text x="550" y="0" fill="{val_color}" font-size="10.5" font-weight="500" text-anchor="end">{escape_xml(val)}</text>')
        svg.append(f'  </g>')
        cur_y += 20

    svg.append('</svg>')
    return "\n".join(svg)


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    with open("data/profile_data.json", "r") as f:
        pdata = json.load(f)
        
    print("Generating dark.svg...")
    dark_svg = generate_svg(theme="dark", profile_data=pdata)
    with open("assets/dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
        
    print("Generating light.svg...")
    light_svg = generate_svg(theme="light", profile_data=pdata)
    with open("assets/light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
        
    print(f"Generated assets/dark.svg ({len(dark_svg.encode('utf-8')) / 1024:.1f} KB)")
    print(f"Generated assets/light.svg ({len(light_svg.encode('utf-8')) / 1024:.1f} KB)")
