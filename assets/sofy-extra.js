(function(){
var v=document.getElementById('videoPlayer'),b=document.getElementById('muteButton');
if(v&&b){b.addEventListener('click',function(){v.muted=!v.muted;b.classList.toggle('mute',!v.muted);b.classList.toggle('unmute',v.muted);});}
// burger menu
var mm=document.getElementById('sx-mm'),bg=document.querySelector('.sx-burger');
if(mm&&bg){bg.addEventListener('click',function(){mm.hidden=false;bg.setAttribute('aria-expanded','true');});
 mm.addEventListener('click',function(e){if(e.target.closest('[data-close]')||e.target.closest('nav a')){mm.hidden=true;bg.setAttribute('aria-expanded','false');}});}
// pad finder
var sg=document.querySelector('[data-finder]');
if(sg){var data=JSON.parse(sg.getAttribute('data-finder'));
 function show(d){document.getElementById('fd-img').src=d.img;document.getElementById('fd-img').alt=d.name;document.getElementById('fd-n').textContent=d.name;
  document.getElementById('fd-l').innerHTML=d.lenlabel;document.getElementById('fd-c').textContent=d.counts;document.getElementById('fd-link').href=d.href;}
 function press(group,btn){group.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===btn?'true':'false');});}
 sg.querySelectorAll('[data-k] button').forEach(function(btn){btn.addEventListener('click',function(){var g=btn.parentNode,k=g.getAttribute('data-k');press(g,btn);
  var d=data.filter(function(x){return x[k]===btn.getAttribute('data-v');})[0];show(d);
  var other=sg.querySelector('[data-k="'+(k==='flow'?'len':'flow')+'"]');press(other,other.querySelector('[data-v="'+(k==='flow'?d.len:d.flow)+'"]'));});});
 sg.querySelectorAll('.sx-mode button').forEach(function(btn){btn.addEventListener('click',function(){press(btn.parentNode,btn);var m=btn.getAttribute('data-m');
  ['flow','len'].forEach(function(k){sg.querySelector('[data-k="'+k+'"]').hidden=(k!==m);sg.querySelector('[data-for="'+k+'"]').hidden=(k!==m);});});});}
// review tabs
document.querySelectorAll('.sx-rv-tabs').forEach(function(tl){tl.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){
 tl.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-selected',x===btn?'true':'false');});
 var sec=tl.parentNode;sec.querySelectorAll('.sx-rv-panel').forEach(function(p){p.hidden=p.getAttribute('data-p')!==btn.getAttribute('data-t');});});});});
// product pack switcher (+ ?pack=ASIN)
var sz=document.querySelector('.sx-sizes');
if(sz){function sel(btn){sz.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===btn?'true':'false');});
 var i=document.getElementById('pp-img');i.src=btn.dataset.img;i.alt=btn.dataset.alt;
 document.getElementById('pp-s').textContent=btn.dataset.size;document.getElementById('pp-l').innerHTML=btn.dataset.len;
 document.getElementById('pp-c').textContent=btn.dataset.count;document.getElementById('pp-r').textContent=btn.dataset.rt;document.getElementById('pp-ret').innerHTML=btn.dataset.ret;}
 sz.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){sel(btn);});});
 var q=new URLSearchParams(location.search).get('pack');if(q){var t=sz.querySelector('[data-asin="'+q+'"]');if(t)sel(t);}}
})();
