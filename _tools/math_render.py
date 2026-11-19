# -*- coding: utf-8 -*-
"""Minimal offline LaTeX-subset -> HTML renderer for the example posters.
No network, no third-party packages: real fraction bars, radicals, limits and
super/subscripts are produced with plain markup + CSS."""
from html import escape

SYMBOLS = {
    "to": "\u2192", "infty": "\u221e", "approx": "\u2248", "cdots": "\u22ef",
    "ldots": "\u2026", "dots": "\u2026", "times": "\u00d7", "cdot": "\u00b7",
    "le": "\u2264", "leq": "\u2264", "ge": "\u2265", "geq": "\u2265",
    "pm": "\u00b1", "mp": "\u2213", "ne": "\u2260", "neq": "\u2260",
    "pi": "\u03c0", "theta": "\u03b8", "xi": "\u03be", "varepsilon": "\u03b5",
    "epsilon": "\u03b5", "alpha": "\u03b1", "beta": "\u03b2", "lambda": "\u03bb",
    "mu": "\u03bc", "sigma": "\u03c3", "varphi": "\u03c6", "phi": "\u03c6",
    "Delta": "\u0394", "delta": "\u03b4", "Rightarrow": "\u21d2", "implies": "\u21d2",
    "Leftrightarrow": "\u21d4", "partial": "\u2202", "prime": "\u2032",
    "degree": "\u00b0", "circ": "\u00b0", "mid": "\u2223", "colon": ":",
    "quad": "\u2003", "qquad": "\u2003\u2003", "ldots\u200b": "",
}
FUNCS = ("sin", "cos", "tan", "cot", "sec", "csc", "arcsin", "arccos", "arctan",
         "sinh", "cosh", "tanh", "ln", "log", "exp", "max", "min", "det")
BIGOPS = {"sum": "\u2211", "prod": "\u220f", "int": "\u222b", "lim": "lim"}


def _atom(s, i):
    if i >= len(s):
        return "", i
    if s[i] == "\\":
        return _cmd(s, i)
    return escape(s[i]), i + 1


def _arg(s, i):
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        return _seq(s, i + 1)
    return _atom(s, i)


def _text(s, i):
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s) or s[i] != "{":
        return "", i
    depth, buf, j = 1, [], i + 1
    while j < len(s):
        c = s[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                break
        buf.append(c)
        j += 1
    return '<span class="txt">%s</span>' % escape("".join(buf)), j + 1


def _script(s, i, parts):
    base = parts.pop() if parts else ""
    sup = sub = ""
    while i < len(s) and s[i] in "^_":
        c = s[i]
        i += 1
        html, i = _arg(s, i)
        if c == "^":
            sup = html
        else:
            sub = html
    out = '<span class="scr">' + base
    if sup:
        out += "<sup>" + sup + "</sup>"
    if sub:
        out += "<sub>" + sub + "</sub>"
    return out + "</span>", i


def _cmd(s, i):
    j = i + 1
    if j < len(s) and s[j].isalpha():
        k = j
        while k < len(s) and s[k].isalpha():
            k += 1
        name, i = s[j:k], k
        if name == "frac":
            a, i = _arg(s, i)
            b, i = _arg(s, i)
            return ('<span class="frac"><span class="num">%s</span>'
                    '<span class="den">%s</span></span>' % (a, b)), i
        if name == "sqrt":
            a, i = _arg(s, i)
            return '<span class="sqrt"><svg class="root-sign" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="M2 57 L22 50 L48 96 L94 2 L100 2" fill="none" stroke="currentColor" stroke-width="5" vector-effect="non-scaling-stroke"/></svg><span class="radicand">%s</span></span>' % a, i
        if name == "binom":
            a, i = _arg(s, i)
            b, i = _arg(s, i)
            return ('<span class="binom"><span class="p">(</span>'
                    '<span class="st"><span class="bn">%s</span>'
                    '<span class="bk">%s</span></span>'
                    '<span class="p">)</span></span>' % (a, b)), i
        if name in BIGOPS:
            up = dn = ""
            while i < len(s) and s[i] in "^_":
                c = s[i]
                i += 1
                h, i = _arg(s, i)
                if c == "^":
                    up = h
                else:
                    dn = h
            sym = BIGOPS[name]
            out = '<span class="op op-%s">' % name
            if up:
                out += '<span class="lim">%s</span>' % up
            out += '<span class="base">%s</span>' % sym
            if dn:
                out += '<span class="lim">%s</span>' % dn
            return out + "</span>", i
        if name in ("vec", "hat", "bar", "tilde"):
            a, i = _arg(s, i)
            mark = {"vec": "\u2192", "hat": "\u02c6", "bar": "\u00af", "tilde": "\u02dc"}[name]
            return ('<span class="acc"><span class="accb">%s</span>'
                    '<span class="accm">%s</span></span>' % (a, mark)), i
        if name == "text":
            return _text(s, i)
        if name in FUNCS:
            html = '<span class="fn">%s</span>' % name
            if i < len(s) and s[i] in "^_":
                return _script(s, i, [html])
            return html, i
        if name in SYMBOLS:
            return SYMBOLS[name], i
        if name in ("left", "right", "big", "Big"):
            return "", i
        return escape(name), i
    if j < len(s):
        c = s[j]
        i = j + 1
        if c in "{}$%_^&":
            return escape(c), i
        if c == ",":
            return "\u2009", i
        if c in ";:":
            return "\u2003", i
        if c == "!":
            return "", i
        if c == "\\":
            return "<br>", i
        return escape(c), i
    return "", i


def _seq(s, i):
    parts = []
    while i < len(s):
        c = s[i]
        if c == "}":
            return "".join(parts), i + 1
        if c == "\\":
            html, i = _cmd(s, i)
            parts.append(html)
            continue
        if c in "^_":
            html, i = _script(s, i, parts)
            parts.append(html)
            continue
        if c == " ":
            i += 1
            continue
        if c == "-":
            parts.append("\u2212")
            i += 1
            continue
        parts.append(escape(c))
        i += 1
    return "".join(parts), i


def render(src):
    """LaTeX subset -> HTML string (tags generated here only; input escaped)."""
    return _seq(src, 0)[0]
