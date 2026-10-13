# Sofy concept generator: mirrors live sofy-arabia.com theme (style.css + main.js) and adds fixed/new sections.
import re, os, json, html
OUT='/workspace/sofy-concept'
SRC=open('/workspace/sofy-src/ar.html').read()
i=SRC.find('<ul class="mt-social'); SOCIAL=SRC[i:SRC.find('</ul>',i)]
SOCIAL=re.sub(r'<li[^>]*lang-item.*?</li>','',SOCIAL,flags=re.S).replace(' nofollow',' rel="noopener nofollow"')
# give social links accessible names
for k,n in [('instagram','Instagram'),('facebook','Facebook'),('snapchat','Snapchat'),('tiktok','TikTok'),('x.com','X'),('youtu','YouTube')]:
    SOCIAL=re.sub(r'(<a href="[^"]*%s[^"]*")'%re.escape(k), r'\1 aria-label="%s"'%n, SOCIAL, count=1)
BASE='https://t7777k.github.io/sofy-concept/'
AMZ='https://www.amazon.sa/dp/'
NAHDI={'ar':'https://www.nahdionline.com/ar-sa/','en':'https://www.nahdionline.com/en-sa/'}

# ---------- verified product data (MarketLens retailer titles + live pack art) ----------
PRODUCTS=[
 dict(slug='olive', theme='green', badge='olive.png',
  name={'ar':'سوفي أوليف','en':'Sofy Olive'},
  tag={'ar':'فوط صحية رقيقة بأجنحة وزيت الزيتون المرطّب','en':'Slim pads with wings and moisturising olive oil'},
  hero='pack-olive-large-30.png',
  icons=[('ic-olive-pad.png',{'ar':'زيت الزيتون المرطّب','en':'Moisturising olive oil'}),('ic-cotton.png',{'ar':'ملمس قطني','en':'Cotton touch'}),
         ('ic-wings.svg',{'ar':'رقيقة بأجنحة','en':'Slim with wings'}),('ic-derma.png',{'ar':'مختبرة جلدياً','en':'Dermatologically tested'})],
  packs=[dict(img='pack-olive-regular-30.png',name={'ar':'عادي · 23 سم · 30 فوطة','en':'Regular · 23 cm · 30 pads'},asin='B08575MHSD',nahdi=None),
         dict(img='pack-olive-large-30.png',name={'ar':'كبيرة · 29 سم · 30 فوطة','en':'Large · 29 cm · 30 pads'},asin='B0B58KTYDY',nahdi='sofy-feminine-napkin-olive-large-pack-30-pads/pdp/102297642'),
         dict(img='pack-olive-large-56.png',name={'ar':'كبيرة · 29 سم · 56 فوطة','en':'Large · 29 cm · 56 pads'},asin='B0B58M4QPN',nahdi='sofy-feminine-napkin-olive-large-pack-56-pads/pdp/102297651')],
  body={'ar':['فوط سوفي أوليف رقيقة بأجنحة، بلمسة قطنية وزيت الزيتون المرطّب للعناية ببشرتكِ خلال أيام الدورة.','متوفرة بمقاسين: عادي بطول 23 سم، وكبيرة بطول 29 سم.'],
        'en':['Sofy Olive pads are slim with wings, with a cotton-touch surface and moisturising olive oil to care for your skin on period days.','Two sizes: Regular (23 cm) and Large (29 cm).']}),
 dict(slug='olive-night', theme='night', badge='olive-night.png',
  name={'ar':'سوفي أوليف الليلية','en':'Sofy Olive Night'},
  tag={'ar':'نوم هانئ مع سوفي','en':'Sweet dreams with Sofy'},
  hero='pack-night-{l}.png',
  icons=[('ic-32.svg',{'ar':'طول 32 سم','en':'32 cm long'}),('ic-absorb.png',{'ar':'ألياف امتصاص فائقة','en':'Super absorbency fibre'}),
         ('ic-japan.svg',{'ar':'تكنولوجيا يابانية','en':'Japan technology'}),('ic-98.svg',{'ar':'98% ناعمة على البشرة','en':'98% soft on skin'})],
  packs=[dict(img='pack-night-{l}.png',name={'ar':'32 سم · 24 فوطة + 2 مجاناً','en':'32 cm · 24 pads + 2 free'},asin='B0BTC2GPYL',nahdi='sofy-night-pad-with-olive-242-free/pdp/102407670')],
  body={'ar':['فوطة سوفي أوليف الليلية بطول 32 سم وأجنحة، مع زيت الزيتون المرطّب وألياف امتصاص فائقة تقلّل الإحساس بالبلل، لتنامي براحة طوال الليل.'],
        'en':['Sofy Olive Night is a 32 cm pad with wings, moisturising olive oil and super absorbency fibre that helps prevent the wet feeling, so you can sleep comfortably through the night.']}),
 dict(slug='olive-pantyliners', theme='green', badge='olive.png',
  name={'ar':'سوفي أوليف فوط يومية','en':'Sofy Olive Pantyliners'},
  tag={'ar':'للاستعمال اليومي','en':'For daily use'},
  hero='pack-liner-40-{l}.png',
  icons=[('ic-flex.png',{'ar':'مرنة جداً','en':'Very flexible'}),('ic-olive.png',{'ar':'قطنية بزيت الزيتون','en':'Cotton with olive oil'}),
         ('ic-155.svg',{'ar':'طول 155 ملم','en':'155 mm long'}),('ic-unscented.svg',{'ar':'غير معطّرة','en':'Unscented'})],
  packs=[dict(img='pack-liner-40-{l}.png',name={'ar':'عادي · 155 ملم · 40 فوطة','en':'Regular · 155 mm · 40 liners'},asin='B0BTBZJZJ7',nahdi='sofy-pantyliner-unscented-with-olive-40-pcs/pdp/102407688'),
         dict(img='pack-liner-80-{l}.png',name={'ar':'عادي · 155 ملم · 80 فوطة','en':'Regular · 155 mm · 80 liners'},asin='B0BTC1DWS5',nahdi='sofy-pantyliner-unscented-with-olive-80-pcs/pdp/102407696')],
  body={'ar':['فوط سوفي أوليف اليومية رقيقة ومرنة وغير معطّرة، بلمسة قطنية وزيت الزيتون، لإحساس بالانتعاش كل يوم.'],
        'en':['Sofy Olive Pantyliners are thin, flexible and unscented, with a cotton touch and olive oil, for a fresh feeling every day.']}),
]
SHOP=[('nahdi-logo.png',{'ar':NAHDI['ar']+'search?query=sofy','en':NAHDI['en']+'search?query=sofy'},'Nahdi'),
      ('amazon-logo.png',{'ar':'https://www.amazon.sa/s?k=sofy+olive&language=ar_AE','en':'https://www.amazon.sa/s?k=sofy+olive&language=en_AE'},'Amazon.sa'),
      ('al-dawaa-logo.png',{'ar':'https://www.al-dawaa.com/ar/','en':'https://www.al-dawaa.com/en/'},'Al-Dawaa'),
      ('noon-logo-1.png',{'ar':'https://www.noon.com/saudi-ar/sofy/','en':'https://www.noon.com/saudi-en/sofy/'},'noon')]

