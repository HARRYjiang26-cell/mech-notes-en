# -*- coding: utf-8 -*-
"""Chapter/section figures with REAL math via math_render + headless Chrome.
Replaces the old Pillow ASCII version. Filenames unchanged (d12_*.png), plus ex_ch9_map.png."""
import os, shutil, sys

from gen_example_posters import BROWSER, CSS, PAGE, WORK, FIG, rich, shoot, trim, W

EXTRA = """
.rows { margin-top:20px; }
.row { display:flex; align-items:center; gap:18px; border:3px solid #3b6fb6; border-radius:12px;
  background:#e9f1fb; padding:14px 20px; margin-bottom:6px; }
.row .no { font:700 30px/1 "Segoe UI",sans-serif; color:#3b6fb6; min-width:44px; }
.row .nm { font:600 22px/1.4 "Segoe UI","Microsoft YaHei",sans-serif; min-width:300px; }
.row .ds { font:400 20px/1.7 "Segoe UI","Microsoft YaHei",sans-serif; color:#333; }
.arr { text-align:center; font:700 26px/1.1 "Segoe UI",sans-serif; color:#8aa4c8; margin:2px 0 8px; }
.cols { display:grid; grid-template-columns:repeat(4,1fr); gap:18px; margin-top:20px; }
.cell { border:3px solid var(--c); border-radius:12px; background:var(--f); padding:0 0 12px; }
.cell h4 { background:var(--c); color:#fff; margin:0 0 10px; padding:10px 14px;
  font:600 20px/1.3 "Segoe UI",sans-serif; border-radius:8px 8px 0 0; }
.cell p { font:400 19px/1.9 "Segoe UI","Microsoft YaHei",sans-serif; margin:0 12px 8px; color:#1a1a1a; }
.formula { font-size:1.15em; }
"""


def render(slug, body, width=None):
    css = (CSS + EXTRA) % {"w": width or W}
    html = PAGE % {"css": css, "body": body}
    os.makedirs(WORK, exist_ok=True)
    hp = os.path.join(WORK, slug + ".html")
    pp = os.path.join(WORK, slug + ".png")
    open(hp, "w", encoding="utf-8").write(html)
    if os.environ.get("FIG_HTML_ONLY"):
        print("HTML", slug)
        return
    if os.path.exists(pp):
        os.remove(pp)
    if not BROWSER:
        print("RESULT FAIL: no headless browser found")
        sys.exit(1)
    if not shoot(hp, pp, width=width or W):
        print("FAIL shoot", slug)
        sys.exit(1)
    size = trim(pp)
    if not size or size[1] < 300:
        print("FAIL small", slug, size)
        sys.exit(1)
    shutil.copyfile(pp, os.path.join(FIG, slug + ".png"))
    print("OK", slug, "%dx%d" % size)


def title_bar(text):
    return '<div class="title">%s</div>' % rich(text)


def rows(items):
    out = ['<div class="rows">']
    for i, (nm, ds) in enumerate(items):
        if i:
            out.append('<div class="arr">&#8595;</div>')
        out.append('<div class="row"><div class="no">%d.</div><div class="nm">%s</div><div class="ds">%s</div></div>'
                   % (i + 1, rich(nm), rich(ds)))
    out.append("</div>")
    return "".join(out)


def fig_d12_map():
    render("d12_map", title_bar("12 November: tools and their conditions") + rows([
        ("Leibniz", r"$D^n(uv)=\sum_{r=0}^n\binom{n}{r}D^ru\,D^{n-r}v$"),
        ("Taylor / Maclaurin", r"For $\sin x$, $\cos x$, $e^x$: every finite $x$. For general $f$, require $R_n\to0$."),
        ("Bouncing ball", r"$D=h\frac{1+r}{1-r}$ for $h>0$, $0\le r<1$."),
        ("Ratio test", r"$L<1$: absolute convergence; $L>1$: divergence; $L=1$: undecided."),
        ("Binomial series", r"Nonterminating series: $R=1$; endpoints separate. Nonnegative integer exponent: polynomial."),
        ("Partial derivatives", r"Freeze the other input. Partial derivatives alone do not imply differentiability."),
    ]))


def fig_d12_leibniz():
    render("d12_leibniz", title_bar("Leibniz: keep the binomial coefficient") + rows([
        ("rule", r"$D^n(uv)=\sum_{r=0}^n\binom{n}{r}D^ru\,D^{n-r}v$"),
        ("$n=2$, $u=x^2$", r"$D^2(x^2e^x)=x^2e^x+2\cdot(2x)e^x+2e^x$"),
        ("polynomial derivatives", r"$D^0u=x^2$, $Du=2x$, $D^2u=2$; higher derivatives vanish."),
        ("where to stop", r"Degree $m$: sum to $\min(m,n)$, at most $\min(m,n)+1$ terms."),
    ]))


