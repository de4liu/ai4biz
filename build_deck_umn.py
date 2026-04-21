from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── UMN Brand Colors ──────────────────────────────────────────
MAROON  = RGBColor(0x7A, 0x00, 0x19)   # UMN Maroon
GOLD    = RGBColor(0xFF, 0xCC, 0x33)   # UMN Gold
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
BLACK   = RGBColor(0x00, 0x00, 0x00)
LGRAY   = RGBColor(0xF5, 0xF5, 0xF5)   # near-white background
MGRAY   = RGBColor(0xE0, 0xE0, 0xE0)   # dividers
DGRAY   = RGBColor(0x33, 0x33, 0x33)   # body text

# ── Fonts ────────────────────────────────────────────────────
FONT_H  = "Raleway"
FONT_B  = "Arial"

prs = Presentation()
prs.slide_width  = Inches(10.0)
prs.slide_height = Inches(5.63)

BLANK = prs.slide_layouts[6]

def add_rect(slide, l, t, w, h, fill=None, line=None, lw=0.5):
    s = slide.shapes.add_shape(1,
        Inches(l), Inches(t), Inches(w), Inches(h))
    s.line.fill.background()
    if fill:
        s.fill.solid(); s.fill.fore_color.rgb = fill
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = line; s.line.width = Pt(lw)
    else:
        s.line.fill.background()
    return s

def txb(slide, text, l, t, w, h,
        sz=16, bold=False, italic=False,
        color=DGRAY, align=PP_ALIGN.LEFT,
        font=None, wrap=True):
    tb = slide.shapes.add_textbox(
        Inches(l), Inches(t), Inches(w), Inches(h))
    tb.word_wrap = wrap
    tf = tb.text_frame; tf.word_wrap = wrap
    p  = tf.paragraphs[0]; p.alignment = align
    r  = p.add_run(); r.text = text
    r.font.size   = Pt(sz)
    r.font.bold   = bold
    r.font.italic = italic
    r.font.color.rgb = color
    r.font.name   = font or FONT_H
    return tb

def txb_lines(slide, lines, l, t, w, h,
              sz=15, bold=False, color=DGRAY,
              align=PP_ALIGN.LEFT, font=None):
    """lines = list of str or (str, bold, sz, color)"""
    tb = slide.shapes.add_textbox(
        Inches(l), Inches(t), Inches(w), Inches(h))
    tb.word_wrap = True
    tf = tb.text_frame; tf.word_wrap = True
    for i, item in enumerate(lines):
        if isinstance(item, str):
            txt, bld, s, col = item, bold, sz, color
        else:
            txt = item[0]
            bld = item[1] if len(item) > 1 else bold
            s   = item[2] if len(item) > 2 else sz
            col = item[3] if len(item) > 3 else color
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = txt
        r.font.size = Pt(s); r.font.bold = bld
        r.font.color.rgb = col
        r.font.name = font or FONT_B
    return tb

def header_bar(slide, title, subtitle=None):
    """Standard UMN-style top bar: white bg, maroon title underlined with gold rule"""
    add_rect(slide, 0, 0, 10, 5.63, fill=WHITE)
    add_rect(slide, 0, 0, 10, 0.95, fill=MAROON)
    txb(slide, title, 0.25, 0.12, 9.2, 0.72,
        sz=24, bold=True, color=WHITE, font=FONT_H)
    if subtitle:
        txb(slide, subtitle, 0.25, 0.75, 9.2, 0.35,
            sz=12, italic=True, color=GOLD, font=FONT_H)
    # Gold rule under header
    add_rect(slide, 0, 0.95, 10, 0.06, fill=GOLD)
    # Footer
    add_rect(slide, 0, 5.35, 10, 0.28, fill=LGRAY)
    txb(slide, "IDSC 4101 · Agentic AI for Business Applications · University of Minnesota",
        0.25, 5.37, 9.5, 0.22, sz=9, italic=True,
        color=RGBColor(0x88, 0x88, 0x88), font=FONT_B,
        align=PP_ALIGN.LEFT)

