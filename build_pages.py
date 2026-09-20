import os
OUT='/home/user/trojan-vpn'
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Luxurious+Roman&family=Instrument+Sans:wght@400;500&display=swap" rel="stylesheet">'
ARROW='<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 6h10M6.5 1.5 11 6l-4.5 4.5"/></svg>'
NAV=['Home','Servers','Pricing','Security','Download']
HREF={'Home':'index.html','Servers':'servers.html','Pricing':'pricing.html','Security':'security.html','Download':'download.html'}

def shell(slug,title,desc,body,current=None):
    links=''.join(f'<li><a href="{HREF[n]}"{" aria-current=\"page\"" if n==current else ""}>{n}</a></li>' for n in NAV)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Trojan VPN</title><meta name="description" content="{desc}"><meta property="og:type" content="website"><meta property="og:site_name" content="Trojan VPN"><meta property="og:title" content="{title} | Trojan VPN"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/og.jpg"><meta name="twitter:card" content="summary_large_image">
{FONTS}<link rel="stylesheet" href="site.css"></head>
<body>
<header class="nav">
  <a class="logo" href="index.html#statue">Trojan VPN <small>MMXXVI</small></a>
  <nav aria-label="Primary"><ul class="nav__links">{links}</ul></nav>
  <div class="nav__right"><a class="btn-play" href="pricing.html">Get protected</a>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button></div>
</header>
<main>
{body}
</main>
<footer class="foot">
  <div class="foot__word" aria-hidden="true">Trojan</div>
  <div class="foot__grid">
    <div class="foot__brand"><a class="logo" href="index.html#statue">Trojan VPN <small>MMXXVI</small></a>
      <p>Encrypts your connection, hides your address, remembers nothing. Named for Troy, the city that taught the world what a wall is for.</p>
      <form class="newsletter" data-fake onsubmit="return false"><input type="email" placeholder="Your email for dispatches" aria-label="Email"><button type="submit">Join</button></form></div>
    <div><h4>Product</h4><ul><li><a href="servers.html">Servers</a></li><li><a href="security.html">Security</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="download.html">Download</a></li></ul></div>
    <div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="audits.html">Audits</a></li><li><a href="transparency.html">Transparency report</a></li><li><a href="careers.html">Careers</a></li></ul></div>
    <div><h4>Legal</h4><ul><li><a href="privacy.html">Privacy policy</a></li><li><a href="terms.html">Terms</a></li><li><a href="canary.html">Warrant canary</a></li><li><a href="contact.html">Contact</a></li></ul></div>
  </div>
  <div class="foot__bar"><span>Trojan VPN, MMXXVI. All rights reserved.</span><span>Roma. Mumbai. New York.</span></div>
</footer>
<div class="menu" id="menu" aria-hidden="true">
  <button class="menu__close" type="button" aria-label="Close menu"><span></span><span></span></button>
  <ul class="menu__list"><li><a href="servers.html">Servers</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="security.html">Security</a></li><li><a href="download.html">Download</a></li></ul>
  <div class="menu__rule"></div><div class="menu__foot"><a class="btn-play" href="pricing.html">Get protected</a></div>
</div>
<script src="site.js"></script>
</body></html>'''

def phero(crumb,h1,p,img,word,meta=None):
    m=''
    if meta:
        m='<div class="phero__meta fx d2">'+''.join(f'<div><b>{v}</b><br>{k}</div>' for k,v in meta)+'</div>'
    return f'''<section class="phero">
  <div class="phero__bg" style="background-image:url('{img}')"></div><div class="phero__shade"></div>
  <div class="phero__word" aria-hidden="true">{word}</div>
  <div class="phero__row"><div>
    <p class="crumb fx"><a href="index.html">Trojan</a><span>{crumb}</span></p>
    <h1 class="fx d1">{h1}</h1>
    <p class="fx d2">{p}</p>
  </div>{m}</div>
