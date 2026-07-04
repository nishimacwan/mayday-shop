from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="MAYDAY Store")

PRICE = 42


# Each product carries a small inline SVG so the catalog has varied,
# hand-drawn feeling visuals with no real photos.
def napkins_svg():
    return """
    <svg viewBox="0 0 200 150" role="img" aria-label="Folded linen napkins">
      <rect x="34" y="44" width="132" height="70" rx="6" fill="#c9b7a3"/>
      <rect x="42" y="54" width="132" height="70" rx="6" fill="#d9cbbd"/>
      <rect x="50" y="64" width="132" height="70" rx="6" fill="#e7ddce"/>
      <line x1="60" y1="74" x2="172" y2="74" stroke="#c9b7a3" stroke-width="3"/>
      <line x1="60" y1="90" x2="172" y2="90" stroke="#c9b7a3" stroke-width="3"/>
      <line x1="60" y1="106" x2="172" y2="106" stroke="#c9b7a3" stroke-width="3"/>
    </svg>"""


def pourover_svg():
    return """
    <svg viewBox="0 0 200 150" role="img" aria-label="Ceramic pour-over dripper">
      <ellipse cx="100" cy="120" rx="40" ry="9" fill="#aab3a6"/>
      <path d="M64 58 L136 58 L112 112 L88 112 Z" fill="#c3ccc0"/>
      <path d="M64 58 L136 58 L128 76 L72 76 Z" fill="#d3dacd"/>
      <rect x="88" y="112" width="24" height="10" rx="3" fill="#aab3a6"/>
      <path d="M136 66 q18 6 8 26" fill="none" stroke="#aab3a6" stroke-width="6" stroke-linecap="round"/>
    </svg>"""


def candle_svg():
    return """
    <svg viewBox="0 0 200 150" role="img" aria-label="Beeswax candle in a glass jar">
      <rect x="74" y="60" width="52" height="64" rx="8" fill="#efe6d3"/>
      <rect x="74" y="60" width="52" height="16" rx="8" fill="#e4d7bd"/>
      <rect x="98" y="40" width="4" height="16" fill="#9a8f79"/>
      <path d="M100 22 q10 10 0 20 q-10 -10 0 -20 Z" fill="#e6c98f"/>
      <path d="M100 28 q5 6 0 12 q-5 -6 0 -12 Z" fill="#d8ae6a"/>
    </svg>"""


def throw_svg():
    return """
    <svg viewBox="0 0 200 150" role="img" aria-label="Folded wool throw blanket">
      <defs>
        <pattern id="weave" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
          <rect width="16" height="16" fill="#c4c9d1"/>
          <rect width="8" height="16" fill="#b6bcc6"/>
        </pattern>
      </defs>
      <rect x="40" y="46" width="120" height="72" rx="8" fill="url(#weave)"/>
      <rect x="40" y="46" width="120" height="72" rx="8" fill="none" stroke="#aab0bb" stroke-width="2"/>
      <line x1="52" y1="118" x2="52" y2="128" stroke="#aab0bb" stroke-width="2"/>
      <line x1="72" y1="118" x2="72" y2="128" stroke="#aab0bb" stroke-width="2"/>
      <line x1="92" y1="118" x2="92" y2="128" stroke="#aab0bb" stroke-width="2"/>
    </svg>"""


def bowl_svg():
    return """
    <svg viewBox="0 0 200 150" role="img" aria-label="Ceramic breakfast bowl">
      <ellipse cx="100" cy="66" rx="56" ry="14" fill="#dcc9bf"/>
      <path d="M44 66 a56 40 0 0 0 112 0 Z" fill="#ccb4a6"/>
      <ellipse cx="100" cy="66" rx="46" ry="10" fill="#e3d4cb"/>
    </svg>"""


def towels_svg():
    svg = ['<svg viewBox="0 0 200 150" role="img" aria-label="Stacked waffle towels">']
    svg.append('<rect x="52" y="48" width="96" height="58" rx="6" fill="#bcc7c4"/>')
    for r in range(4):
        for c in range(6):
            x = 60 + c * 14
            y = 56 + r * 12
            svg.append(f'<rect x="{x}" y="{y}" width="8" height="8" rx="2" fill="#cdd6d2"/>')
    svg.append('<rect x="52" y="106" width="96" height="12" rx="4" fill="#a9b6b2"/>')
    svg.append("</svg>")
    return "".join(svg)


