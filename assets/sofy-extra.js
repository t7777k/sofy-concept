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
 var sec=tl.parentNode;sec.querySelectorAll('.sx-rv-panel,.sx-rg-panel').forEach(function(p){p.hidden=p.getAttribute('data-p')!==btn.getAttribute('data-t');});});});});
// product pack switcher (+ ?pack=ASIN)
var sz=document.querySelector('.sx-sizes');
if(sz){function sel(btn){sz.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===btn?'true':'false');});
 var i=document.getElementById('pp-img');i.src=btn.dataset.img;i.alt=btn.dataset.alt;
 document.getElementById('pp-s').textContent=btn.dataset.size;document.getElementById('pp-l').innerHTML=btn.dataset.len;
 document.getElementById('pp-c').textContent=btn.dataset.count;document.getElementById('pp-r').textContent=btn.dataset.rt;document.getElementById('pp-ret').innerHTML=btn.dataset.ret;}
 sz.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){sel(btn);});});
 var q=new URLSearchParams(location.search).get('pack');if(q){var t=sz.querySelector('[data-asin="'+q+'"]');if(t)sel(t);}}
})();
/* v4: sections fade up once on scroll (no bird motion outside the hero) */
(function(){if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
document.querySelectorAll('#facts,#ranges,#finder,#shop,#guide,#reviews').forEach(function(s){s.classList.add('sx-reveal');
 var io=new IntersectionObserver(function(e){if(e[0].isIntersecting){s.classList.add('in');io.disconnect();}},{threshold:.12});io.observe(s);});})();
/* v4.1: tail swoosh under section titles (draws in when the section is revealed) */
(function(){var sw='<svg class="sx-swoosh" viewBox="0 0 120 18" aria-hidden="true"><path pathLength="1" d="M4 6C30 14 62 14 92 8S112 2 116 4"/><circle cx="116" cy="10" r="3.2"/></svg>';
document.querySelectorAll('#facts h2,#ranges h2,#guide h2,#reviews h2,.sx-plist h1,.sx-guide-page h1').forEach(function(h){h.insertAdjacentHTML('afterend',sw);});
if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
document.querySelectorAll('.sx-swoosh').forEach(function(s){if(s.closest('.sx-reveal'))return;var io=new IntersectionObserver(function(e){if(e[0].isIntersecting){s.classList.add('in');io.disconnect();}});io.observe(s);});})();

/* v5: hero video slot + FLIP bird intro + range colourways */
(function(){
 var v=document.querySelector('.sx-atf-v');
 if(v){var src=matchMedia('(min-width:768px)').matches?v.dataset.srcDesktop:v.dataset.srcMobile;if(src){v.src=src;v.play&&v.play().catch(function(){})}}
 document.querySelectorAll('.sx-rg-tabs [data-bf]').forEach(function(b){b.addEventListener('click',function(){var r=document.documentElement.style;r.setProperty('--bf',b.dataset.bf);r.setProperty('--bb',b.dataset.bb)})});
 var hb=document.querySelector('.sx-hb'),atf=document.querySelector('.sx-atf');
 if(!hb||!atf||!hb.animate)return;
 if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
 try{if(sessionStorage.getItem('sxIntro'))return;sessionStorage.setItem('sxIntro','1')}catch(e){}
 var s=hb.getBoundingClientRect(),a=atf.getBoundingClientRect();
 var bw=Math.min(a.width*.62,a.height*.5,420),k=bw/s.width,bh=s.height*k;
 var tx=a.left+a.width/2-bw/2-s.left,ty=a.top+a.height*.42-bh/2-s.top;
 var big='translate('+tx+'px,'+ty+'px) scale('+k+')';
 hb.classList.add('is-intro');
 var an=hb.animate([
  {transform:'translate('+tx+'px,'+(ty+30)+'px) scale('+k*.92+')',opacity:0},
  {transform:big,opacity:1,offset:.18},
  {transform:'translate('+tx+'px,'+(ty-14)+'px) scale('+k+')',opacity:1,offset:.5,easing:'cubic-bezier(.65,0,.25,1)'},
  {transform:'none',opacity:1}],{duration:2700,easing:'cubic-bezier(.33,1,.68,1)',fill:'backwards'});
 setTimeout(function(){hb.classList.add('is-beat')},350);
 an.onfinish=function(){hb.classList.remove('is-intro','is-beat')};
})();
