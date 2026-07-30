import re
import json

def html_to_jsx(html_content):
    # Basic replacements for JSX compatibility
    jsx = html_content.replace('class=', 'className=')
    jsx = jsx.replace('onclick=', 'onClick=')
    jsx = jsx.replace('onchange=', 'onChange=')
    jsx = jsx.replace('onmouseover=', 'onMouseOver=')
    jsx = jsx.replace('onmouseout=', 'onMouseOut=')
    jsx = jsx.replace(' for=', ' htmlFor=')
    jsx = jsx.replace('colspan=', 'colSpan=')
    
    # Fix colSpan="3" to colSpan={3}
    jsx = re.sub(r'colSpan="([0-9]+)"', r'colSpan={\1}', jsx)
    
    # Replace HTML comments <!-- comment --> with {/* comment */}
    jsx = re.sub(r'<!--(.*?)-->', r'{/*\1*/}', jsx, flags=re.DOTALL)
    
    # Close self-closing tags
    jsx = re.sub(r'<img([^>]+)(?<!/)>', r'<img\1 />', jsx)
    jsx = re.sub(r'<input([^>]+)(?<!/)>', r'<input\1 />', jsx)
    jsx = re.sub(r'<link([^>]+)(?<!/)>', r'<link\1 />', jsx)
    jsx = re.sub(r'<meta([^>]+)(?<!/)>', r'<meta\1 />', jsx)
    jsx = re.sub(r'<br([^>]*)(?<!/)>', r'<br\1 />', jsx)
    jsx = re.sub(r'<hr([^>]*)(?<!/)>', r'<hr\1 />', jsx)
    
    # Convert inline styles: style="x: y; a: b;" to style={{x: 'y', a: 'b'}}
    def style_replacer(match):
        style_str = match.group(1)
        rules = [r.strip() for r in style_str.split(';') if r.strip()]
        style_dict = {}
        for rule in rules:
            if ':' in rule:
                key, val = rule.split(':', 1)
                key = key.strip()
                # camelCase the key
                parts = key.split('-')
                if len(parts) > 1:
                    key = parts[0] + ''.join(p.capitalize() for p in parts[1:])
                val = val.strip()
                style_dict[key] = val
        return 'style={' + json.dumps(style_dict) + '}'

    jsx = re.sub(r'style="([^"]*)"', style_replacer, jsx)
    jsx = re.sub(r"style='([^']*)'", style_replacer, jsx)
    
    return jsx

with open('Main_Hub/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract body contents
body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
if body_match:
    body_content = body_match.group(1)
    # Remove script tags
    body_content = re.sub(r'<script.*?>.*?</script>', '', body_content, flags=re.DOTALL)
    
    jsx_content = html_to_jsx(body_content)
    
    page_tsx = f"""
'use client';
import Script from 'next/script';
import {{ useEffect }} from 'react';

export default function Home() {{
  return (
    <>
      {{/* The original Vanilla JS logic */}}
      <Script src="/app.js" strategy="lazyOnload" />
      {jsx_content}
    </>
  );
}}
"""
    with open('frontend/src/app/page.tsx', 'w', encoding='utf-8') as out_f:
        out_f.write(page_tsx)
    print("Successfully converted index.html to page.tsx")
    
# Extract styles to globals.css
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    css_content = style_match.group(1)
    
    # Wrap in tailwind
    tailwind_css = f"""
@import "tailwindcss";

@layer components {{
{css_content}
}}
"""
    with open('frontend/src/app/globals.css', 'w', encoding='utf-8') as out_f:
        out_f.write(tailwind_css)
    print("Successfully extracted CSS to globals.css")