PRODUCTS = [
    {
        "name": "Stone-Washed Linen Napkins",
        "desc": "A set of four, washed soft so they feel lived in from the first meal.",
        "price": PRICE,
        "bg": "#efe7dc",
        "svg": napkins_svg(),
    },
    {
        "name": "Hand-Glazed Pour-Over",
        "desc": "Stoneware for slow mornings, glazed by hand. Fits most standard filters.",
        "price": PRICE + 14,
        "bg": "#e6ebe4",
        "svg": pourover_svg(),
    },
    {
        "name": "Beeswax Candle",
        "desc": "Poured with a simple cotton wick. Burns clean for around forty hours.",
        "price": PRICE - 18,
        "bg": "#f1ead9",
        "svg": candle_svg(),
    },
    {
        "name": "Merino Wool Throw",
        "desc": "Light for spring, warm for winter. Good on the couch or the end of the bed.",
        "price": PRICE + 46,
        "bg": "#e7e9ee",
        "svg": throw_svg(),
    },
    {
        "name": "Ceramic Breakfast Bowl",
        "desc": "A deep, everyday bowl for oats, soup, or a big handful of berries.",
        "price": PRICE - 8,
        "bg": "#f0e7e0",
        "svg": bowl_svg(),
    },
    {
        "name": "Waffle Bath Towels",
        "desc": "A soft, quick-drying pair with a gentle waffle weave that gets better with washing.",
        "price": PRICE + 6,
        "bg": "#e5ebe9",
        "svg": towels_svg(),
    },
]


def compute_status():
    """Derive the status badge from PRICE. A valid positive number is healthy."""
    healthy = (
        isinstance(PRICE, (int, float))
        and not isinstance(PRICE, bool)
        and PRICE > 0
    )
    if healthy:
        return {"ok": True, "text": "All systems operational",
                "fg": "#3f6152", "bg": "#e4ede6", "dot": "#6b9080"}
    return {"ok": False, "text": "Something is off with pricing",
            "fg": "#8a4a42", "bg": "#f3e0dc", "dot": "#b56b60"}