def fig_d12_bounce():
    render("d12_bounce", title_bar("Bouncing ball: one drop, two legs per rebound") + rows([
        ("assumptions", r"$h>0$, $0\le r<1$; $N$ counts completed up-and-down rebounds."),
        ("partial distances", r"$D_1=h+2rh$, $D_2=h+2rh+2r^2h$"),
        ("finite total", r"$D_N=h+2h\sum_{n=1}^N r^n$"),
        ("limit", r"$\lim_{N\to\infty}D_N=h\frac{1+r}{1-r}$"),
        ("numbers", r"$h=1.5$ m, $r=0.7$: $D=8.5$ m, $D_3=6.099$ m $\approx6.10$ m."),
    ]))


def fig_d12_ratio():
    render("d12_ratio", title_bar("Ratio test: three outcomes") + rows([
        ("compute", r"$L=\lim_{r\to\infty}\left|\frac{a_{r+1}}{a_r}\right|$"),
        ("$L<1$", "absolutely convergent"),
        ("$L>1$", "divergent"),
        ("$L=1$", "inconclusive: use a different test"),
        ("important distinction", r"Convergence alone does not identify a Taylor series with $f$; also show $R_n\to0$."),
    ]))


def fig_d12_binom():
    render("d12_binom", title_bar("Binomial series: interior, endpoints, termination") + rows([
        ("series", r"$(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\cdots$"),
        ("nonterminating case", r"Absolute convergence for $|x|<1$; $R=1$; endpoints require separate tests."),
        ("terminating case", r"If $n$ is a nonnegative integer, the polynomial identity holds for every real $x$."),
        ("safe substitution", r"$\sqrt{51}=7\sqrt{1+\frac{2}{49}}$; $\left|\frac{2}{49}\right|<1$."),
    ]))


def fig_d12_cheat():
    render("d12_cheatsheet", title_bar("12 November: formula card with conditions") + rows([
        ("Leibniz", r"$D^n(uv)=\sum_{r=0}^n\binom{n}{r}D^ru\,D^{n-r}v$"),
        ("Taylor", r"$f(a+h)=\sum_{k=0}^n\frac{h^k}{k!}f^{(k)}(a)+R_n$"),
        ("Maclaurin", r"$\sin x$, $\cos x$, $e^x$: series equal the functions for all finite $x$; $R_n\to0$."),
        ("Geometric", r"$\sum_{n=0}^{\infty}x^n=\frac{1}{1-x}$ for $|x|<1$."),
        ("Bouncing ball", r"$D_N=h+2h\sum_{n=1}^N r^n$, $D=h\frac{1+r}{1-r}$; $h>0$, $0\le r<1$."),
        ("Ratio", r"$L=\lim_{r\to\infty}\left|\frac{a_{r+1}}{a_r}\right|$; $L=1$ is inconclusive."),
        ("Binomial", r"Nonterminating: $R=1$, endpoints separate. Nonnegative integer exponent: polynomial."),
        ("Partial", r"$f_x(x_0,y_0)=\lim_{\delta x\to0}\frac{f(x_0+\delta x,y_0)-f(x_0,y_0)}{\delta x}$"),
    ]))


def fig_ch9_map():
    cells = [
        ("9.1 partial derivatives", "freeze one variable",
         ["$f_{x}=\\frac{\\partial f}{\\partial x}$ with $y$ frozen"]),
        ("9.2 higher order", "second, mixed, order can be swapped",
         ["$f_{xy}=f_{yx}$ for continuous second partials in a neighborhood"]),
        ("9.3 small changes", "total differential",
         ["$\\delta z\\approx z_{x}\\delta x+z_{y}\\delta y$"]),
        ("9.4 chain rule", "three cases",
         ["$x(t),y(t)$", "$y(x)$", "$z(x,y)=C$"]),
    ]
    pal = ["#c0504d", "#3b6fb6", "#4a9e5c", "#8a63b0"]
    fil = ["#fdecec", "#e9f1fb", "#eaf7ee", "#f3ecfa"]
    body = [title_bar("Chapter 9 (to 9.4): partial differentiation - the map")]
    body.append('<div class="cols">')
    for i, (h4, sub, lines) in enumerate(cells):
        body.append('<div class="cell" style="--c:%s;--f:%s"><h4>%s</h4>' % (pal[i], fil[i], rich(h4)))
        body.append('<p>%s</p>' % rich(sub))
        for ln in lines:
            body.append('<p class="formula">%s</p>' % rich(ln))
        body.append("</div>")
    body.append("</div>")
    render("ex_ch9_map", "".join(body), width=1500)


FIGS = {
    "d12_map": fig_d12_map, "d12_leibniz": fig_d12_leibniz, "d12_bounce": fig_d12_bounce,
    "d12_ratio": fig_d12_ratio, "d12_binom": fig_d12_binom, "d12_cheatsheet": fig_d12_cheat,
    "ex_ch9_map": fig_ch9_map,
}

if __name__ == "__main__":
    only = sys.argv[1:]
    for name, fn in FIGS.items():
        if only and name not in only:
            continue
        fn()
    print("RESULT PASS figures -> figures/")
