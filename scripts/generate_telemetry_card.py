#!/usr/bin/env python3
"""
Generate Pixel-Perfect Dark Cyberpunk GitHub Telemetry & Language Stats Card
Using Meghana Kotambari's real GitHub metrics:
- Total Contributions: 947+
- Active Streak: 241 Days 🔥
- Public Repositories: 17 Repos
- Repository Forks: 0 Forks
- System Runtime: 100% Optimal
- Rank: A+
- Most Used Languages: JavaScript (60.3%), Python (27.0%), CSS (9.7%), HTML (2.4%), PHP (0.6%), Others (< 0.1%)
"""

import os

def generate_telemetry_svg(output_path="profile/telemetry.svg"):
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="876" height="248" viewBox="0 0 876 248" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">Meghana Kotambari GitHub Telemetry &amp; Stats</title>
  <desc id="desc">Futuristic HUD telemetry dashboard showing GitHub statistics and most used languages.</desc>
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="canvasBg" x1="0" y1="0" x2="876" y2="248" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#080C14" />
      <stop offset="100%" stop-color="#0B101C" />
    </linearGradient>
    <linearGradient id="cardBg" x1="0" y1="0" x2="416" y2="216" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#090E1B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>

    <!-- Neon Glow Filters -->
    <filter id="cyanGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="badgeGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur1" />
      <feGaussianBlur stdDeviation="3" result="blur2" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="blur2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Progress Bar Clip Mask for Smooth Pill Shape -->
    <clipPath id="progressBarClip">
      <rect x="0" y="0" width="374" height="11" rx="5.5" />
    </clipPath>

    <style>
      .card-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
        font-size: 16px;
        font-weight: 700;
        fill: #22D3EE;
        letter-spacing: 0.5px;
      }
      .stat-label {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13.5px;
        font-weight: 600;
        fill: #94A3B8;
      }
      .stat-value {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13.5px;
        font-weight: 700;
        fill: #F8FAFC;
      }
      .lang-name {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13px;
        font-weight: 600;
        fill: #E2E8F0;
      }
      .lang-pct {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
        font-size: 12.5px;
        font-weight: 600;
        fill: #94A3B8;
      }
      .rank-grade {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
        font-size: 22px;
        font-weight: 900;
        fill: #00F0FF;
      }
      .rank-sub {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'JetBrains Mono', monospace;
        font-size: 9px;
        font-weight: 800;
        fill: #10B981;
        letter-spacing: 2px;
      }
      .corner-bracket {
        stroke: #22D3EE;
        stroke-width: 1.5;
        fill: none;
        stroke-linecap: square;
      }
      .hud-line {
        stroke: #1E293B;
        stroke-width: 1;
      }
    </style>
  </defs>

  <!-- Canvas Outer Container -->
  <rect width="876" height="248" rx="8" fill="url(#canvasBg)" stroke="#172033" stroke-width="1.2" />

  <!-- ================================================================= -->
  <!-- LEFT CARD: GITHUB TELEMETRY                                       -->
  <!-- ================================================================= -->
  <g transform="translate(16, 16)">
    <!-- Card Base Box -->
    <rect width="416" height="216" rx="6" fill="url(#cardBg)" stroke="#1E293B" stroke-width="1.2" />

    <!-- Corner Reticles / Cyan Brackets -->
    <path class="corner-bracket" d="M 8 18 L 8 8 L 18 8" />
    <path class="corner-bracket" d="M 408 198 L 408 208 L 398 208" />

    <!-- Header Section -->
    <g transform="translate(20, 26)">
      <!-- Lightning Bolt Icon -->
      <path d="M 6 0 L 0 8 L 5 8 L 4 14 L 11 5 L 6 5 Z" fill="#F59E0B" />
      <text x="18" y="11" class="card-title">GitHub Telemetry</text>
    </g>

    <!-- Header Divider Line -->
    <line x1="20" y1="46" x2="396" y2="46" class="hud-line" />

    <!-- Telemetry Stats List (Left Side) -->
    <g transform="translate(20, 58)">
      <!-- Row 1: Total Contributions -->
      <g transform="translate(0, 18)">
        <circle cx="5" cy="5" r="4.5" fill="#22D3EE" opacity="0.95" />
        <text x="18" y="9" class="stat-label">Total Contributions:</text>
        <text x="165" y="9" class="stat-value">947+</text>
      </g>

      <!-- Row 2: Active Streak -->
      <g transform="translate(0, 46)">
        <circle cx="5" cy="5" r="4.5" fill="#10B981" opacity="0.95" />
        <text x="18" y="9" class="stat-label">Active Streak:</text>
        <text x="165" y="9" class="stat-value">241 Days</text>
        <text x="232" y="9" font-size="12">🔥</text>
      </g>

      <!-- Row 3: Public Repositories -->
      <g transform="translate(0, 74)">
        <circle cx="5" cy="5" r="4.5" fill="#22D3EE" opacity="0.95" />
        <text x="18" y="9" class="stat-label">Public Repositories:</text>
        <text x="165" y="9" class="stat-value">17 Repos</text>
      </g>

      <!-- Row 4: Repository Forks -->
      <g transform="translate(0, 102)">
        <circle cx="5" cy="5" r="4.5" fill="#F59E0B" opacity="0.95" />
        <text x="18" y="9" class="stat-label">Repository Forks:</text>
        <text x="165" y="9" class="stat-value">0 Forks</text>
      </g>

      <!-- Row 5: System Runtime -->
      <g transform="translate(0, 130)">
        <circle cx="5" cy="5" r="4.5" fill="#A78BFA" opacity="0.95" />
        <text x="18" y="9" class="stat-label">System Runtime:</text>
        <text x="165" y="9" class="stat-value">100% Optimal</text>
      </g>
    </g>

    <!-- Glowing Circular A+ RANK Badge (Right Side) -->
    <g transform="translate(348, 126)">
      <!-- Outer Cyan Glow Ring -->
      <circle cx="0" cy="0" r="35" fill="none" stroke="#00F0FF" stroke-width="2.8" opacity="0.95" filter="url(#badgeGlow)" />
      
      <!-- Inner Dark Badge Body -->
      <circle cx="0" cy="0" r="33.5" fill="#060C18" stroke="#00F0FF" stroke-width="1.8" />
      
      <!-- Concentric Inner Detail Line -->
      <circle cx="0" cy="0" r="29" fill="none" stroke="#0A2D42" stroke-width="1" stroke-dasharray="2 3" opacity="0.8" />

      <!-- A+ Typography -->
      <text x="0" y="2" text-anchor="middle" class="rank-grade">A+</text>
      
      <!-- RANK Label -->
      <text x="0" y="16" text-anchor="middle" class="rank-sub">RANK</text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- RIGHT CARD: MOST USED LANGUAGES                                   -->
  <!-- ================================================================= -->
  <g transform="translate(444, 16)">
    <!-- Card Base Box -->
    <rect width="416" height="216" rx="6" fill="url(#cardBg)" stroke="#1E293B" stroke-width="1.2" />

    <!-- Corner Reticles / Cyan Brackets -->
    <path class="corner-bracket" d="M 8 18 L 8 8 L 18 8" />
    <path class="corner-bracket" d="M 408 198 L 408 208 L 398 208" />

    <!-- Header Section -->
    <g transform="translate(20, 26)">
      <!-- Crossed Tools / Wrench Icon -->
      <g fill="#22D3EE" opacity="0.9">
        <path d="M12.8 2.2a3.5 3.5 0 0 0-4.6.4l-1.3 1.3 4.2 4.2 1.3-1.3a3.5 3.5 0 0 0 .4-4.6l-1.8 1.8-1.4-.4-.4-1.4 1.6-1.6z" />
        <path d="M6.2 4.6L.4 10.4a1.2 1.2 0 0 0 0 1.7l1.7 1.7a1.2 1.2 0 0 0 1.7 0l5.8-5.8-3.4-3.4z" />
      </g>
      <text x="20" y="11" class="card-title">Most Used Languages</text>
    </g>

    <!-- Header Divider Line -->
    <line x1="20" y1="46" x2="396" y2="46" class="hud-line" />

    <!-- Progress Bar Section -->
    <g transform="translate(20, 60)">
      <!-- Background Track -->
      <rect width="374" height="11" rx="5.5" fill="#151E2E" />

      <!-- Clipped Segmented Color Bar -->
      <g clip-path="url(#progressBarClip)">
        <!-- JavaScript (60.3%) -> 225.5px -->
        <rect x="0" y="0" width="225.5" height="11" fill="#F7DF1E" />
        <!-- Python (27.0%) -> 101.0px -->
        <rect x="225.5" y="0" width="101.0" height="11" fill="#38BDF8" />
        <!-- CSS / Styling (9.7%) -> 36.3px -->
        <rect x="326.5" y="0" width="36.3" height="11" fill="#A855F7" />
        <!-- HTML (2.4%) -> 9.0px -->
        <rect x="362.8" y="0" width="9.0" height="11" fill="#F97316" />
        <!-- PHP / Others (0.6%) -> 2.2px -->
        <rect x="371.8" y="0" width="2.2" height="11" fill="#B45309" />
      </g>
    </g>

    <!-- 2-Column Languages Legend -->
    <g transform="translate(20, 92)">
      <!-- Left Column (3 items) -->
      <g transform="translate(4, 0)">
        <!-- JavaScript -->
        <g transform="translate(0, 12)">
          <circle cx="5" cy="5" r="4.5" fill="#F7DF1E" />
          <text x="18" y="9" class="lang-name">JavaScript</text>
          <text x="126" y="9" class="lang-pct">60.3%</text>
        </g>
        <!-- Python -->
        <g transform="translate(0, 42)">
          <circle cx="5" cy="5" r="4.5" fill="#38BDF8" />
          <text x="18" y="9" class="lang-name">Python</text>
          <text x="126" y="9" class="lang-pct">27.0%</text>
        </g>
        <!-- CSS / Styling -->
        <g transform="translate(0, 72)">
          <circle cx="5" cy="5" r="4.5" fill="#A855F7" />
          <text x="18" y="9" class="lang-name">CSS / Styling</text>
          <text x="126" y="9" class="lang-pct">9.7%</text>
        </g>
      </g>

      <!-- Right Column (3 items) -->
      <g transform="translate(200, 0)">
        <!-- HTML -->
        <g transform="translate(0, 12)">
          <circle cx="5" cy="5" r="4.5" fill="#F97316" />
          <text x="18" y="9" class="lang-name">HTML</text>
          <text x="126" y="9" class="lang-pct">2.4%</text>
        </g>
        <!-- PHP / Backend -->
        <g transform="translate(0, 42)">
          <circle cx="5" cy="5" r="4.5" fill="#B45309" />
          <text x="18" y="9" class="lang-name">PHP</text>
          <text x="126" y="9" class="lang-pct">0.6%</text>
        </g>
        <!-- Others / Solidity -->
        <g transform="translate(0, 72)">
          <circle cx="5" cy="5" r="4.5" fill="#C084FC" />
          <text x="18" y="9" class="lang-name">Others</text>
          <text x="126" y="9" class="lang-pct">&lt; 0.1%</text>
        </g>
      </g>
    </g>
  </g>
</svg>
'''
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_telemetry_svg()
