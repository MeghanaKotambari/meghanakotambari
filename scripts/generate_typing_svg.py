import html
import os

def clean_text(text):
    return html.escape(str(text), quote=True)

def generate_typing_svg(output_path="assets/typing.svg"):
    width = 750
    height = 36
    
    lines = [
        "Crafting high-performance web & mobile applications...",
        "Engineering multi-tenant SaaS & AI-driven backends...",
        "Turning complex ideas into scalable production systems ⚡"
    ]
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: transparent; font-family: \'JetBrains Mono\', \'Fira Code\', -apple-system, monospace;">')
    svg.append('  <defs>')
    svg.append('    <style>')
    svg.append('      @keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }')
    svg.append('      .cursor { animation: blink 0.8s infinite; fill: #22D3EE; }')
    svg.append('      .type-text { font-size: 15px; font-weight: 600; fill: #22D3EE; letter-spacing: 0.5px; }')
    svg.append('    </style>')
    svg.append('  </defs>')
    
    # Line 1 (0s -> 4s)
    svg.append(f'  <text x="{width/2}" y="23" text-anchor="middle" class="type-text" opacity="0">')
    svg.append(f'    {clean_text(lines[0])}')
    svg.append(f'    <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.05;0.28;0.33;1" dur="12s" repeatCount="indefinite" />')
    svg.append(f'  </text>')
    
    # Line 2 (4s -> 8s)
    svg.append(f'  <text x="{width/2}" y="23" text-anchor="middle" class="type-text" opacity="0">')
    svg.append(f'    {clean_text(lines[1])}')
    svg.append(f'    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.33;0.38;0.61;0.66;1" dur="12s" repeatCount="indefinite" />')
    svg.append(f'  </text>')
    
    # Line 3 (8s -> 12s)
    svg.append(f'  <text x="{width/2}" y="23" text-anchor="middle" class="type-text" opacity="0">')
    svg.append(f'    {clean_text(lines[2])}')
    svg.append(f'    <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.66;0.71;0.95;1" dur="12s" repeatCount="indefinite" />')
    svg.append(f'  </text>')
    
    svg.append('</svg>')

    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_typing_svg()
