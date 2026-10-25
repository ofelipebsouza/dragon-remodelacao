const fs=require('fs'), vm=require('vm'), assert=require('assert');
const nodes=new Map();
function el(id){if(nodes.has(id))return nodes.get(id);let attrs={},events={},classes=new Set();const x={value:'',textContent:'',hidden:true,dataset:{},classList:{add:k=>classes.add(k),remove:k=>classes.delete(k),contains:k=>classes.has(k),toggle:(k,v)=>v?classes.add(k):classes.delete(k)},setAttribute:(k,v)=>attrs[k]=v,getAttribute:k=>attrs[k],addEventListener:(k,f)=>events[k]=f,querySelectorAll:()=>[],focus:()=>x.focused=true,select:()=>x.selected=true,reportValidity:()=>true,setCustomValidity:v=>x.validity=v,events};nodes.set(id,x);return x}
const document={querySelector:el,querySelectorAll:()=>[],addEventListener:()=>{}};
let data={name:' Maria ',location:' Lisboa ',service:'Pintura',description:' Sala '};
const context={document,window:{matchMedia:()=>({addEventListener:()=>{}})},navigator:{},FormData:class{get(k){return data[k]}},Date};
vm.runInNewContext(fs.readFileSync(__dirname+'/../src/scripts/project.js','utf8'),context);
let prevented=false;el('#project-form').events.submit({preventDefault(){prevented=true}});
assert(prevented);assert(el('#summary').value.includes('Nome: Maria'));assert(el('#summary').value.includes('Não enviado'));assert.equal(el('#summary-section').hidden,false);assert(el('#summary-title').focused);
data.description='Novo resumo';el('#project-form').events.submit({preventDefault(){}});assert(el('#summary').value.includes('Novo resumo'));assert(!el('#summary').value.includes('\nSala\n'));
data.description='  ';el('#project-form').events.submit({preventDefault(){}});assert(el('#description').validity);el('#description').events.input({target:el('#description')});assert.equal(el('#description').validity,'');
el('.menu-toggle').events.click();assert.equal(el('.menu-toggle').getAttribute('aria-expanded'),'true');el('.menu-toggle').events.click();assert.equal(el('.menu-toggle').getAttribute('aria-expanded'),'false');
(async()=>{await el('#copy-summary').events.click();assert(el('#summary').selected);assert(el('#copy-status').textContent.includes('Nada foi enviado'));context.navigator.clipboard={writeText:async text=>assert(text.includes('Novo resumo'))};await el('#copy-summary').events.click();assert(el('#copy-status').textContent.includes('Resumo copiado'));console.log('PASS: local summary; repeat replaces summary; whitespace validation; menu state; copy success and fallback. DOM mocked, not browser QA.');})();