</section>'''

def head(k,h,n=None):
    r=f'<div class="num-roman fx d2">{n}</div>' if n else ''
    return f'<div class="sec__head"><div><p class="kicker fx">{k}</p><h2 class="h2 fx d1">{h}</h2></div>{r}</div>'

pages={}

# ---------------- SERVERS ----------------
cities=[('Mumbai','IN',48,'12 ms'),('Chennai','IN',22,'9 ms'),('Delhi','IN',30,'31 ms'),('Singapore','SG',96,'54 ms'),('Tokyo','JP',88,'118 ms'),('Sydney','AU',64,'142 ms'),('Dubai','AE',40,'62 ms'),('Frankfurt','DE',210,'128 ms'),('Amsterdam','NL',150,'131 ms'),('London','GB',188,'135 ms'),('Roma','IT',72,'126 ms'),('Paris','FR',120,'130 ms'),('Zurich','CH',60,'127 ms'),('Stockholm','SE',54,'140 ms'),('New York','US',240,'196 ms'),('Los Angeles','US',170,'232 ms'),('Toronto','CA',90,'205 ms'),('Sao Paulo','BR',66,'300 ms'),('Johannesburg','ZA',36,'168 ms'),('Seoul','KR',70,'110 ms')]
rows=''.join(f'<li class="fx"><span class="i">{c[1]}</span><span class="t">{c[0]}</span><span class="r">{c[2]} servers · {c[3]}</span></li>' for c in cities)
pages['servers']=('Servers','The Trojan VPN network: 3,200 RAM-only servers across 94 cities and 41 nations.', 
 phero('Servers','All roads lead<br><em>wherever you point them.</em>','Rome built roads so a message could cross an empire without stopping. Ours run at 10 gigabits and never keep a diary. Connect to the nearest city for full speed, or pick another country and browse as if you lived there.','assets/gen-globe.webp','III',[('Servers','3,200+'),('Cities','94'),('Nations','41')])+
 f'''<section class="sec">{head('The network','Built for speed,<br><em>sworn to silence.</em>','III')}
 <div class="grid4">
  <div class="tile fx"><span class="tile__num">01</span><b data-count="3200">0<small>+</small></b><span class="lab">RAM only servers</span></div>
  <div class="tile fx d1"><span class="tile__num">02</span><b data-count="10">0<small> Gbps</small></b><span class="lab">Uplink per node</span></div>
  <div class="tile fx d2"><span class="tile__num">03</span><b data-count="99.98" data-dec="2">0<small>%</small></b><span class="lab">Uptime, trailing year</span></div>
  <div class="tile fx d3"><span class="tile__num">04</span><b data-count="0">0</b><span class="lab">Logs written, ever</span></div>
 </div></section>
 <section class="sec sec--alt"><div class="split">
  <div><p class="kicker fx">Latency from Nellore</p><h2 class="h2 fx d1">Every road,<br><em>measured.</em></h2>
  <p class="lead fx d2">Live figures from our nearest probe to you. Pick any city in the app to connect through it, or leave it on Auto and we choose the fastest server for you.</p>
  <div class="cta-row fx d3"><a class="btn-solid" href="download.html">Get the app {ARROW}</a><a class="link-plain" href="security.html">How routing stays private</a></div></div>
  <ul class="list">{rows}</ul>
 </div></section>
 <section class="sec"><div class="split split--rev">
  <figure class="fig fx"><img src="assets/gen-network.webp" alt="Marble bust of Mercury"><figcaption>Fig. 01, The Messenger</figcaption></figure>
  <div><p class="kicker fx">How a node is built</p><h2 class="h2 fx d1">Nothing touches<br><em>a disk.</em></h2>
  <ul class="steps fx d2" style="margin-top:2rem">
   <li><div><h4>Boot from a signed image</h4><p>Every server boots a read-only image we sign in Zurich. If the checksum differs by a single byte, the server refuses to go online.</p></div></li>
   <li><div><h4>Run entirely in memory</h4><p>No hard drive is mounted. Session state lives in RAM and vanishes on reboot or power loss.</p></div></li>
   <li><div><h4>Rotate keys hourly</h4><p>WireGuard keys are regenerated every hour, so even a captured node reveals nothing about earlier traffic.</p></div></li>
   <li><div><h4>Audit the fleet, not the story</h4><p>Independent auditors pick nodes at random each quarter and verify all of the above with root access.</p></div></li>
  </ul></div>
 </div></section>
 <section class="band"><div class="bg" style="background-image:url('assets/gen-forum.webp')"></div><blockquote class="quote fx"><p>"All roads lead to Rome. Ours just <em>refuse to remember</em> who walked them."</p><cite>From the Trojan engineering handbook</cite></blockquote></section>''','Servers')

# ---------------- SECURITY ----------------
pages['security']=('Security','How Trojan VPN protects you: AES-256, WireGuard, RAM-only servers, kill switch and the obfuscated Trojan protocol.',
 phero('Security','Walls you can<br><em>inspect yourself.</em>','Troy fell to a gift, not a siege. So we obsess over the gate: what gets in, what gets out, and what is left behind. Here is every layer, in the order an attacker would meet it.','assets/gen-shield.webp','IV',[('Cipher','AES-256'),('Protocol','WireGuard'),('Logs','None')])+
 f'''<section class="sec">{head('The armour','Five layers between<br>you and <em>the watchers.</em>','IV')}
 <div class="grid3">
  <div class="tile fx"><span class="tile__num">I</span><h3>AES-256-GCM and ChaCha20</h3><p>State-grade ciphers over WireGuard, with perfect forward secrecy. Keys rotate hourly and never touch a disk.</p></div>
  <div class="tile fx d1"><span class="tile__num">II</span><h3>Strict no log policy</h3><p>No browsing history, no connection timestamps, no source IPs, no bandwidth per user. Verified by independent audit.</p></div>
  <div class="tile fx d2"><span class="tile__num">III</span><h3>Kill switch and leak guard</h3><p>If the tunnel falters the gates close. Traffic is blocked at the system level. DNS, IPv6 and WebRTC leaks sealed by default.</p></div>
  <div class="tile fx d3"><span class="tile__num">IV</span><h3>Stealth mode</h3><p>Our namesake. Traffic is wrapped to look like ordinary HTTPS so deep packet inspection sees nothing but browsing.</p></div>
  <div class="tile fx d4"><span class="tile__num">V</span><h3>Open source, openly audited</h3><p>Apps and protocol are public. Professionals are paid to break them and reports are published in full.</p></div>
  <div class="tile fx d4"><span class="tile__num">VI</span><h3>Private DNS</h3><p>Every query resolves on our own encrypted resolvers inside the tunnel. Nothing leaves in the clear.</p></div>
 </div></section>
 <section class="sec sec--alt"><div class="split">
  <div><p class="kicker fx">The Trojan protocol</p><h2 class="h2 fx d1">Hidden in<br><em>plain sight.</em></h2>
  <p class="lead fx d2">Most VPNs are easy to spot on the wire, which is why restrictive networks block them. Trojan wraps WireGuard inside a TLS session that is indistinguishable from a visit to any ordinary website. The censor sees traffic to a web server. Inside, your traffic moves.</p>
  <div class="cta-row fx d3"><a class="btn-solid" href="audits.html">Read the audits {ARROW}</a><a class="link-plain" href="https://github.com" target="_blank" rel="noopener">Source code</a></div></div>
  <ul class="acc fx d1">
   <li class="is-open"><button type="button" aria-expanded="true"><span class="i">01</span>What exactly do you not log?<span class="plus"></span></button><div class="acc__body"><div><p>Your real IP, the servers you connect to, timestamps, DNS queries, the sites you visit, and per-user bandwidth. We keep aggregate load per server, nothing tied to a person.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">02</span>What happens if a server is seized?<span class="plus"></span></button><div class="acc__body"><div><p>It powers off. Because it runs from RAM with no disk, the seizing party receives a blank machine. This has happened once, in 2024, and we published the outcome in the transparency report.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">03</span>Do you use RAM-only servers everywhere?<span class="plus"></span></button><div class="acc__body"><div><p>Yes. Every node in all 94 cities boots from a signed read-only image and mounts no persistent storage.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">04</span>Where is Trojan based?<span class="plus"></span></button><div class="acc__body"><div><p>Trojan Privacy AG is incorporated in Zurich, Switzerland, outside the Five Eyes and Fourteen Eyes agreements and with no mandatory data retention law for VPNs.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">05</span>Is the code really open?<span class="plus"></span></button><div class="acc__body"><div><p>All client apps and the protocol implementation are on GitHub under the GPL. Server orchestration is private for operational security but is in scope for every audit.</p></div></div></li>
  </ul>
 </div></section>
 <section class="sec"><div class="split split--rev">
  <figure class="fig fx"><img src="assets/gen-helmet.webp" alt="Marble Roman helmet"><figcaption>Fig. 02, The Helmet</figcaption></figure>
  <div><p class="kicker fx">Threat model</p><h2 class="h2 fx d1">Who we<br><em>defend against.</em></h2>
  <ul class="list fx d2" style="margin-top:2rem">
   <li><span class="i">A</span><span class="t">Your ISP and mobile carrier</span><span class="r">Sees only a tunnel</span></li>
   <li><span class="i">B</span><span class="t">Public Wi-Fi operators</span><span class="r">Sees encrypted noise</span></li>
   <li><span class="i">C</span><span class="t">Advertisers and trackers</span><span class="r">Lose your real IP</span></li>
   <li><span class="i">D</span><span class="t">Censors and DPI systems</span><span class="r">See ordinary HTTPS</span></li>
   <li><span class="i">E</span><span class="t">Us</span><span class="r">Nothing to hand over</span></li>
  </ul></div>
 </div></section>''','Security')

# ---------------- PRICING ----------------
pages['pricing']=('Pricing','Trojan VPN plans: Citizen, Senator and Emperor. 30 day money back guarantee.',
 phero('Pricing','One wall.<br><em>Choose how many stand behind it.</em>','Every plan gets every server, every feature and the same promise to remember nothing. The only thing that changes is how many devices come with you. Thirty days to decide, full refund if not.','assets/gen-laurel.webp','V')+
 f'''<section class="sec">
 <div class="sec__head"><div><p class="kicker fx">Choose your rank</p><h2 class="h2 fx d1">Simple tribute,<br><em>no hidden tax.</em></h2></div>
  <div class="toggle fx d2"><button class="is-on" data-mode="two">2 years</button><button data-mode="one">1 year</button><button data-mode="mo">Monthly</button></div></div>
 <div class="plans">
  <div class="plan fx"><h3>Citizen</h3><div class="price">$<span data-m data-two="2.99" data-one="4.49" data-mo="9.99">2.99</span><small>/ month</small></div><div class="bill" data-m data-two="Billed $71.76 every 2 years" data-one="Billed $53.88 yearly" data-mo="Billed monthly">Billed $71.76 every 2 years</div>
   <ul><li>All 3,200+ servers</li><li>5 devices at once</li><li>AES-256 and WireGuard</li><li>Kill switch and leak guard</li><li>Private DNS</li><li>24/7 support</li></ul><a class="btn-outline" href="download.html">Choose Citizen</a></div>
  <div class="plan plan--hero fx d1"><span class="plan__tag">Most chosen</span><h3>Senator</h3><div class="price">$<span data-m data-two="3.49" data-one="5.29" data-mo="11.99">3.49</span><small>/ month</small></div><div class="bill" data-m data-two="Billed $83.76 every 2 years" data-one="Billed $63.48 yearly" data-mo="Billed monthly">Billed $83.76 every 2 years</div>
   <ul><li>Everything in Citizen</li><li>10 devices at once</li><li>Stealth mode</li><li>Multi-hop routes</li><li>Dedicated IP add on</li><li>Priority support</li></ul><a class="btn-outline" href="download.html">Choose Senator</a></div>
  <div class="plan fx d2"><h3>Emperor</h3><div class="price">$<span data-m data-two="4.99" data-one="6.99" data-mo="14.99">4.99</span><small>/ month</small></div><div class="bill" data-m data-two="Billed $119.76 every 2 years" data-one="Billed $83.88 yearly" data-mo="Billed monthly">Billed $119.76 every 2 years</div>
   <ul><li>Everything in Senator</li><li>Unlimited devices</li><li>Encrypted password vault</li><li>Breach monitoring</li><li>Family sharing for 6</li><li>Router firmware support</li></ul><a class="btn-outline" href="download.html">Choose Emperor</a></div>
 </div>
 <p class="fx d3" style="text-align:center;margin-top:1.8rem;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(233,228,216,.45)">30 day money back guarantee. Cards, UPI, PayPal and Monero accepted.</p>
 </section>
 <section class="sec sec--alt">{head('Compare','Every rank,<br><em>side by side.</em>')}
 <div class="fx" style="overflow:auto"><table class="cmp">
  <tr><th></th><th>Citizen</th><th>Senator</th><th>Emperor</th></tr>
  <tr><td>Servers in 94 cities</td><td class="ok">Yes</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
  <tr><td>Devices at once</td><td>5</td><td>10</td><td>Unlimited</td></tr>
  <tr><td>WireGuard and AES-256</td><td class="ok">Yes</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
  <tr><td>Stealth mode</td><td class="no">No</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
  <tr><td>Multi-hop</td><td class="no">No</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
  <tr><td>Dedicated IP</td><td class="no">No</td><td>Add on</td><td>Included</td></tr>
  <tr><td>Password vault</td><td class="no">No</td><td class="no">No</td><td class="ok">Yes</td></tr>
  <tr><td>Breach monitoring</td><td class="no">No</td><td class="no">No</td><td class="ok">Yes</td></tr>
  <tr><td>Support</td><td>24/7 chat</td><td>Priority</td><td>Priority</td></tr>
 </table></div></section>
 <section class="sec"><div class="split">
  <div><p class="kicker fx">Questions</p><h2 class="h2 fx d1">Before you<br><em>swear in.</em></h2></div>
  <ul class="acc fx d1">
   <li class="is-open"><button type="button" aria-expanded="true"><span class="i">01</span>Can I pay anonymously?<span class="plus"></span></button><div class="acc__body"><div><p>Yes. We accept Monero and cash by post. Accounts are identified by a random number, not an email, unless you choose to add one for recovery.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">02</span>How does the refund work?<span class="plus"></span></button><div class="acc__body"><div><p>Ask within 30 days and we refund in full, no questions. Crypto refunds are paid at the original fiat value.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">03</span>Can I upgrade later?<span class="plus"></span></button><div class="acc__body"><div><p>Any time. You pay only the prorated difference for the remaining term.</p></div></div></li>
   <li><button type="button" aria-expanded="false"><span class="i">04</span>Is there a free trial?<span class="plus"></span></button><div class="acc__body"><div><p>Not a free tier, because free VPNs pay their bills with your data. The 30 day guarantee is our trial.</p></div></div></li>
  </ul></div></section>''','Pricing')

# ---------------- DOWNLOAD ----------------
plat=[('macOS','13 Ventura or later','<path d="M16.5 3c.1 1.4-.5 2.6-1.4 3.5-.9.9-2.2 1.4-3.4 1.3-.1-1.3.5-2.6 1.4-3.5C14 3.4 15.3 2.9 16.5 3zM19.8 17.3c-.6 1.4-1.4 2.7-2.5 3.7-.8.7-1.7.9-2.7.5-.9-.4-1.8-.4-2.8 0-1 .4-1.9.3-2.7-.5-2.6-2.5-4.1-7.7-1.6-11 1.1-1.5 3-2 4.4-1.4.9.4 1.7.4 2.6 0 1.7-.7 3.5-.2 4.6 1.3-2.8 1.8-2.3 5.6.7 7.4z"/>'),
('Windows','10 and 11','<path d="M3 5.5 11 4.4v7.1H3zM12 4.2 21 3v8.5h-9zM3 12.5h8v7.1L3 18.5zM12 12.5h9V21l-9-1.2z"/>'),
('Android','9 or later','<path d="M6 9.5a6 6 0 0 1 12 0V17H6zM6 17h12M4 10l2-1M20 10l-2-1M8 3l1.5 2.5M16 3l-1.5 2.5"/>'),
('iOS','iOS 16 or later','<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18.5h2"/>'),
('Linux','deb, rpm, AUR','<path d="M12 3c-3 0-4.5 2.5-4.5 5.5 0 2-1.5 3.5-2.5 5.5-.8 1.7 0 3.5 1.5 4.5 1.3.8 2.5.3 3.5-.5h4c1 .8 2.2 1.3 3.5.5 1.5-1 2.3-2.8 1.5-4.5-1-2-2.5-3.5-2.5-5.5C16.5 5.5 15 3 12 3z"/>'),
('Router','OpenWrt, ASUS, pfSense','<rect x="3" y="14" width="18" height="6" rx="1"/><path d="M7 14V9M12 14V4M17 14V9M6.5 17h.01M9.5 17h.01"/>')]
ptiles=''.join(f'<a class="platform fx d{i%4}" href="#"><svg viewBox="0 0 24 24">{svg}</svg><span>{n}</span><small>{v}</small></a>' for i,(n,v,svg) in enumerate(plat))
pages['download']=('Download','Download Trojan VPN for macOS, Windows, Android, iOS, Linux and routers.',
 phero('Download','Carry the wall<br><em>with you.</em>','Mac, Windows, Android, iOS, Linux, browser extensions, and a router setup that covers everything in the house. One account, and then you stop thinking about it.','assets/gen-forum.webp','VI',[('Platforms','6'),('Version','4.2'),('Size','38 MB')])+
 f'''<section class="sec">{head('Apps','Pick your<br><em>gate.</em>','VI')}<div class="platforms">{ptiles}</div>
 <div class="cta-row fx d3" style="justify-content:center"><a class="link-plain" href="#">Browser extensions for Chrome, Firefox and Safari</a><a class="link-plain" href="#">Verify signatures (PGP)</a></div></section>
 <section class="sec sec--alt"><div class="split">
  <div><p class="kicker fx">Three steps</p><h2 class="h2 fx d1">From download<br>to <em>unseen.</em></h2>
  <ol class="steps fx d2" style="margin-top:2rem">
   <li><div><h4>Install the app</h4><p>Download for your platform above. The installer is signed and reproducible; the checksum is printed on this page and in the PGP file.</p></div></li>
   <li><div><h4>Sign in with your account number</h4><p>No email needed. Your 16 digit number is the only credential. Keep it somewhere safe.</p></div></li>
   <li><div><h4>Press connect</h4><p>We pick the fastest server automatically. Choose a city if you prefer, or turn on Stealth mode if your network blocks VPNs.</p></div></li>
  </ol></div>
  <figure class="fig fx"><img src="assets/gen-scroll.webp" alt="Sealed scroll on marble"><figcaption>Fig. 03, The Dispatch</figcaption></figure>
 </div></section>
 <section class="sec"><div class="split split--rev">
  <div class="canary fx">SHA-256 checksums, v4.2.0

