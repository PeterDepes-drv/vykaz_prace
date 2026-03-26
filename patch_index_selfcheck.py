from pathlib import Path

path = Path(r'c:\Users\peter\Nový priečinok\Claude_code\index.html')
text = path.read_text(encoding='utf-8')

if 'function runSelfCheck()' not in text:
    insert_point = 'bootstrap().then(() => initApp());'
    if insert_point in text:
        runcheck = """
// ── SELF CHECK ─────────────────────────────────────────────────────────────
function runSelfCheck() {
  const requiredIds = ['loginPage','driverPage','adminPage','recordOverlay','driverTableBody','adminTableBody','dFilterMonth','aFilterMonth'];
  const missing = requiredIds.filter(id => !document.getElementById(id));
  let ok = missing.length === 0;
  let msg = ok ? 'Index app self-check OK' : 'Missing elements: ' + missing.join(', ');

  try {
    localStorage.setItem('__dl_check', 'ok');
    if (localStorage.getItem('__dl_check') !== 'ok') throw new Error('localStorage mismatch');
    localStorage.removeItem('__dl_check');
  } catch (e) {
    ok = false;
    msg = 'localStorage unavailable';
  }

  if (!window.firebase || !window.firebase.database) {
    ok = false;
    msg = 'Firebase SDK not loaded';
  }

  if (ok) {
    console.log('[IndexApp]', msg);
  } else {
    console.error('[IndexApp] self-check failed:', msg);
    const header = document.querySelector('.header') || document.body;
    const warn = document.createElement('div');
    warn.style = 'position:fixed;top:0;right:0;padding:6px 10px;background:#c62828;color:#fff;z-index:9999;font-size:13px;';
    warn.textContent = msg;
    header.appendChild(warn);
    setTimeout(() => warn.remove(), 8000);
  }
}
"""
        text = text.replace(insert_point, runcheck + '\n' + insert_point)

    # Run the check after init
    text = text.replace('bootstrap().then(() => initApp());', 'bootstrap().then(() => { initApp(); runSelfCheck(); });')

    path.write_text(text, encoding='utf-8')
    print('Updated index.html self-check logic')
else:
    print('runSelfCheck already exists, no change')