MYTHS={'ar':[
 ('الاستحمام أثناء الدورة الشهرية يوقفها.','غير صحيح. النظافة الشخصية من أهم ما تعتنين به، والاستحمام اليومي بماء دافئ مفيد لكِ.'),
 ('المشي أو أي نشاط عادي أثناء الدورة مضرّ.','بالعكس، النشاط البدني يسهّل عليكِ أيام الدورة.'),
 ('يجب أن تأكلي كمية أكبر أثناء الدورة.','المهم نوعية الطعام لا كميته.'),
 ('الأطعمة الحامضة ممنوعة لأنها تُنشّف الجسم.','احتباس بعض السوائل أسفل البطن أمر طبيعي، ولا علاقة له بنوع الطعام.'),
 ('الآيسكريم والمشروبات الباردة توقف الدورة.','لا علاقة لنوع الطعام بتوقف الدورة.'),
 ('الصابون العادي مناسب لتنظيف المناطق الحساسة.','المستحضرات المخصّصة للمناطق الحساسة أنسب من الصابون العادي.'),
 ('كلما زاد الألم كانت الدورة طبيعية أكثر.','غير صحيح. شدة الألم لا تدل على حالة الدورة.'),
 ('المسكّنات مفيدة دائماً أثناء الدورة.','لا يُنصح بالمسكّنات إلا عند الألم الذي لا يُحتمل.'),
 ('القرفة تسبّب نزيفاً حاداً.','القرفة قد تساعد على تخفيف الألم خلال أيام الدورة.'),
 ('الدورة الطبيعية تستمر سبعة أيام بالضبط.','غير صحيح. قد تتراوح بين 4 و7 أيام.')],
 'en':[
 ('Bathing during your period stops it.','Not true. Personal hygiene matters most, and a daily warm shower is good for you.'),
 ('Walking or normal activity during your period is harmful.','The opposite: physical activity makes period days easier.'),
 ('You should eat more during your period.','What matters is the type of food, not the amount.'),
 ('Sour foods are forbidden because they dry out the body.','Holding some fluid in the lower abdomen is normal and has nothing to do with what you eat.'),
 ('Ice cream and cold drinks stop your period.','What you eat has nothing to do with your period stopping.'),
 ('Regular soap is fine for intimate areas.','Products made for intimate areas are better than regular soap.'),
 ('The more it hurts, the more normal your period is.','Not true. How much it hurts says nothing about your period.'),
 ('Painkillers are always useful during your period.','Painkillers are only recommended for pain you cannot bear.'),
 ('Cinnamon causes heavy bleeding.','Cinnamon may help ease period pain.'),
 ('A normal period lasts exactly seven days.','Not true. It can last anywhere from 4 to 7 days.')]}