macOS     3f9a2c7e0b1d4a6f8e2c1b0a9d8e7f6c5b4a3d2e1f0a9b8c7d6e5f4a3b2c1d0e
Windows   a1b2c3d4e5f60718293a4b5c6d7e8f90a1b2c3d4e5f60718293a4b5c6d7e8f90
Android   9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d
Linux     5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b

Signing key: 0xC0FFEE42 TROJAN (release) &lt;release@trojanvpn.example&gt;</div>
  <div><p class="kicker fx">Verify</p><h2 class="h2 fx d1">Trust, but<br><em>check the seal.</em></h2><p class="lead fx d2">Every build is reproducible and signed. Compare the checksum of your download to the list here or on our GitHub releases page before installing.</p>
  <div class="cta-row fx d3"><a class="btn-solid" href="pricing.html">Get an account {ARROW}</a></div></div>
 </div></section>''','Download')

# ---------------- ABOUT ----------------
pages['about']=('About','Trojan VPN is a Swiss privacy company. Ancient discipline, modern encryption.',
 phero('About','Named for the city<br><em>that held ten years.</em>','Trojan was founded in 2021 by three engineers who kept getting asked the same question by friends abroad: which VPN can I actually trust? None of the answers held up. So we built one whose word could be checked.','assets/gen-forum.webp','I',[('Founded','2021'),('Based','Zurich'),('People','46')])+
 f'''<section class="sec"><div class="split">
  <div><p class="kicker fx">Principles</p><h2 class="h2 fx d1">Carved,<br><em>not written.</em></h2></div>
  <ul class="list fx d1">
   <li><span class="i">I</span><span class="t">Keep nothing</span><span class="d">If we do not have it, we cannot lose it, sell it or be forced to hand it over. Every design decision starts here.</span></li>
   <li><span class="i">II</span><span class="t">Show the work</span><span class="d">Open code, public audits, a warrant canary and a transparency report twice a year.</span></li>
   <li><span class="i">III</span><span class="t">Charge money</span><span class="d">We are paid by our users and no one else. There is no free tier because free is never free.</span></li>
   <li><span class="i">IV</span><span class="t">Stay small</span><span class="d">Forty six people. Enough to run the service well, few enough that everyone knows why we do it.</span></li>
  </ul></div></section>
 <section class="sec sec--alt">{head('The road so far','A short<br><em>history.</em>')}
 <ul class="tl fx d1">
  <li><small>MMXXI</small><b>Founded in Zurich</b><p>Three engineers, one rented rack, and a promise written on the whiteboard: keep nothing.</p></li>
  <li><small>MMXXII</small><b>First audit passed</b><p>Cure53 reviewed the apps and infrastructure. Every finding was fixed and published.</p></li>
  <li><small>MMXXIII</small><b>The Trojan protocol ships</b><p>Our obfuscation layer goes live, opening the network to users behind national firewalls.</p></li>
  <li><small>MMXXIV</small><b>A server is seized</b><p>Authorities took a node in a European city. It held nothing. We published the full story.</p></li>
  <li><small>MMXXV</small><b>3,000 servers, 41 nations</b><p>The network doubles. Memory-only servers become standard across the whole fleet.</p></li>
  <li><small>MMXXVI</small><b>Today</b><p>Half a million citizens, senators and emperors move unseen every day.</p></li>
 </ul></section>
 <section class="sec">{head('The council','Who stands<br><em>at the gate.</em>')}
 <div class="team">
  <div class="person fx" data-init="LV"><b>Livia Varga</b><span>Chief executive</span></div>
  <div class="person fx d1" data-init="MA"><b>Marcus Adler</b><span>Chief technology</span></div>
  <div class="person fx d2" data-init="AR"><b>Anjali Rao</b><span>Head of infrastructure</span></div>
  <div class="person fx d3" data-init="TB"><b>Tomas Brenner</b><span>Head of security</span></div>
 </div>
 <div class="cta-row fx d3"><a class="btn-solid" href="careers.html">See open roles {ARROW}</a><a class="link-plain" href="contact.html">Contact us</a></div></section>''')

# ---------------- AUDITS ----------------
pages['audits']=('Audits','Independent security audits of Trojan VPN, published in full.',
 phero('Audits','Tested by people<br>paid to <em>break us.</em>','Every year we hire independent firms to attack our apps, servers and claims, then publish what they found without edits. Here is every report.','assets/gen-shield.webp','IV',[('Audits','7'),('Open findings','0'),('Last','Jun 2026')])+
 f'''<section class="sec">{head('Reports','Every finding,<br><em>every fix.</em>')}
 <ul class="list">
  <li class="fx"><span class="i">07</span><span class="t">Infrastructure and no log verification</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Securitum, June 2026. Random node sampling with root access across 12 cities. Confirmed RAM-only operation and absence of user logs. 2 low findings, both fixed.</span></li>
  <li class="fx"><span class="i">06</span><span class="t">Trojan protocol cryptographic review</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Cure53, January 2026. Review of the obfuscation layer and handshake. 1 medium finding regarding timing side channel, fixed in v4.1.</span></li>
  <li class="fx"><span class="i">05</span><span class="t">Desktop and mobile apps</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Cure53, July 2025. Full source review of macOS, Windows, Linux, iOS and Android clients. 4 low findings, all fixed.</span></li>
  <li class="fx"><span class="i">04</span><span class="t">No log policy verification</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Deloitte, February 2025. Assurance engagement on the no log claim against ISAE 3000.</span></li>
  <li class="fx"><span class="i">03</span><span class="t">Browser extensions</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Radically Open Security, September 2024. 1 medium finding in WebRTC handling, fixed.</span></li>
  <li class="fx"><span class="i">02</span><span class="t">Infrastructure</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Cure53, March 2024. First fleet-wide review after RAM-only rollout.</span></li>
  <li class="fx"><span class="i">01</span><span class="t">Initial application audit</span><span class="r"><span class="tag tag--ok">Passed</span></span><span class="d">Cure53, August 2022. 9 findings including 1 high in the kill switch, fixed before public launch.</span></li>
 </ul>
 <div class="cta-row fx"><a class="btn-outline" href="#">Download all reports (PDF)</a><a class="link-plain" href="canary.html">Warrant canary</a></div></section>
 <section class="band"><div class="bg" style="background-image:url('assets/gen-laurel.webp')"></div><blockquote class="quote fx"><p>"A claim you cannot verify is <em>a rumour</em>. We publish so you never have to take our word."</p><cite>Tomas Brenner, head of security</cite></blockquote></section>''')

# ---------------- TRANSPARENCY ----------------
pages['transparency']=('Transparency report','Requests received by Trojan VPN and what we were able to provide: nothing.',
 phero('Transparency','What they asked.<br><em>What we had.</em>','Twice a year we publish every legal request received, from whom, and what we handed over. The last column has never changed.','assets/gen-scroll.webp','II',[('Requests, H1 2026','23'),('Data provided','0'),('Servers seized','0')])+
 f'''<section class="sec">{head('H1 2026','January to <em>June.</em>')}
 <div class="grid4">
  <div class="tile fx"><span class="tile__num">Requests</span><b data-count="23">0</b><span class="lab">Total received</span></div>
  <div class="tile fx d1"><span class="tile__num">Court orders</span><b data-count="6">0</b><span class="lab">From 4 jurisdictions</span></div>
  <div class="tile fx d2"><span class="tile__num">DMCA notices</span><b data-count="17">0</b><span class="lab">All answered, none actionable</span></div>
  <div class="tile fx d3"><span class="tile__num">Provided</span><b data-count="0">0</b><span class="lab">Bytes of user data</span></div>
 </div>
 <div class="split" style="margin-top:4rem"><div class="prose fx">
  <h2>How we respond</h2><p>Every request is reviewed by outside counsel in Zurich. Where a request is valid under Swiss law we reply truthfully: we hold no data that identifies a user or their activity. Where a request is not valid, we say so and publish it here.</p>
  <h2>Seizures</h2><p>No hardware was seized in this period. The single seizure in our history, in 2024, yielded nothing because the node ran from memory. The report for that period describes the event in full.</p>
  <h2>Gag orders</h2><p>We have never received a gag order. If we do, the warrant canary will stop being renewed.</p>
 </div><ul class="tl fx d1"><li><small>Previous reports</small><b>H2 2025</b><p>19 requests, 0 provided.</p></li><li><b>H1 2025</b><p>14 requests, 0 provided.</p></li><li><b>H2 2024</b><p>11 requests, 1 server seized, 0 provided.</p></li><li><b>H1 2024</b><p>8 requests, 0 provided.</p></li></ul></div></section>''')

# ---------------- CAREERS ----------------
pages['careers']=('Careers','Join Trojan VPN. Remote first, based in Zurich.',
 phero('Careers','Help hold<br><em>the wall.</em>','Forty six people across nine countries, remote first, paid in the top quartile, and asked to do one thing well: keep nothing.','assets/gen-helmet.webp','VII',[('Open roles','5'),('Countries','9'),('Remote','Yes')])+
 f'''<section class="sec">{head('Open roles','Who we are<br><em>looking for.</em>')}
 <ul class="list">
  <li class="fx"><span class="i">01</span><span class="t">Senior network engineer</span><span class="r">Remote, Europe or India</span><span class="d">Own the fleet. WireGuard, BGP, and the discipline to never mount a disk.</span></li>
  <li class="fx"><span class="i">02</span><span class="t">iOS engineer</span><span class="r">Remote, any timezone</span><span class="d">Swift, Network Extension framework, and an eye for detail that matches the marble.</span></li>
  <li class="fx"><span class="i">03</span><span class="t">Cryptography engineer</span><span class="r">Zurich or remote</span><span class="d">Evolve the Trojan protocol against the next generation of DPI.</span></li>
  <li class="fx"><span class="i">04</span><span class="t">Support specialist, India</span><span class="r">Remote, India</span><span class="d">Front line for our fastest growing region. Hindi, Telugu or Tamil plus English.</span></li>
  <li class="fx"><span class="i">05</span><span class="t">Brand designer</span><span class="r">Remote, Europe</span><span class="d">You saw the homepage. Make the rest of the site look like that.</span></li>
 </ul></section>
 <section class="sec sec--alt"><div class="split">
  <div><p class="kicker fx">Why here</p><h2 class="h2 fx d1">The<br><em>terms.</em></h2></div>
  <div class="grid2 fx d1">
   <div class="tile"><h3>Remote first</h3><p>Work from anywhere. We meet in Zurich twice a year.</p></div>
   <div class="tile"><h3>Top quartile pay</h3><p>Benchmarked to Swiss rates regardless of where you live.</p></div>
   <div class="tile"><h3>Four day weeks</h3><p>Thirty two hours, full pay. Rested people do better work.</p></div>
   <div class="tile"><h3>Open by default</h3><p>Salaries, decisions and audits are visible to everyone inside.</p></div>
  </div></div>
 <div class="cta-row fx d2"><a class="btn-solid" href="contact.html">Apply {ARROW}</a></div></section>''')

# ---------------- CONTACT ----------------
pages['contact']=('Contact','Contact Trojan VPN. Support, press, security disclosures.',
 phero('Contact','Send word.<br><em>We answer.</em>','Support answers around the clock. Press and security reports go to the people below. Nothing you send here is logged beyond the reply.','assets/gen-scroll.webp','VIII')+
 f'''<section class="sec"><div class="split">
  <form class="form fx" data-fake>
   <div class="field"><label for="n">Name or account number</label><input id="n" placeholder="Optional"></div>
   <div class="field"><label for="e">Reply address</label><input id="e" type="email" placeholder="you@example.com"></div>
   <div class="field"><label for="s">Subject</label><select id="s"><option>Support</option><option>Billing</option><option>Press</option><option>Security disclosure</option><option>Careers</option></select></div>
   <div class="field"><label for="m">Message</label><textarea id="m"></textarea></div>
   <div class="notice">Messages are encrypted in transit and deleted 30 days after the thread closes.</div>
   <div><button class="btn-solid" type="submit">Send {ARROW}</button></div>
  </form>
  <div>
   <ul class="list fx d1">
    <li><span class="i">A</span><span class="t">Support</span><span class="r">24/7</span><span class="d">support@trojanvpn.example, or the chat inside the app.</span></li>
    <li><span class="i">B</span><span class="t">Security disclosures</span><span class="r">PGP 0xC0FFEE42</span><span class="d">security@trojanvpn.example. Bounties from $500 to $25,000.</span></li>
    <li><span class="i">C</span><span class="t">Press</span><span class="r">Within one day</span><span class="d">press@trojanvpn.example</span></li>
    <li><span class="i">D</span><span class="t">Post</span><span class="r">Zurich</span><span class="d">Trojan Privacy AG, Bahnhofstrasse 100, 8001 Zurich, Switzerland</span></li>
   </ul>
  </div></div></section>''')

# ---------------- LEGAL ----------------
def legal(slug,title,intro,sections,img,word):
    toc=''.join(f'<li><a href="#s{i}">{t}</a></li>' for i,(t,_) in enumerate(sections))
    body=''.join(f'<h2 id="s{i}">{t}</h2>{p}' for i,(t,p) in enumerate(sections))
    return (title,intro,phero('Legal',title.replace(' ','<br>',1) if ' ' in title else title,intro,img,word)+
      f'<section class="sec"><div class="split" style="align-items:start;grid-template-columns:14rem 1fr"><ul class="toc fx">{toc}</ul><div class="prose fx d1">{body}<p style="margin-top:3rem;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(233,228,216,.45)">Last updated 1 September 2026</p></div></div></section>')

pages['privacy']=legal('privacy','Privacy policy','The short version: we do not collect what we do not need, and we need almost nothing.',[
 ('What we collect','<p>An account number generated at signup. If you choose, an email for recovery. Payment records held by the processor, not linked to your activity.</p>'),
 ('What we never collect','<ul><li>Your browsing history or DNS queries</li><li>Your real IP address after connection</li><li>Connection timestamps or session duration</li><li>Bandwidth per user</li></ul>'),
 ('How servers work','<p>All servers run from memory with no persistent storage. Rebooting a server erases everything on it.</p>'),
 ('Cookies','<p>This website sets one cookie to remember your pricing currency. No analytics scripts, no advertising pixels.</p>'),
 ('Your rights','<p>Under Swiss and EU law you may ask what we hold about you. The answer will be short. Delete your account at any time from the app.</p>'),
 ('Changes','<p>Changes are announced 30 days ahead on this page and in the transparency report.</p>')],'assets/gen-scroll.webp','LEX')

pages['terms']=legal('terms','Terms of service','Plain terms for a plain promise.',[
 ('The service','<p>Trojan Privacy AG provides encrypted network access. You may use it on the number of devices your plan allows.</p>'),
 ('Acceptable use','<p>Do not use the service to attack others, send spam, or break the law where you live. We cannot see what you do, but we will terminate accounts reported for abuse with credible evidence.</p>'),
 ('Payment and refunds','<p>Plans renew automatically unless cancelled. Any plan may be refunded in full within 30 days of purchase.</p>'),
 ('Availability','<p>We target 99.9 percent uptime and publish real figures on the servers page. No service is perfect; we do not promise otherwise.</p>'),
 ('Liability','<p>To the extent permitted by Swiss law, our liability is limited to the fees you paid in the previous twelve months.</p>'),
 ('Governing law','<p>Swiss law, courts of Zurich.</p>')],'assets/gen-forum.webp','LEX')

pages['canary']=('Warrant canary','Trojan VPN warrant canary, renewed on the first of every month.',
 phero('Legal','The canary<br><em>still sings.</em>','On the first day of every month we sign a statement that we have received no secret orders. If this page ever goes stale, assume the worst.','assets/gen-laurel.webp','IX',[('Renewed','1 Sep 2026'),('Next','1 Oct 2026'),('Status','Alive')])+
 '''<section class="sec"><div class="split" style="align-items:start">
 <div class="canary fx">-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Trojan Privacy AG warrant canary
