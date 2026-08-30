#!/usr/bin/env python3
"""
Generate High-Tech Typewriter Header for Meghana Kotambari's Profile
Features:
- Main Greeting typing in: "👋 Hey, I'm Meghana Kotambari! 🚀"
- Dynamic Blue Subtitle Line that cycles frequently through 5 high-impact highlights
- Native SVG animation with 100% reliability in GitHub markdown
"""

import os
import html

def clean_text(text):
    return html.escape(str(text), quote=True)

def generate_typing_svg(output_path="assets/typing.svg"):
    width = 800
    height = 96
    
    subtitles = [
        "⚡ Full-Stack & React Native Engineer",
        "🏢 4x Industrial Intern @ IIIT Dharwad & Agencies",
        "🚀 Builder of 40+ Production Web & Mobile Projects",
        "🏆 2x Hackathon Winner & High-Impact Shipper",
        "🤖 Crafting Multi-Tenant SaaS & AI-Driven Backends"
    ]
    
    cycle_dur = 12.5  # 2.5s per line
    n = len(subtitles)
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append('    <style>')
    svg.append('      @keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }')
    svg.append('      .cursor-blink { animation: blink 0.7s infinite; fill: #22D3EE; }')
    svg.append('      .main-title { font-size: 26px; font-weight: 900; fill: #F8FAFC; letter-spacing: 0.5px; }')
    svg.append('      .sub-line { font-size: 16px; font-weight: 700; fill: #22D3EE; letter-spacing: 0.8px; font-family: \'JetBrains Mono\', \'Fira Code\', monospace; }')
    svg.append('    </style>')
    svg.append('  </defs>')
    
    # 1. Main Welcome Header Line
    svg.append(f'  <!-- Main Title: Hey, I\'m Meghana Kotambari! -->')
    svg.append(f'  <g transform="translate({width/2}, 38)">')
    svg.append(f'    <text x="0" y="0" text-anchor="middle" class="main-title">')
    svg.append(f'      👋 Hey, I\'m <tspan fill="#22D3EE">Meghana Kotambari</tspan>! 🚀')
    svg.append(f'    </text>')
    svg.append(f'  </g>')
    
    # 2. Fast-Switching Dynamic Subtitle Lines (cycling every 2.5s)
    svg.append(f'  <!-- Dynamic Blue Cycling Subtitle Lines -->')
    for i, line in enumerate(subtitles):
        t_start = i / n
        t_fade_in = t_start + 0.03
        t_hold = (i + 0.90) / n
        t_fade_out = (i + 0.98) / n
        
        # Build keyTimes and values
        key_times = f"0;{t_start:.3f};{t_fade_in:.3f};{t_hold:.3f};{t_fade_out:.3f};1"
        if i == 0:
            vals = "1;1;1;1;0;0"
            key_times = f"0;{t_start:.3f};{t_fade_in:.3f};{t_hold:.3f};{t_fade_out:.3f};1"
            svg.append(f'  <g transform="translate({width/2}, 76)">')
            svg.append(f'    <text x="0" y="0" text-anchor="middle" class="sub-line" opacity="1">')
            svg.append(f'      {clean_text(line)} <tspan class="cursor-blink">|</tspan>')
            svg.append(f'      <animate attributeName="opacity" values="1;1;1;0;0" keyTimes="0;0.16;0.18;0.20;1" dur="{cycle_dur}s" repeatCount="indefinite" />')
            svg.append(f'    </text>')
            svg.append(f'  </g>')
        else:
            svg.append(f'  <g transform="translate({width/2}, 76)">')
            svg.append(f'    <text x="0" y="0" text-anchor="middle" class="sub-line" opacity="0">')
            svg.append(f'      {clean_text(line)} <tspan class="cursor-blink">|</tspan>')
            svg.append(f'      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{t_start:.2f};{t_fade_in:.2f};{t_hold:.2f};{t_fade_out:.2f};1" dur="{cycle_dur}s" repeatCount="indefinite" />')
            svg.append(f'    </text>')
            svg.append(f'  </g>')
            
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_typing_svg()