FAQ={'ar':[
 ('ما الفرق بين سوفي أوليف عادي وكبيرة؟','العادي بطول 23 سم، والكبيرة بطول 29 سم. كلاهما رقيقة بأجنحة وبزيت الزيتون المرطّب.'),
 ('متى أستخدم سوفي أوليف الليلية؟','للنوم. طولها 32 سم لحماية أطول خلال الليل.'),
 ('هل سوفي أوليف فوط يومية معطّرة؟','لا، هي غير معطّرة، وطولها 155 ملم.'),
 ('من أين أشتري منتجات سوفي؟','من النهدي وAmazon.sa والدواء وnoon، وروابط كل منتج موجودة في صفحته.')],
 'en':[
 ('What is the difference between Sofy Olive Regular and Large?','Regular is 23 cm and Large is 29 cm. Both are slim, with wings and moisturising olive oil.'),
 ('When should I use Sofy Olive Night?','At night. It is 32 cm long for longer cover while you sleep.'),
 ('Are Sofy Olive Pantyliners scented?','No, they are unscented and 155 mm long.'),
 ('Where can I buy Sofy?','At Nahdi, Amazon.sa, Al-Dawaa and noon. Each product page links to its retailers.')]}

REV=json.load(open('/workspace/sofy-reviews.json'))

