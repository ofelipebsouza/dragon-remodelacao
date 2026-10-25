'use strict';
const toggle=document.querySelector('.menu-toggle');
const navigation=document.querySelector('#navigation');
function closeMenu(restoreFocus=false){navigation.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Abrir menu');if(restoreFocus)toggle.focus();}
toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';navigation.classList.toggle('open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Fechar menu':'Abrir menu');});
navigation.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>closeMenu()));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&navigation.classList.contains('open'))closeMenu(true);});
document.addEventListener('click',event=>{if(!event.target.closest('.header'))closeMenu();});
window.matchMedia('(min-width:761px)').addEventListener('change',event=>{if(event.matches)closeMenu();});
document.querySelectorAll('[data-service]').forEach(link=>link.addEventListener('click',()=>{document.querySelector('#service').value=link.dataset.service;}));
const form=document.querySelector('#project-form');
form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const data=new FormData(form);const description=data.get('description').trim();if(!description){document.querySelector('#description').setCustomValidity('Descreva brevemente a sua ideia.');form.reportValidity();return;}
const lines=['RESUMO DO PROJETO — DRAGON REMODELAÇÃO', ''];if(data.get('name').trim())lines.push(`Nome: ${data.get('name').trim()}`);if(data.get('location').trim())lines.push(`Localização: ${data.get('location').trim()}`);lines.push(`Serviço: ${data.get('service')}`,'',description,'','Resumo preparado localmente. Não enviado. Sujeito a avaliação técnica; não constitui orçamento.');document.querySelector('#summary').value=lines.join('\n');document.querySelector('#summary-section').hidden=false;document.querySelector('#copy-status').textContent='';document.querySelector('#summary-title').focus();});
document.querySelector('#description').addEventListener('input',event=>event.target.setCustomValidity(''));
document.querySelector('#copy-summary').addEventListener('click',async()=>{const summary=document.querySelector('#summary');const status=document.querySelector('#copy-status');try{if(!navigator.clipboard)throw new Error('Clipboard unavailable');await navigator.clipboard.writeText(summary.value);status.textContent='Resumo copiado. Nada foi enviado.';}catch{summary.focus();summary.select();status.textContent='Selecione e copie o texto acima com o comando Copiar do seu dispositivo. Nada foi enviado.';}});
document.querySelector('#year').textContent=new Date().getFullYear();
