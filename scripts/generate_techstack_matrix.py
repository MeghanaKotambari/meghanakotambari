#!/usr/bin/env python3
"""
Generate Pixel-Perfect Tech Stack Capability Matrix SVG for Meghana Kotambari
Features:
- Exact layout matching the reference graphic
- 8 category cards with custom badge pills, colored icons, and generous breathing room
- Rotating central Cyber Reactor Core with dual animated HUD rings and pulsing energy glows
- Interactive glowing CSS hover effects on all cards and badge pills
- Tailored specifically to Meghana's tech stack (Docker and SQL removed)
- 100% strict XML compliant for seamless GitHub rendering
"""

import os

def build_svg():
    width = 1180
    height = 800
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" fill="none" role="img" aria-labelledby="title desc">')
    svg.append('  <title id="title">Meghana Kotambari Tech Stack Capability Matrix</title>')
    svg.append('  <desc id="desc">Futuristic cyber telemetry capability matrix with rotating animated core and interactive glowing cards.</desc>')
    
    # ------------------ DEFS & GRADIENTS ------------------
    svg.append('  <defs>')
    svg.append('    <!-- Background Gradients -->')
    svg.append('    <linearGradient id="canvasBg" x1="0" y1="0" x2="1180" y2="800" gradientUnits="userSpaceOnUse">')
    svg.append('      <stop offset="0%" stop-color="#050811" />')
    svg.append('      <stop offset="50%" stop-color="#060B16" />')
    svg.append('      <stop offset="100%" stop-color="#04070D" />')
    svg.append('    </linearGradient>')
    
    svg.append('    <linearGradient id="cardGrad" x1="0" y1="0" x2="1" y2="1">')
    svg.append('      <stop offset="0%" stop-color="#080E1C" stop-opacity="0.95" />')
    svg.append('      <stop offset="100%" stop-color="#060A14" stop-opacity="0.98" />')
    svg.append('    </linearGradient>')

    # Neon Glow Filters
    svg.append('    <filter id="glow-cyan" x="-30%" y="-30%" width="160%" height="160%">')
    svg.append('      <feGaussianBlur stdDeviation="3.5" result="blur" />')
    svg.append('      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg.append('    </filter>')
    svg.append('    <filter id="glow-purple" x="-30%" y="-30%" width="160%" height="160%">')
    svg.append('      <feGaussianBlur stdDeviation="3.5" result="blur" />')
    svg.append('      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg.append('    </filter>')
    svg.append('    <filter id="glow-green" x="-30%" y="-30%" width="160%" height="160%">')
    svg.append('      <feGaussianBlur stdDeviation="3.5" result="blur" />')
    svg.append('      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg.append('    </filter>')
    svg.append('    <filter id="glow-amber" x="-30%" y="-30%" width="160%" height="160%">')
    svg.append('      <feGaussianBlur stdDeviation="3.5" result="blur" />')
    svg.append('      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg.append('    </filter>')
    svg.append('    <filter id="glow-pink" x="-30%" y="-30%" width="160%" height="160%">')
    svg.append('      <feGaussianBlur stdDeviation="3.5" result="blur" />')
    svg.append('      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg.append('    </filter>')
    svg.append('    <filter id="coreGlow" x="-50%" y="-50%" width="200%" height="200%">')
    svg.append('      <feGaussianBlur stdDeviation="8" result="blur1" />')
    svg.append('      <feGaussianBlur stdDeviation="3" result="blur2" />')
    svg.append('      <feMerge><feMergeNode in="blur1"/><feMergeNode in="blur2"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg.append('    </filter>')

    # Interactive CSS Styles with Hover Transitions
    svg.append('    <style>')
    svg.append('      .mono { font-family: \'JetBrains Mono\', Consolas, \'Fira Code\', monospace; }')
    svg.append('      .sans { font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Ubuntu, sans-serif; }')
    svg.append('      .tech-card { cursor: pointer; transition: transform 0.25s ease, filter 0.25s ease; }')
    svg.append('      .tech-card:hover { transform: translateY(-3px); filter: drop-shadow(0 6px 16px rgba(0, 240, 255, 0.2)); }')
    svg.append('      .tech-card:hover rect.card-bg { stroke: #00F0FF !important; fill: #0B1424 !important; }')
    svg.append('      .badge { cursor: pointer; transition: transform 0.2s ease, filter 0.2s ease; }')
    svg.append('      .badge:hover { transform: translateY(-2px); }')
    svg.append('      .badge:hover rect { stroke: #00F0FF !important; fill: #132238 !important; }')
    svg.append('      @keyframes rotateClockwise { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }')
    svg.append('      @keyframes rotateCounter { from { transform: rotate(360deg); } to { transform: rotate(0deg); } }')
    svg.append('      @keyframes pulseCore { 0%, 100% { opacity: 0.9; } 50% { opacity: 1; filter: drop-shadow(0 0 12px #00F0FF); } }')
    svg.append('      .rotating-outer { transform-origin: 590px 430px; animation: rotateClockwise 20s linear infinite; }')
    svg.append('      .rotating-inner { transform-origin: 590px 430px; animation: rotateCounter 28s linear infinite; }')
    svg.append('      .pulse-core { animation: pulseCore 3s ease-in-out infinite; }')
    svg.append('    </style>')
    svg.append('  </defs>')

    # Canvas background & cyber grid / border
    svg.append('  <!-- Canvas & Outer Frame -->')
    svg.append('  <rect width="1180" height="800" rx="10" fill="url(#canvasBg)" stroke="#132338" stroke-width="1.5" />')
    svg.append('  <rect x="8" y="8" width="1164" height="784" rx="8" fill="none" stroke="#0B1828" stroke-width="1" />')

    # ------------------ TOP SECTION HEADER ------------------
    svg.append('  <!-- Top Header Box -->')
    svg.append('  <g transform="translate(18, 16)">')
    svg.append('    <rect width="1144" height="42" rx="5" fill="#080E1A" stroke="#142C44" stroke-width="1" />')
    svg.append('    <text x="16" y="27" class="mono" font-size="16" font-weight="800" fill="#00F0FF" letter-spacing="1">[ TECH_STACK ] <tspan fill="#A855F7">//</tspan> <tspan fill="#C084FC">CAPABILITY_MATRIX</tspan></text>')
    svg.append('    <text x="1108" y="26" text-anchor="end" class="mono" font-size="11" font-weight="700" fill="#64748B" letter-spacing="1">SYS.PRODUCTION_STACK</text>')
    svg.append('    <circle cx="1122" cy="22" r="4.5" fill="#10B981" filter="url(#glow-green)">')
    svg.append('      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite" />')
    svg.append('    </circle>')
    svg.append('  </g>')

    # ------------------ TELEMETRY STATUS BAR ------------------
    svg.append('  <!-- Telemetry Status Bar -->')
    svg.append('  <g transform="translate(18, 66)">')
    svg.append('    <rect width="1144" height="34" rx="5" fill="#060A14" stroke="#0E1E32" stroke-width="1" />')
    svg.append('    <g transform="translate(24, 22)" class="mono" font-size="11" font-weight="700">')
    svg.append('      <text x="0" y="0" fill="#64748B">STACK.STATUS : <tspan fill="#10B981">ACTIVE</tspan></text>')
    svg.append('      <text x="320" y="0" fill="#64748B">CORE.MODULES : <tspan fill="#00F0FF">LOADED</tspan></text>')
    svg.append('      <text x="640" y="0" fill="#64748B">STACK.VERSION : <tspan fill="#A855F7">2.0.1</tspan></text>')
    svg.append('      <text x="960" y="0" fill="#64748B">LAST.UPDATE : <tspan fill="#10B981">NOW</tspan></text>')
    svg.append('    </g>')
    svg.append('  </g>')

    # ------------------ CIRCUIT BUS LINES (BEHIND CARDS) ------------------
    svg.append('  <!-- Connecting Circuit Bus Lines -->')
    cx, cy = 590, 430
    
    # Left Bus Lines
    svg.append('  <g opacity="0.85">')
    svg.append('    <path d="M 400 195 L 490 195 L 515 285 L 530 330" fill="none" stroke="#00F0FF" stroke-width="1.4" stroke-dasharray="3 3" opacity="0.6"/>')
    svg.append('    <path d="M 400 195 L 485 195 L 525 350" fill="none" stroke="#00F0FF" stroke-width="1.8" />')
    svg.append('    <circle cx="400" cy="195" r="3.5" fill="#00F0FF" filter="url(#glow-cyan)" />')
    svg.append('    <circle cx="500" cy="290" r="3" fill="#00F0FF" />')
    
    svg.append('    <path d="M 400 370 L 485 370 L 510 405" fill="none" stroke="#A855F7" stroke-width="1.8" />')
    svg.append('    <circle cx="400" cy="370" r="3.5" fill="#A855F7" filter="url(#glow-purple)" />')
    svg.append('    <circle cx="485" cy="370" r="3" fill="#A855F7" />')

    svg.append('    <path d="M 400 520 L 485 520 L 510 455" fill="none" stroke="#10B981" stroke-width="1.8" />')
    svg.append('    <circle cx="400" cy="520" r="3.5" fill="#10B981" filter="url(#glow-green)" />')
    svg.append('    <circle cx="485" cy="520" r="3" fill="#10B981" />')

    svg.append('    <path d="M 400 635 L 485 635 L 530 520" fill="none" stroke="#0284C7" stroke-width="1.8" />')
    svg.append('    <circle cx="400" cy="635" r="3.5" fill="#0284C7" filter="url(#glow-cyan)" />')
    svg.append('    <circle cx="485" cy="635" r="3" fill="#0284C7" />')

    # Right Bus Lines
    svg.append('    <path d="M 780 195 L 695 195 L 655 350" fill="none" stroke="#F59E0B" stroke-width="1.8" />')
    svg.append('    <circle cx="780" cy="195" r="3.5" fill="#F59E0B" filter="url(#glow-amber)" />')
    svg.append('    <circle cx="680" cy="290" r="3" fill="#F59E0B" />')

    svg.append('    <path d="M 780 370 L 695 370 L 670 405" fill="none" stroke="#00F0FF" stroke-width="1.8" />')
    svg.append('    <circle cx="780" cy="370" r="3.5" fill="#00F0FF" filter="url(#glow-cyan)" />')
    svg.append('    <circle cx="695" cy="370" r="3" fill="#00F0FF" />')

    svg.append('    <path d="M 780 520 L 695 520 L 670 455" fill="none" stroke="#A855F7" stroke-width="1.8" />')
    svg.append('    <circle cx="780" cy="520" r="3.5" fill="#A855F7" filter="url(#glow-purple)" />')
    svg.append('    <circle cx="695" cy="520" r="3" fill="#A855F7" />')

    svg.append('    <path d="M 780 635 L 695 635 L 650 520" fill="none" stroke="#EC4899" stroke-width="1.8" />')
    svg.append('    <circle cx="780" cy="635" r="3.5" fill="#EC4899" filter="url(#glow-pink)" />')
    svg.append('    <circle cx="695" cy="635" r="3" fill="#EC4899" />')
    svg.append('  </g>')

    # ------------------ ROTATING ANIMATED CYBER REACTOR CORE ------------------
    svg.append('  <!-- Central Cyber Reactor Core (Animated & Rotating) -->')
    
    # Outer Rotating Dashed HUD Ring
    svg.append('  <g class="rotating-inner">')
    svg.append(f'    <circle cx="{cx}" cy="{cy}" r="114" fill="none" stroke="#0E2840" stroke-width="1.5" stroke-dasharray="6 8" opacity="0.7" />')
    svg.append(f'    <circle cx="{cx}" cy="{cy}" r="102" fill="none" stroke="#133654" stroke-width="1.2" stroke-dasharray="14 10" />')
    svg.append('  </g>')

    # Rotating Segment Arcs (Clockwise)
    svg.append('  <g class="rotating-outer">')
    svg.append(f'    <g transform="translate({cx}, {cy})">')
    # 4 Glowing Rotating Segment Arcs
    svg.append('      <path d="M 0 -92 A 92 92 0 0 1 80 -46" fill="none" stroke="#00F0FF" stroke-width="5.5" stroke-linecap="round" filter="url(#glow-cyan)" />')
    svg.append('      <path d="M 80 46 A 92 92 0 0 1 0 92" fill="none" stroke="#A855F7" stroke-width="5.5" stroke-linecap="round" filter="url(#glow-purple)" />')
    svg.append('      <path d="M 0 92 A 92 92 0 0 1 -80 46" fill="none" stroke="#00F0FF" stroke-width="5.5" stroke-linecap="round" filter="url(#glow-cyan)" />')
    svg.append('      <path d="M -80 -46 A 92 92 0 0 1 0 -92" fill="none" stroke="#38BDF8" stroke-width="5.5" stroke-linecap="round" filter="url(#glow-cyan)" />')
    # Orbiting Beacon Dots
    svg.append('      <circle cx="80" cy="-46" r="3" fill="#FFF" />')
    svg.append('      <circle cx="0" cy="92" r="3" fill="#FFF" />')
    svg.append('      <circle cx="-80" cy="46" r="3" fill="#FFF" />')
    svg.append('      <circle cx="0" cy="-92" r="3" fill="#FFF" />')
    svg.append('    </g>')
    svg.append('  </g>')

    # Core Center Base & Glowing Reactor
    svg.append(f'  <g transform="translate({cx}, {cy})" class="pulse-core">')
    svg.append('    <circle cx="0" cy="0" r="92" fill="#050B16" stroke="#102538" stroke-width="2" />')
    
    # Reticle Triangles
    svg.append('    <polygon points="0,-102 -5,-110 5,-110" fill="#00F0FF" />')
    svg.append('    <polygon points="0,102 -5,110 5,110" fill="#00F0FF" />')
    svg.append('    <polygon points="-102,0 -110,-5 -110,5" fill="#00F0FF" />')
    svg.append('    <polygon points="102,0 110,-5 110,5" fill="#00F0FF" />')

    # Inner Core
    svg.append('    <circle cx="0" cy="0" r="76" fill="#040812" stroke="#0F2B44" stroke-width="1.8" />')
    svg.append('    <circle cx="0" cy="0" r="68" fill="none" stroke="#0D1E30" stroke-width="1" stroke-dasharray="4 4" />')
    
    # Reactor Typography
    svg.append('    <text x="0" y="-18" text-anchor="middle" class="mono" font-size="14.5" font-weight="900" fill="#00F0FF" letter-spacing="1">FULL STACK</text>')
    svg.append('    <text x="0" y="2" text-anchor="middle" class="mono" font-size="14.5" font-weight="900" fill="#00F0FF" letter-spacing="1">DEVELOPER</text>')
    svg.append('    <text x="0" y="22" text-anchor="middle" class="mono" font-size="15" font-weight="800" fill="#38BDF8">&lt;/&gt;</text>')
    svg.append('    <text x="0" y="44" text-anchor="middle" class="mono" font-size="8.5" font-weight="800" fill="#00F0FF" letter-spacing="1.5">BUILD • SHIP • SCALE</text>')
    svg.append('  </g>')

    # ------------------ HELPER FUNCTIONS FOR CARDS & BADGES ------------------
    def draw_badge(bx, by, label, icon_type=None, custom_color=None, width_override=None, height_override=25):
        bw = width_override or (len(label) * 8 + 36)
        bh = height_override
        
        svg.append(f'      <g class="badge" transform="translate({bx}, {by})">')
        svg.append(f'        <rect width="{bw}" height="{bh}" rx="4" fill="#0C1524" stroke="#1A2D44" stroke-width="1" />')
        
        ix, iy = 7, 4.5
        if icon_type == "js":
            svg.append(f'        <rect x="{ix}" y="{iy}" width="16" height="16" rx="2" fill="#F7DF1E" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="sans" font-size="9" font-weight="900" fill="#000">JS</text>')
        elif icon_type == "ts":
            svg.append(f'        <rect x="{ix}" y="{iy}" width="16" height="16" rx="2" fill="#3178C6" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="sans" font-size="9" font-weight="900" fill="#FFF">TS</text>')
        elif icon_type == "python":
            svg.append(f'        <path d="M{ix+8} {iy+1} c-3 0 -5 1 -5 3 v2 h5 v1 h-7 c-2 0 -3 2 -3 4 s1 4 3 4 h1 v-2 c0 -2 2 -3 4 -3 h5 c2 0 3 -1 3 -3 v-3 c0 -2 -2 -3 -6 -3 z" fill="#38BDF8"/>')
            svg.append(f'        <path d="M{ix+8} {iy+15} c3 0 5 -1 5 -3 v-2 h-5 v-1 h7 c2 0 3 -2 3 -4 s-1 -4 -3 -4 h-1 v2 c0 2 -2 3 -4 3 h-5 c-2 0 -3 1 -3 3 v3 c0 2 2 3 6 3 z" fill="#FACC15"/>')
        elif icon_type == "html5":
            svg.append(f'        <rect x="{ix}" y="{iy}" width="16" height="16" rx="2" fill="#E44D26" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="sans" font-size="9" font-weight="900" fill="#FFF">5</text>')
        elif icon_type == "css3":
            svg.append(f'        <rect x="{ix}" y="{iy}" width="16" height="16" rx="2" fill="#264DE4" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="sans" font-size="9" font-weight="900" fill="#FFF">3</text>')
        elif icon_type == "react":
            svg.append(f'        <ellipse cx="{ix+8}" cy="{iy+8}" rx="7" ry="2.5" fill="none" stroke="#61DAFB" stroke-width="1" transform="rotate(30 {ix+8} {iy+8})" />')
            svg.append(f'        <ellipse cx="{ix+8}" cy="{iy+8}" rx="7" ry="2.5" fill="none" stroke="#61DAFB" stroke-width="1" transform="rotate(90 {ix+8} {iy+8})" />')
            svg.append(f'        <ellipse cx="{ix+8}" cy="{iy+8}" rx="7" ry="2.5" fill="none" stroke="#61DAFB" stroke-width="1" transform="rotate(150 {ix+8} {iy+8})" />')
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="1.5" fill="#61DAFB" />')
        elif icon_type == "nextjs":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="8" fill="#000" stroke="#475569" stroke-width="0.8" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="sans" font-size="10" font-weight="900" fill="#FFF">N</text>')
        elif icon_type == "tailwind":
            svg.append(f'        <path d="M{ix+2} {iy+8} Q{ix+5} {iy+4} {ix+8} {iy+7} T{ix+14} {iy+6} Q{ix+11} {iy+10} {ix+8} {iy+9} T{ix+2} {iy+8} Z" fill="#38BDF8" />')
        elif icon_type == "shadcn":
            svg.append(f'        <line x1="{ix+3}" y1="{iy+12}" x2="{ix+8}" y2="{iy+4}" stroke="#FFF" stroke-width="1.8" />')
            svg.append(f'        <line x1="{ix+8}" y1="{iy+12}" x2="{ix+13}" y2="{iy+4}" stroke="#FFF" stroke-width="1.8" />')
        elif icon_type == "redux":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="6" fill="none" stroke="#764ABC" stroke-width="1.8" />')
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="2" fill="#764ABC" />')
        elif icon_type == "framer":
            svg.append(f'        <path d="M{ix+4} {iy+3} h8 l-4 5 h4 l-8 8 v-8 h4 z" fill="#0055FF" />')
        elif icon_type == "nodejs":
            svg.append(f'        <polygon points="{ix+8},{iy+2} {ix+14},{iy+5} {ix+14},{iy+12} {ix+8},{iy+15} {ix+2},{iy+12} {ix+2},{iy+5}" fill="#68A063" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+11.5}" text-anchor="middle" class="sans" font-size="8" font-weight="900" fill="#FFF">N</text>')
        elif icon_type == "express":
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="mono" font-size="9" font-weight="900" fill="#CBD5E1">ex</text>')
        elif icon_type == "rest":
            svg.append(f'        <text x="{ix+8}" y="{iy+12}" text-anchor="middle" class="mono" font-size="9" font-weight="900" fill="#22D3EE">{{}}</text>')
        elif icon_type == "jwt":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="6" fill="#D63AFF" opacity="0.3"/>')
            svg.append(f'        <path d="M{ix+8} {iy+3} L{ix+9.5} {iy+6.5} L{ix+13} {iy+8} L{ix+9.5} {iy+9.5} L{ix+8} {iy+13} L{ix+6.5} {iy+9.5} L{ix+3} {iy+8} L{ix+6.5} {iy+6.5} Z" fill="#D63AFF"/>')
        elif icon_type == "rbac":
            svg.append(f'        <path d="M{ix+8} {iy+2} L{ix+14} {iy+5} V{iy+10} Q{ix+8} {iy+15} {ix+8} {iy+15} Q{ix+2} {iy+10} {ix+2} {iy+5} Z" fill="#10B981" />')
            svg.append(f'        <path d="M{ix+5} {iy+8} L{ix+7} {iy+10} L{ix+11} {iy+6}" fill="none" stroke="#FFF" stroke-width="1.2" />')
        elif icon_type == "ai":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="6" fill="#8B5CF6" opacity="0.2"/>')
            svg.append(f'        <path d="M{ix+8} {iy+2} Q{ix+8} {iy+8} {ix+14} {iy+8} Q{ix+8} {iy+8} {ix+8} {iy+14} Q{ix+8} {iy+8} {ix+2} {iy+8} Q{ix+8} {iy+8} {ix+8} {iy+2} Z" fill="#A78BFA" />')
        elif icon_type == "mongodb":
            svg.append(f'        <path d="M{ix+8} {iy+2} C{ix+4} {iy+7} {ix+4} {iy+11} {ix+8} {iy+14} C{ix+12} {iy+11} {ix+12} {iy+7} {ix+8} {iy+2} Z" fill="#13AA52" />')
        elif icon_type == "mongoose":
            svg.append(f'        <rect x="{ix+2}" y="{iy+3}" width="12" height="10" rx="2" fill="#880000" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+11}" text-anchor="middle" class="sans" font-size="8" font-weight="900" fill="#FFF">M</text>')
        elif icon_type == "aws":
            svg.append(f'        <text x="{ix+8}" y="{iy+10}" text-anchor="middle" class="sans" font-size="7" font-weight="900" fill="#FF9900">AWS</text>')
            svg.append(f'        <path d="M{ix+3} {iy+12} Q{ix+8} {iy+14} {ix+13} {iy+12}" fill="none" stroke="#FF9900" stroke-width="1" />')
        elif icon_type == "cloudinary":
            svg.append(f'        <path d="M{ix+4} {iy+10} a3 3 0 0 1 3 -4 a4 4 0 0 1 5 1 a3 3 0 0 1 2 3 z" fill="#3448C5" />')
        elif icon_type == "git":
            svg.append(f'        <rect x="{ix+3}" y="{iy+3}" width="10" height="10" rx="2" fill="#F05032" transform="rotate(45 {ix+8} {iy+8})" />')
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="2" fill="#FFF" />')
        elif icon_type == "github":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="7" fill="#24292E" stroke="#6E7681" stroke-width="0.8" />')
            svg.append(f'        <path d="M{ix+5} {iy+10} c0 -2 1.5 -3 3 -3 s3 1 3 3 z" fill="#FFF" />')
        elif icon_type == "postman":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="7" fill="#FF6C37" />')
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="2.5" fill="#FFF" />')
        elif icon_type == "cicd":
            svg.append(f'        <circle cx="{ix+5}" cy="{iy+8}" r="3.5" fill="none" stroke="#00F0FF" stroke-width="1.4" />')
            svg.append(f'        <circle cx="{ix+11}" cy="{iy+8}" r="3.5" fill="none" stroke="#00F0FF" stroke-width="1.4" />')
        elif icon_type == "razorpay":
            svg.append(f'        <path d="M{ix+6} {iy+2} L{ix+12} {iy+2} L{ix+9} {iy+8} L{ix+12} {iy+8} L{ix+4} {iy+14} L{ix+7} {iy+7} L{ix+5} {iy+7} Z" fill="#0C2340" stroke="#3395FF" stroke-width="0.8"/>')
        elif icon_type == "stripe":
            svg.append(f'        <rect x="{ix+2}" y="{iy+3}" width="12" height="10" rx="2" fill="#635BFF" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+11}" text-anchor="middle" class="sans" font-size="8" font-weight="900" fill="#FFF">S</text>')
        elif icon_type == "pwa":
            svg.append(f'        <rect x="{ix+1}" y="{iy+3}" width="14" height="10" rx="2" fill="#5A0FC8" />')
            svg.append(f'        <text x="{ix+8}" y="{iy+10.5}" text-anchor="middle" class="mono" font-size="6.5" font-weight="900" fill="#FFF">PWA</text>')
        elif icon_type == "vscode":
            svg.append(f'        <path d="M{ix+11} {iy+2} L{ix+14} {iy+4} V{iy+12} L{ix+11} {iy+14} L{ix+6} {iy+10} L{ix+3} {iy+12} L{ix+1} {iy+11} V{iy+5} L{ix+3} {iy+4} L{ix+6} {iy+6} Z" fill="#007ACC" />')
        elif icon_type == "uiux":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="6" fill="none" stroke="#EC4899" stroke-width="1.4"/>')
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="2" fill="#EC4899"/>')
        elif icon_type == "problem":
            svg.append(f'        <polygon points="{ix+8},{iy+2} {ix+13},{iy+6} {ix+13},{iy+12} {ix+8},{iy+14} {ix+3},{iy+12} {ix+3},{iy+6}" fill="none" stroke="#EC4899" stroke-width="1.3" />')
        elif icon_type == "learning":
            svg.append(f'        <path d="M{ix+3} {iy+4} h10 v8 h-10 z" fill="none" stroke="#EC4899" stroke-width="1.2" />')
            svg.append(f'        <line x1="{ix+8}" y1="{iy+4}" x2="{ix+8}" y2="{iy+12}" stroke="#EC4899" stroke-width="1" />')
        elif icon_type == "opensource":
            svg.append(f'        <circle cx="{ix+8}" cy="{iy+8}" r="6" fill="none" stroke="#EC4899" stroke-width="1.3" stroke-dasharray="8 3" />')
        elif icon_type == "dot":
            # Styled tech dot badge
            svg.append(f'        <circle cx="{ix+5}" cy="{iy+8}" r="3" fill="{custom_color or "#00F0FF"}" opacity="0.9" />')
            ix = ix - 2
        else:
            svg.append(f'        <circle cx="{ix+5}" cy="{iy+8}" r="2.5" fill="{custom_color or "#38BDF8"}" />')
            ix = ix - 4

        text_x = ix + 21 if icon_type else ix + 14
        svg.append(f'        <text x="{text_x}" y="16.5" class="sans" font-size="11.5" font-weight="600" fill="#E2E8F0">{label}</text>')
        svg.append('      </g>')

    # ------------------ 8 SECTION CARDS ------------------
    # Card 01: LANGUAGES (Top Left)
    svg.append('  <!-- Card 01: LANGUAGES -->')
    svg.append('  <g class="tech-card" transform="translate(18, 114)">')
    svg.append('    <rect class="card-bg" width="365" height="134" rx="6" fill="url(#cardGrad)" stroke="#0E4A63" stroke-width="1.2" />')
    svg.append('    <polygon points="36,18 52,27 52,45 36,54 20,45 20,27" fill="#081826" stroke="#00F0FF" stroke-width="1.3" />')
    svg.append('    <text x="36" y="40" text-anchor="middle" class="mono" font-size="11" font-weight="900" fill="#00F0FF">&lt;/&gt;</text>')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#00F0FF" letter-spacing="0.5">01. LANGUAGES</text>')
    draw_badge(66, 52, "JavaScript", "js", width_override=94)
    draw_badge(166, 52, "TypeScript", "ts", width_override=94)
    draw_badge(266, 52, "Python", "python", width_override=82)
    draw_badge(66, 86, "HTML5", "html5", width_override=78)
    draw_badge(150, 86, "CSS3", "css3", width_override=76)
    svg.append('  </g>')

    # Card 02: FRONTEND & MOBILE (Mid-Upper Left)
    svg.append('  <!-- Card 02: FRONTEND & MOBILE -->')
    svg.append('  <g class="tech-card" transform="translate(18, 258)">')
    svg.append('    <rect class="card-bg" width="365" height="152" rx="6" fill="url(#cardGrad)" stroke="#4C1D95" stroke-width="1.2" />')
    svg.append('    <rect x="20" y="20" width="32" height="32" rx="5" fill="#130E26" stroke="#A855F7" stroke-width="1.3" />')
    svg.append('    <rect x="25" y="25" width="14" height="18" rx="2" fill="none" stroke="#C084FC" stroke-width="1" />')
    svg.append('    <rect x="37" y="31" width="10" height="16" rx="2" fill="none" stroke="#C084FC" stroke-width="1" />')
    svg.append('    <text x="66" y="40" class="mono" font-size="13.5" font-weight="800" fill="#C084FC" letter-spacing="0.5">02. FRONTEND &amp; MOBILE</text>')
    draw_badge(66, 54, "React.js", "react", width_override=82)
    draw_badge(154, 54, "Next.js", "nextjs", width_override=78)
    draw_badge(238, 54, "React Native", "react", width_override=112)
    draw_badge(66, 86, "Tailwind CSS", "tailwind", width_override=106)
    draw_badge(178, 86, "Shadcn UI", "shadcn", width_override=94)
    draw_badge(66, 118, "Redux Toolkit", "redux", width_override=110)
    draw_badge(182, 118, "Framer Motion", "framer", width_override=116)
    svg.append('  </g>')

    # Card 03: BACKEND & SYSTEMS (Mid-Lower Left)
    svg.append('  <!-- Card 03: BACKEND & SYSTEMS -->')
    svg.append('  <g class="tech-card" transform="translate(18, 420)">')
    svg.append('    <rect class="card-bg" width="365" height="126" rx="6" fill="url(#cardGrad)" stroke="#065F46" stroke-width="1.2" />')
    svg.append('    <polygon points="36,18 52,27 52,45 36,54 20,45 20,27" fill="#082018" stroke="#10B981" stroke-width="1.3" />')
    svg.append('    <rect x="27" y="28" width="18" height="6" rx="1" fill="none" stroke="#10B981" stroke-width="1" />')
    svg.append('    <rect x="27" y="38" width="18" height="6" rx="1" fill="none" stroke="#10B981" stroke-width="1" />')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#10B981" letter-spacing="0.5">03. BACKEND &amp; SYSTEMS</text>')
    draw_badge(66, 52, "Node.js", "nodejs", width_override=82)
    draw_badge(154, 52, "Express.js", "express", width_override=92)
    draw_badge(252, 52, "RESTful APIs", "rest", width_override=100)
    draw_badge(66, 86, "JWT", "jwt", width_override=64)
    draw_badge(136, 86, "RBAC", "rbac", width_override=74)
    draw_badge(216, 86, "AI Integration", "ai", width_override=112)
    svg.append('  </g>')

    # Card 04: DATABASE & CLOUD (Bottom Left)
    svg.append('  <!-- Card 04: DATABASE & CLOUD -->')
    svg.append('  <g class="tech-card" transform="translate(18, 556)">')
    svg.append('    <rect class="card-bg" width="365" height="126" rx="6" fill="url(#cardGrad)" stroke="#0369A1" stroke-width="1.2" />')
    svg.append('    <polygon points="36,18 52,27 52,45 36,54 20,45 20,27" fill="#081C2E" stroke="#0284C7" stroke-width="1.3" />')
    svg.append('    <path d="M28 38 a4 4 0 0 1 4 -4 a5 5 0 0 1 7 1 a4 4 0 0 1 3 3 z" fill="none" stroke="#00F0FF" stroke-width="1.2" />')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#38BDF8" letter-spacing="0.5">04. DATABASE &amp; CLOUD</text>')
    draw_badge(66, 52, "MongoDB", "mongodb", width_override=94)
    draw_badge(166, 52, "Mongoose", "mongoose", width_override=96)
    draw_badge(66, 86, "AWS", "aws", width_override=74)
    draw_badge(146, 86, "Cloudinary", "cloudinary", width_override=96)
    svg.append('  </g>')

    # Card 05: TOOLS & DEVOPS (Top Right)
    svg.append('  <!-- Card 05: TOOLS & DEVOPS -->')
    svg.append('  <g class="tech-card" transform="translate(797, 114)">')
    svg.append('    <rect class="card-bg" width="365" height="152" rx="6" fill="url(#cardGrad)" stroke="#B45309" stroke-width="1.2" />')
    svg.append('    <polygon points="36,18 52,27 52,45 36,54 20,45 20,27" fill="#241406" stroke="#F59E0B" stroke-width="1.3" />')
    svg.append('    <circle cx="36" cy="36" r="6" fill="none" stroke="#F59E0B" stroke-width="1.8" />')
    svg.append('    <path d="M36 26 v3 M36 43 v3 M26 36 h3 M43 36 h3" stroke="#F59E0B" stroke-width="1.8" />')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#F59E0B" letter-spacing="0.5">05. TOOLS &amp; DEVOPS</text>')
    draw_badge(66, 54, "Git", "git", width_override=66)
    draw_badge(138, 54, "GitHub", "github", width_override=82)
    draw_badge(226, 54, "Postman", "postman", width_override=88)
    draw_badge(66, 86, "CI/CD", "cicd", width_override=78)
    draw_badge(150, 86, "Razorpay", "razorpay", width_override=94)
    draw_badge(250, 86, "Stripe", "stripe", width_override=78)
    draw_badge(66, 118, "PWA", "pwa", width_override=70)
    draw_badge(142, 118, "VS Code", "vscode", width_override=92)
    svg.append('  </g>')

    # Card 06: ARCHITECTURE & CONCEPTS (Mid-Upper Right) - Enhanced with proper vertical & horizontal spacing
    svg.append('  <!-- Card 06: ARCHITECTURE & CONCEPTS -->')
    svg.append('  <g class="tech-card" transform="translate(797, 276)">')
    svg.append('    <rect class="card-bg" width="365" height="134" rx="6" fill="url(#cardGrad)" stroke="#0E4A63" stroke-width="1.2" />')
    svg.append('    <rect x="20" y="20" width="32" height="32" rx="5" fill="#081826" stroke="#00F0FF" stroke-width="1.3" />')
    svg.append('    <rect x="32" y="25" width="8" height="6" rx="1" fill="none" stroke="#00F0FF" stroke-width="1" />')
    svg.append('    <rect x="24" y="38" width="8" height="6" rx="1" fill="none" stroke="#00F0FF" stroke-width="1" />')
    svg.append('    <rect x="40" y="38" width="8" height="6" rx="1" fill="none" stroke="#00F0FF" stroke-width="1" />')
    svg.append('    <path d="M36 31 v4 M28 35 h16" stroke="#00F0FF" stroke-width="1" />')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#00F0FF" letter-spacing="0.5">06. ARCHITECTURE &amp; CONCEPTS</text>')
    # Generously spaced rows (y=50, 78, 106) with 24px badge height for a clean 4px vertical margin
    draw_badge(66, 50, "Microservices", "dot", custom_color="#00F0FF", width_override=104, height_override=24)
    draw_badge(176, 50, "System Design", "dot", custom_color="#00F0FF", width_override=108, height_override=24)
    draw_badge(66, 77, "REST", "dot", custom_color="#00F0FF", width_override=60, height_override=24)
    draw_badge(132, 77, "API Design", "dot", custom_color="#00F0FF", width_override=88, height_override=24)
    draw_badge(226, 77, "MVC", "dot", custom_color="#00F0FF", width_override=58, height_override=24)
    draw_badge(66, 104, "Agile", "dot", custom_color="#00F0FF", width_override=64, height_override=24)
    draw_badge(136, 104, "SDLC", "dot", custom_color="#00F0FF", width_override=64, height_override=24)
    draw_badge(206, 104, "OOPs", "dot", custom_color="#00F0FF", width_override=66, height_override=24)
    svg.append('  </g>')

    # Card 07: CORE COMPUTER SCIENCE (Mid-Lower Right) - Enhanced with proper vertical & horizontal spacing
    svg.append('  <!-- Card 07: CORE COMPUTER SCIENCE -->')
    svg.append('  <g class="tech-card" transform="translate(797, 420)">')
    svg.append('    <rect class="card-bg" width="365" height="126" rx="6" fill="url(#cardGrad)" stroke="#4C1D95" stroke-width="1.2" />')
    svg.append('    <rect x="20" y="20" width="32" height="32" rx="5" fill="#140D26" stroke="#A855F7" stroke-width="1.3" />')
    svg.append('    <rect x="27" y="27" width="18" height="18" rx="2" fill="none" stroke="#A855F7" stroke-width="1.2" />')
    svg.append('    <rect x="31" y="31" width="10" height="10" fill="#A855F7" opacity="0.4" />')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#C084FC" letter-spacing="0.5">07. CORE COMPUTER SCIENCE</text>')
    draw_badge(66, 52, "DSA", "dot", custom_color="#A855F7", width_override=58)
    draw_badge(130, 52, "DBMS", "dot", custom_color="#A855F7", width_override=68)
    draw_badge(204, 52, "OS", "dot", custom_color="#A855F7", width_override=52)
    draw_badge(66, 86, "CN", "dot", custom_color="#A855F7", width_override=52)
    draw_badge(124, 86, "OOPS", "dot", custom_color="#A855F7", width_override=62)
    draw_badge(192, 86, "Computer Networks", "dot", custom_color="#A855F7", width_override=130)
    svg.append('  </g>')

    # Card 08: SPECIAL INTERESTS (Bottom Right)
    svg.append('  <!-- Card 08: SPECIAL INTERESTS -->')
    svg.append('  <g class="tech-card" transform="translate(797, 556)">')
    svg.append('    <rect class="card-bg" width="365" height="126" rx="6" fill="url(#cardGrad)" stroke="#831843" stroke-width="1.2" />')
    svg.append('    <polygon points="36,18 52,27 52,45 36,54 20,45 20,27" fill="#240A18" stroke="#EC4899" stroke-width="1.3" />')
    svg.append('    <path d="M36 44 L30 38 A4 4 0 0 1 36 32 A4 4 0 0 1 42 38 Z" fill="none" stroke="#F472B6" stroke-width="1.3" />')
    svg.append('    <text x="66" y="38" class="mono" font-size="13.5" font-weight="800" fill="#F472B6" letter-spacing="0.5">08. SPECIAL INTERESTS</text>')
    draw_badge(66, 52, "UI/UX Design", "uiux", width_override=112)
    draw_badge(184, 52, "Problem Solving", "problem", width_override=126)
    draw_badge(66, 86, "Learning", "learning", width_override=92)
    draw_badge(164, 86, "Open Source", "opensource", width_override=106)
    svg.append('  </g>')

    # ------------------ BOTTOM TERMINAL DISPATCH FOOTER ------------------
    svg.append('  <!-- Bottom Terminal Dispatch Footer -->')
    svg.append('  <g transform="translate(18, 700)">')
    svg.append('    <rect width="1144" height="42" rx="5" fill="#060A14" stroke="#0E2034" stroke-width="1" />')
    svg.append('    <rect x="12" y="10" width="30" height="22" rx="3" fill="#0A1626" stroke="#10B981" stroke-width="1" />')
    svg.append('    <text x="27" y="25" text-anchor="middle" class="mono" font-size="12" font-weight="900" fill="#10B981">&gt;_</text>')
    svg.append('    <text x="54" y="26" class="mono" font-size="12" font-weight="700" fill="#10B981">echo <tspan fill="#38BDF8">"Building scalable solutions with clean code &amp; great UX"</tspan></text>')
    svg.append('    <text x="1090" y="26" text-anchor="end" class="mono" font-size="11" font-weight="700" fill="#64748B">STATUS: <tspan fill="#10B981">DEPLOYED SUCCESSFULLY</tspan> | </text>')
    svg.append('    <text x="1108" y="27" font-size="14">🚀</text>')
    svg.append('  </g>')

    svg.append('</svg>')
    
    return "\n".join(svg)

def main(output_path="assets/techstack_matrix.svg"):
    content = build_svg()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
