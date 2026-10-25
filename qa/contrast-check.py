from pathlib import Path
import re

def luminance(h):
 rgb=[int(h[i:i+2],16)/255 for i in (1,3,5)]
 return sum((c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4)*w for c,w in zip(rgb,(.2126,.7152,.0722)))
def ratio(a,b):
 x,y=sorted((luminance(a),luminance(b)));return (y+.05)/(x+.05)
pairs=[('body','#173c2b','#ffffff',4.5),('body on cream','#173c2b','#f7f6f0',4.5),('secondary','#58645b','#ffffff',4.5),('secondary on cream','#58645b','#f7f6f0',4.5),('small numbers','#5d6b60','#f7f6f0',4.5),('button','#ffffff','#b5222a',4.5),('button hover','#ffffff','#961c23',4.5),('green band','#edf4ec','#00623b',4.5),('green section','#ffffff','#00623b',4.5),('green section secondary','#dceadc','#00623b',4.5),('red heading and links','#b5222a','#ffffff',4.5),('focus on white','#b5222a','#ffffff',3),('focus on cream','#b5222a','#f7f6f0',3),('input border','#7c897e','#ffffff',3)]
for name,a,b,minimum in pairs:
 r=ratio(a,b);assert r>=minimum,(name,r);print(f'PASS {name}: {r:.2f}:1 (min {minimum})')
s=(Path(__file__).resolve().parent.parent/'src/styles/global.css').read_text()
old=['--navy','--blue','#122b45','#244f79','#172c40','#5b6874','#326a9f','#56738c','#0f2239','#718290','#6a8094','#c2cfdb','#3983bc']
assert not any(x in s for x in old)
print('PASS no legacy blue tokens in source CSS. Photo-overlay contrast requires visual QA; tests cover solid UI color pairs, not WCAG certification.')
