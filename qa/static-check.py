from html.parser import HTMLParser
from pathlib import Path
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[]; self.anchors=[]; self.images=[]; self.labels=[]; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='a' and a.get('href','').startswith('#'):self.anchors.append(a['href'][1:])
  if tag=='img':self.images.append(a)
  if tag=='label':self.labels.append(a['for'])
p=Path(__file__).resolve().parent.parent
s=(p/'dist/index.html').read_text();d=Page();d.feed(s)
assert d.h1==1
assert len(d.ids)==len(set(d.ids))
assert all(x in d.ids for x in d.anchors+d.labels)
assert all(x.get('alt') and (p/'dist'/x['src'].lstrip('/')).is_file() for x in d.images)
assert 'noindex' not in s
assert 'generativelanguage' not in s
assert 'enviado com sucesso' not in s.lower()
css=''.join(x.read_text() for x in (p/'dist/_astro').glob('*.css'))
assert 'tailwindcss' in css and 'grid-template-columns' in css
print('PASS: built HTML, anchors, labels, local assets, SEO, Tailwind output and no false-send/AI integrations')
