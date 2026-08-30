#!/usr/bin/env python3
"""
Custom Portrait Processor for Meghana Kotambari's GitHub Profile Hero
Transforms any user headshot into a Floyd-Steinberg 1-bit dithered dot matrix
ready for injection into the SVG hero particle animation.

Usage:
    python scripts/process_portrait.py [path_to_photo.jpg/png]
"""

import sys
import os
import json
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

def process_custom_portrait(image_path, output_width=280, output_height=310):
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return None

    print(f"Processing headshot: {image_path}...")
    img = Image.open(image_path).convert("L") # Greyscale
    
    # Auto-contrast & moderate edge enhancement
    img = ImageOps.autocontrast(img, cutoff=2)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.35)
    
    # Resize keeping aspect ratio & crop head-and-shoulders center
    w, h = img.size
    target_ratio = output_width / output_height
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        # Image is wider: crop sides
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        # Image is taller: crop bottom (keep top/headshots)
        new_h = int(w / target_ratio)
        top = int((h - new_h) * 0.2) # prioritize top 20% head region
        img = img.crop((0, top, w, top + new_h))
        
    img = img.resize((output_width, output_height), Image.Resampling.LANCZOS)
    
    # Floyd-Steinberg dithering with Serpentine scanning
    arr = np.array(img, dtype=float)
    h, w = arr.shape
    dots = []
    
    for y in range(0, h, 2):
        row_range = range(0, w, 2) if (y // 2) % 2 == 0 else range(w - 2, -1, -2)
        for x in row_range:
            old_val = arr[y, x]
            new_val = 255 if old_val > 128 else 0
            err = old_val - new_val
            
            if new_val == 255:
                dots.append((x + 30, y + 60))
                
            # Distribute error
            if x + 1 < w:
                arr[y, x + 1] += err * 7 / 16
            if y + 1 < h:
                if x - 1 >= 0:
                    arr[y + 1, x - 1] += err * 3 / 16
                arr[y + 1, x] += err * 5 / 16
                if x + 1 < w:
                    arr[y + 1, x + 1] += err * 1 / 16

    print(f"Extracted {len(dots)} high-precision portrait vector dots.")
    return dots

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_custom_portrait(sys.argv[1])
    else:
        print("Usage: python scripts/process_portrait.py <path_to_photo>")
