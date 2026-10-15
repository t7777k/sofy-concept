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

/* v5: hero video + crisp FLIP bird intro (animates SVG width, never scales a bitmap) + range colourways */
(function(){
 var v=document.querySelector('.sx-atf-v');
 if(v){var mob=!matchMedia('(min-width:768px)').matches;if(mob&&v.dataset.posterMobile)v.poster=v.dataset.posterMobile;
  var av1=mob&&v.dataset.srcMobileAv1&&v.canPlayType('video/mp4; codecs="av01.0.08M.08"')==='probably';var src=mob?(av1?v.dataset.srcMobileAv1:v.dataset.srcMobile):v.dataset.srcDesktop;
  if(src&&!(navigator.connection&&navigator.connection.saveData)){v.src=src;var p=v.play();p&&p.catch&&p.catch(function(){})}}
 document.querySelectorAll('.sx-rg-tabs [data-bf]').forEach(function(b){b.addEventListener('click',function(){var r=document.documentElement.style;r.setProperty('--bf',b.dataset.bf);r.setProperty('--bb',b.dataset.bb)})});
 var hb=document.querySelector('.sx-hb'),atf=document.querySelector('.sx-atf-media')||document.querySelector('.sx-atf');
 var svg=hb&&hb.querySelector('svg');
 if(!svg||!atf||!svg.animate)return;
 if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
 try{if(sessionStorage.getItem('sxIntro'))return;sessionStorage.setItem('sxIntro','1')}catch(e){}
 var s=hb.getBoundingClientRect(),a=atf.getBoundingClientRect();
 var bw=Math.round(Math.min(a.width*.5,a.height*.55*1210/1420,360)),bh=bw*1420/1210;
 var tx=a.left+a.width/2-bw/2-s.left,ty=a.top+a.height*.46-bh/2-s.top;
 function k(x,y,w,o){return {transform:'translate('+x+'px,'+y+'px)',width:w+'px',opacity:o}}
 hb.classList.add('is-intro');
 var an=svg.animate([k(tx,ty+32,bw,0),Object.assign(k(tx,ty,bw,1),{offset:.18}),Object.assign(k(tx,ty-16,bw,1),{offset:.5,easing:'cubic-bezier(.65,0,.25,1)'}),k(0,0,s.width,1)],{duration:2700,easing:'cubic-bezier(.33,1,.68,1)'});
 setTimeout(function(){hb.classList.add('is-beat')},350);setTimeout(function(){hb.classList.remove('is-intro')},1500);
 an.onfinish=function(){hb.classList.remove('is-intro','is-beat')};
})();

/* v6: header bird takes the colourway of the range band in view */
(function(){var bs=document.querySelectorAll('.sx-rband[data-bf]');if(!bs.length||!('IntersectionObserver' in window))return;var r=document.documentElement.style;
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){r.setProperty('--bf',e.target.dataset.bf);r.setProperty('--bb',e.target.dataset.bb)}})},{rootMargin:'-45% 0px -45% 0px'});bs.forEach(function(b){io.observe(b)});
 var rs=document.getElementById('ranges');if(rs)new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&e.boundingClientRect.top>0){r.removeProperty('--bf');r.removeProperty('--bb')}})}).observe(rs)})();

/* v7: products page filters (Pads | Pantyliners, then sub-brand) */
(function(){var tabs=document.querySelectorAll('.sx-ptabs [data-g]');if(!tabs.length)return;var subs=document.querySelectorAll('.sx-psubs [data-s]'),cards=document.querySelectorAll('.sx-pcard[data-g]');
 function apply(g,s){tabs.forEach(function(b){b.setAttribute('aria-selected',b.dataset.g===g)});subs.forEach(function(b){b.hidden=!(g==='all'||b.dataset.g===g);b.setAttribute('aria-pressed',b.dataset.s===s)});
  cards.forEach(function(c){c.hidden=!((g==='all'||c.dataset.g===g)&&(!s||c.dataset.s===s))})}
 tabs.forEach(function(b){b.addEventListener('click',function(){apply(b.dataset.g,null);history.replaceState(null,'',b.dataset.g==='all'?location.pathname:'#'+b.dataset.g)})});
 subs.forEach(function(b){b.addEventListener('click',function(){var on=b.getAttribute('aria-pressed')==='true';apply(document.querySelector('.sx-ptabs [aria-selected=true]').dataset.g==='all'?b.dataset.g:document.querySelector('.sx-ptabs [aria-selected=true]').dataset.g,on?null:b.dataset.s)})});
 var h=location.hash.slice(1);apply(['pads','liners','mama'].indexOf(h)>-1?h:'all',null)})();
/* close other dropdowns */
document.addEventListener('click',function(e){document.querySelectorAll('.sx-nav .sx-dd[open]').forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})});

/* v7.1 finder: Pads | Pantyliners */
(function(){var sg=document.querySelector('[data-finder2]');if(!sg)return;var D=JSON.parse(sg.getAttribute('data-finder2')),L=document.getElementById('fd-l'),pre=L.textContent.split(':')[0];
 function show(g,v){var d=D.filter(function(x){return x.g===g&&x.v===v})[0];if(!d)return;
  sg.querySelectorAll('.sx-fopts button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.g===g&&b.dataset.v===v)});
  var im=document.getElementById('fd-img');im.src=d.img;im.alt=d.name;document.getElementById('fd-n').textContent=d.name;L.textContent=pre+': '+d.len;document.getElementById('fd-c').textContent=d.counts;document.getElementById('fd-link').href=d.href}
 sg.querySelectorAll('.sx-ftype button').forEach(function(b){b.addEventListener('click',function(){var g=b.dataset.t;sg.querySelectorAll('.sx-ftype button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
  sg.querySelectorAll('.sx-fopts').forEach(function(o){o.hidden=o.dataset.grp!==g});show(g,D.filter(function(x){return x.g===g})[0].v)})});
 sg.querySelectorAll('.sx-fopts button').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.g,b.dataset.v)})})})();