def render_home():
    status = compute_status()

    cards = "".join(
        f"""
        <article class="card">
          <div class="thumb" style="background:{p['bg']};">{p['svg']}</div>
          <div class="card-body">
            <h3 class="card-title">{p['name']}</h3>
            <p class="card-desc">{p['desc']}</p>
            <div class="card-row">
              <span class="price">${p['price']}</span>
              <button class="add-btn" data-name="{p['name']}" data-price="{p['price']}">Add to cart</button>
            </div>
          </div>
        </article>"""
        for p in PRODUCTS
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>MAYDAY Store</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --bg: #f7f4ef;
      --surface: #ffffff;
      --ink: #35322d;
      --muted: #8b857b;
      --line: #ece7df;
      --accent: #6b8f81;
      --accent-dark: #557567;
      --shadow: 0 1px 2px rgba(53,50,45,0.04), 0 8px 24px rgba(53,50,45,0.06);
      --shadow-lg: 0 2px 4px rgba(53,50,45,0.05), 0 16px 40px rgba(53,50,45,0.09);
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      background: var(--bg); color: var(--ink);
      -webkit-font-smoothing: antialiased; line-height: 1.55;
    }}
    svg {{ width: 100%; height: 100%; display: block; }}

    /* Nav */
    .nav {{
      position: sticky; top: 0; z-index: 50;
      display: flex; align-items: center; justify-content: space-between; gap: 1rem;
      padding: 1.1rem clamp(1.25rem, 4vw, 3.5rem);
      background: rgba(247,244,239,0.85);
      backdrop-filter: saturate(140%) blur(10px);
      border-bottom: 1px solid var(--line);
    }}
    .brand {{ display: flex; align-items: center; gap: 0.7rem; font-weight: 700; font-size: clamp(1.1rem,1.5vw,1.35rem); letter-spacing: -0.01em; }}
    .brand .logo {{ width: 2rem; height: 2rem; border-radius: 0.6rem; background: var(--accent); color: #fff; display: grid; place-items: center; font-size: 1rem; font-weight: 700; }}
    .nav-right {{ display: flex; align-items: center; gap: clamp(0.85rem, 2vw, 1.5rem); }}
    .status {{ display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.4rem 0.8rem; border-radius: 999px; font-size: 0.83rem; font-weight: 500; white-space: nowrap; color: {status['fg']}; background: {status['bg']}; }}
    .status .dot {{ width: 0.55rem; height: 0.55rem; border-radius: 50%; background: {status['dot']}; }}
    .signin {{ color: var(--ink); text-decoration: none; font-size: 0.9rem; font-weight: 500; opacity: 0.85; }}
    .signin:hover {{ opacity: 1; }}
    .cart {{
      position: relative; display: inline-flex; align-items: center; justify-content: center;
      width: 2.5rem; height: 2.5rem; border-radius: 0.7rem;
      background: var(--surface); border: 1px solid var(--line); cursor: pointer; font-size: 1.05rem;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}
    .cart:hover {{ transform: translateY(-1px); box-shadow: var(--shadow); }}
    .cart-count {{
      position: absolute; top: -0.35rem; right: -0.35rem; min-width: 1.25rem; height: 1.25rem; padding: 0 0.3rem;
      background: var(--accent); color: #fff; font-size: 0.7rem; font-weight: 600; border-radius: 999px;
      display: grid; place-items: center; border: 2px solid var(--surface);
      transform: scale(0); transition: transform 0.18s ease;
    }}
    .cart-count.show {{ transform: scale(1); }}

    /* Hero */
    .hero {{ max-width: 1120px; margin: 0 auto; padding: clamp(2.5rem,7vw,5rem) clamp(1.25rem,4vw,3.5rem) clamp(1.25rem,3vw,2.5rem); text-align: center; }}
    .eyebrow {{ display: inline-block; margin-bottom: 1.1rem; font-size: 0.82rem; font-weight: 600; color: var(--accent-dark); letter-spacing: 0.08em; text-transform: uppercase; }}
    .hero h1 {{ margin: 0 auto 1.1rem; max-width: 18ch; font-size: clamp(2.1rem,5vw,3.6rem); font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; }}
    .hero p {{ margin: 0 auto; max-width: 52ch; font-size: clamp(1rem,1.4vw,1.15rem); color: var(--muted); }}
    .hero .cta {{ margin-top: 1.8rem; }}
    .btn-primary {{ padding: 0.8rem 1.6rem; border: none; border-radius: 0.7rem; background: var(--accent); color: #fff; font-weight: 600; font-size: 1rem; cursor: pointer; transition: background 0.15s ease, transform 0.15s ease; }}
    .btn-primary:hover {{ background: var(--accent-dark); transform: translateY(-1px); }}

    /* Section head */
    .section-head {{ max-width: 1120px; margin: 1.25rem auto 0; padding: 0 clamp(1.25rem,4vw,3.5rem); display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; }}
    .section-head h2 {{ font-size: clamp(1.3rem,2.2vw,1.7rem); font-weight: 700; letter-spacing: -0.01em; margin: 0; }}
    .section-head span {{ color: var(--muted); font-size: 0.9rem; }}

    /* Grid */
    .grid {{ max-width: 1120px; margin: 1.25rem auto clamp(3rem,8vw,5.5rem); padding: 0 clamp(1.25rem,4vw,3.5rem); display: grid; gap: clamp(1rem,2vw,1.6rem); grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }}
    .card {{ background: var(--surface); border-radius: 1rem; overflow: hidden; border: 1px solid var(--line); transition: transform 0.18s ease, box-shadow 0.18s ease; display: flex; flex-direction: column; }}
    .card:hover {{ transform: translateY(-4px); box-shadow: var(--shadow-lg); }}
    .thumb {{ aspect-ratio: 4 / 3; width: 100%; padding: 0.5rem; }}
    .card-body {{ padding: 1.15rem 1.25rem 1.3rem; display: flex; flex-direction: column; gap: 0.55rem; flex: 1; }}
    .card-title {{ margin: 0; font-size: 1.08rem; font-weight: 600; letter-spacing: -0.01em; }}
    .card-desc {{ margin: 0; color: var(--muted); font-size: 0.92rem; }}
    .card-row {{ display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; margin-top: 0.85rem; }}
    .price {{ font-size: 1.2rem; font-weight: 700; letter-spacing: -0.01em; }}
    .add-btn {{ padding: 0.55rem 1rem; border: 1px solid var(--accent); border-radius: 0.6rem; background: transparent; color: var(--accent-dark); font-weight: 600; font-size: 0.88rem; cursor: pointer; transition: background 0.15s ease, color 0.15s ease; }}
    .add-btn:hover {{ background: var(--accent); color: #fff; }}

    footer {{ border-top: 1px solid var(--line); padding: 2rem clamp(1.25rem,4vw,3.5rem); text-align: center; color: var(--muted); font-size: 0.88rem; }}

    /* Cart panel */
    .overlay {{ position: fixed; inset: 0; background: rgba(53,50,45,0.35); opacity: 0; pointer-events: none; transition: opacity 0.25s ease; z-index: 80; }}
    .overlay.open {{ opacity: 1; pointer-events: auto; }}
    .panel {{
      position: fixed; top: 0; right: 0; height: 100%; width: min(400px, 92vw);
      background: var(--surface); box-shadow: var(--shadow-lg); z-index: 90;
      transform: translateX(100%); transition: transform 0.28s ease;
      display: flex; flex-direction: column;
    }}
    .panel.open {{ transform: translateX(0); }}
    .panel-head {{ display: flex; align-items: center; justify-content: space-between; padding: 1.25rem 1.4rem; border-bottom: 1px solid var(--line); }}
    .panel-head h2 {{ margin: 0; font-size: 1.15rem; font-weight: 700; }}
    .close-btn {{ background: none; border: none; font-size: 1.5rem; line-height: 1; color: var(--muted); cursor: pointer; padding: 0.2rem 0.4rem; border-radius: 0.5rem; }}
    .close-btn:hover {{ background: var(--bg); color: var(--ink); }}
    .panel-items {{ flex: 1; overflow-y: auto; padding: 0.75rem 1.4rem; }}
    .empty {{ color: var(--muted); text-align: center; margin-top: 3rem; font-size: 0.95rem; }}
    .line-item {{ display: flex; align-items: center; gap: 0.75rem; padding: 0.85rem 0; border-bottom: 1px solid var(--line); }}
    .line-item .li-name {{ flex: 1; font-size: 0.95rem; font-weight: 500; }}
    .line-item .li-qty {{ color: var(--muted); font-size: 0.85rem; }}
    .line-item .li-price {{ font-weight: 600; min-width: 3.2rem; text-align: right; }}
    .li-remove {{ background: none; border: none; color: var(--muted); cursor: pointer; font-size: 1.1rem; padding: 0 0.2rem; border-radius: 0.4rem; }}
    .li-remove:hover {{ color: #8a4a42; }}
    .panel-foot {{ padding: 1.25rem 1.4rem; border-top: 1px solid var(--line); }}
    .total-row {{ display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 1rem; }}
    .total-row .t-label {{ color: var(--muted); font-size: 0.9rem; }}
    .total-row .t-value {{ font-size: 1.4rem; font-weight: 700; }}
    .checkout {{ width: 100%; padding: 0.85rem; border: none; border-radius: 0.7rem; background: var(--accent); color: #fff; font-weight: 600; font-size: 1rem; cursor: pointer; transition: background 0.15s ease; }}
    .checkout:hover {{ background: var(--accent-dark); }}
    .checkout:disabled {{ background: #cfcabf; cursor: not-allowed; }}

    /* Toast */
    .toast {{ position: fixed; bottom: 1.5rem; left: 50%; transform: translateX(-50%) translateY(200%); background: var(--ink); color: #fff; padding: 0.75rem 1.25rem; border-radius: 0.7rem; font-weight: 500; font-size: 0.92rem; box-shadow: var(--shadow-lg); transition: transform 0.3s ease; z-index: 100; }}
    .toast.show {{ transform: translateX(-50%) translateY(0); }}
  </style>
</head>
<body>
  <nav class="nav">
    <div class="brand"><span class="logo">M</span> MAYDAY Store</div>
    <div class="nav-right">
      <span class="status" role="status" aria-live="polite"><span class="dot"></span>{status['text']}</span>
      <a class="signin" href="#" onclick="return false;">Sign in</a>
      <button class="cart" aria-label="Open cart" onclick="openCart()">
        \U0001F6D2
        <span class="cart-count" id="cart-count">0</span>
      </button>
    </div>
  </nav>

  <header class="hero">
    <span class="eyebrow">Everyday things, made well</span>
    <h1>Small goods for a calmer home.</h1>
    <p>A short list of things we actually use and like. Nothing flashy, just honest pieces meant to last a while.</p>
    <div class="cta"><button class="btn-primary" onclick="document.getElementById('shop').scrollIntoView({{behavior:'smooth'}})">Browse the shop</button></div>
  </header>

  <div class="section-head" id="shop">
    <h2>The collection</h2>
    <span>{len(PRODUCTS)} pieces</span>
  </div>
  <main class="grid">
    {cards}
  </main>

  <footer>MAYDAY Store. Made with care for the hackathon. Thanks for looking around.</footer>

  <!-- Cart -->
  <div class="overlay" id="overlay" onclick="closeCart()"></div>
  <aside class="panel" id="panel" aria-label="Shopping cart">
    <div class="panel-head">
      <h2>Your cart</h2>
      <button class="close-btn" aria-label="Close cart" onclick="closeCart()">&times;</button>
    </div>
    <div class="panel-items" id="panel-items"></div>
    <div class="panel-foot">
      <div class="total-row"><span class="t-label">Total</span><span class="t-value" id="cart-total">$0</span></div>
      <button class="checkout" id="checkout" disabled onclick="checkout()">Checkout</button>
    </div>
  </aside>

  <div class="toast" id="toast"></div>

  <script>
    const cart = [];
    const countEl = document.getElementById('cart-count');
    const itemsEl = document.getElementById('panel-items');
    const totalEl = document.getElementById('cart-total');
    const checkoutEl = document.getElementById('checkout');
    const overlay = document.getElementById('overlay');
    const panel = document.getElementById('panel');
    const toastEl = document.getElementById('toast');
    let toastTimer;

    document.querySelectorAll('.add-btn').forEach(btn => {{
      btn.addEventListener('click', () => addToCart(btn.dataset.name, Number(btn.dataset.price)));
    }});

    function addToCart(name, price) {{
      const existing = cart.find(i => i.name === name);
      if (existing) {{ existing.qty++; }}
      else {{ cart.push({{ name, price, qty: 1 }}); }}
      render();
      showToast(name + ' is in your cart');
    }}

    function removeFromCart(name) {{
      const idx = cart.findIndex(i => i.name === name);
      if (idx > -1) cart.splice(idx, 1);
      render();
    }}

    function render() {{
      const totalQty = cart.reduce((n, i) => n + i.qty, 0);
      countEl.textContent = totalQty;
      countEl.classList.toggle('show', totalQty > 0);

      if (cart.length === 0) {{
        itemsEl.innerHTML = '<p class="empty">Your cart is empty for now.</p>';
      }} else {{
        itemsEl.innerHTML = cart.map(i => `
          <div class="line-item">
            <span class="li-name">${{i.name}}${{i.qty > 1 ? ' <span class="li-qty">x' + i.qty + '</span>' : ''}}</span>
            <span class="li-price">$${{i.price * i.qty}}</span>
            <button class="li-remove" aria-label="Remove" onclick="removeFromCart('${{i.name.replace(/'/g, "\\\\'")}}')">&times;</button>
          </div>`).join('');
      }}

      const total = cart.reduce((sum, i) => sum + i.price * i.qty, 0);
      totalEl.textContent = '$' + total;
      checkoutEl.disabled = cart.length === 0;
    }}

    function openCart() {{ overlay.classList.add('open'); panel.classList.add('open'); }}
    function closeCart() {{ overlay.classList.remove('open'); panel.classList.remove('open'); }}
    function checkout() {{ showToast('This is a demo, so there is nothing to pay. Thanks though.'); }}

    function showToast(msg) {{
      toastEl.textContent = msg;
      toastEl.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => toastEl.classList.remove('show'), 2200);
    }}

    document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeCart(); }});
    render();
  </script>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def home():
    return render_home()


@app.get("/health")
def health():
    return {"status": "ok"}
