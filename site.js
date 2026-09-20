(function(){
  /* mobile menu */
  var burger=document.querySelector('.burger'), menu=document.getElementById('menu');
  function setMenu(open){
    if(!menu) return;
    menu.classList.toggle('is-open',open);
    menu.setAttribute('aria-hidden',String(!open));
    burger.setAttribute('aria-expanded',String(open));
    burger.setAttribute('aria-label',open?'Close menu':'Open menu');
    document.body.classList.toggle('menu-open',open);
  }
  if(burger){ burger.addEventListener('click',function(){ setMenu(!menu.classList.contains('is-open')); });
    var mc=menu.querySelector('.menu__close'); if(mc) mc.addEventListener('click',function(){ setMenu(false); });
    menu.addEventListener('click',function(e){ if(e.target===menu) setMenu(false); }); }
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') setMenu(false); });

  /* scroll reveal */
  var io=new IntersectionObserver(function(es){es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });},{threshold:.12});
  document.querySelectorAll('.fx').forEach(function(el){ io.observe(el); });

  /* accordions */
  document.querySelectorAll('.acc').forEach(function(acc){
    acc.querySelectorAll(':scope > li > button').forEach(function(btn){
      btn.addEventListener('click',function(){
        var li=btn.parentElement, open=li.classList.contains('is-open');
        acc.querySelectorAll(':scope > li').forEach(function(x){ x.classList.remove('is-open'); x.querySelector('button').setAttribute('aria-expanded','false'); });
        if(!open){ li.classList.add('is-open'); btn.setAttribute('aria-expanded','true'); }
      });
    });
  });

  /* count up */
  var cio=new IntersectionObserver(function(es){es.forEach(function(e){
    if(!e.isIntersecting) return; cio.unobserve(e.target);
    var el=e.target, target=+el.getAttribute('data-count'), t0=null, dec=el.getAttribute('data-dec')|0;
    function step(ts){ if(!t0) t0=ts; var k=Math.min(1,(ts-t0)/1600); k=1-Math.pow(1-k,3);
      el.firstChild.nodeValue=(target*k).toLocaleString(undefined,{minimumFractionDigits:dec,maximumFractionDigits:dec}); if(k<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  });},{threshold:.5});
  document.querySelectorAll('[data-count]').forEach(function(el){ cio.observe(el); });

  /* pricing toggle */
  var tg=document.querySelector('.toggle');
  if(tg){
    tg.querySelectorAll('button').forEach(function(b){
      b.addEventListener('click',function(){
        tg.querySelectorAll('button').forEach(function(x){x.classList.remove('is-on')}); b.classList.add('is-on');
        var mode=b.getAttribute('data-mode');
        document.querySelectorAll('[data-m]').forEach(function(el){ el.textContent=el.getAttribute('data-'+mode); });
      });
    });
  }

  /* fake forms */
  document.querySelectorAll('form[data-fake]').forEach(function(f){
    f.addEventListener('submit',function(e){ e.preventDefault(); var n=f.querySelector('.notice'); if(n){ n.textContent='Received. A courier will reply within one day.'; n.style.borderColor='var(--gold)'; } });
  });
})();

/* Exhibits: 3D objects with pins, scroll-driven turn, graceful fallback */
(function(){
  var exs=document.querySelectorAll('.exhibit'); if(!exs.length) return;
  var canGL=(function(){try{var c=document.createElement('canvas');return !!(c.getContext('webgl2')||c.getContext('webgl'));}catch(e){return false;}})();
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  exs.forEach(function(ex){
    var mv=ex.querySelector('model-viewer'); if(!mv) return;
    var cap=ex.querySelector('.exhibit__caption');
    function fallback(){ ex.classList.add('exhibit--fallback'); }
    if(!canGL||!('customElements' in window)){ fallback(); return; }
    fetch(mv.getAttribute('src'),{method:'HEAD'}).then(function(r){ if(!r.ok) fallback(); }).catch(fallback);
    mv.addEventListener('error',fallback);
    mv.addEventListener('load',function(){ mv.classList.add('is-ready'); });
    var base=parseFloat(mv.dataset.base||'-30'), turn=parseFloat(mv.dataset.turn||'220');
    var cur=base,target=base,raf=0,userOffset=0;
    function unclip(){ var sr=mv.shadowRoot; if(!sr||sr.querySelector('#unclip')) return; var s=document.createElement('style'); s.id='unclip'; s.textContent='.slot.default>div,.slot.default,.container{overflow:visible !important}'; sr.appendChild(s); }
    unclip(); mv.addEventListener('load',unclip); customElements.whenDefined('model-viewer').then(unclip);
    var pins=[].slice.call(mv.querySelectorAll('.pin')), open=null;
    function place(p){
        var r=p.getBoundingClientRect(), right=p.classList.contains('pin--right');
        var rem=parseFloat(getComputedStyle(document.documentElement).fontSize)||16;
        var lead=parseFloat(getComputedStyle(p).getPropertyValue('--lead'))||7.5;
        var card=p.querySelector('.pin__card'); if(!card) return;
        var need=lead*rem+card.offsetWidth+24;
        var roomR=window.innerWidth-r.left, roomL=r.left;
        var natural=right?roomR:roomL, other=right?roomL:roomR;
        p.classList.toggle('pin--flip', natural<need && other>natural);
        /* last resort (narrow phones): slide the card so it stays fully on screen */
        card.style.setProperty('--shift','0px');
        var c=card.getBoundingClientRect(), pad=12, shift=0;
        if(c.right>window.innerWidth-pad) shift=window.innerWidth-pad-c.right;
        if(c.left+shift<pad) shift=pad-c.left;
        card.style.setProperty('--shift',shift+'px');
      }
    function show(p){
      pins.forEach(function(x){x.classList.toggle('is-open',x===p)});
      ex.classList.toggle('has-open',!!p); open=p||null; if(p) place(p);
    }
    pins.forEach(function(p){ p.addEventListener('click',function(e){ e.stopPropagation(); show(open===p?null:p); }); });
    document.addEventListener('pointerdown',function(e){ if(open && !e.target.closest('.pin')) show(null); },true);
    document.addEventListener('keydown',function(e){ if(e.key==='Escape') show(null); });
    mv.addEventListener('camera-change',function(e){ if(e.detail.source==='user-interaction'){ var o=mv.getCameraOrbit(); userOffset=o.theta*180/Math.PI-cur; if(open) place(open); } });
    function tick(){ raf=0; cur+=(target-cur)*0.1; mv.cameraOrbit=(cur+userOffset).toFixed(2)+'deg auto auto'; if(Math.abs(target-cur)>0.05) raf=requestAnimationFrame(tick); }
    function onScroll(){
      if(reduce) return;
      var r=ex.getBoundingClientRect(), vh=window.innerHeight;
      var p=Math.max(0,Math.min(1,(vh-r.top)/(vh+r.height)));
      target=base+p*turn; if(!raf) raf=requestAnimationFrame(tick);
    }
    window.addEventListener('scroll',onScroll,{passive:true}); onScroll();
  });
})();