T={'ar':dict(dir='rtl',lang='ar',other='en',otherlabel='English',home='الرئيسية',
  title='سوفي العربية | فوط سوفي أوليف بزيت الزيتون',desc='سوفي أوليف: فوط صحية رقيقة بأجنحة وزيت الزيتون المرطّب، فوط ليلية بطول 32 سم، وفوط يومية غير معطّرة. اعرفي أين تشترين سوفي في السعودية.',
  h1='المشكلة مو فيكي…',h1b='المشكلة في الفوطة',shop='تسوّقي سوفي',details='تفاصيل المنتج',guide_t='دليلكِ لأيام الدورة',guide_cta='اقرئي الدليل كاملاً',myth='خرافة',fact='الحقيقة',
  rev_t='آراء العميلات على Amazon.sa',rev_tr='مترجمة من الإنجليزية',rev_orig='النص الأصلي',verified='مشترية موثّقة',faq_t='أسئلة شائعة',dl_t='معلومات عن الدورة الشهرية',dl1='حقائق عن الدورة الشهرية',dl2='خرافات وحقائق',
  foot='© 2026 سوفي العربية. جميع الحقوق محفوظة.',buy='اشتري من',sizes='المقاسات المتوفرة',products='منتجاتنا',guide_page='دليل الدورة الشهرية',
  alt_logo='شعار سوفي',alt_darin='دارين، سفيرة سوفي',alt_sig='توقيع دارين',alt_bill='حملة سوفي مع دارين',mute='تشغيل الصوت أو كتمه',top='العودة إلى الأعلى'),
 'en':dict(dir='ltr',lang='en',other='ar',otherlabel='العربية',home='Home',
  title='Sofy Arabia | Sofy Olive pads with olive oil',desc='Sofy Olive: slim pads with wings and moisturising olive oil, 32 cm night pads and unscented pantyliners. Find where to buy Sofy in Saudi Arabia.',
  h1='The problem is not you…',h1b="it's the pad",shop='Shop Sofy',details='Product details',guide_t='Your period guide',guide_cta='Read the full guide',myth='Myth',fact='Fact',
  rev_t='Customer reviews on Amazon.sa',rev_tr='Translated from Arabic',rev_orig='Original text',verified='Verified purchase',faq_t='FAQ',dl_t='Period info',dl1='Period facts',dl2='Myths and facts',
  foot='© 2026 Sofy Arabia. All rights reserved.',buy='Buy at',sizes='Available sizes',products='Our products',guide_page='Period guide',
  alt_logo='Sofy logo',alt_darin='Darin, Sofy ambassador',alt_sig="Darin's signature",alt_bill='Sofy campaign with Darin',mute='Toggle sound',top='Back to top')}

def pre(l,depth): return ('../'*depth)+('' if l=='ar' else '../')  # path to site root
def page(l,depth,slug,title,desc,body,canon_ar,canon_en):
    t=T[l]; r=('../'*(depth+(1 if l=='en' else 0)))
    fx=lambda c: c+'index.html' if (c=='' or c.endswith('/')) else c
    alt_href = (r+fx(canon_en)) if l=='ar' else (r+fx(canon_ar))
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{BASE}{canon_ar if l=='ar' else canon_en}">
<link rel="alternate" hreflang="ar" href="{BASE}{canon_ar}"><link rel="alternate" hreflang="en" href="{BASE}{canon_en}"><link rel="alternate" hreflang="x-default" href="{BASE}{canon_ar}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{BASE}assets/up/sofy-logo.png">
<link rel="icon" href="{r}assets/up/cropped-favicon-32x32.png" sizes="32x32"><link rel="apple-touch-icon" href="{r}assets/up/cropped-favicon-180x180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=El+Messiri:wght@400..700&family=Montserrat:wght@400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.css">
<link rel="stylesheet" href="{r}assets/theme/style.css">
<link rel="stylesheet" href="{r}assets/sofy-extra.css">
</head>
<body class="{'rtl ' if l=='ar' else ''}sx-{slug}">
<div class="mt-wrapper">
<header class="mt-header d-flex align-items-center"><div class="container-xl"><div class="row">
<div class="col-3 col-md-3"><div class="mt-logo"><a href="{r}{'' if l=='ar' else 'en/'}index.html"><img src="{r}assets/up/sofy-logo.png" width="531" height="309" alt="{t['alt_logo']}"></a></div></div>
<div class="col-9 col-md-9 align-items-center d-flex justify-content-end text-end">{SOCIAL}<li class="lang-item lang-item-{t['other']}"><a href="{alt_href}" hreflang="{t['other']}" lang="{t['other']}"><img src="{r}assets/up/{'en.png' if l=='ar' else 'ain-color.png'}" alt="{t['otherlabel']}" width="24" height="24"></a></li></ul></div>
</div></div></header>
<main>
{body}
</main>
<footer class="mt-footer mt-secondary_bgr pt-4 pb-4"><div class="container-xl text-center">
<nav class="sx-foot-nav"><a href="{r}{'' if l=='ar' else 'en/'}index.html">{t['home']}</a><a href="{r}{'' if l=='ar' else 'en/'}index.html#products">{t['products']}</a><a href="{r}{'' if l=='ar' else 'en/'}guide.html">{t['guide_page']}</a></nav>
<p class="mb-0">{t['foot']}</p></div></footer>
</div>
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.js"></script>
<script src="{r}assets/theme/main.js"></script>
<script src="{r}assets/sofy-extra.js"></script>
</body></html>'''

def ret_links(l,p,r):
    t=T[l]; out=[f'<a href="{AMZ}{p["asin"]}" target="_blank" rel="noopener"><img src="{r}assets/up/amazon-logo.png" alt="{t["buy"]} Amazon.sa" width="408" height="208"></a>']
    if p['nahdi']: out.insert(0,f'<a href="{NAHDI[l]}{p["nahdi"]}" target="_blank" rel="noopener"><img src="{r}assets/up/nahdi-logo.png" alt="{t["buy"]} {"النهدي" if l=="ar" else "Nahdi"}" width="408" height="208"></a>')
    return '<div class="sx-ret">'+''.join(out)+'</div>'

def band(l,p,r,link):
    t=T[l]; img=p['hero'].format(l=l)
    icons=''.join(f'<li><span class="sx-ic"><img src="{r}assets/img/{f}" alt="" width="120" height="120"></span><b>{n[l]}</b></li>' for f,n in p['icons'])
    return f'''<section class="mt-section mt-features_section {'mt-night' if p['theme']=='night' else 'mt-pantyliners'} sx-band" id="{p['slug']}">
