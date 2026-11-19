"""Figures for ME1 Thermodynamics Tutorial Sheet Set 2 (Exercise 2: Basic Concepts).

Pillow only, same house style as the existing notes:
  * white background, dark text, <= 3 accent colours
  * every label >= 22 px, English text only
Run:  python gen_set2_figs.py  (writes into OUT)
"""
import math, os, re
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "ME1 Thermodynamics", "ME1 Thermodynamics - Tutorial Set 2", "figures")
os.makedirs(OUT, exist_ok=True)

BG = (255, 255, 255)
FG = (25, 25, 25)
GRAY = (110, 110, 110)
LGRAY = (205, 205, 205)
BLUE = (24, 76, 160)      # accent 1: system / C.V. / "yes"
RED = (176, 34, 40)       # accent 2: heat / energy flow / "no"
GREEN = (22, 112, 70)     # accent 3: property / "could be"
FILL_B = (224, 233, 246)
FILL_R = (250, 228, 228)
FILL_G = (224, 240, 228)
FILL_Y = (253, 245, 214)

W = 1200            # every figure is 1200 px wide


def font(size, bold=True, cn=True):
    """Pick a font that actually has CJK glyphs: msyh first, Arial only for pure-ASCII."""
    if cn:
        names = ["msyhbd.ttc", "simhei.ttf"] if bold else ["msyh.ttc", "simhei.ttf"]
    else:
        names = []
    names += ["arialbd.ttf" if bold else "arial.ttf", "msyhbd.ttc" if bold else "msyh.ttc",
              "simhei.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            continue
    return ImageFont.load_default()


CJK = re.compile(r"[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]")


def new(w, h):
    img = Image.new("RGB", (w, h), BG)
    return img, ImageDraw.Draw(img)


def arrow(d, p0, p1, color=FG, w=4, head=14):
    d.line([p0, p1], fill=color, width=w)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (-0.45, 0.45):
        d.line([p1, (p1[0] - head * math.cos(ang - s), p1[1] - head * math.sin(ang - s))],
               fill=color, width=w)


def label(d, xy, text, size=24, color=FG, bold=True, anchor="mm"):
    d.text(xy, text, font=font(size, bold, bool(CJK.search(text))), fill=color, anchor=anchor)


def title(d, text, sub=None, y=34):
    label(d, (W // 2, y), text, 34)
    if sub:
        label(d, (W // 2, y + 44), sub, 26, GRAY, bold=False)


def save(img, name):
    img.save(os.path.join(OUT, name), dpi=(150, 150))
    print("wrote", name, img.size)


# ---------------------------------------------------------------- fig 2.1a
def fig_2_1_station():
    img, d = new(W, 470)
    title(d, "Question 2.1(a): station efficiency, coal per day",
          "station efficiency: how much coal is burnt each day")

    # input bar
    d.rectangle([80, 130, 210, 400], fill=FILL_R, outline=RED, width=4)
    label(d, (145, 185), "coal", 26, RED)
    label(d, (145, 220), "fuel", 26, RED)
    label(d, (145, 270), "Q_in", 30, RED)
    label(d, (145, 310), "22 000", 24, RED)
    label(d, (145, 340), "kJ/kg", 24, RED)
    arrow(d, (215, 265), (330, 265), RED, 6)
    label(d, (272, 235), "100 %", 24, RED)

    # plant box
    d.rounded_rectangle([335, 175, 665, 355], radius=18, fill=FILL_B, outline=BLUE, width=4)
    label(d, (500, 215), "power station", 28, BLUE)
    label(d, (500, 262), "eta = 35 %", 34, BLUE)
    label(d, (500, 305), "only 35 % of the heat", 23, BLUE, bold=False)
    label(d, (500, 333), "becomes electricity", 23, BLUE, bold=False)

    arrow(d, (670, 265), (790, 265), BLUE, 6)
    label(d, (730, 232), "P_elec", 24, BLUE)
    label(d, (730, 298), "1000 MW", 24, BLUE)

    # reject arrow
    arrow(d, (500, 360), (500, 415), GRAY, 5)
    label(d, (500, 438), "65 % rejected as waste heat", 24, GRAY, bold=False)

    # right: the day box
    d.rounded_rectangle([815, 120, 1150, 400], radius=16, outline=FG, width=4)
    label(d, (982, 160), "one day = 24 h", 26)
    label(d, (982, 200), "= 86 400 s", 26, GRAY, bold=False)
    label(d, (982, 262), "E_in = P / eta", 28, FG)
    label(d, (982, 312), "= 1000 / 0.35", 26, GRAY, bold=False)
    label(d, (982, 342), "= 2857 MW", 26, GRAY, bold=False)
    label(d, (982, 380), "-> m = 11 220 t/day", 26, RED)
    save(img, "fig2_1a_station.png")


# ---------------------------------------------------------------- fig 2.1b
def fig_2_1_so2():
    img, d = new(W, 430)
    title(d, "Question 2.1(b): sulphur -> SO2 mass balance",
          "sulphur burnt to SO2: mass balance")

    boxes = [
        ("coal", "1.6 % S by mass", "11 220 t/day", FILL_Y, FG),
        ("sulphur", "S = 1.6 % x coal", "180 t/day", FILL_Y, FG),
        ("SO2", "S + O2 -> SO2", "2 O per S: 64/32 = 2", FILL_G, GREEN),
        ("emission", "SO2 to atmosphere", "359 t/day", FILL_R, RED),
    ]
    x = 60
    for i, (t1, t2, t3, fill, edge) in enumerate(boxes):
        d.rounded_rectangle([x, 130, x + 240, 330], radius=14, fill=fill, outline=edge, width=4)
        label(d, (x + 120, 178), t1, 28, edge)
        label(d, (x + 120, 228), t2, 23, FG, bold=False)
        label(d, (x + 120, 285), t3, 27, FG)
        if i < 3:
            arrow(d, (x + 245, 230), (x + 300, 230), FG, 5)
        x += 300

    label(d, (W // 2, 385), "M(S)=32, M(O)=16 -> M(SO2)=64 -> mass factor 2.0",
          26, GRAY, bold=False)
    label(d, (W // 2, 415), "each S takes two O, so the mass doubles", 24, GRAY, bold=False)
    save(img, "fig2_1b_so2.png")


# ---------------------------------------------------------------- fig 2.2
def fig_2_2_framework():
    img, d = new(W, 470)
    title(d, "Question 2.2: which framework? system or control volume",
          "system or control volume?")

    panels = [
        ("(a) the bottle", "C.V.", BLUE, FILL_B,
         "gas LEAVES it\nleaves the bottle"),
        ("(b) the valve", "C.V.", BLUE, FILL_B,
         "gas crosses it at\n2 ports"),
        ("(c) bottle + balloon", "system", GREEN, FILL_G,
         "gas stays INSIDE\nno gas escapes"),
    ]
    x0 = 55
    for i, (ttl, kind, col, fill, why) in enumerate(panels):
        x = x0 + i * 380
        label(d, (x + 160, 120), ttl, 26, FG)
        # bottle
        d.rounded_rectangle([x + 30, 200, x + 150, 300], radius=26, fill=fill, outline=col, width=4)
        label(d, (x + 90, 250), "gas", 24, col)
        # balloon
        if i != 1:
            cx = x + 250
            d.ellipse([cx - 60, 190, cx + 70, 310], fill=fill, outline=col, width=4)
            label(d, (cx + 5, 250), "balloon", 22, col, bold=False)
            d.line([x + 150, 250, cx - 60, 250], fill=col, width=4)
        else:
            d.rectangle([x + 165, 230, x + 205, 270], fill=(230, 230, 230), outline=FG, width=3)
            label(d, (x + 185, 205), "valve", 22, FG, bold=False)
            arrow(d, (x + 210, 250), (x + 260, 250), RED, 5)
            label(d, (x + 290, 250), "flow", 22, RED, bold=False)
        # the framework box
        if i == 0:
            d.rectangle([x + 20, 190, x + 160, 310], outline=BLUE, width=5)
        if i == 1:
            d.rectangle([x + 160, 224, x + 212, 276], outline=BLUE, width=5)
        if i == 2:
            d.rectangle([x + 20, 180, x + 340, 320], outline=GREEN, width=5, )
        label(d, (x + 160, 350), kind, 32, col)
        for j, line in enumerate(why.split("\n")):
            label(d, (x + 160, 395 + j * 30), line, 23, GRAY, bold=False)
    save(img, "fig2_2_framework.png")


# ---------------------------------------------------------------- fig 2.3
def fig_2_3_climbers():
    img, d = new(W, 540)
    title(d, "Question 2.3: properties, path and a cycle",
          "property (state only) vs path (process)")

    A = (110, 360)
    B = (1000, 130)
    d.polygon([(70, 390), A, B, (1080, 160), (1080, 390)], fill=(240, 240, 240), outline=LGRAY, width=3)
    pts_steep = [A, (280, 310), (420, 245), (600, 195), (790, 155), B]
    pts_gentle = [A, (250, 345), (520, 285), (760, 220), (920, 165), B]
    d.line(pts_steep, fill=RED, width=5, joint="curve")
    d.line(pts_gentle, fill=BLUE, width=5, joint="curve")
    for px, py in pts_steep[1:-1]:
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED)
    for px, py in pts_gentle[1:-1]:
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=BLUE)
    for a, b in [((420, 245), (520, 285)), ((790, 155), (920, 165))]:
        d.line([a, b], fill=GRAY, width=3)

    label(d, (110, 410), "A base camp", 23, FG, anchor="lm")
    label(d, (1060, 100), "B high camp", 23, FG, anchor="rm")
    label(d, (330, 175), "steep, short", 23, RED, anchor="lm")
    label(d, (470, 250), "gentle, long", 23, BLUE, anchor="lm")

    d.rounded_rectangle([60, 430, 740, 525], radius=12, fill=FILL_G, outline=GREEN, width=3)
    label(d, (80, 455), "property: lat / long / altitude  -- same at B on both routes",
          23, GREEN, anchor="lm")
    label(d, (80, 498), "these follow from the state, not from the route", 22, GRAY, bold=False, anchor="lm")

    d.rounded_rectangle([770, 430, 1150, 525], radius=12, fill=FILL_R, outline=RED, width=3)
    label(d, (790, 455), "path: distance travelled", 23, RED, anchor="lm")
    label(d, (790, 498), "the two routes give different distances", 22, GRAY, bold=False, anchor="lm")
    save(img, "fig2_3_climbers.png")


# ---------------------------------------------------------------- fig 2.4
def _tank(d, x, tags, hole=False, removed=False, caption="", verdict="", vcol=FG):
    """One tank panel. tags = [(frac, text)] : surface height marker per section."""
    top, bot = 175, 335
    d.rectangle([x, top, x + 260, bot], outline=FG, width=4)
    if not removed:
        d.line([(x + 130, top), (x + 130, bot)], fill=FG, width=6)
    def surf(xa, xb, frac):
        y = int(bot - (bot - top) * frac)
        d.rectangle([xa, y, xb, bot], fill=FILL_B)
        d.line([(xa, y), (xb, y)], fill=BLUE, width=4)
        return y
    if removed:
        y = surf(x + 4, x + 256, 0.45)
        for k in range(0, 11):
            xa = x + 8 + k * 23
            d.line([(xa, y + (7 if k % 2 else -7)), (xa + 11, y + (-7 if k % 2 else 7))],
                   fill=BLUE, width=3)
    else:
        surf(x + 4, x + 126, tags[0])
        surf(x + 134, x + 256, tags[1])
        if hole:
            d.ellipse([x + 122, 258, x + 138, 274], fill=BG, outline=FG, width=3)
            d.line([(x + 140, 266), (x + 190, 300)], fill=BLUE, width=3)
            arrow(d, (x + 190, 300), (x + 215, 312), BLUE, 3)
    label(d, (x + 130, bot + 30), caption, 24, FG)
    label(d, (x + 130, bot + 70), verdict, 23, vcol)


def fig_2_4_tank():
    img, d = new(W, 560)
    title(d, "Question 2.4: can a single height describe the state?",
          "can one liquid height describe the whole system?")
    _tank(d, 40, (0.75, 0.0), caption="(i) initial: eqm",
          verdict="flat surface -> one height", vcol=BLUE)
    _tank(d, 410, (0.62, 0.30), removed=True, caption="(a) partition removed",
          verdict="sloshing -> NOT q-e", vcol=RED)
    _tank(d, 780, (0.74, 0.05), hole=True, caption="(b) hole drilled, slow flow",
          verdict="2 uniform heights -> q-e", vcol=GREEN)
    d.rounded_rectangle([60, 455, 1140, 535], radius=12, fill=FILL_Y, outline=FG, width=3)
    label(d, (600, 478), "q-e means: at every instant the whole system has one value for each property",
          24, FG)
    label(d, (600, 512), "q-e = one value per property, everywhere, at every instant", 23, GRAY, bold=False)
    save(img, "fig2_4_tank.png")


# ---------------------------------------------------------------- fig 2.5
def _cyl(d, x, y, w=250, h=175):
    d.rectangle([x, y, x + w, y + h], outline=FG, width=4)


def fig_2_5_four():
    img, d = new(W, 600)
    title(d, "Question 2.5: four ways to expand a gas",
          "a: unresisted   b: partly resisted   c, d: could be quasi-equilibrium")

    # (a) diaphragm burst
    x, y = 40, 110
    _cyl(d, x, y)
    d.rectangle([x + 4, y + 4, x + 118, y + 171], fill=FILL_B)
    label(d, (x + 61, y + 88), "gas", 24, BLUE)
    d.line([(x + 122, y + 4), (x + 122, y + 171)], fill=RED, width=5)
    for k in range(5):
        d.line([(x + 145 + (k % 2) * 10, y + 30 + k * 28), (x + 200 - (k % 2) * 10, y + 42 + k * 28)],
               fill=RED, width=3)
    label(d, (x + 125, y + 205), "(a) diaphragm burst", 23, FG)
    label(d, (x + 125, y + 236), "diaphragm burst", 22, FG, anchor="mm")
    label(d, (x + 125, y + 275), "NOT q-e: unresisted", 22, RED, bold=False)
    label(d, (x + 125, y + 305), "P not uniform yet", 22, GRAY, bold=False)

    # (b) spring
    x, y = 325, 110
    _cyl(d, x, y)
    d.rectangle([x + 4, y + 4, x + 110, y + 171], fill=FILL_B)
    label(d, (x + 57, y + 88), "gas", 24, BLUE)
    d.rectangle([x + 110, y + 4, x + 122, y + 171], fill=(90, 90, 90))
    pts = []
    for k in range(6):
        pts.append((x + 128 + k * 16, y + 88 + (-16 if k % 2 else 16)))
    d.line([(x + 122, y + 88)] + pts + [(x + 240, y + 88)], fill=FG, width=3)
    label(d, (x + 125, y + 205), "(b) spring catch released", 23, FG)
    label(d, (x + 125, y + 236), "spring catch released", 22, FG, anchor="mm")
    label(d, (x + 125, y + 275), "NOT q-e: partly resisted", 22, RED, bold=False)
    label(d, (x + 125, y + 305), "spring force starts at 0", 22, GRAY, bold=False)

    # (c) weight
    x, y = 625, 110
    _cyl(d, x, y)
    d.rectangle([x + 4, y + 45, x + 246, y + 171], fill=FILL_B)
    label(d, (x + 125, y + 120), "gas, heated", 24, BLUE)
    d.rectangle([x + 4, y + 25, x + 246, y + 45], fill=(90, 90, 90))
    arrow(d, (x + 125, y + 20), (x + 125, y + 2), GRAY, 4)
    label(d, (x + 305, y + 35), "weight", 22, GRAY, anchor="lm")
    label(d, (x + 125, y + 205), "(c) weight + slow heating", 23, FG)
    label(d, (x + 125, y + 236), "loaded, heated slowly", 22, FG, anchor="mm")
    label(d, (x + 125, y + 275), "COULD BE q-e", 22, GREEN, bold=False)
    label(d, (x + 125, y + 305), "balanced -> P fixed", 22, GRAY, bold=False)

    # (d) crankshaft
    x, y = 925, 110
    _cyl(d, x, y)
    d.rectangle([x + 4, y + 55, x + 246, y + 171], fill=FILL_B)
    label(d, (x + 125, y + 128), "gas, heated", 24, BLUE)
    d.rectangle([x + 4, y + 30, x + 246, y + 55], fill=(90, 90, 90))
    d.line([(x + 125, y + 55), (x + 165, y + 171)], fill=FG, width=5)
    d.ellipse([x + 143, y + 149, x + 187, y + 193], outline=GRAY, width=4)
    label(d, (x + 125, y + 215), "(d) crankshaft linkage", 23, FG)
    label(d, (x + 125, y + 246), "crank, heated slowly", 22, FG, anchor="mm")
    label(d, (x + 125, y + 285), "COULD BE q-e", 22, GREEN, bold=False)
    label(d, (x + 125, y + 305), "slow -> q-e, but P varies", 22, GRAY, bold=False)

    d.rounded_rectangle([40, 450, 1160, 585], radius=14, fill=FILL_Y, outline=FG, width=3)
    label(d, (600, 478), "The one test: is the gas pressure the SAME everywhere at every instant?",
          25, FG)
    label(d, (600, 513), "and does it follow the boundary slowly enough?",
          23, GRAY, bold=False)
    label(d, (600, 552), "yes -> q-e, so W = integral P dV  ||  no -> W comes from the surroundings",
          23, RED, bold=False)
    save(img, "fig2_5_four.png")


# ---------------------------------------------------------------- fig 2.6
def fig_2_6_bottle():
    img, d = new(W, 600)
    title(d, "Question 2.6: 130 bar -> 80 bar, which closed system?",
          "venting a cylinder: which closed system keeps a fixed mass?")

    # left: the apparatus
    d.rounded_rectangle([50, 115, 290, 265], radius=45, fill=FILL_B, outline=BLUE, width=5)
    label(d, (170, 158), "air", 25, BLUE)
    label(d, (170, 193), "130 bar", 25, BLUE)
    label(d, (170, 228), "-> 80 bar", 25, BLUE)
    d.rectangle([282, 172, 320, 212], fill=(230, 230, 230), outline=FG, width=3)
    label(d, (301, 240), "valve", 21, FG)
    arrow(d, (325, 192), (425, 192), RED, 5)
    label(d, (300, 290), "to atmosphere, 1 bar", 22, RED, anchor="lm")
    label(d, (300, 330), "opened to atmosphere, 1 bar", 22, GRAY, bold=False, anchor="lm")

    # left: (b) answer card
    d.rounded_rectangle([50, 375, 500, 555], radius=12, fill=FILL_Y, outline=GREEN, width=3)
    label(d, (70, 412), "(b) slow discharge -> q-e?", 23, GREEN, anchor="lm")
    label(d, (70, 450), "yes, IF the discharge is slow enough", 22, FG, anchor="lm", bold=False)
    label(d, (70, 482), "p uniform at every instant; no big", 21, GRAY, bold=False, anchor="lm")
    label(d, (70, 507), "pressure gradient or churning", 21, GRAY, bold=False, anchor="lm")
    label(d, (70, 535), "slow enough that P stays uniform", 21, GRAY, bold=False, anchor="lm")

    d.line([(520, 100), (520, 580)], fill=LGRAY, width=3)

    rows = [
        ("(i) ALL gas that was in the bottle", "NO", RED, FILL_R,
         "at the end, part of the boundary (the free", "surface) can no longer be found",
         "part of the boundary (a free surface) is gone"),
        ("(ii) the gas that ESCAPES", "NO", RED, FILL_R,
         "no part of its boundary can be defined", "at all in the final state",
         "no boundary can be pinned down at all"),
        ("(iii) the gas that REMAINS in it", "YES", GREEN, FILL_G,
         "boundary = the bottle's inside surface", "at every instant -> usable",
         "boundary is always the bottle wall -> usable"),
    ]
    y = 100
    for t, verdict, col, fill, l1, l2, cn in rows:
        d.rounded_rectangle([545, y, 1160, y + 160], radius=12, fill=fill, outline=col, width=3)
        label(d, (568, y + 28), t, 24, FG, anchor="lm")
        label(d, (1140, y + 28), verdict, 27, col, anchor="rm")
        label(d, (568, y + 70), l1, 21, GRAY, bold=False, anchor="lm")
        label(d, (568, y + 98), l2, 21, GRAY, bold=False, anchor="lm")
        label(d, (568, y + 134), cn, 21, GRAY, bold=False, anchor="lm")
        y += 172
    save(img, "fig2_6_bottle.png")


# ---------------------------------------------------------------- cheat sheet
def fig_cheatsheet():
    img, d = new(W, 700)
    title(d, "Set 2 one-glance card",
          "system vs control volume - property vs process - q-e test")

    cols = [
        ("System / Control volume", BLUE, FILL_B, [
            "system = fixed mass",
            "fixed mass, energy may cross",
            "C.V. = fixed region",
            "fixed region, matter may cross",
            "test: does matter cross?",
            "ask: does matter cross?",
        ]),
        ("Property / Process", GREEN, FILL_G, [
            "property: fixed by the state",
            "fixed by the state (P, V, T, U)",
            "heat Q, work W: path",
            "path, so not a property",
            "cycle: start = end",
            "same state at start and end",
        ]),
        ("Quasi-equilibrium", RED, FILL_R, [
            "slow enough, uniform inside",
            "slow enough -> uniform inside",
            "W = integral P dV only if q-e",
            "the W integral needs q-e",
            "unresisted -> not q-e",
            "unresisted expansion is not q-e",
        ]),
    ]
    x = 40
    for ttl, col, fill, lines in cols:
        d.rounded_rectangle([x, 110, x + 360, 620], radius=18, fill=fill, outline=col, width=4)
        label(d, (x + 180, 150), ttl, 26, col)
        yy = 205
        for k, ln in enumerate(lines):
            big = k % 2 == 0
            label(d, (x + 180, yy), ln, 24 if big else 22, FG if big else GRAY, bold=big)
            yy += 62 if big else 58
        x += 380
    label(d, (W // 2, 660), "3 tests: matter crosses? state or path? fast or slow?",
          26, FG)
    save(img, "fig2_cheatsheet.png")


if __name__ == "__main__":
    fig_2_1_station()
    fig_2_1_so2()
    fig_2_2_framework()
    fig_2_3_climbers()
    fig_2_4_tank()
    fig_2_5_four()
    fig_2_6_bottle()
    fig_cheatsheet()
