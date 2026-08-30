#!/usr/bin/env python3
"""
Futuristic 3D Quantum Hologram & Tech Morph Hero Generator for Meghana Kotambari
Theme: term://meghana.os/profile.sh --live
Replaces avatar with an interactive 3D Holographic Quantum Matrix & Tech Particle Engine
"""

import json
import math
import os
import random
import html
import numpy as np

def clean_text(text):
    escaped = html.escape(str(text), quote=True)
    return escaped.replace("·", "&#183;").replace("—", "&#8212;").replace("➔", "&#8594;")


def generate_logo_points(logo_type, num_points=750, width=280, height=300, offset_x=30, offset_y=65):
    cx = offset_x + width / 2.0
    cy = offset_y + height / 2.0
    points = []
    
    if logo_type == "core":
        # 3D Quantum Octahedron / Diamond Wireframe Point Cloud
        # 6 Vertices + dense edge points + inner core
        vertices = [
            (0, -95, 0), (0, 95, 0),
            (75, 0, 0), (-75, 0, 0),
            (0, 0, 75), (0, 0, -75)
        ]
        # Edges between vertices
        edges = [
            (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 4), (4, 3), (3, 5), (5, 2)
        ]
        points_per_edge = int(num_points * 0.7) // len(edges)
        for u, v in edges:
            v1, v2 = vertices[u], vertices[v]
            for i in range(points_per_edge):
                t = i / float(points_per_edge)
                # 3D coordinates
                px = v1[0] + t * (v2[0] - v1[0])
                py = v1[1] + t * (v2[1] - v1[1])
                pz = v1[2] + t * (v2[2] - v1[2])
                # Isometric projection
                iso_x = cx + (px - pz) * math.cos(math.pi / 6) * 0.85
                iso_y = cy + py * 0.85 + (px + pz) * math.sin(math.pi / 6) * 0.45
                points.append((iso_x, iso_y))
                
        # Glowing nucleus core
        n_nucleus = num_points - len(points)
        for i in range(n_nucleus):
            r = math.sqrt(random.random()) * 22
            th = random.random() * 2 * math.pi
            points.append((cx + r * math.cos(th), cy + r * math.sin(th)))

    elif logo_type == "react":
        # React Logo: Nucleus + 3 Rotated Ellipses
        n_nucleus = int(num_points * 0.18)
        for i in range(n_nucleus):
            r = math.sqrt(random.random()) * 18
            th = random.random() * 2 * math.pi
            points.append((cx + r * math.cos(th), cy + r * math.sin(th)))
            
        n_ellipse = (num_points - len(points)) // 3
        angles = [0, math.pi / 3, 2 * math.pi / 3]
        a, b = 92, 34
        for rot in angles:
            for i in range(n_ellipse):
                t = (2 * math.pi * i) / n_ellipse + (random.random() - 0.5) * 0.05
                ex = a * math.cos(t)
                ey = b * math.sin(t)
                rx = ex * math.cos(rot) - ey * math.sin(rot)
                ry = ex * math.sin(rot) + ey * math.cos(rot)
                points.append((cx + rx, cy + ry))
                
    elif logo_type == "nodejs":
        # Node.js Hexagon + Structure
        radius = 92
        n_hex = int(num_points * 0.55)
        for i in range(n_hex):
            side = random.randint(0, 5)
            t = random.random()
            a1 = side * math.pi / 3 - math.pi / 6
            a2 = (side + 1) * math.pi / 3 - math.pi / 6
            x1, y1 = cx + radius * math.cos(a1), cy + radius * math.sin(a1)
            x2, y2 = cx + radius * math.cos(a2), cy + radius * math.sin(a2)
            points.append((x1 + t * (x2 - x1), y1 + t * (y2 - y1)))
            
        n_inner = num_points - len(points)
        for i in range(n_inner):
            sub = random.random()
            if sub < 0.33:
                points.append((cx - 38, cy - 48 + random.random() * 96))
            elif sub < 0.66:
                points.append((cx + 38, cy - 48 + random.random() * 96))
            else:
                points.append((cx - 38 + random.random() * 76, cy - 48 + random.random() * 96))

    elif logo_type == "typescript":
        # TypeScript Badge & TS Glyphs
        s = 82
        badge_points = int(num_points * 0.45)
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
                points.append((cx - 62 + random.random() * 42, cy - 24))
            else:
                points.append((cx - 41, cy - 24 + random.random() * 62))
                
        n_s = num_points - len(points)
        for i in range(n_s):
            t = random.random()
            if t < 0.25:
                points.append((cx + 5 + random.random() * 34, cy - 24))
            elif t < 0.5:
                points.append((cx + 5, cy - 24 + random.random() * 30))
            elif t < 0.75:
                points.append((cx + 5 + random.random() * 34, cy + 6))
            elif t < 0.9:
                points.append((cx + 39, cy + 6 + random.random() * 30))
            else:
                points.append((cx + 5 + random.random() * 34, cy + 36))

    while len(points) < num_points:
        points.append((cx + (random.random() - 0.5) * 60, cy + (random.random() - 0.5) * 60))
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


