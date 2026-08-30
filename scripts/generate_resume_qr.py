#!/usr/bin/env python3
"""
Futuristic Cyber QR Generator for Meghana Kotambari's Resume
Creates a dark-mode styled SVG QR code with HUD corner brackets, scanning telemetry,
and high contrast for reliable smartphone scanning.
"""

import qrcode
import os

def generate_resume_qr_svg(output_path="assets/resume_qr.svg"):
    resume_url = "https://drive.google.com/file/d/1gV66MqHhcaJzJRVpa-82R1VmVX_wMwPq/view?usp=drivesdk"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(resume_url)
    qr.make(fit=True)
    
    matrix = qr.get_matrix()
    matrix_size = len(matrix)
    
    # We will build a terminal-styled 380x420 SVG
    width = 380
    height = 420
    qr_display_size = 240
    offset_x = (width - qr_display_size) / 2
    offset_y = 90
    cell_size = qr_display_size / matrix_size
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #0A101F; border-radius: 12px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'JetBrains Mono\', monospace;">')
    svg.append('  <defs>')
    svg.append('    <filter id="qr-glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2" result="blur" /><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    svg.append('    <linearGradient id="scan-line-grad" x1="0%" y1="0%" x2="0%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/>')
    svg.append('      <stop offset="50%" stop-color="#10B981" stop-opacity="0.8"/>')
    svg.append('      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>')
    svg.append('    </linearGradient>')
    svg.append('  </defs>')
    
    # Outer frame
    svg.append(f'  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="12" fill="#0A101F" stroke="#1E293B" stroke-width="1.5" />')
    
    # Header bar
    svg.append(f'  <rect x="1" y="1" width="{width-2}" height="36" rx="12" fill="#1E293B" />')
    svg.append(f'  <path d="M1 24 L1 36 L{width-1} 36 L{width-1} 24 Z" fill="#1E293B" />')
    svg.append(f'  <line x1="1" y1="36" x2="{width-1}" y2="36" stroke="#334155" stroke-width="1" />')
    
    # Terminal dots
    svg.append('  <circle cx="18" cy="18" r="4.5" fill="#EF4444" />')
    svg.append('  <circle cx="32" cy="18" r="4.5" fill="#F59E0B" />')
    svg.append('  <circle cx="46" cy="18" r="4.5" fill="#10B981" />')
    svg.append('  <text x="65" y="22" fill="#22D3EE" font-size="11" font-weight="700" letter-spacing="0.5">RESUME.SCAN // CV_TELEMETRY</text>')
    
    # High-contrast white background card for 100% reliable QR scanner camera recognition
    qr_card_padding = 14
    card_x = offset_x - qr_card_padding
    card_y = offset_y - qr_card_padding
    card_size = qr_display_size + qr_card_padding * 2
    svg.append(f'  <rect x="{card_x}" y="{card_y}" width="{card_size}" height="{card_size}" rx="8" fill="#FFFFFF" stroke="#22D3EE" stroke-width="1.5" />')
    
    # Render QR matrix
    for r in range(matrix_size):
        for c in range(matrix_size):
            if matrix[r][c]:
                px = offset_x + c * cell_size
                py = offset_y + r * cell_size
                svg.append(f'  <rect x="{px:.2f}" y="{py:.2f}" width="{cell_size+0.2:.2f}" height="{cell_size+0.2:.2f}" fill="#0A101F" />')
                
    # HUD Corner Reticles (Cyan / Emerald)
    bracket_len = 16
    svg.append(f'  <path d="M{card_x-6} {card_y+bracket_len} L{card_x-6} {card_y-6} L{card_x+bracket_len} {card_y-6}" stroke="#10B981" stroke-width="2.5" fill="none" />')
    svg.append(f'  <path d="M{card_x+card_size+6-bracket_len} {card_y-6} L{card_x+card_size+6} {card_y-6} L{card_x+card_size+6} {card_y+bracket_len}" stroke="#10B981" stroke-width="2.5" fill="none" />')
    svg.append(f'  <path d="M{card_x-6} {card_y+card_size+6-bracket_len} L{card_x-6} {card_y+card_size+6} L{card_x+bracket_len} {card_y+card_size+6}" stroke="#10B981" stroke-width="2.5" fill="none" />')
    svg.append(f'  <path d="M{card_x+card_size+6-bracket_len} {card_y+card_size+6} L{card_x+card_size+6} {card_y+card_size+6} L{card_x+card_size+6} {card_y+card_size+6-bracket_len}" stroke="#10B981" stroke-width="2.5" fill="none" />')
    
    # Animated subtle HUD laser scanner line across the QR card
    svg.append(f'  <rect x="{card_x}" y="{card_y}" width="{card_size}" height="6" fill="url(#scan-line-grad)" opacity="0.8">')
    svg.append(f'    <animate attributeName="y" values="{card_y};{card_y+card_size-6};{card_y}" dur="3.5s" repeatCount="indefinite" />')
    svg.append('  </rect>')
    
    # Bottom Telemetry Instructions
    svg.append(f'  <text x="{width/2}" y="380" fill="#F8FAFC" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="0.5">SCAN WITH CAMERA OR CLICK TO OPEN</text>')
    svg.append(f'  <text x="{width/2}" y="398" fill="#94A3B8" font-size="10.5" font-weight="500" text-anchor="middle">Google Drive Verified // PDF v2026</text>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_resume_qr_svg()