Date: 2026-09-01

As of the date above, Trojan Privacy AG has:

  * never received a national security letter
  * never received a gag order of any kind
  * never been compelled to modify its software or infrastructure
  * never handed any user data to any party
  * never had a server compromised to our knowledge

Servers seized to date: 1 (2024, no data recovered)

This notice will be renewed on the first day of each month.

Proof of freshness:
Bitcoin block 912,344 hash 0000000000000000000212ab...e4f1
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCgAdFiEEc0ffee42...
-----END PGP SIGNATURE-----</div>
 <div class="prose fx d1"><h2>How to read this</h2><p>A warrant canary is a statement that something has not happened. Law can forbid us from telling you about a secret order, but it cannot easily compel us to lie and renew a statement that is no longer true.</p><h2>Verify it</h2><p>Check the PGP signature against key 0xC0FFEE42, published on our GitHub and on keys.openpgp.org. The Bitcoin block hash proves the statement was written after that block was mined.</p><h2>If it stops</h2><p>If this page is not renewed within seven days of the first of the month, treat the service as compromised and assume we were prevented from speaking.</p></div>
 </div></section>''')

for slug,(title,desc,body,*cur) in pages.items():
    html=shell(slug,title,desc,body,cur[0] if cur else None)
    open(os.path.join(OUT,slug+'.html'),'w').write(html)
    print('wrote',slug+'.html')
