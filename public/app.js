async function load() {
  const s = await (await fetch('../data/state.json')).json();
  const c = await (await fetch('../data/confessions.json')).json();
  document.getElementById('stats').innerText =
    `Confessioni: ${c.length} • Fondo: ${s.fund_pool} • Pausa: ${s.is_paused}`;
  const box = document.getElementById('confessions');
  c.slice(-10).reverse().forEach(x=>{
    const p=document.createElement('p'); p.textContent=`#${x.id||'?'} — "${x.text}"`;
    box.appendChild(p);
  });
}
load();