# ═══════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, 10, 5.63, fill=WHITE)
add_rect(s, 0, 0, 0.22, 5.63, fill=MAROON)   # left sidebar
add_rect(s, 0.22, 4.5, 9.78, 0.08, fill=GOLD) # gold rule bottom

# UMN wordmark placeholder
txb(s, "UNIVERSITY OF MINNESOTA", 0.4, 0.2, 9.2, 0.35,
    sz=10, bold=True, color=MAROON, font=FONT_H, align=PP_ALIGN.LEFT)
add_rect(s, 0.4, 0.52, 1.8, 0.04, fill=MAROON)

txb(s, "IDSC 4101", 0.4, 0.75, 9, 0.42,
    sz=14, bold=False, italic=True, color=MAROON, font=FONT_H)
txb(s, "Generative and Agentic\nAI for Business", 0.4, 1.15, 8.8, 1.8,
    sz=40, bold=True, color=MAROON, font=FONT_H)
txb(s, "A 2-credit upper-division course for all business majors",
    0.4, 2.95, 8.5, 0.45, sz=17, color=DGRAY, font=FONT_B)
add_rect(s, 0.4, 3.45, 9.2, 0.04, fill=MGRAY)
txb(s, "No coding required  ·  7 weeks  ·  14 sessions  ·  Project-based capstone",
    0.4, 3.55, 8.8, 0.38, sz=13, color=DGRAY, font=FONT_B)
txb(s, "[Your Name]  ·  Carlson School of Management  ·  [Semester Year]",
    0.4, 4.1, 8.8, 0.35, sz=11, italic=True,
    color=RGBColor(0x88,0x88,0x88), font=FONT_B)

# ═══════════════════════════════════════════════════════════════
# SLIDE 2 — The Gap
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
header_bar(s, "The Gap We're Filling")

txb(s, "Business graduates are already using AI — but most lack the vocabulary and judgment to lead with it.",
    0.3, 1.1, 9.4, 0.55, sz=16, bold=False, color=DGRAY, font=FONT_B)
add_rect(s, 0.3, 1.68, 9.4, 0.04, fill=MGRAY)

# Two columns
txb(s, "What students typically have", 0.3, 1.82, 4.5, 0.38,
    sz=13, bold=True, color=MAROON, font=FONT_H)
txb_lines(s, [
    "✓  Experience using a chatbot interface",
    "✗  Understanding of why AI behaves as it does",
    "✗  Ability to spot automation opportunities",
    "✗  Vocabulary to evaluate vendor claims",
    "✗  Awareness of responsible AI risks",
], 0.3, 2.2, 4.5, 2.9, sz=13, color=DGRAY)

txb(s, "What this course delivers", 5.1, 1.82, 4.5, 0.38,
    sz=13, bold=True, color=MAROON, font=FONT_H)
txb_lines(s, [
    "✓  Builder + ideation mindset",
    "✓  Hands-on tool fluency (no coding)",
    "✓  Workflow automation skills",
    "✓  Agentic AI literacy",
    "✓  Responsible AI judgment",
], 5.1, 2.2, 4.5, 2.9, sz=13, color=DGRAY)

add_rect(s, 4.9, 1.82, 0.04, 3.3, fill=GOLD)

add_rect(s, 0.3, 5.0, 9.4, 0.28, fill=LGRAY)
txb(s, "No peer program currently offers a no-code agentic AI course combining conceptual depth + hands-on fluency.",
    0.4, 5.02, 9.2, 0.24, sz=10, italic=True,
    color=RGBColor(0x55,0x55,0x55), font=FONT_B)

# ═══════════════════════════════════════════════════════════════
# SLIDE 3 — What Makes This Course Different
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
header_bar(s, "What Makes IDSC 4101 Different")