def generate_svg(theme="dark", profile_data=None):
    if profile_data is None:
        with open("data/profile_data.json", "r", encoding="utf-8") as f:
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
        grid_dot = "#1E293B"
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
        grid_dot = "#CBD5E1"
        header_bar = "#E2E8F0"
        pill_bg = "#FFFFFF"

    # Compute Hologram Particles (750 Points)
    p_core = generate_logo_points("core", num_points=750)
    p_react = generate_logo_points("react", num_points=750)
    p_node = generate_logo_points("nodejs", num_points=750)
    p_ts = generate_logo_points("typescript", num_points=750)
    
    p_react_matched = match_points_nearest(p_core, p_react)
    p_node_matched = match_points_nearest(p_react_matched, p_node)
    p_ts_matched = match_points_nearest(p_node_matched, p_ts)
    p_return_matched = match_points_nearest(p_ts_matched, p_core)

    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 470" width="100%" height="100%" style="background-color: {bg_color}; border-radius: 12px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append(f'    <filter id="glow-cyan" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append(f'    <filter id="glow-emerald" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <clipPath id="hologram-clip"><rect x="20" y="55" width="306" height="370" rx="8" /></clipPath>')
    svg.append('  </defs>')

    # Master Window Frame
    svg.append(f'  <rect x="1" y="1" width="938" height="468" rx="12" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5" />')
    
    # Window Top Bar
    svg.append(f'  <rect x="1" y="1" width="938" height="40" rx="12" fill="{header_bar}" />')
    svg.append(f'  <path d="M1 28 L1 40 L939 40 L939 28 Z" fill="{header_bar}" />')
    svg.append(f'  <line x1="1" y1="40" x2="939" y2="40" stroke="{border_color}" stroke-width="1" />')

    # Window Controls
    svg.append(f'  <circle cx="22" cy="20" r="5.5" fill="#EF4444" />')
    svg.append(f'  <circle cx="40" cy="20" r="5.5" fill="#F59E0B" />')
    svg.append(f'  <circle cx="58" cy="20" r="5.5" fill="#10B981" />')

    # Title prompt
    svg.append(f'  <text x="82" y="25" fill="{chrome_color}" font-size="13" font-weight="600" letter-spacing="0.5">term://meghana.os/profile.sh <tspan fill="{text_secondary}">--live</tspan></text>')

    # Handle Pill
    svg.append(f'  <g transform="translate(680, 10)">')
    svg.append(f'    <rect x="0" y="0" width="140" height="22" rx="11" fill="{pill_bg}" stroke="{chrome_secondary}" stroke-width="1" />')
    svg.append(f'    <text x="70" y="15.5" fill="{chrome_color}" font-size="11" font-weight="600" text-anchor="middle">@{clean_text(profile_data["github"])}</text>')
    svg.append(f'  </g>')

    # Live Beacon
    svg.append(f'  <g transform="translate(850, 20)">')
    svg.append(f'    <circle cx="0" cy="0" r="4.5" fill="{accent_emerald}" filter="url(#glow-emerald)">')
    svg.append(f'      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />')
    svg.append(f'    </circle>')
    svg.append(f'    <text x="10" y="4.5" fill="{accent_emerald}" font-size="11.5" font-weight="700" letter-spacing="1">LIVE</text>')
    svg.append(f'  </g>')

    # ==========================================
    # 2. Left Panel: [ VISUAL.MAP ]
    # ==========================================
    svg.append(f'  <!-- Left Panel: VISUAL.MAP -->')
    svg.append(f'  <rect x="18" y="52" width="310" height="404" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <rect x="18" y="52" width="310" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'  <path d="M18 66 L18 78 L328 78 L328 66 Z" fill="{header_bar}" />')
    svg.append(f'  <line x1="18" y1="78" x2="328" y2="78" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <text x="28" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ VISUAL.MAP ]</text>')
    svg.append(f'  <text x="318" y="70" fill="{text_secondary}" font-size="9.5" font-weight="600" text-anchor="end">300x340 // DITHER.FS</text>')

    # Background HUD Radar Grid & Technical Reticles
    svg.append(f'  <g clip-path="url(#hologram-clip)">')
    cx, cy = 173, 230
    # Radar concentric circles
    svg.append(f'    <circle cx="{cx}" cy="{cy}" r="120" stroke="{border_color}" stroke-width="1" stroke-dasharray="4 4" fill="none" opacity="0.4" />')
    svg.append(f'    <circle cx="{cx}" cy="{cy}" r="80" stroke="{border_color}" stroke-width="1" stroke-dasharray="2 4" fill="none" opacity="0.5" />')
    svg.append(f'    <circle cx="{cx}" cy="{cy}" r="40" stroke="{border_color}" stroke-width="1" fill="none" opacity="0.3" />')
    # Crosshair axes
    svg.append(f'    <line x1="{cx-125}" y1="{cy}" x2="{cx+125}" y2="{cy}" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 4" opacity="0.4" />')
    svg.append(f'    <line x1="{cx}" y1="{cy-125}" x2="{cx}" y2="{cy+125}" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 4" opacity="0.4" />')
    # Corner HUD crosshairs
    svg.append(f'    <path d="M26 86 L34 86 M26 86 L26 94" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'    <path d="M320 86 L312 86 M320 86 L320 94" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'    <path d="M26 420 L34 420 M26 420 L26 412" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'    <path d="M320 420 L312 420 M320 420 L320 412" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')

    # Animated Holographic 3D Rotating Octahedron Wireframe Lines (Layer 1)
    svg.append(f'    <g stroke="{chrome_color}" stroke-width="1.8" fill="none" opacity="0.85" filter="url(#glow-cyan)">')
    d1 = f"M{cx} {cy-95} L{cx+75} {cy} L{cx} {cy+95} L{cx-75} {cy} Z"
    d2 = f"M{cx} {cy-95} L{cx+30} {cy-25} L{cx} {cy+95} L{cx-30} {cy+25} Z"
    d3 = f"M{cx} {cy-95} L{cx-75} {cy} L{cx} {cy+95} L{cx+75} {cy} Z"
    svg.append(f'      <path d="{d1}">')
    svg.append(f'        <animate attributeName="d" values="{d1};{d2};{d3};{d2};{d1}" dur="8s" repeatCount="indefinite" />')
    svg.append(f'        <animate attributeName="opacity" values="0.9;0.9;0;0;0;0;0;0.9;0.9" keyTimes="0;0.28;0.34;0.52;0.68;0.84;0.92;0.96;1" dur="14s" repeatCount="indefinite" />')
    svg.append(f'      </path>')
    
    # Internal Axis Cross
    svg.append(f'      <line x1="{cx-75}" y1="{cy}" x2="{cx+75}" y2="{cy}" stroke="{accent_emerald}" stroke-width="1.2">')
    svg.append(f'        <animate attributeName="x1" values="{cx-75};{cx-30};{cx+75};{cx+30};{cx-75}" dur="8s" repeatCount="indefinite" />')
    svg.append(f'        <animate attributeName="x2" values="{cx+75};{cx+30};{cx-75};{cx-30};{cx+75}" dur="8s" repeatCount="indefinite" />')
    svg.append(f'        <animate attributeName="opacity" values="0.8;0.8;0;0;0;0;0;0.8;0.8" keyTimes="0;0.28;0.34;0.52;0.68;0.84;0.92;0.96;1" dur="14s" repeatCount="indefinite" />')
    svg.append(f'      </line>')
    svg.append(f'    </g>')

    # 750 Hologram Morph Particles (Layer 2)
    for i in range(len(p_core)):
        x0, y0 = round(p_core[i][0], 1), round(p_core[i][1], 1)
        x1, y1 = round(p_react_matched[i][0], 1), round(p_react_matched[i][1], 1)
        x2, y2 = round(p_node_matched[i][0], 1), round(p_node_matched[i][1], 1)
        x3, y3 = round(p_ts_matched[i][0], 1), round(p_ts_matched[i][1], 1)
        
        svg.append(f'    <circle cx="{x0:g}" cy="{y0:g}" r="1.3" fill="{chrome_color}">')
        key_times = "0;0.28;0.38;0.52;0.58;0.70;0.76;0.88;0.94;1"
        cx_vals = f"{x0:g};{x0:g};{x1:g};{x1:g};{x2:g};{x2:g};{x3:g};{x3:g};{x0:g};{x0:g}"
        cy_vals = f"{y0:g};{y0:g};{y1:g};{y1:g};{y2:g};{y2:g};{y3:g};{y3:g};{y0:g};{y0:g}"
        svg.append(f'      <animate attributeName="cx" values="{cx_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="cy" values="{cy_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="fill" values="{chrome_color};{chrome_color};{chrome_color};{chrome_color};{accent_emerald};{accent_emerald};{chrome_color};{chrome_color};{chrome_color};{chrome_color}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" />')
        svg.append(f'      <animate attributeName="opacity" values="0.85;0.85;0.95;0.95;0.95;0.95;0.95;0.95;0.85;0.85" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" />')
        svg.append(f'    </circle>')
    svg.append(f'  </g>')

    # Bottom Mode Indicator Pill on Visual Map
    svg.append(f'  <g transform="translate(28, 432)">')
    svg.append(f'    <rect x="0" y="0" width="290" height="18" rx="4" fill="{header_bar}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <rect x="0" y="0" width="46" height="18" rx="4" fill="{chrome_secondary}" />')
    svg.append(f'    <text x="23" y="13" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">MODE</text>')
    svg.append(f'    <text x="56" y="13" fill="{accent_emerald}" font-size="9" font-weight="600" letter-spacing="0.5">PARTICLE.MORPH [CORE &#8594; REACT &#8594; NODE &#8594; TS]</text>')
    svg.append(f'  </g>')

    # ==========================================
    # 3. Right Panel: [ SYSTEM.INFO ]
    # ==========================================
    svg.append(f'  <!-- Right Panel: SYSTEM.INFO -->')
    svg.append(f'  <rect x="340" y="52" width="582" height="404" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <rect x="340" y="52" width="582" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'  <path d="M340 66 L340 78 L922 78 L922 66 Z" fill="{header_bar}" />')
    svg.append(f'  <line x1="340" y1="78" x2="922" y2="78" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'  <text x="352" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ SYSTEM.INFO ]</text>')
    svg.append(f'  <text x="910" y="70" fill="{accent_emerald}" font-size="9.5" font-weight="600" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')

    info_fields_top = [
        ("Subject", profile_data["name"]),
        ("Role", profile_data["role"]),
        ("Origin", profile_data["origin"]),
        ("Status", profile_data["status"]),
        ("ToolChain", profile_data["tools"])
    ]

    cur_y = 96
    for label, val in info_fields_top:
        svg.append(f'  <g transform="translate(356, {cur_y})">')
        svg.append(f'    <text x="0" y="0" fill="{text_secondary}" font-size="11" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'    <text x="85" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_emerald if label in ["Status"] else (chrome_color if label in ["Subject", "Role"] else text_primary)
        val_weight = "700" if label in ["Subject", "Status"] else "500"
        svg.append(f'    <text x="550" y="0" fill="{val_color}" font-size="11" font-weight="{val_weight}" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'  </g>')
        cur_y += 22

    # Divider
    svg.append(f'  <line x1="356" y1="{cur_y + 1}" x2="906" y2="{cur_y + 1}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 18

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
        svg.append(f'    <text x="0" y="0" fill="{text_secondary}" font-size="10.5" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'    <text x="100" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        svg.append(f'    <text x="550" y="0" fill="{chrome_color}" font-size="10.5" font-weight="500" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'  </g>')
        cur_y += 20

    # Divider
    svg.append(f'  <line x1="356" y1="{cur_y + 1}" x2="906" y2="{cur_y + 1}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 18

    # Grid Links Block
    grid_fields = [
        ("Grid.Mail", profile_data["email"]),
        ("Grid.Portfolio", profile_data["portfolio"]),
        ("Grid.LinkedIn", "linkedin.com/in/meghana-kotambari-58a4332b0"),
        ("Grid.GitHub", f"github.com/{profile_data['github']}")
    ]

    for label, val in grid_fields:
        svg.append(f'  <g transform="translate(356, {cur_y})">')
        svg.append(f'    <text x="0" y="0" fill="{text_secondary}" font-size="10" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'    <text x="95" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_purple if "GitHub" in label else (accent_emerald if "Portfolio" in label else text_primary)
        svg.append(f'    <text x="550" y="0" fill="{val_color}" font-size="10" font-weight="500" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'  </g>')
        cur_y += 19


    svg.append('</svg>')
    return "\n".join(svg)


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    with open("data/profile_data.json", "r", encoding="utf-8") as f:
        pdata = json.load(f)
        
    print("Generating dark.svg with 3D Holographic Core & Particle Morphs...")
    dark_svg = generate_svg(theme="dark", profile_data=pdata)
    with open("assets/dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
        
    print("Generating light.svg with 3D Holographic Core & Particle Morphs...")
    light_svg = generate_svg(theme="light", profile_data=pdata)
    with open("assets/light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
        
    print(f"Generated assets/dark.svg ({len(dark_svg.encode('utf-8')) / 1024:.1f} KB)")
    print(f"Generated assets/light.svg ({len(light_svg.encode('utf-8')) / 1024:.1f} KB)")
