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