rows = [
    ("Most AI courses for business", "IDSC 4101"),
    ("Prompt engineering focus only", "Builder + ideation mindset throughout"),
    ("Lecture and case study only", "Build sprints every other week"),
    ("No hands-on tool time", "Students build automations and agents in class"),
    ("Ethics as a standalone week", "Responsible AI woven across all 7 weeks"),
    ("One-shot final presentation", "AI Innovation Showcase with external guests"),
]

for i, (left, right) in enumerate(rows):
    y = 1.05 + i * 0.63
    is_header = (i == 0)
    bg = MAROON if is_header else (LGRAY if i % 2 == 0 else WHITE)
    tc = WHITE if is_header else DGRAY
    add_rect(s, 0.25, y, 4.55, 0.58, fill=bg)
    add_rect(s, 4.9,  y, 4.85, 0.58, fill=bg)
    txb(s, left,  0.35, y+0.1, 4.35, 0.42,
        sz=13 if not is_header else 13,
        bold=is_header, color=WHITE if is_header else DGRAY, font=FONT_B)
    txb(s, right, 5.0,  y+0.1, 4.65, 0.42,
        sz=13 if not is_header else 13,
        bold=is_header, color=WHITE if is_header else MAROON, font=FONT_B)

add_rect(s, 4.78, 1.05, 0.06, 3.78, fill=GOLD)

# ═══════════════════════════════════════════════════════════════
# SLIDE 4 — The 7-Week Arc
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
header_bar(s, "The 7-Week Arc")

phases = [
    ("Wks 1–2",  "Foundations\n& Personal AI",      MAROON),
    ("Wks 3–4",  "Team Workflows\n& Biz Apps",       RGBColor(0x5A,0x00,0x14)),
    ("Wks 5–6",  "Agentic AI\n& Product Thinking",  RGBColor(0x99,0x00,0x1F)),
    ("Wk 7",     "Strategy,\nEthics & Showcase",    RGBColor(0x3D,0x00,0x0C)),
]
details = [
    "Gemini · NotebookLM\nPrompt strategy\nPersonal productivity",
    "Zapier / Make\nBusiness function apps\nMidterm exam",
    "n8n · Voiceflow\nAgent blueprints\nBuild sprint #2",
    "AI strategy frames\nResponsible AI session\nCapstone pitches",
]
for i, ((wk, phase, col), detail) in enumerate(zip(phases, details)):
    x = 0.25 + i * 2.4
    add_rect(s, x, 1.08, 2.2, 0.7, fill=col)
    txb(s, wk,    x+0.05, 1.1,  2.1, 0.3, sz=12, bold=True,  color=GOLD,  font=FONT_H)
    txb(s, phase, x+0.05, 1.38, 2.1, 0.38, sz=11, bold=False, color=WHITE, font=FONT_H)
    add_rect(s, x, 1.78, 2.2, 2.1, fill=LGRAY, line=MGRAY, lw=0.5)
    txb(s, detail, x+0.1, 1.85, 2.0, 1.95,
        sz=12, color=DGRAY, font=FONT_B)
    if i < 3:
        txb(s, "→", x+2.2, 2.2, 0.2, 0.5,
            sz=16, bold=True, color=MAROON, align=PP_ALIGN.CENTER, font=FONT_H)

add_rect(s, 0.25, 3.92, 9.5, 0.04, fill=GOLD)
txb(s, "Personal  →  Team  →  Agentic  →  Strategic",
    0.25, 4.0, 9.5, 0.35,
    sz=13, bold=True, color=MAROON, align=PP_ALIGN.CENTER, font=FONT_H)
txb(s, "14 sessions  ·  3 Build Sprints  ·  4 Reflection Posts  ·  Midterm + Final Exam  ·  Team Capstone Pitch",
    0.25, 4.38, 9.5, 0.28,
    sz=11, color=DGRAY, align=PP_ALIGN.CENTER, font=FONT_B)

# ═══════════════════════════════════════════════════════════════
# SLIDE 5 — Tools
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
header_bar(s, "Tools Students Use — No Coding Required")