<div class="container-xl"><div class="sx-band-in">
<div class="sx-badge"><img src="{r}assets/up/{p['badge']}" alt="" width="1979" height="286"></div>
<h2 class="sx-band-title">{p['name'][l]}</h2>
<div class="sx-band-grid">
<ul class="sx-icons">{icons}</ul>
<a class="sx-pack" href="{link}"><img src="{r}assets/up/{img}" alt="{p['name'][l]}"></a>
</div>
<div class="sx-cta"><a class="mt-btn" href="{link}">{t['details']}</a></div>
</div></div></section>'''

def stars(n): n=int(float(n)); return '<span class="sx-stars" aria-label="%d/5">'%n+'★'*n+'<i>'+'★'*(5-n)+'</i></span>'

def reviews(l):
    t=T[l]; cards=[]
    for rv in REV:
        orig_lang=rv['lang']; txt=rv['text'] if orig_lang==l else rv['tr'][l]
        tr='' if orig_lang==l else f'<small class="sx-tr">{t["rev_tr"] if l=="en" else "مترجمة من الإنجليزية"}</small><details><summary>{t["rev_orig"]}</summary><p dir="{"rtl" if orig_lang=="ar" else "ltr"}">{html.escape(rv["text"])}</p></details>'
        cards.append(f'<article class="sx-rev">{stars(rv["stars"])}<h3>{html.escape(rv["title"] if orig_lang==l else rv["title_tr"][l])}</h3><p>{html.escape(txt)}</p>{tr}<footer><span>{t["verified"]} · {rv["date_"+l]}</span><span class="sx-rev-p">{html.escape(rv["product_"+l])}</span></footer></article>')
    return f'''<section class="mt-section sx-reviews mt-medium_pt mt-medium_pb" id="reviews"><div class="container-xl">
