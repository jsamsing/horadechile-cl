(function(){
var CAMBIOS=__CAMBIOS__, GA='__GA4__';
var fmtH=function(tz,s){return new Intl.DateTimeFormat('es-CL',{timeZone:tz,hour:'2-digit',minute:'2-digit',second:s?'2-digit':undefined,hour12:false}).format(new Date())};
var fmtF=function(tz){return new Intl.DateTimeFormat('es-CL',{timeZone:tz,weekday:'long',day:'numeric',month:'long',year:'numeric'}).format(new Date())};
var off=function(tz){var d=new Date(),p=new Intl.DateTimeFormat('en-US',{timeZone:tz,hourCycle:'h23',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit'}).formatToParts(d),o={};p.forEach(function(x){o[x.type]=x.value});return Math.round((Date.UTC(o.year,o.month-1,o.day,o.hour,o.minute)-Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),d.getUTCDate(),d.getUTCHours(),d.getUTCMinutes()))/60000)};
var utc=function(m){var h=m/60;return 'UTC'+(h<0?'−':'+')+Math.abs(h)};
function tick(){
document.querySelectorAll('.reloj[data-tz]').forEach(function(r){var tz=r.dataset.tz;r.querySelector('[data-h]').textContent=fmtH(tz,1);r.querySelector('[data-f]').textContent=fmtF(tz);r.querySelector('[data-u]').textContent=utc(off(tz))});
var b=document.querySelector('[data-base]');if(b)b.textContent=fmtH('America/Santiago');
var cl=off('America/Santiago');
document.querySelectorAll('[data-dif] tr[data-tz]').forEach(function(r){var tz=r.dataset.tz,d=(off(tz)-cl)/60;r.querySelector('[data-h]').textContent=fmtH(tz);r.querySelector('[data-d]').textContent=d===0?'Misma hora':(d>0?'+':'−')+Math.abs(d)+(Math.abs(d)===1?' hora':' horas')});
document.querySelectorAll('[data-difp]').forEach(function(e){var d=(off(e.dataset.tz)-cl)/60;e.querySelector('[data-dd]').textContent=d===0?'misma hora':(d>0?'+':'−')+Math.abs(d)+(Math.abs(d)===1?' hora':' horas')+(d>0?' (va por delante)':' (va detrás)')});
document.querySelectorAll('[data-eq]').forEach(function(t){var d=off(t.dataset.tz)-cl;t.querySelectorAll('[data-eqh]').forEach(function(c){var p=c.dataset.eqh.split(':'),m=((+p[0])*60+(+p[1])+d)%1440,dia='';if(m<0){m+=1440;dia=' (día anterior)'}else if((+p[0])*60+d>=1440)dia=' (día siguiente)';c.textContent=('0'+Math.floor(m/60)).slice(-2)+':'+('0'+m%60).slice(-2)+dia})});
var now=Date.now(),c=CAMBIOS.filter(function(x){return Date.parse(x.utc)>now})[0];
document.querySelectorAll('[data-prox]').forEach(function(s){if(!c){s.hidden=true;return}
s.querySelector('[data-pc-fecha]').textContent=c.txt+', 24:00';s.querySelector('[data-pc-tipo]').textContent=c.tipo==='atrasar'?'atrasan':'adelantan';
var t=Math.floor((Date.parse(c.utc)-now)/1000),dd=Math.floor(t/86400),hh=Math.floor(t%86400/3600),mm=Math.floor(t%3600/60),ss=t%60;
s.querySelector('[data-cd]').textContent=dd+' días, '+hh+' h '+mm+' min '+ss+' s'});
}
tick();setInterval(tick,1000);
// Consentimiento y GA4 (solo en el dominio real y si acepta)
window.ckShow=function(){document.getElementById('ck').hidden=false};
window.ckSet=function(v){try{localStorage.setItem('hc_ck',v?'g':'d')}catch(e){}document.getElementById('ck').hidden=true;if(v)ga()};
function ga(){if(!GA||location.hostname!=='horadechile.cl'||window.gtag)return;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA)}
var k=null;try{k=localStorage.getItem('hc_ck')}catch(e){}
if(k==='g')ga();else if(!k&&GA)setTimeout(ckShow,1500);
document.addEventListener('click',function(e){var a=e.target.closest('[data-ev]');if(a&&window.gtag)gtag('event',a.dataset.ev,{cta_label:a.dataset.label})});
})();