tools = [
    ("Conversational AI\n& Research",   "Google Gemini\nNotebookLM\nGoogle AI Studio",     "Weeks 1–3"),
    ("No-Code\nAutomation",              "Zapier  /  Make\nRelevance AI",                    "Weeks 3–5"),
    ("Agentic AI\nPlatforms",            "n8n\nVoiceflow",                                   "Weeks 5–6"),
]
for i, (cat, tools_txt, wks) in enumerate(tools):
    x = 0.3 + i * 3.2
    add_rect(s, x, 1.08, 2.95, 0.62, fill=MAROON)
    txb(s, cat, x+0.1, 1.1, 2.75, 0.58,
        sz=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, font=FONT_H)
    add_rect(s, x, 1.7, 2.95, 2.55, fill=LGRAY, line=MGRAY, lw=0.5)
    txb(s, tools_txt, x+0.1, 1.85, 2.75, 2.2,
        sz=15, color=DGRAY, align=PP_ALIGN.CENTER, font=FONT_B)
    add_rect(s, x, 4.25, 2.95, 0.38, fill=GOLD)
    txb(s, wks, x+0.1, 4.28, 2.75, 0.32,
        sz=12, bold=True, color=MAROON, align=PP_ALIGN.CENTER, font=FONT_H)

txb(s, "All platforms have free tiers sufficient for coursework. Tool categories are durable — specific platforms can be swapped as the landscape evolves.",
    0.3, 4.72, 9.4, 0.5,
    sz=10, italic=True, color=RGBColor(0x77,0x77,0x77),
    align=PP_ALIGN.CENTER, font=FONT_B)

# ═══════════════════════════════════════════════════════════════
# SLIDE 6 — Assessment Model
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
header_bar(s, "Assessment: Hybrid Model")

items = [
    ("20%", "Reflection Posts ×4",           "Individual · 200–300 words · Bi-weekly · Personal observations"),
    ("25%", "Midterm Conceptual Exam",        "Take-home · Open-note · Case-based · No coding"),
    ("25%", "Final Conceptual Exam",          "Take-home · Open-note · Integrative cases · Strategy + ethics"),
    ("25%", "AI Innovation Showcase",         "Team pitch · No prototype · External guests · Trade show format"),
    ("10%", "Participation + Build Sprints",  "In-class builds (Wk 3 + Wk 5) · Engagement · Attendance"),
]
for i, (pct, title, desc) in enumerate(items):
    y = 1.05 + i * 0.85
    add_rect(s, 0.25, y, 1.1, 0.75, fill=MAROON)
    txb(s, pct, 0.25, y+0.12, 1.1, 0.52,
        sz=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER, font=FONT_H)
    add_rect(s, 1.45, y, 8.3, 0.75, fill=LGRAY if i%2==0 else WHITE, line=MGRAY, lw=0.3)
    txb(s, title, 1.6, y+0.04, 4.5, 0.38,
        sz=14, bold=True, color=MAROON, font=FONT_H)
    txb(s, desc,  1.6, y+0.4, 8.0, 0.3,
        sz=11, color=DGRAY, font=FONT_B)

# ═══════════════════════════════════════════════════════════════
# SLIDE 7 — AI Innovation Showcase
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
header_bar(s, "The AI Innovation Showcase", "Week 7 · Trade show format · External guests")

add_rect(s, 0.25, 1.08, 9.5, 0.72, fill=LGRAY, line=MGRAY, lw=0.3)
txb_lines(s, [
    ("Teams design an AI-assisted solution to a real business problem — no working prototype required.", False, 14, DGRAY),
    ("External practitioners rotate through team stations, ask structured questions, and give real feedback.", False, 14, DGRAY),
], 0.4, 1.12, 9.2, 0.65, font=FONT_B)

# Milestone strip
steps = [
    ("Wk 4",   "Teams form\n+ problem\nstatement"),
    ("Wk 5\nS1","Solution\ndesign sketch"),
    ("Wk 5\nS2","Peer pitch\npractice"),
    ("Wk 7\nS1","Slide deck\nsubmitted"),
    ("Wk 7\nS2","AI Innovation\nShowcase 🎉"),
]
cols = [MAROON, RGBColor(0x5A,0x00,0x14), RGBColor(0x99,0x00,0x1F),
        RGBColor(0x3D,0x00,0x0C), MAROON]
