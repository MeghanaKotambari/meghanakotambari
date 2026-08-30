#!/usr/bin/env python3
"""
Futuristic Tech Stack Matrix Hero Generator for Meghana Kotambari
Features:
- [ TECH.STACK ] Live Matrix with 12 Connected Radial Technology Nodes
- Center Core: FULL STACK DEVELOPER
- Connected nodes: React, React Native, Node.js, Express.js, TypeScript, JavaScript, MongoDB, PostgreSQL, Tailwind CSS, Redux, AWS, Docker
- Animated flowing data pulses along connection lines
- Glowing nodes with subtle pulsing / floating animations
- Terminal Status Bar: ● 12+ CORE TECHNOLOGIES    //    STACK: ACTIVE
- Untouched [ SYSTEM.INFO ] right panel with generous padding
"""

import json
import math
import os
import html

def clean_text(text):
    escaped = html.escape(str(text), quote=True)
    return escaped.replace("·", "&#183;").replace("—", "&#8212;").replace("➔", "&#8594;")


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
        node_bg = "#0B1528"
        node_stroke = "#1E3A5F"
        center_bg = "#091B33"
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
        node_bg = "#F1F5F9"
        node_stroke = "#CBD5E1"
        center_bg = "#E0F2FE"

    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 470" width="100%" height="100%" style="background-color: {bg_color}; border-radius: 12px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append(f'    <filter id="glow-cyan" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.5" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append(f'    <filter id="glow-emerald" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <clipPath id="tech-clip"><rect x="20" y="55" width="306" height="370" rx="8" /></clipPath>')
    svg.append('    <style>')
    svg.append('      @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }')
    svg.append('      .tech-node { transition: transform 0.25s ease, filter 0.25s ease; cursor: default; }')
    svg.append('      .tech-node:hover { transform: scale(1.08); filter: drop-shadow(0 0 8px #22D3EE); }')
    svg.append('      .tech-node:hover rect { stroke: #22D3EE !important; fill: #0F223D !important; }')
    svg.append('      .tech-node:hover text { fill: #22D3EE !important; font-weight: 700; }')
    svg.append('      .panel-box { transition: filter 0.3s ease; }')
    svg.append('      .panel-box:hover { filter: drop-shadow(0 0 16px rgba(34, 211, 238, 0.35)); }')
    svg.append('      .info-row { cursor: default; transition: opacity 0.2s ease; }')
    svg.append('      .info-row:hover text { fill: #22D3EE !important; font-weight: 700; }')
    svg.append('    </style>')
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

    # =========================================================================
    # 2. Left Panel: [ TECH.STACK ] (Interactive Developer Tech Matrix)
    # =========================================================================
    svg.append(f'  <!-- Left Panel: TECH.STACK -->')
    svg.append(f'  <g class="panel-box">')
    svg.append(f'    <rect x="18" y="52" width="310" height="404" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <rect x="18" y="52" width="310" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'    <path d="M18 66 L18 78 L328 78 L328 66 Z" fill="{header_bar}" />')
    svg.append(f'    <line x1="18" y1="78" x2="328" y2="78" stroke="{border_color}" stroke-width="1" />')
    
    # Left Header: [ TECH.STACK ]
    svg.append(f'    <text x="28" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ TECH.STACK ]</text>')
    
    # Right Header: LIVE Indicator with dot
    svg.append(f'    <circle cx="282" cy="65.5" r="3.5" fill="{accent_emerald}" filter="url(#glow-emerald)">')
    svg.append(f'      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite" />')
    svg.append(f'    </circle>')
    svg.append(f'    <text x="318" y="70" fill="{accent_emerald}" font-size="10" font-weight="700" letter-spacing="1" text-anchor="end">LIVE</text>')

    # Inside Visual Tech Matrix Area
    svg.append(f'    <g clip-path="url(#tech-clip)">')
    cx, cy = 173, 234

    # Background Technical Grid & Radial Orbits
    svg.append(f'      <circle cx="{cx}" cy="{cy}" r="126" stroke="{border_color}" stroke-width="1" stroke-dasharray="4 4" fill="none" opacity="0.3" />')
    svg.append(f'      <circle cx="{cx}" cy="{cy}" r="88" stroke="{border_color}" stroke-width="1" stroke-dasharray="2 4" fill="none" opacity="0.4" />')
    svg.append(f'      <circle cx="{cx}" cy="{cy}" r="52" stroke="{border_color}" stroke-width="1" fill="none" opacity="0.25" />')
    
    # Background subtle crosshairs
    svg.append(f'      <line x1="{cx-130}" y1="{cy}" x2="{cx+130}" y2="{cy}" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 4" opacity="0.35" />')
    svg.append(f'      <line x1="{cx}" y1="{cy-130}" x2="{cx}" y2="{cy+130}" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 4" opacity="0.35" />')

    # Corner Technical Reticles
    svg.append(f'      <path d="M26 86 L32 86 M26 86 L26 92" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.5"/>')
    svg.append(f'      <path d="M320 86 L314 86 M320 86 L320 92" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.5"/>')
    svg.append(f'      <path d="M26 422 L32 422 M26 422 L26 416" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.5"/>')
    svg.append(f'      <path d="M320 422 L314 422 M320 420 M320 422 L320 416" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.5"/>')

    # 12 Technology Nodes Definition
    # (name, radius_x, radius_y, angle_deg, color_accent)
    tech_nodes = [
        ("React", 0, -114, "#61DAFB"),
        ("TypeScript", 66, -98, "#3178C6"),
        ("Node.js", 108, -54, "#339933"),
        ("Express.js", 116, 0, "#94A3B8"),
        ("PostgreSQL", 108, 54, "#336791"),
        ("MongoDB", 66, 98, "#47A248"),
        ("React Native", 0, 114, "#61DAFB"),
        ("Tailwind CSS", -66, 98, "#06B6D4"),
        ("Redux", -108, 54, "#764ABC"),
        ("AWS", -116, 0, "#FF9900"),
        ("Docker", -108, -54, "#2496ED"),
        ("JavaScript", -66, -98, "#F7DF1E")
    ]

    # Draw Connecting Lines from Center to each Tech Node with Flowing Pulse
    for idx, (name, dx, dy, color) in enumerate(tech_nodes):
        nx, ny = cx + dx, cy + dy
        # Base connecting line
        svg.append(f'      <line x1="{cx}" y1="{cy}" x2="{nx}" y2="{ny}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" />')
        
        # Animated glowing photon / pulse along line
        svg.append(f'      <circle r="1.8" fill="{color}" filter="url(#glow-cyan)">')
        svg.append(f'        <animate attributeName="cx" values="{cx};{nx};{cx}" dur="{3.5 + (idx % 3)*0.8}s" repeatCount="indefinite" />')
        svg.append(f'        <animate attributeName="cy" values="{cy};{ny};{cy}" dur="{3.5 + (idx % 3)*0.8}s" repeatCount="indefinite" />')
        svg.append(f'        <animate attributeName="opacity" values="0.2;0.9;0.2" dur="{3.5 + (idx % 3)*0.8}s" repeatCount="indefinite" />')
        svg.append(f'      </circle>')

    # Center Hub: FULL STACK DEVELOPER
    cw, ch = 86, 44
    svg.append(f'      <!-- Center Core: FULL STACK DEVELOPER -->')
    svg.append(f'      <g transform="translate({cx}, {cy})">')
    # Center Outer Glow Pulse
    svg.append(f'        <rect x="{-cw/2 - 3}" y="{-ch/2 - 3}" width="{cw + 6}" height="{ch + 6}" rx="8" fill="none" stroke="{chrome_color}" stroke-width="1" opacity="0.4" filter="url(#glow-cyan)">')
    svg.append(f'          <animate attributeName="opacity" values="0.3;0.8;0.3" dur="3s" repeatCount="indefinite" />')
    svg.append(f'        </rect>')
    # Center Box
    svg.append(f'        <rect x="{-cw/2}" y="{-ch/2}" width="{cw}" height="{ch}" rx="6" fill="{center_bg}" stroke="{chrome_color}" stroke-width="1.6" />')
    # Center Stacked Typography
    svg.append(f'        <text x="0" y="-8" fill="{chrome_color}" font-size="8.5" font-weight="800" letter-spacing="1.5" text-anchor="middle">FULL</text>')
    svg.append(f'        <text x="0" y="3" fill="{text_primary}" font-size="8.5" font-weight="800" letter-spacing="1.5" text-anchor="middle">STACK</text>')
    svg.append(f'        <text x="0" y="14" fill="{accent_emerald}" font-size="7.5" font-weight="700" letter-spacing="0.8" text-anchor="middle">DEVELOPER</text>')
    svg.append(f'      </g>')

    # Render 12 Technology Nodes (Pills & Dots)
    for idx, (name, dx, dy, color) in enumerate(tech_nodes):
        nx, ny = cx + dx, cy + dy
        nw = max(len(name) * 5.8 + 14, 42)
        nh = 17
        
        svg.append(f'      <!-- Node {idx+1}: {name} -->')
        svg.append(f'      <g class="tech-node" transform="translate({nx}, {ny})">')
        # Floating micro-animation
        svg.append(f'        <animateTransform attributeName="transform" type="translate" values="{nx} {ny}; {nx} {ny-2}; {nx} {ny}" dur="{4 + (idx%4)*0.5}s" repeatCount="indefinite" />')
        
        # Node Pill Background
        svg.append(f'        <rect x="{-nw/2}" y="{-nh/2}" width="{nw}" height="{nh}" rx="4" fill="{node_bg}" stroke="{node_stroke}" stroke-width="1" />')
        
        # Small Indicator Dot
        svg.append(f'        <circle cx="{-nw/2 + 6}" cy="0" r="2.2" fill="{color}" filter="url(#glow-cyan)">')
        svg.append(f'          <animate attributeName="opacity" values="0.7;1;0.7" dur="{2 + (idx%3)}s" repeatCount="indefinite" />')
        svg.append(f'        </circle>')
        
        # Node Label
        svg.append(f'        <text x="{-nw/2 + 12}" y="3.5" fill="{text_primary}" font-size="8.5" font-weight="600" letter-spacing="0.3">{name}</text>')
        svg.append(f'      </g>')

    svg.append(f'    </g>')

    # Bottom Status Line: ● 12+ CORE TECHNOLOGIES    //    STACK: ACTIVE
    svg.append(f'    <!-- Bottom Status Line -->')
    svg.append(f'    <g transform="translate(28, 432)">')
    svg.append(f'      <rect x="0" y="0" width="290" height="18" rx="4" fill="{header_bar}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'      <circle cx="12" cy="9" r="3" fill="{accent_emerald}" filter="url(#glow-emerald)">')
    svg.append(f'        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />')
    svg.append(f'      </circle>')
    svg.append(f'      <text x="22" y="12.5" fill="{text_primary}" font-size="8.5" font-weight="700" letter-spacing="0.5">12+ CORE TECHNOLOGIES</text>')
    svg.append(f'      <text x="175" y="12.5" fill="{border_color}" font-size="9" font-weight="600">//</text>')
    svg.append(f'      <text x="190" y="12.5" fill="{accent_emerald}" font-size="8.5" font-weight="700" letter-spacing="0.5">STACK: ACTIVE</text>')
    svg.append(f'    </g>')
    svg.append(f'  </g>')

    # =========================================================================
    # 3. Right Panel: [ SYSTEM.INFO ] (Preserved Exactly with Safe Spacing)
    # =========================================================================
    svg.append(f'  <!-- Right Panel: SYSTEM.INFO -->')
    svg.append(f'  <g class="panel-box">')
    svg.append(f'    <rect x="340" y="52" width="582" height="404" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <rect x="340" y="52" width="582" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'    <path d="M340 66 L340 78 L922 78 L922 66 Z" fill="{header_bar}" />')
    svg.append(f'    <line x1="340" y1="78" x2="922" y2="78" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <text x="352" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ SYSTEM.INFO ]</text>')
    svg.append(f'    <text x="910" y="70" fill="{accent_emerald}" font-size="9.5" font-weight="600" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')

    info_fields_top = [
        ("Subject", profile_data["name"]),
        ("Role", profile_data["role"]),
        ("Origin", profile_data["origin"]),
        ("Status", profile_data["status"]),
        ("ToolChain", profile_data["tools"])
    ]

    cur_y = 96
    for label, val in info_fields_top:
        svg.append(f'    <g class="info-row" transform="translate(356, {cur_y})">')
        svg.append(f'      <text x="0" y="0" fill="{text_secondary}" font-size="11" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'      <text x="85" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_emerald if label in ["Status"] else (chrome_color if label in ["Subject", "Role"] else text_primary)
        val_weight = "700" if label in ["Subject", "Status"] else "500"
        svg.append(f'      <text x="550" y="0" fill="{val_color}" font-size="11" font-weight="{val_weight}" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'    </g>')
        cur_y += 22

    # Divider
    svg.append(f'    <line x1="356" y1="{cur_y + 1}" x2="906" y2="{cur_y + 1}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
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
        svg.append(f'    <g class="info-row" transform="translate(356, {cur_y})">')
        svg.append(f'      <text x="0" y="0" fill="{text_secondary}" font-size="10.5" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'      <text x="100" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        svg.append(f'      <text x="550" y="0" fill="{chrome_color}" font-size="10.5" font-weight="500" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'    </g>')
        cur_y += 20

    # Divider
    svg.append(f'    <line x1="356" y1="{cur_y + 1}" x2="906" y2="{cur_y + 1}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 18

    # Grid Links Block
    grid_fields = [
        ("Grid.Mail", profile_data["email"]),
        ("Grid.Portfolio", profile_data["portfolio"]),
        ("Grid.LinkedIn", "linkedin.com/in/meghana-kotambari-58a4332b0"),
        ("Grid.GitHub", f"github.com/{profile_data['github']}")
    ]

    for label, val in grid_fields:
        svg.append(f'    <g class="info-row" transform="translate(356, {cur_y})">')
        svg.append(f'      <text x="0" y="0" fill="{text_secondary}" font-size="10" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'      <text x="95" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_purple if "GitHub" in label else (accent_emerald if "Portfolio" in label else text_primary)
        svg.append(f'      <text x="550" y="0" fill="{val_color}" font-size="10" font-weight="500" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'    </g>')
        cur_y += 19

    svg.append(f'  </g>')

    svg.append('</svg>')
    return "\n".join(svg)


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    with open("data/profile_data.json", "r", encoding="utf-8") as f:
        pdata = json.load(f)
        
    print("Generating dark.svg with [ TECH.STACK ] Matrix...")
    dark_svg = generate_svg(theme="dark", profile_data=pdata)
    with open("assets/dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
        
    print("Generating light.svg with [ TECH.STACK ] Matrix...")
    light_svg = generate_svg(theme="light", profile_data=pdata)
    with open("assets/light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
        
    print(f"Generated assets/dark.svg ({len(dark_svg.encode('utf-8')) / 1024:.1f} KB)")
    print(f"Generated assets/light.svg ({len(light_svg.encode('utf-8')) / 1024:.1f} KB)")