<header class="mt-section_header text-center"><h2 class="mt-section_title">{t['rev_t']}</h2></header>
<div class="sx-rev-grid">{''.join(cards)}</div>
<div class="sx-cta"><a class="mt-btn" href="https://www.amazon.sa/s?k=sofy&language={'ar_AE' if l=='ar' else 'en_AE'}" target="_blank" rel="noopener">{'كل التقييمات على Amazon.sa' if l=='ar' else 'All reviews on Amazon.sa'}</a></div>
</div></section>'''

def shopband(l,r):
    t=T[l]; tiles=''.join(f'<a href="{u[l]}" target="_blank" rel="noopener"><img src="{r}assets/up/{img}" alt="{t["buy"]} {n}" width="408" height="208"></a>' for img,u,n in SHOP)
    return f'''<section class="mt-section sx-shop" id="shop"><div class="container-xl text-center">
<h2 class="sx-shop-title">{t['shop']}</h2><div class="sx-shop-tiles">{tiles}</div></div></section>'''

def myth_cards(l,items):
    t=T[l]; return '<div class="sx-myths">'+''.join(f'<article class="sx-myth"><p class="sx-m"><b>{t["myth"]}</b>{m}</p><p class="sx-f"><b>{t["fact"]}</b>{f}</p></article>' for m,f in items)+'</div>'

def home(l):
    t=T[l]; r='' if l=='ar' else '../'
    pre_=('' if l=='ar' else '')
    bills=['Billboard_Darin_1920X1080px-SET01-1024x576.jpg','Billboard_Darin_1920X1080px-SET05-1024x576.jpg','Billboard_Darin_1920X1080px-SET06-1024x576.png','SET02-Billboard_Darin_1920X1080px-1024x576.jpg','SET03-Billboard_Darin_1920X1080px-1024x576.jpg','SET04-Billboard_Darin_1920X1080px-1024x576.jpg']
    gal=''.join(f'<div class="mt-gallery_item mt-gallery_{i+1}"><figure class="mt-thumb"><img src="{r}assets/up/{b}" alt="{t["alt_bill"]}" width="1024" height="576" loading="lazy"></figure></div>' for i,b in enumerate(bills))
    bands=''.join(band(l,p,r,f'product-{p["slug"]}.html') for p in PRODUCTS)
    body=f'''<section class="mt-banner_section">
<video src="{r}assets/up/SOFY-2048-x-858_80-sec-3.mp4" class="mt-video" id="videoPlayer" poster="{r}assets/up/SOFY-2048-x-858_cover-0.jpg" autoplay playsinline muted loop></video>
<button class="mt-sound" id="muteButton" aria-label="{t['mute']}"><img src="{r}assets/up/mute-plain.png" alt=""></button></section>
<section class="mt-section mt-hero_section mt-medium_pt mt-plain_bgr">
<figure class="mt-thumb mt-hero_thumb"><img src="{r}assets/up/darin.png" width="1784" height="1347" alt="{t['alt_darin']}"></figure>
<div class="container-xl"><div class="row align-items-center justify-content-start"><div class="col-12 col-md-9">
<h1 class="sx-h1">{t['h1']}<span>{t['h1b']}</span></h1>
</div></div></div></section>
<section class="mt-section mt-gallery_section mt-medium_pt"><div class="container-xl"><div class="mt-gallery_grid">{gal}</div></div></section>
{shopband(l,r)}
<div id="products">{bands}</div>
<section class="mt-section sx-guide mt-medium_pt mt-medium_pb" id="guide"><div class="container-xl">
<header class="mt-section_header text-center"><h2 class="mt-section_title">{t['guide_t']}</h2></header>
{myth_cards(l,MYTHS[l][:3])}
<div class="sx-cta"><a class="mt-btn" href="guide.html">{t['guide_cta']}</a></div></div></section>
{reviews(l)}
<div class="mt-medium_pt mt-medium_pb text-center"><a href="#" id="goTopBtn" class="mt-go_top" aria-label="{t['top']}"><img src="{r}assets/up/sofy-logo.png" alt="" width="160"></a></div>'''
    return page(l,0,'home',t['title'],t['desc'],body,'','en/')

def product(l,p):
    t=T[l]; r='' if l=='ar' else '../'
    cards=''.join(f'<article class="sx-size"><div class="sx-pack sx-pack-sm"><img src="{r}assets/up/{k["img"].format(l=l)}" alt="{p["name"][l]} {k["name"][l]}" loading="lazy"></div><h3>{k["name"][l]}</h3>{ret_links(l,k,r)}</article>' for k in p['packs'])
    paras=''.join(f'<p>{x}</p>' for x in p['body'][l])
    icons=''.join(f'<li><span class="sx-ic"><img src="{r}assets/img/{f}" alt="" width="120" height="120"></span><b>{n[l]}</b></li>' for f,n in p['icons'])
    body=f'''<section class="mt-section sx-pdp mt-small_pt"><div class="container-xl">
