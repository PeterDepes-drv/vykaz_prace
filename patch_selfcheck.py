from pathlib import Path
path = Path('kniha_jazd.html')
text = path.read_text(encoding='utf-8')

if 'id="selfCheckStatus"' not in text:
    text = text.replace(
        '<div class="header">\n  <h1>&#128661; Kniha jazd</h1>',
        '<div class="header">\n  <h1>&#128661; Kniha jazd</h1>\n  <div id="selfCheckStatus" style="font-size:0.82rem;color:#fff;background:#2e7d32;padding:4px 8px;border-radius:6px;display:none;">Self-check OK</div>'
    )

if 'runSelfCheck();' not in text:
    text = text.replace(
        "document.getElementById('tripDate').value = todayISO();\nbuildButtons();\nloadState();\nrender();",
        "document.getElementById('tripDate').value = todayISO();\nbuildButtons();\nloadState();\nrender();\nrunSelfCheck();"
    )

if 'function runSelfCheck()' not in text:
    marker = 'function dlFile(content, filename, mime) {'
    i = text.find(marker)
    if i != -1:
        text = text.replace(marker, marker + "\n// ── SELF CHECK ─────────────────────────────────────────────────────────────\nfunction runSelfCheck() {\n  const statusEl = document.getElementById('selfCheckStatus');\n  const requiredIds = ['driverName','vehicleId','tripDate','actButtons','statusPanel','logBody','summaryPanel'];\n  const missing = requiredIds.filter(id => !document.getElementById(id));\n  let text = '';\n  let ok = true;\n  if (missing.length) { ok = false; text = 'Chýba DOM element: ' + missing.join(', '); }\n  try { localStorage.setItem('__kj_ping', 'ok'); if (localStorage.getItem('__kj_ping') !== 'ok') throw new Error('LS read mismatch'); localStorage.removeItem('__kj_ping'); } catch (e) { ok = false; text = 'localStorage unavailable'; }\n  if (ok && (!ACTS || !ACTS.length)) { ok = false; text = 'ACTS je prázdne'; }\n  if (ok) { text = 'Self-check OK'; console.log('[KnihaJazd] self-check OK'); } else { console.error('[KnihaJazd] self-check failed:', text); }\n  if (statusEl) { statusEl.textContent = text; statusEl.style.display = 'inline-block'; statusEl.style.background = ok ? '#2e7d32' : '#c62828'; }\n}\n")

path.write_text(text, encoding='utf-8')
print('Updated kniha_jazd.html with self-check')
