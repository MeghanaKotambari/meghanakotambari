#!/usr/bin/env python3
"""
Generate Clean, Enlarged Telemetry Metric HUD Cards for Meghana Kotambari's Profile
Features:
- Removed small redundant top headings for a cleaner, bolder look
- Enlarged card dimensions and big, bold stat values
- Animated pulsing corner beacons and glowing CSS hover effects
"""

import html
import os

def clean_text(text):
    return html.escape(str(text), quote=True)

def generate_hud_svg(output_path="assets/metrics_hud.svg"):
    width = 940
    height = 98
    
    stats = [
        ("1.5+ YRS", "4 Internships Completed", "#22D3EE"),
        ("9.00 CGPA", "B.E. Computer Science", "#10B981"),
        ("2x WINNER", "Top 10 in 800+ Teams", "#A78BFA"),
        ("40+ BUILT", "Full-Stack & Mobile Apps", "#38BDF8"),
        ("PRODUCTION", "Ready to Build & Scale", "#F59E0B")
    ]
    
    card_w = 176
    card_h = 84
    gap = 12
    start_x = 10
    start_y = 6
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append('    <filter id="hud-glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.5" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <style>')
    svg.append('      .hud-card { cursor: pointer; transition: transform 0.25s ease, filter 0.25s ease; }')
    svg.append('      .hud-card:hover { transform: translateY(-4px); filter: drop-shadow(0 6px 14px rgba(34, 211, 238, 0.4)); }')
    svg.append('      .hud-card:hover rect.card-body { stroke: #22D3EE !important; fill: #0c182c !important; }')
    svg.append('    </style>')
    svg.append('  </defs>')
    
    for i, (val, desc, color) in enumerate(stats):
        x = start_x + i * (card_w + gap)
        y = start_y
        
        svg.append(f'  <!-- Metric Card {i+1} -->')
        svg.append(f'  <g class="hud-card" transform="translate({x}, {y})">')
        # Glass background
        svg.append(f'    <rect class="card-body" x="0" y="0" width="{card_w}" height="{card_h}" rx="9" fill="#0A101F" stroke="#1E293B" stroke-width="1.3" />')
        
        # Top accent bar
        svg.append(f'    <line x1="12" y1="2" x2="{card_w-12}" y2="2" stroke="{color}" stroke-width="2" stroke-linecap="round" opacity="0.9" />')
        
        # Corner reticles
        svg.append(f'    <path d="M6 16 L6 8 L14 8" stroke="{color}" stroke-width="1.2" fill="none" opacity="0.6" />')
        svg.append(f'    <path d="M{card_w-6} {card_h-16} L{card_w-6} {card_h-8} L{card_w-14} {card_h-8}" stroke="{color}" stroke-width="1.2" fill="none" opacity="0.6" />')
        
        # Pulsing Beacon in Top Right
        svg.append(f'    <circle cx="{card_w-14}" cy="16" r="3" fill="{color}" filter="url(#hud-glow)">')
        svg.append(f'      <animate attributeName="opacity" values="1;0.35;1" dur="{2+i*0.4}s" repeatCount="indefinite" />')
        svg.append(f'    </circle>')
        
        # Big Bold Stat Value (Enlarged)
        svg.append(f'    <text x="14" y="44" fill="{color}" font-size="21" font-weight="900" letter-spacing="0.5">{clean_text(val)}</text>')
        
        # Clear Subtitle Description
        svg.append(f'    <text x="14" y="66" fill="#94A3B8" font-size="11" font-weight="500">{clean_text(desc)}</text>')
        svg.append(f'  </g>')
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_hud_svg()