<nav class="sx-crumb"><a href="index.html">{t['home']}</a> / <span>{p['name'][l]}</span></nav>
<div class="sx-pdp-grid"><div class="sx-pack sx-pack-lg"><img src="{r}assets/up/{p['hero'].format(l=l)}" alt="{p['name'][l]}"></div>
<div class="sx-pdp-txt"><h1>{p['name'][l]}</h1><p class="sx-lead">{p['tag'][l]}</p>{paras}<ul class="sx-icons sx-icons-row">{icons}</ul></div></div></div></section>
<section class="mt-section sx-sizes mt-medium_pt mt-medium_pb"><div class="container-xl"><header class="mt-section_header text-center"><h2 class="mt-section_title">{t['sizes']}</h2></header>
<div class="sx-size-grid">{cards}</div></div></section>'''
    return page(l,0,'pdp',f'{p["name"][l]} | '+('سوفي العربية' if l=='ar' else 'Sofy Arabia'),p['tag'][l]+('. ' if l=='en' else '، ')+p['body'][l][0][:110],body,f'product-{p["slug"]}.html',f'en/product-{p["slug"]}.html')

def guide(l):
    t=T[l]; r='' if l=='ar' else '../'
    faq=''.join(f'<details class="sx-faq"><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ[l])
    body=f'''<section class="mt-section sx-guide mt-small_pt mt-medium_pb"><div class="container-xl">
<nav class="sx-crumb"><a href="index.html">{t['home']}</a> / <span>{t['guide_page']}</span></nav>
<h1 class="sx-page-h1">{t['guide_t']}</h1>{myth_cards(l,MYTHS[l])}</div></section>
<section class="mt-section sx-faqs mt-medium_pb"><div class="container-xl"><header class="mt-section_header text-center"><h2 class="mt-section_title">{t['faq_t']}</h2></header>{faq}</div></section>
<section class="mt-section mt-download_section mt-medium_pb"><div class="container-xl"><header class="mt-section_header text-center"><h2 class="mt-section_title">{t['dl_t']}</h2></header>
<div class="row g-5 justify-content-center"><div class="col-auto text-center"><a href="{r}assets/up/period-Info.pdf" class="mt-download_link"><img src="{r}assets/up/period_facts.png" width="400" height="400" alt=""><span>{t['dl1']} (PDF)</span></a></div>
<div class="col-auto text-center"><a href="{r}assets/up/MythFact.pdf" class="mt-download_link"><img src="{r}assets/up/facts_myth.png" width="400" height="400" alt=""><span>{t['dl2']} (PDF)</span></a></div></div></div></section>'''
    title=t['guide_page']+' | '+('سوفي العربية' if l=='ar' else 'Sofy Arabia')
    desc='خرافات وحقائق عن الدورة الشهرية وأسئلة شائعة عن منتجات سوفي أوليف.' if l=='ar' else 'Period myths and facts, plus answers to common questions about Sofy Olive products.'
    return page(l,0,'guide',title,desc,body,'guide.html','en/guide.html')

for l in ('ar','en'):
    d=OUT if l=='ar' else OUT+'/en'; os.makedirs(d,exist_ok=True)
    open(d+'/index.html','w').write(home(l)); open(d+'/guide.html','w').write(guide(l))
    for p in PRODUCTS: open(d+f'/product-{p["slug"]}.html','w').write(product(l,p))
open(OUT+'/robots.txt','w').write('User-agent: *\nDisallow: /\n')
print('built')