for i, (lbl, desc) in enumerate(steps):
    x = 0.25 + i * 1.88
    add_rect(s, x, 1.9, 1.7, 0.5, fill=cols[i])
    txb(s, lbl, x, 1.93, 1.7, 0.44,
        sz=11, bold=True, color=WHITE if i < 4 else GOLD,
        align=PP_ALIGN.CENTER, font=FONT_H)
    add_rect(s, x, 2.4, 1.7, 1.35, fill=LGRAY, line=MGRAY, lw=0.3)
    txb(s, desc, x+0.05, 2.45, 1.6, 1.25,
        sz=11, color=DGRAY, align=PP_ALIGN.CENTER, font=FONT_B)
    if i < 4:
        txb(s, "›", x+1.7, 2.5, 0.18, 0.5,
            sz=18, bold=True, color=MAROON,
            align=PP_ALIGN.CENTER, font=FONT_H)

add_rect(s, 0.25, 3.82, 9.5, 0.04, fill=GOLD)
txb(s, "Rubric: Problem clarity  ·  Solution design  ·  Business value  ·  Responsible AI awareness  ·  Pitch quality",
    0.25, 3.9, 9.5, 0.3,
    sz=11, italic=True, color=DGRAY, align=PP_ALIGN.CENTER, font=FONT_B)

add_rect(s, 0.25, 4.28, 9.5, 0.68, fill=MAROON)
txb(s, "\"The hardest part of any AI project is defining the problem and designing the solution clearly — that's exactly what this format tests, and what employers are hiring for.\"",
    0.4, 4.33, 9.2, 0.6,
    sz=11, italic=True, color=GOLD, align=PP_ALIGN.CENTER, font=FONT_H)

# ═══════════════════════════════════════════════════════════════
# SLIDE 8 — Call to Action
# ═══════════════════════════════════════════════════════════════
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, 10, 5.63, fill=WHITE)
add_rect(s, 0, 0, 0.22, 5.63, fill=MAROON)
add_rect(s, 0.22, 1.52, 9.78, 0.06, fill=GOLD)

txb(s, "UNIVERSITY OF MINNESOTA",
    0.4, 0.12, 9.2, 0.35, sz=10, bold=True,
    color=MAROON, font=FONT_H)
add_rect(s, 0.4, 0.45, 1.8, 0.04, fill=MAROON)
txb(s, "Ready to Launch",
    0.4, 0.62, 9.2, 0.85,
    sz=36, bold=True, color=MAROON, font=FONT_H)

points = [
    "Full 7-week syllabus with session-level detail — complete",
    "Hybrid model: 2 conceptual exams + capstone pitch + 4 reflection posts",
    "No coding — accessible to all business concentrations",
    "All tools have free student tiers; AI Studio coordinated with IT",
    "AI Innovation Showcase creates a high-visibility department event",
    "Fills a genuine whitespace: no comparable course at peer institutions",
]
for i, pt in enumerate(points):
    y = 1.65 + i * 0.54
    add_rect(s, 0.4, y+0.08, 0.22, 0.22, fill=GOLD)
    txb(s, pt, 0.75, y, 9.0, 0.5, sz=14, color=DGRAY, font=FONT_B)

add_rect(s, 0.4, 4.98, 9.2, 0.04, fill=MAROON)
txb(s, "Seeking department support to offer IDSC 4101 in [Semester Year].",
    0.4, 5.06, 8.5, 0.35,
    sz=13, bold=True, color=MAROON, font=FONT_H)

# ── Save ─────────────────────────────────────────────────────
prs.save("/workspace/IDSC4101_UMN_proposal.pptx")
print("Saved: /workspace/IDSC4101_UMN_proposal.pptx")
