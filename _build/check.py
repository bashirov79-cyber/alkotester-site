#!/usr/bin/env python3
"""alkotester.az — dərcdən əvvəl yoxlama. İstifadə (repo kökündən): python3 _build/check.py
Yoxlayır: qırıq daxili keçidlər/şəkillər, hər məhsulun 3 dildə olması, sitemap və search.json-un səhifələrlə uyğunluğu."""
import json, os, re, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
os.chdir(R)
pages = [f for f in os.listdir('.') if f.endswith('.html')]
errs = []
for d in ('', 'ru/', 'en/'):
    for f in pages:
        if f != '404.html' and not os.path.exists(d + f): errs.append(f'yoxdur: {d}{f}')
    for f in os.listdir(d or '.'):
        if not f.endswith('.html'): continue
        s = re.sub(r'<script.*?</script>', '', open(d + f, encoding='utf-8').read(), flags=re.S)
        for h in re.findall(r'(?:href|src|srcset)="([^"]+)"', s):
            h = h.split('#')[0].split('?')[0]
            if not h or ':' in h or h.startswith('/'): continue
            p = os.path.normpath(os.path.join(d, h))
            if h.endswith('/') or h in ('.', './'): p = os.path.join(p, 'index.html')
            if not os.path.exists(p): errs.append(f'qırıq keçid: {d}{f} → {h}')
locs = re.findall(r'<loc>https://alkotester\.az/([^<]*)</loc>', open('sitemap.xml', encoding='utf-8').read())
for u in locs:
    p = u + 'index.html' if u == '' or u.endswith('/') else u
    if not os.path.exists(p): errs.append(f'sitemap-da var, fayl yoxdur: {u}')
for d in ('', 'ru/', 'en/'):
    for f in pages:
        if f != '404.html' and (d + f).replace('index.html', '') not in locs: errs.append(f'sitemap-da yoxdur: {d}{f}')
    for e in json.load(open(d + 'search.json', encoding='utf-8')):
        u = e.get('u') or e.get('url') or ''
        if u and not os.path.exists(os.path.normpath(os.path.join(d, u.split('#')[0]))): errs.append(f'search.json qırıq: {d} {u}')
print('\n'.join(errs) if errs else f'OK: {len(pages)} səhifə × 3 dil, keçidlər, sitemap və axtarış qaydasındadır')
sys.exit(1 if errs else 0)
