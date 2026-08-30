#!/usr/bin/env python3
"""
Generate Futuristic Telemetry Metric HUD for Meghana Kotambari's Profile
Displays 5 glowing holographic stat cards with animated scan indicators and CSS hover effects.
"""

import html
import os

def clean_text(text):
    return html.escape(str(text), quote=True)

def generate_hud_svg(output_path="assets/metrics_hud.svg"):
    width = 940
    height = 92
    
    stats = [
        ("EXPERIENCE", "1.5+ YRS", "4 Internships Completed", "#22D3EE"),
        ("ACADEMICS", "9.00 CGPA", "B.E. Computer Science", "#10B981"),
        ("HACKATHONS", "2x WINNER", "Top 10 in 800+ Teams", "#A78BFA"),
        ("PORTFOLIO", "40+ BUILT", "Full-Stack & Mobile Apps", "#38BDF8"),
        ("DISPATCH", "PRODUCTION", "Ready to Build & Scale", "#F59E0B")
    ]
    
    card_w = 176
    card_h = 76
    gap = 12
    start_x = 10
    start_y = 8
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append('    <filter id="hud-glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <style>')
    svg.append('      .hud-card { cursor: pointer; transition: transform 0.25s ease, filter 0.25s ease; }')
    svg.append('      .hud-card:hover { transform: translateY(-3px); filter: drop-shadow(0 4px 12px rgba(34, 211, 238, 0.45)); }')
    svg.append('      .hud-card:hover rect.card-body { stroke: #22D3EE !important; fill: #0d1627 !important; }')
    svg.append('    </style>')
    svg.append('  </defs>')
    
    for i, (label, val, desc, color) in enumerate(stats):
        x = start_x + i * (card_w + gap)
        y = start_y
        
        svg.append(f'  <!-- Metric Card {i+1} -->')
        svg.append(f'  <g class="hud-card" transform="translate({x}, {y})">')
        # Glass background
        svg.append(f'    <rect class="card-body" x="0" y="0" width="{card_w}" height="{card_h}" rx="8" fill="#0A101F" stroke="#1E293B" stroke-width="1.2" />')
        # Top accent header
        svg.append(f'    <path d="M0 8 Q0 0 8 0 L{card_w-8} 0 Q{card_w} 0 {card_w} 8 L{card_w} 12 L0 12 Z" fill="#0F172A" />')
        svg.append(f'    <line x1="0" y1="12" x2="{card_w}" y2="12" stroke="{color}" stroke-width="1.5" opacity="0.8" />')
        
        # Corner reticles
        svg.append(f'    <path d="M4 18 L4 14 L8 14" stroke="{color}" stroke-width="1" fill="none" opacity="0.6" />')
        svg.append(f'    <path d="M{card_w-4} {card_h-6} L{card_w-4} {card_h-2} L{card_w-8} {card_h-2}" stroke="{color}" stroke-width="1" fill="none" opacity="0.6" />')
        
        # Label & Beacon
        svg.append(f'    <circle cx="10" cy="6" r="2.5" fill="{color}" filter="url(#hud-glow)">')
        svg.append(f'      <animate attributeName="opacity" values="1;0.4;1" dur="{2+i*0.5}s" repeatCount="indefinite" />')
        svg.append(f'    </circle>')
        svg.append(f'    <text x="18" y="9" fill="#94A3B8" font-size="8.5" font-weight="700" letter-spacing="0.8">{clean_text(label)}</text>')
        
        # Big Stat Value
        svg.append(f'    <text x="10" y="40" fill="{color}" font-size="16" font-weight="800" letter-spacing="0.5">{clean_text(val)}</text>')
        
        # Subtitle
        svg.append(f'    <text x="10" y="60" fill="#94A3B8" font-size="9.5" font-weight="500">{clean_text(desc)}</text>')
        svg.append(f'  </g>')
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_hud_svg()
