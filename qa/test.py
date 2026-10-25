from playwright.sync_api import sync_playwright
import json, pathlib
root=pathlib.Path(__file__).resolve().parent
results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width in [360,390,768,1440]:
  page=browser.new_page(viewport={'width':width,'height':900},device_scale_factor=1)
  errors=[]; posts=[]
  page.on('pageerror',lambda e: errors.append(str(e)))
  page.on('request',lambda r: posts.append(r.url) if r.method=='POST' else None)
  response=page.goto(__import__('os').environ.get('BASE_URL','http://127.0.0.1:8765/'),wait_until='networkidle')
  page.screenshot(path=str(root/f'desktop-{width}.png'),full_page=True)
  assert response.status==200
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),f'overflow {width}'
  assert page.locator('img').evaluate_all('(imgs)=>imgs.every(i=>i.complete&&i.naturalWidth>0)')
  assert page.locator('a[href^="#"]').evaluate_all('(links)=>links.every(a=>document.getElementById(a.hash.slice(1)))')
  if width<761:
   toggle=page.locator('.menu-toggle');toggle.focus();page.keyboard.press('Enter');assert toggle.get_attribute('aria-expanded')=='true'
   page.keyboard.press('Tab');assert page.locator('#navigation a').first.evaluate('(el)=>el===document.activeElement')
   page.keyboard.press('Escape');assert toggle.get_attribute('aria-expanded')=='false';assert toggle.evaluate('(el)=>el===document.activeElement')
   toggle.click();page.locator('#navigation a[href="#servicos"]').click();assert toggle.get_attribute('aria-expanded')=='false'
   toggle.click();toggle.click();assert toggle.get_attribute('aria-expanded')=='false'
  page.locator('[data-service="Pintura"]').click();assert page.locator('#service').input_value()=='Pintura'
  page.locator('#name').fill('Teste local')
  page.locator('#description').fill('Pintar a sala de 20 m².')
  page.locator('button[type=submit]').click()
  assert 'Pintar a sala' in page.locator('#summary').input_value()
  assert page.locator('#description').input_value()=='Pintar a sala de 20 m².'
  assert page.locator('#summary-title').evaluate('(el)=>el===document.activeElement')
  page.locator('#description').fill('Nova ideia: cozinha.')
  page.locator('button[type=submit]').click();assert 'Nova ideia' in page.locator('#summary').input_value();assert 'Pintar a sala' not in page.locator('#summary').input_value()
  page.locator('#copy-summary').click();assert 'Nada foi enviado.' in page.locator('#copy-status').inner_text()
  assert not posts;assert not errors,errors
  page.emulate_media(reduced_motion='reduce');assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
  results.append({'width':width,'status':'passed','console_errors':errors,'post_requests':posts,'images':'loaded','overflow':False,'local_summary':'passed','menu_keyboard':'passed' if width<761 else 'desktop navigation'})
  page.close()
 browser.close()
(root/'results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
