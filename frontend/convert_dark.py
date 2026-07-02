import os
import re

src_dir = os.path.join(os.path.dirname(__file__), 'src')

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove :root definitions in vue files to rely on global theme
    if ':root {' in content:
        content = re.sub(r':root\s*\{[^}]+\}', '', content, flags=re.MULTILINE)
    
    # Color replacements mapping
    # Note: re.sub replacements are sequential, so order matters.
    replacements = [
        # Hardcoded gradients
        (r'background:\s*linear-gradient\([^)]+#FFFFFF[^)]+\);', r'background: var(--surface);'),
        (r'background:\s*linear-gradient\([^)]+#000000[^)]+\);', r'background: linear-gradient(90deg, var(--accent) 0%, var(--accent-hover) 100%);'),
        (r'background:\s*linear-gradient\([^)]+#FFF7ED[^)]+\);', r'background: var(--surface-hover);'),
        
        # Backgrounds
        (r'background(?:-color)?:\s*#FFF(?:FFF)?\b', r'background: var(--surface)'),
        (r'background(?:-color)?:\s*#000(?:000)?\b', r'background: var(--surface-hover)'), # Some buttons are black in light mode, now they should be a lighter surface
        (r'background(?:-color)?:\s*#(?:FA|F5|F0){2,3}\b', r'background: var(--bg-dark)'),
        (r'background(?:-color)?:\s*#EEE(?:EEE)?\b', r'background: var(--surface-hover)'),
        (r'background(?:-color)?:\s*#FFF5F2\b', r'background: var(--surface-hover)'),
        (r'background(?:-color)?:\s*#FFF3E0\b', r'background: var(--surface-hover)'),
        
        (r'background(?:-color)?:\s*#(?:F9FAFB|F3F4F6|E5E7EB|D1D5DB)\b', r'background: var(--surface)'),
        (r'background(?:-color)?:\s*#(?:111827|1F2937|374151)\b', r'background: var(--surface-hover)'),

        # Colors (Tailwind grays)
        (r'color:\s*#(?:111827|1F2937|374151)\b', r'color: var(--text-primary)'),
        (r'color:\s*#(?:4B5563|6B7280|9CA3AF)\b', r'color: var(--text-secondary)'),
        
        # Original Colors
        (r'color:\s*#000(?:000)?\b', r'color: var(--text-primary)'),
        (r'color:\s*#FFF(?:FFF)?\b', r'color: var(--text-primary)'), # In dark mode, light text stays light
        (r'color:\s*#(?:333|444|555)\b', r'color: var(--text-primary)'),
        (r'color:\s*#(?:666|888|999)\b', r'color: var(--text-secondary)'),
        
        # Borders (Tailwind grays)
        (r'border(?:-[a-z]+)?-color:\s*#(?:111827|1F2937|374151|D1D5DB|E5E7EB)\b', r'border-color: var(--border)'),
        (r'border:\s*(\d+px [a-z]+) #(?:111827|1F2937|374151|D1D5DB|E5E7EB)\b', r'border: \1 var(--border)'),
        
        # Original Borders
        (r'border(?:-[a-z]+)?-color:\s*#000(?:000)?\b', r'border-color: var(--border)'),
        (r'border(?:-[a-z]+)?-color:\s*#FFF(?:FFF)?\b', r'border-color: var(--border)'),
        (r'border(?:-[a-z]+)?-color:\s*#(?:CCC|DDD|EEE)\b', r'border-color: var(--border)'),
        (r'border:\s*(\d+px [a-z]+) #(?:CCC|DDD|EEE|000(?:000)?|FFF(?:FFF)?)\b', r'border: \1 var(--border)'),
        
        # SVG Stokes / Fills
        (r'stroke="#000(?:000)?"', r'stroke="var(--text-secondary)"'),
        (r'stroke="#FFF(?:FFF)?"', r'stroke="var(--bg-dark)"'),
        (r'fill="#000(?:000)?"', r'fill="var(--text-primary)"'),
        
        # RGBA replacements (often shadows or faint backgrounds)
        (r'rgba\(0,\s*0,\s*0,\s*0\.\d+\)', r'rgba(0, 0, 0, 0.4)'), # Darker shadows in dark mode
        (r'rgba\(255,\s*255,\s*255,\s*0\.\d+\)', r'rgba(255, 255, 255, 0.1)')
    ]
    
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content, flags=re.IGNORECASE)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, _, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.vue') or file.endswith('.css'):
            replace_in_file(os.path.join(root, file))

print("Conversion complete.")
