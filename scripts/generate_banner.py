#!/usr/bin/env python3
"""
Pixel-Perfect Tech Stack Matrix & System Dashboard Generator
Adjusted panel proportions per user request:
- Left Panel: Expanded width (360px) so the radial tech matrix & central hub look bigger & bolder
- Right Panel: Slimmer width (532px) while maintaining all telemetry content, alignment, and spacing
"""

import json
import math
import os
import html

def clean_text(text):
    escaped = html.escape(str(text), quote=True)
    return escaped.replace("·", "&#183;").replace("—", "&#8212;").replace("➔", "&#8594;")

def get_tech_logo(name, cx, cy, color):
    """Generates crisp inline SVG vector icons for each of the 12 technologies"""
    svg_icons = []
    
    if name == "React":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <ellipse rx="9.5" ry="3.5" stroke="{color}" stroke-width="1.1" fill="none" />')
        svg_icons.append(f'  <ellipse rx="9.5" ry="3.5" stroke="{color}" stroke-width="1.1" fill="none" transform="rotate(60)" />')
        svg_icons.append(f'  <ellipse rx="9.5" ry="3.5" stroke="{color}" stroke-width="1.1" fill="none" transform="rotate(120)" />')
        svg_icons.append(f'  <circle r="2" fill="{color}" />')
        svg_icons.append(f'</g>')
        
    elif name == "Next.js":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <circle r="7.5" fill="#000000" stroke="{color}" stroke-width="1" />')
        svg_icons.append(f'  <path d="M-3.5 4 L-3.5 -4 L-1.5 -4 L2.5 2.5 L2.5 -4 L4 -4 L4 4 L2 4 L-2 -2 L-2 4 Z" fill="#FFFFFF" />')
        svg_icons.append(f'</g>')
        
    elif name == "React Native":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <ellipse rx="9" ry="3.2" stroke="{color}" stroke-width="1.1" fill="none" />')
        svg_icons.append(f'  <ellipse rx="9" ry="3.2" stroke="{color}" stroke-width="1.1" fill="none" transform="rotate(60)" />')
        svg_icons.append(f'  <ellipse rx="9" ry="3.2" stroke="{color}" stroke-width="1.1" fill="none" transform="rotate(120)" />')
        svg_icons.append(f'  <circle r="1.8" fill="{color}" />')
        svg_icons.append(f'</g>')
        
    elif name == "Node.js":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(0.95)">')
        svg_icons.append(f'  <path d="M0 -8 L7 -4 L7 4 L0 8 L-7 4 L-7 -4 Z" stroke="{color}" stroke-width="1.2" fill="none" />')
        svg_icons.append(f'  <text x="0" y="2.5" fill="{color}" font-size="6.5" font-weight="800" text-anchor="middle">JS</text>')
        svg_icons.append(f'</g>')
        
    elif name == "Express.js":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <text x="0" y="3.5" fill="{color}" font-size="8.5" font-weight="800" text-anchor="middle" font-family="monospace">ex</text>')
        svg_icons.append(f'</g>')
        
    elif name == "TypeScript":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <rect x="-7.5" y="-6.5" width="15" height="13" rx="2" fill="{color}" />')
        svg_icons.append(f'  <text x="0" y="3" fill="#FFFFFF" font-size="7" font-weight="900" text-anchor="middle" font-family="monospace">TS</text>')
        svg_icons.append(f'</g>')
        
    elif name == "JavaScript":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <rect x="-7.5" y="-6.5" width="15" height="13" rx="2" fill="{color}" />')
        svg_icons.append(f'  <text x="0" y="3.5" fill="#000000" font-size="7.5" font-weight="900" text-anchor="middle" font-family="sans-serif">JS</text>')
        svg_icons.append(f'</g>')
        
    elif name == "MongoDB":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(0.95)">')
        svg_icons.append(f'  <path d="M0 -8 C3 -4 5 1 0 8 C-5 1 -3 -4 0 -8 Z" fill="{color}" />')
        svg_icons.append(f'  <line x1="0" y1="-7" x2="0" y2="7" stroke="#070D19" stroke-width="0.8" />')
        svg_icons.append(f'</g>')
        
    elif name == "Git":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <rect x="-5.5" y="-5.5" width="11" height="11" rx="2" fill="{color}" transform="rotate(45)" />')
        svg_icons.append(f'  <circle cx="-1.5" cy="0" r="1.3" fill="#FFFFFF" />')
        svg_icons.append(f'  <circle cx="2" cy="-2" r="1.3" fill="#FFFFFF" />')
        svg_icons.append(f'  <circle cx="2" cy="2" r="1.3" fill="#FFFFFF" />')
        svg_icons.append(f'  <path d="M-1.5 0 L2 -2 M-1.5 0 L2 2" stroke="#FFFFFF" stroke-width="0.8" />')
        svg_icons.append(f'</g>')
        
    elif name == "Tailwind CSS":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(0.9)">')
        svg_icons.append(f'  <path d="M-7 1 C-5 -3 0 -3 2 0 C4 3 7 3 8 1 C7 5 3 5 1 2 C-1 -1 -4 -1 -5 2 Z" fill="{color}" />')
        svg_icons.append(f'  <path d="M-5 -3 C-3 -7 2 -7 4 -4 C6 -1 9 -1 10 -3 C9 1 5 1 3 -2 C1 -5 -2 -5 -3 -2 Z" fill="{color}" />')
        svg_icons.append(f'</g>')
        
    elif name == "Redux":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(0.95)">')
        svg_icons.append(f'  <circle cx="0" cy="-4.5" r="2" fill="{color}" />')
        svg_icons.append(f'  <circle cx="-4" cy="3" r="2" fill="{color}" />')
        svg_icons.append(f'  <circle cx="4" cy="3" r="2" fill="{color}" />')
        svg_icons.append(f'  <path d="M0 -4.5 C-6 -2 -6 5 -4 3 C-2 1 2 1 4 3 C6 5 6 -2 0 -4.5 Z" stroke="{color}" stroke-width="1" fill="none" />')
        svg_icons.append(f'</g>')
        
    elif name == "AWS":
        svg_icons.append(f'<g transform="translate({cx}, {cy}) scale(1.05)">')
        svg_icons.append(f'  <text x="0" y="0.5" fill="{color}" font-size="6.5" font-weight="900" text-anchor="middle" font-family="monospace">aws</text>')
        svg_icons.append(f'  <path d="M-5 3.5 Q0 6.5 5 3.5" stroke="{color}" stroke-width="1" fill="none" />')
        svg_icons.append(f'  <polygon points="5,3.5 3.5,2.5 4,4.5" fill="{color}" />')
        svg_icons.append(f'</g>')
        
    return "\n".join(svg_icons)


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
        header_bar = "#0F172A"
        pill_bg = "#0F172A"
        node_bg = "#0B1528"
        node_border = "#1E3A5F"
        center_bg = "#071426"
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
        header_bar = "#E2E8F0"
        pill_bg = "#FFFFFF"
        node_bg = "#F8FAFC"
        node_border = "#CBD5E1"
        center_bg = "#E0F2FE"

    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 460" width="100%" height="100%" style="background-color: {bg_color}; border-radius: 12px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append(f'    <filter id="glow-cyan" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.5" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append(f'    <filter id="glow-emerald" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <clipPath id="tech-clip"><rect x="18" y="55" width="356" height="370" rx="8" /></clipPath>')
    svg.append('    <style>')
    svg.append('      @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }')
    svg.append('      .tech-node-badge { transition: transform 0.25s ease, filter 0.25s ease; cursor: pointer; }')
    svg.append('      .tech-node-badge:hover { transform: scale(1.12); filter: drop-shadow(0 0 8px #22D3EE); }')
    svg.append('      .tech-node-badge:hover polygon.badge-bg { stroke: #22D3EE !important; fill: #0d223a !important; }')
    svg.append('      .panel-box { transition: filter 0.3s ease; }')
    svg.append('      .panel-box:hover { filter: drop-shadow(0 0 16px rgba(34, 211, 238, 0.35)); }')
    svg.append('      .info-row { cursor: default; transition: opacity 0.2s ease; }')
    svg.append('      .info-row:hover text { fill: #22D3EE !important; font-weight: 700; }')
    svg.append('    </style>')
    svg.append('  </defs>')

    # Master Window Frame
    svg.append(f'  <rect x="1" y="1" width="938" height="458" rx="12" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5" />')
    
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
    # 2. Left Panel: [ TECH.STACK ] (Enlarged 360px Width & Big Radial Matrix)
    # =========================================================================
    left_w = 360
    svg.append(f'  <!-- Left Panel: TECH.STACK (Expanded Width) -->')
    svg.append(f'  <g class="panel-box">')
    svg.append(f'    <rect x="18" y="52" width="{left_w}" height="394" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <rect x="18" y="52" width="{left_w}" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'    <path d="M18 66 L18 78 L{18+left_w} 78 L{18+left_w} 66 Z" fill="{header_bar}" />')
    svg.append(f'    <line x1="18" y1="78" x2="{18+left_w}" y2="78" stroke="{border_color}" stroke-width="1" />')
    
    # Left Header: [ TECH.STACK ]
    svg.append(f'    <text x="28" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ TECH.STACK ]</text>')
    svg.append(f'    <text x="{18+left_w-10}" y="70" fill="{text_secondary}" font-size="9" font-weight="600" text-anchor="end" letter-spacing="0.5">RADAR.MATRIX // 240 FPS</text>')

    # Inside Visual Tech Matrix Area (Centered vertically with balanced margins)
    svg.append(f'    <g clip-path="url(#tech-clip)">')
    cx, cy = 198, 250

    # Top Status labels under header
    svg.append(f'      <path d="M26 86 L32 86 M26 86 L26 92" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'      <text x="32" y="93" fill="{text_secondary}" font-size="8" font-family="monospace" letter-spacing="0.5">Trx: 0xAF7E // STK_OK</text>')
    svg.append(f'      <path d="{18+left_w-10} 86 L{18+left_w-16} 86 M{18+left_w-10} 86 L{18+left_w-10} 92" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'      <text x="{18+left_w-16}" y="93" fill="{accent_emerald}" font-size="8" font-family="monospace" text-anchor="end" letter-spacing="0.5">LIVE_SYNC</text>')

    # Enlarged Concentric Radial Orbit Circles
    svg.append(f'      <circle cx="{cx}" cy="{cy}" r="126" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" fill="none" opacity="0.4" />')
    svg.append(f'      <circle cx="{cx}" cy="{cy}" r="92" stroke="{border_color}" stroke-width="1" stroke-dasharray="2 3" fill="none" opacity="0.5" />')
    svg.append(f'      <circle cx="{cx}" cy="{cy}" r="55" stroke="{border_color}" stroke-width="1" fill="none" opacity="0.3" />')

    # 12 Technologies (Expanded radii for bigger display)
    tech_nodes = [
        ("React", 270, "#61DAFB", 124),         # Top (12:00)
        ("Next.js", 300, "#FFFFFF", 126),       # (1:00)
        ("React Native", 330, "#61DAFB", 124),  # (2:00)
        ("Node.js", 0, "#339933", 128),         # Right (3:00)
        ("Express.js", 30, "#94A3B8", 126),     # (4:00)
        ("TypeScript", 60, "#3178C6", 124),     # (5:00)
        ("JavaScript", 90, "#F7DF1E", 126),     # Bottom (6:00)
        ("MongoDB", 120, "#47A248", 124),       # (7:00)
        ("Git", 150, "#F05032", 126),           # (8:00)
        ("Tailwind CSS", 180, "#06B6D4", 128),  # Left (9:00)
        ("Redux", 210, "#764ABC", 126),         # (10:00)
        ("AWS", 240, "#FF9900", 124)            # (11:00)
    ]

    # Draw Connected Radial Lines & Flowing Data Pulses
    for idx, (name, angle, color, r) in enumerate(tech_nodes):
        rad = math.radians(angle)
        nx = cx + r * math.cos(rad)
        ny = cy + r * math.sin(rad) * 0.94
        
        svg.append(f'      <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{border_color}" stroke-width="1.2" opacity="0.6" />')
        
        mid_x = cx + 55 * math.cos(rad)
        mid_y = cy + 55 * math.sin(rad) * 0.94
        svg.append(f'      <circle cx="{mid_x:.1f}" cy="{mid_y:.1f}" r="1.6" fill="{chrome_color}" opacity="0.8" />')
        
        mid_x2 = cx + 92 * math.cos(rad)
        mid_y2 = cy + 92 * math.sin(rad) * 0.94
        svg.append(f'      <circle cx="{mid_x2:.1f}" cy="{mid_y2:.1f}" r="1.6" fill="{chrome_color}" opacity="0.8" />')

        svg.append(f'      <circle r="2" fill="{color}" filter="url(#glow-cyan)">')
        svg.append(f'        <animate attributeName="cx" values="{cx};{nx:.1f};{cx}" dur="{3 + (idx % 3)*0.6}s" repeatCount="indefinite" />')
        svg.append(f'        <animate attributeName="cy" values="{cy};{ny:.1f};{cy}" dur="{3 + (idx % 3)*0.6}s" repeatCount="indefinite" />')
        svg.append(f'        <animate attributeName="opacity" values="0.2;1;0.2" dur="{3 + (idx % 3)*0.6}s" repeatCount="indefinite" />')
        svg.append(f'      </circle>')

    # Center Hub: FULL STACK DEVELOPER (Enlarged Radius: 42px)
    cr = 42
    svg.append(f'      <!-- Center Core: FULL STACK DEVELOPER (Enlarged) -->')
    svg.append(f'      <g transform="translate({cx}, {cy})">')
    svg.append(f'        <circle cx="0" cy="0" r="{cr + 4}" fill="none" stroke="{chrome_color}" stroke-width="1.2" opacity="0.4" filter="url(#glow-cyan)">')
    svg.append(f'          <animate attributeName="r" values="{cr+3};{cr+6};{cr+3}" dur="3s" repeatCount="indefinite" />')
    svg.append(f'          <animate attributeName="opacity" values="0.3;0.7;0.3" dur="3s" repeatCount="indefinite" />')
    svg.append(f'        </circle>')
    svg.append(f'        <circle cx="0" cy="0" r="{cr}" fill="{center_bg}" stroke="{chrome_color}" stroke-width="2" />')
    svg.append(f'        <circle cx="0" cy="0" r="{cr-3.5}" fill="none" stroke="{border_color}" stroke-width="1" stroke-dasharray="2 3" />')
    svg.append(f'        <text x="0" y="-11" fill="{chrome_color}" font-size="9.5" font-weight="900" letter-spacing="1.2" text-anchor="middle">FULL</text>')
    svg.append(f'        <text x="0" y="2" fill="{text_primary}" font-size="9.5" font-weight="900" letter-spacing="1.2" text-anchor="middle">STACK</text>')
    svg.append(f'        <text x="0" y="15" fill="{chrome_color}" font-size="8.5" font-weight="800" letter-spacing="0.8" text-anchor="middle">DEVELOPER</text>')
    svg.append(f'      </g>')

    # Render 12 Technology Octagonal/Circular Badge Nodes
    for idx, (name, angle, color, r) in enumerate(tech_nodes):
        rad = math.radians(angle)
        nx = cx + r * math.cos(rad)
        ny = cy + r * math.sin(rad) * 0.94
        
        svg.append(f'      <!-- Node {idx+1}: {name} -->')
        svg.append(f'      <g class="tech-node-badge" transform="translate({nx:.1f}, {ny:.1f})">')
        bw = 14.5
        pts = f"{-bw},-7.5 {-7.5},{-bw} {7.5},{-bw} {bw},-7.5 {bw},7.5 {7.5},{bw} {-7.5},{bw} {-bw},7.5"
        svg.append(f'        <polygon class="badge-bg" points="{pts}" fill="{node_bg}" stroke="{node_border}" stroke-width="1.2" />')
        svg.append(get_tech_logo(name, 0, 0, color))
        svg.append(f'        <text x="0" y="22" fill="{text_primary}" font-size="7.5" font-weight="600" letter-spacing="0.2" text-anchor="middle">{name}</text>')
        svg.append(f'      </g>')

    svg.append(f'    </g>')

    # Bottom Status Line
    svg.append(f'    <!-- Bottom Status Line -->')
    svg.append(f'    <g transform="translate(28, 422)">')
    svg.append(f'      <path d="M2 5 L2 0 L7 0" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'      <path d="{left_w-22} 5 L{left_w-22} 0 L{left_w-27} 0" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'      <path d="M2 13 L2 18 L7 18" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    svg.append(f'      <path d="{left_w-22} 13 L{left_w-22} 18 L{left_w-27} 18" stroke="{chrome_secondary}" stroke-width="1" fill="none" opacity="0.6"/>')
    
    svg.append(f'      <circle cx="16" cy="9" r="3.2" fill="{accent_emerald}" filter="url(#glow-emerald)">')
    svg.append(f'        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />')
    svg.append(f'      </circle>')
    svg.append(f'      <text x="26" y="12.5" fill="{chrome_color}" font-size="8.5" font-weight="700" letter-spacing="0.5">12+ CORE TECHNOLOGIES</text>')
    svg.append(f'      <text x="185" y="12.5" fill="{border_color}" font-size="9" font-weight="600">//</text>')
    svg.append(f'      <text x="200" y="12.5" fill="{accent_emerald}" font-size="8.5" font-weight="700" letter-spacing="0.5">STACK: ACTIVE</text>')
    svg.append(f'    </g>')
    svg.append(f'  </g>')

    # =========================================================================
    # 3. Right Panel: [ SYSTEM.INFO ] (Slimmer 532px Width, Preserved Content)
    # =========================================================================
    right_x = 390
    right_w = 532
    svg.append(f'  <!-- Right Panel: SYSTEM.INFO (Slimmer Proportions) -->')
    svg.append(f'  <g class="panel-box">')
    svg.append(f'    <rect x="{right_x}" y="52" width="{right_w}" height="394" rx="8" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <rect x="{right_x}" y="52" width="{right_w}" height="26" rx="8" fill="{header_bar}" />')
    svg.append(f'    <path d="M{right_x} 66 L{right_x} 78 L{right_x+right_w} 78 L{right_x+right_w} 66 Z" fill="{header_bar}" />')
    svg.append(f'    <line x1="{right_x}" y1="78" x2="{right_x+right_w}" y2="78" stroke="{border_color}" stroke-width="1" />')
    svg.append(f'    <text x="{right_x+12}" y="70" fill="{chrome_color}" font-size="11.5" font-weight="700" letter-spacing="1">[ SYSTEM.INFO ]</text>')
    svg.append(f'    <text x="{right_x+right_w-12}" y="70" fill="{accent_emerald}" font-size="9" font-weight="600" text-anchor="end" letter-spacing="0.5">STATUS: ACTIVE // 240 FPS</text>')

    # Top Block (5 fields)
    info_fields_top = [
        ("Subject", profile_data["name"]),
        ("Role", profile_data["role"]),
        ("Origin", profile_data["origin"]),
        ("Status", profile_data["status"]),
        ("ToolChain", profile_data["tools"])
    ]

    cur_y = 100
    for label, val in info_fields_top:
        svg.append(f'    <g class="info-row" transform="translate({right_x+14}, {cur_y})">')
        svg.append(f'      <text x="0" y="0" fill="{text_secondary}" font-size="11" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'      <text x="80" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_emerald if label in ["Status"] else (chrome_color if label in ["Subject", "Role"] else text_primary)
        val_weight = "700" if label in ["Subject", "Status"] else "500"
        svg.append(f'      <text x="{right_w-28}" y="0" fill="{val_color}" font-size="11" font-weight="{val_weight}" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'    </g>')
        cur_y += 24

    # Divider 1
    svg.append(f'    <line x1="{right_x+14}" y1="{cur_y + 1}" x2="{right_x+right_w-14}" y2="{cur_y + 1}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 20

    # Core Block (5 fields)
    info_fields_core = [
        ("Core.Lang", profile_data["core_languages"]),
        ("Core.Frontend", profile_data["core_frontend"]),
        ("Core.Backend", profile_data["core_backend"]),
        ("Core.Database", profile_data["core_database"]),
        ("Core.Infra", profile_data["core_infra"])
    ]

    for label, val in info_fields_core:
        svg.append(f'    <g class="info-row" transform="translate({right_x+14}, {cur_y})">')
        svg.append(f'      <text x="0" y="0" fill="{text_secondary}" font-size="10.5" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'      <text x="95" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        svg.append(f'      <text x="{right_w-28}" y="0" fill="{chrome_color}" font-size="10.5" font-weight="500" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'    </g>')
        cur_y += 22

    # Divider 2
    svg.append(f'    <line x1="{right_x+14}" y1="{cur_y + 1}" x2="{right_x+right_w-14}" y2="{cur_y + 1}" stroke="{border_color}" stroke-width="1" stroke-dasharray="3 3" />')
    cur_y += 20

    # Grid Block (4 fields)
    port_display = profile_data["portfolio"].replace("https://", "").replace("http://", "").rstrip("/")
    grid_fields = [
        ("Grid.Mail", profile_data["email"]),
        ("Grid.Portfolio", port_display),
        ("Grid.LinkedIn", "linkedin.com/in/meghana-kotambari-58a4332b0"),
        ("Grid.GitHub", f"github.com/{profile_data['github']}")
    ]

    for label, val in grid_fields:
        svg.append(f'    <g class="info-row" transform="translate({right_x+14}, {cur_y})">')
        svg.append(f'      <text x="0" y="0" fill="{text_secondary}" font-size="10" font-weight="600">{clean_text(label)}</text>')
        svg.append(f'      <text x="90" y="0" fill="{border_color}" font-size="11" letter-spacing="2">. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</text>')
        val_color = accent_purple if "GitHub" in label else (accent_emerald if "Portfolio" in label else text_primary)
        svg.append(f'      <text x="{right_w-28}" y="0" fill="{val_color}" font-size="10" font-weight="500" text-anchor="end">{clean_text(val)}</text>')
        svg.append(f'    </g>')
        cur_y += 20

    svg.append(f'  </g>')

    svg.append('</svg>')
    return "\n".join(svg)


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    with open("data/profile_data.json", "r", encoding="utf-8") as f:
        pdata = json.load(f)
        
    print("Generating dark.svg with enlarged Tech Stack Matrix & balanced right panel...")
    dark_svg = generate_svg(theme="dark", profile_data=pdata)
    with open("assets/dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
        
    print("Generating light.svg with enlarged Tech Stack Matrix & balanced right panel...")
    light_svg = generate_svg(theme="light", profile_data=pdata)
    with open("assets/light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
        
    print(f"Generated assets/dark.svg ({len(dark_svg.encode('utf-8')) / 1024:.1f} KB)")
    print(f"Generated assets/light.svg ({len(light_svg.encode('utf-8')) / 1024:.1f} KB)")
