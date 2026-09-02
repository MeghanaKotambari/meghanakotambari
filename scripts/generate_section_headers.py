#!/usr/bin/env python3
"""
Generate High-Contrast Neon Cyber Section Headers for Meghana Kotambari's Profile
Bypasses GitHub HTML style sanitization with crisp, glowing, theme-colored SVG headers.
"""

import os
import html

def generate_header(title_prefix, title_main, subtitle, accent_color, icon_char, output_path):
    width = 940
    height = 54
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background-color: transparent; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append(f'    <filter id="h-glow-{accent_color[1:]}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('  </defs>')
    
    # Background glass pill
    svg.append(f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="8" fill="#0A101F" stroke="#1E293B" stroke-width="1.2" />')
    
    # Left accent beacon bar
    svg.append(f'  <path d="M2 10 Q2 2 10 2 L14 2 L14 {height-2} L10 {height-2} Q2 {height-2} 2 {height-10} Z" fill="{accent_color}" />')
    svg.append(f'  <line x1="14" y1="2" x2="14" y2="{height-2}" stroke="{accent_color}" stroke-width="1.5" />')
    
    # Corner HUD bracket
    svg.append(f'  <path d="M24 12 L32 12 M24 12 L24 20" stroke="{accent_color}" stroke-width="1.2" fill="none" opacity="0.6"/>')
    svg.append(f'  <path d="{width-24} {height-12} L{width-32} {height-12} M{width-24} {height-12} L{width-24} {height-20}" stroke="{accent_color}" stroke-width="1.2" fill="none" opacity="0.6"/>')
    
    # Icon & Title
    svg.append(f'  <text x="36" y="34" fill="{accent_color}" font-size="18" font-weight="900">{icon_char}</text>')
    svg.append(f'  <text x="64" y="34" fill="#F8FAFC" font-size="16" font-weight="800" letter-spacing="1">{html.escape(title_prefix)} <tspan fill="{accent_color}">// {html.escape(title_main)}</tspan></text>')
    
    # Subtitle on right
    svg.append(f'  <text x="{width-36}" y="33" fill="#94A3B8" font-size="11" font-weight="600" text-anchor="end" letter-spacing="0.5">SYS.{html.escape(subtitle)}</text>')
    svg.append(f'  <circle cx="{width-22}" cy="29" r="3" fill="{accent_color}" filter="url(#h-glow-{accent_color[1:]})">')
    svg.append(f'    <animate attributeName="opacity" values="1;0.4;1" dur="2.2s" repeatCount="indefinite" />')
    svg.append(f'  </circle>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")


def main():
    headers = [
        ("ENGINEERING", "BUILDING // SHIPPING", "CORE_PHILOSOPHY", "#22D3EE", "⚡", "assets/headers/header_engineering.svg"),
        ("TELEMETRY", "ACTIVE_DEPLOYMENTS", "LIVE_CONTEXT", "#22D3EE", "📡", "assets/headers/header_telemetry.svg"),
        ("EXPERIENCE", "4_INDUSTRIAL_INTERNSHIPS", "TRACK_RECORD", "#10B981", "💼", "assets/headers/header_experience.svg"),
        ("TECH_STACK", "CAPABILITY_MATRIX", "PRODUCTION_STACK", "#A78BFA", "🛠️", "assets/headers/header_techstack.svg"),
        ("SELECTED_WORK", "PRODUCTION_BUILDS", "FLAGSHIP_PROJECTS", "#38BDF8", "🚀", "assets/headers/header_projects.svg"),
        ("ACHIEVEMENTS", "HACKATHON_RECORDS", "MILESTONES", "#F59E0B", "🏆", "assets/headers/header_achievements.svg"),
        ("CREDENTIALS", "RESUME_SCANNER", "OFFICIAL_CV", "#22D3EE", "📄", "assets/headers/header_resume.svg"),
        ("TELEMETRY", "OBSERVABILITY_METRICS", "GITHUB_STATS", "#22D3EE", "📊", "assets/headers/header_metrics.svg"),
        ("TIMELINE", "CONTRIBUTION_STREAM", "ACTIVITY_MATRIX", "#A78BFA", "🐍", "assets/headers/header_timeline.svg"),
        ("COMM_LINK", "CONNECT", "DISPATCH_CHANNEL", "#22D3EE", "🌐", "assets/headers/header_connect.svg")
    ]
    
    for prefix, main_t, sub, col, icon, path in headers:
        generate_header(prefix, main_t, sub, col, icon, path)

if __name__ == "__main__":
    main()
