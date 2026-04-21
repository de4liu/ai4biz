from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ── Brand colors ──────────────────────────────────────────────
NAVY   = RGBColor(0x1A, 0x2A, 0x4A)   # deep navy — background / accents
AMBER  = RGBColor(0xF5, 0xA6, 0x23)   # amber — highlight
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LGRAY  = RGBColor(0xF2, 0xF4, 0xF7)   # light gray — body bg
DGRAY  = RGBColor(0x44, 0x44, 0x55)   # dark gray — body text
TEAL   = RGBColor(0x1A, 0x8C, 0x8C)   # teal — secondary accent

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

BLANK = prs.slide_layouts[6]  # truly blank

def add_rect(slide, l, t, w, h, fill_color=None, line_color=None, line_width=None):
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    shape.line.fill.background()
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(line_width or 1)
    else:
        shape.line.fill.background()
    return shape

def add_text(slide, text, l, t, w, h,
             size=18, bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, wrap=True, italic=False):
    txb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    txb.word_wrap = wrap
    tf = txb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txb

def add_text_lines(slide, lines, l, t, w, h,
                   size=16, bold=False, color=DGRAY,
                   align=PP_ALIGN.LEFT, spacing=1.15):
    """lines = list of (text, bold_override, size_override)"""
    txb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    txb.word_wrap = True
    tf = txb.text_frame
    tf.word_wrap = True
    from pptx.util import Pt as PT
    from pptx.oxml.ns import qn
    import lxml.etree as etree
    for i, item in enumerate(lines):
        if isinstance(item, str):
            txt, bld, sz = item, bold, size
        else:
            txt = item[0]
            bld = item[1] if len(item) > 1 else bold
            sz  = item[2] if len(item) > 2 else size
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        run = p.add_run()
        run.text = txt
        run.font.size = PT(sz)
        run.font.bold = bld
        run.font.color.rgb = color
    return txb

def navy_slide(title_text, subtitle_text=None):
    slide = prs.slides.add_slide(BLANK)
    add_rect(slide, 0, 0, 13.33, 7.5, fill_color=NAVY)
    add_rect(slide, 0, 6.9, 13.33, 0.6, fill_color=AMBER)
    add_text(slide, title_text, 0.6, 2.2, 12, 2.0,
             size=40, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    if subtitle_text:
        add_text(slide, subtitle_text, 0.6, 4.0, 12, 0.7,
                 size=20, color=AMBER, align=PP_ALIGN.CENTER)
    add_text(slide, "IDSC 4101 · Agentic AI for Business Applications",
             0.6, 7.0, 12, 0.4, size=11, color=WHITE,
             align=PP_ALIGN.CENTER, italic=True)
    return slide

def body_slide(title_text, accent_bar=True):
    slide = prs.slides.add_slide(BLANK)
    add_rect(slide, 0, 0, 13.33, 7.5, fill_color=LGRAY)
    add_rect(slide, 0, 0, 13.33, 1.1, fill_color=NAVY)
    if accent_bar:
        add_rect(slide, 0, 1.1, 0.12, 6.4, fill_color=AMBER)
    add_text(slide, title_text, 0.3, 0.18, 12.5, 0.8,
             size=26, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
    add_text(slide, "IDSC 4101", 11.8, 0.25, 1.4, 0.5,
             size=11, color=AMBER, align=PP_ALIGN.RIGHT, italic=True)
    return slide

# ── SLIDE 1: Title ─────────────────────────────────────────────
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, 13.33, 7.5, fill_color=NAVY)
add_rect(s, 0, 0, 0.35, 7.5, fill_color=AMBER)
add_rect(s, 0, 6.7, 13.33, 0.8, fill_color=RGBColor(0x0F, 0x1A, 0x33))
add_text(s, "IDSC 4101", 0.55, 1.6, 12, 0.7,
         size=18, bold=True, color=AMBER, align=PP_ALIGN.LEFT)
add_text(s, "Generative and Agentic\nAI for Business", 0.55, 2.2, 11.5, 2.4,
         size=46, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
add_text(s, "A 2-credit upper-division course for business majors\nNo coding required  ·  7 weeks  ·  Project-based",
         0.55, 4.55, 11, 0.9, size=18, color=LGRAY, align=PP_ALIGN.LEFT)
add_text(s, "[Your Name]  ·  Department of Information Systems  ·  [Semester Year]",
         0.55, 6.85, 12, 0.45, size=13, color=RGBColor(0xAA, 0xBB, 0xCC),
         align=PP_ALIGN.LEFT, italic=True)

# ── SLIDE 2: The Gap ───────────────────────────────────────────
s = body_slide("The Gap We're Filling")
add_text_lines(s, [
    ("Business graduates are already using AI — but most lack the vocabulary,",  False, 18),
    ("frameworks, and judgment to lead with it.", False, 18),
    ("", False, 8),
    ("What they typically have:", True, 16),
    ("  ✓  Experience using a chatbot interface", False, 16),
    ("  ✗  Understanding of why AI behaves the way it does", False, 16),
    ("  ✗  Ability to identify automation opportunities in a workflow", False, 16),
    ("  ✗  Vocabulary to evaluate vendor claims or lead an AI initiative", False, 16),
    ("  ✗  Awareness of responsible AI risks in business deployment", False, 16),
    ("", False, 8),
    ("No top-10 business school currently offers a no-code agentic AI course", True, 16),
    ("combining conceptual depth + hands-on tool fluency for non-technical students.", False, 16),
], 0.35, 1.25, 12.6, 5.8, color=DGRAY)

# ── SLIDE 3: What Makes This Course Different ──────────────────
s = body_slide("What Makes This Course Different")
# Two columns
add_rect(s, 0.35, 1.25, 6.1, 5.8, fill_color=WHITE)
add_rect(s, 6.85, 1.25, 6.1, 5.8, fill_color=WHITE)
add_text(s, "Most AI courses for business", 0.55, 1.35, 5.7, 0.5,
         size=14, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
add_text_lines(s, [
    ("→  Prompt engineering focus", False, 15),
    ("→  Lecture + case study only", False, 15),
    ("→  No hands-on tool time", False, 15),
    ("→  Ethics as a standalone week", False, 15),
    ("→  One-shot final presentation", False, 15),
], 0.55, 1.85, 5.7, 4.5, color=DGRAY)
add_text(s, "IDSC 4101", 7.05, 1.35, 5.7, 0.5,
         size=14, bold=True, color=AMBER, align=PP_ALIGN.LEFT)
add_text_lines(s, [
    ("→  Builder + ideation mindset", False, 15),
    ("→  Build sprints every other week", False, 15),
    ("→  No-code tools students keep using after class", False, 15),
    ("→  Ethics woven in, not siloed", False, 15),
    ("→  AI Innovation Showcase with external guests", False, 15),
], 7.05, 1.85, 5.7, 4.5, color=DGRAY)
add_rect(s, 6.6, 1.25, 0.05, 5.8, fill_color=LGRAY)

# ── SLIDE 4: The 7-Week Arc ────────────────────────────────────
s = body_slide("The 7-Week Arc")
weeks = [
    ("Wk 1–2", "Foundations + Personal AI",    AMBER),
    ("Wk 3–4", "Team Workflows + Business Apps", TEAL),
    ("Wk 5–6", "Agentic AI + Product Thinking",  RGBColor(0x7B, 0x68, 0xEE)),
    ("Wk 7",   "Strategy, Ethics + Showcase",    RGBColor(0xE0, 0x5C, 0x2A)),
]
for i, (wk, label, color) in enumerate(weeks):
    x = 0.35 + i * 3.2
    add_rect(s, x, 1.3, 2.9, 1.0, fill_color=color)
    add_text(s, wk, x, 1.35, 2.9, 0.45, size=15, bold=True,
             color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, label, x, 1.75, 2.9, 0.5, size=13,
             color=WHITE, align=PP_ALIGN.CENTER)

arrow_labels = [
    "Personal productivity\nFirst contact with Gemini\nNotebookLM deep dive",
    "Automating with Zapier / Make\nBusiness function applications\nMidterm exam",
    "What is an agent?\nn8n + Voiceflow build sprint\nAI product ideation",
    "AI strategy frameworks\nResponsible AI session\nCapstone pitches"
]
for i, txt in enumerate(arrow_labels):
    x = 0.35 + i * 3.2
    add_rect(s, x, 2.45, 2.9, 2.4, fill_color=WHITE)
    add_text(s, txt, x + 0.1, 2.5, 2.7, 2.3, size=13,
             color=DGRAY, align=PP_ALIGN.LEFT)

add_text(s, "Personal → Team → Agentic → Strategic",
         0.35, 5.05, 12.6, 0.5, size=15, bold=True,
         color=NAVY, align=PP_ALIGN.CENTER)
add_rect(s, 0.35, 5.55, 12.6, 0.05, fill_color=AMBER)
add_text_lines(s, [
    ("14 sessions  ·  3 Build Sprints  ·  4 Reflection Posts  ·  Midterm + Final Exam  ·  Team Capstone Pitch", False, 14),
], 0.35, 5.65, 12.6, 0.6, color=DGRAY, align=PP_ALIGN.CENTER)

# ── SLIDE 5: Tools Students Use ───────────────────────────────
s = body_slide("Tools Students Use — No Coding Required")
tools = [
    ("Conversational AI\n& Research", "Google Gemini\nNotebookLM\nGoogle AI Studio", NAVY, "Weeks 1–3"),
    ("No-Code\nAutomation", "Zapier  /  Make\nRelevance AI", TEAL, "Weeks 3–5"),
    ("Agentic AI\nPlatforms", "n8n\nVoiceflow", RGBColor(0x7B, 0x68, 0xEE), "Weeks 5–6"),
]
for i, (cat, tools_txt, col, wks) in enumerate(tools):
    x = 0.6 + i * 4.15
    add_rect(s, x, 1.3, 3.7, 4.8, fill_color=WHITE)
    add_rect(s, x, 1.3, 3.7, 0.65, fill_color=col)
    add_text(s, cat, x + 0.1, 1.32, 3.5, 0.6, size=14,
             bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, tools_txt, x + 0.15, 2.1, 3.4, 2.0, size=16,
             color=DGRAY, align=PP_ALIGN.CENTER)
    add_rect(s, x + 0.3, 5.5, 3.1, 0.4, fill_color=LGRAY)
    add_text(s, wks, x + 0.3, 5.52, 3.1, 0.38, size=12,
             color=col, bold=True, align=PP_ALIGN.CENTER)

add_text(s, "All platforms have free tiers sufficient for coursework. Tool categories are durable — specific platforms can be swapped as the landscape evolves.",
         0.35, 6.25, 12.6, 0.7, size=12, color=DGRAY,
         align=PP_ALIGN.CENTER, italic=True)

# ── SLIDE 6: Assessment Model ─────────────────────────────────
s = body_slide("Assessment: Hybrid Model")
items = [
    ("20%", "Reflection Posts ×4", "Individual · 200–300 words · Bi-weekly\nPersonal observations, not summaries", TEAL),
    ("25%", "Midterm Exam", "Take-home · Open-note · Case-based\nNo coding — conceptual reasoning only", NAVY),
    ("25%", "Final Exam", "Take-home · Open-note · Integrative cases\nAI strategy, ethics, governance", NAVY),
    ("25%", "AI Innovation Showcase", "Team pitch (3–4 students) · No prototype required\nExternal guests rotate through — trade show format", AMBER),
    ("10%", "Participation + Build Sprints", "In-class builds: Week 3 (automation) + Week 5 (agent)\nEngagement, peer feedback, attendance", TEAL),
]
for i, (pct, title, desc, col) in enumerate(items):
    y = 1.25 + i * 1.18
    add_rect(s, 0.35, y, 1.1, 1.0, fill_color=col)
    add_text(s, pct, 0.35, y + 0.18, 1.1, 0.65,
             size=24, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_rect(s, 1.55, y, 11.4, 1.0, fill_color=WHITE)
    add_text(s, title, 1.7, y + 0.05, 6.0, 0.45,
             size=16, bold=True, color=NAVY, align=PP_ALIGN.LEFT)
    add_text(s, desc, 1.7, y + 0.48, 11.1, 0.5,
             size=13, color=DGRAY, align=PP_ALIGN.LEFT)

# ── SLIDE 7: AI Innovation Showcase ───────────────────────────
s = body_slide("The AI Innovation Showcase")
add_rect(s, 0.35, 1.25, 12.6, 2.1, fill_color=WHITE)
add_text(s, "Trade show format · Week 7 · External guests invited",
         0.55, 1.32, 12.2, 0.5, size=15, bold=True,
         color=NAVY, align=PP_ALIGN.LEFT)
add_text_lines(s, [
    ("Teams of 3–4 identify a real business problem and design an AI-assisted solution using course tools.", False, 15),
    ("No working prototype required — the pitch IS the deliverable.", True, 15),
    ("External practitioners rotate through team stations, ask structured questions, and provide feedback.", False, 15),
], 0.55, 1.82, 12.1, 1.4, color=DGRAY)

steps = [
    ("Wk 4", "Teams form\n+ problem\nstatement"),
    ("Wk 5", "Solution\ndesign\nsketch"),
    ("Wk 6", "Peer pitch\npractice +\nfeedback"),
    ("Wk 7\nS1", "Slide deck\nsubmitted"),
    ("Wk 7\nS2", "AI Innovation\nShowcase\n🎉"),
]
colors = [TEAL, TEAL, TEAL, AMBER, NAVY]
for i, (lbl, desc) in enumerate(steps):
    x = 0.5 + i * 2.5
    add_rect(s, x, 3.55, 2.1, 0.55, fill_color=colors[i])
    add_text(s, lbl, x, 3.57, 2.1, 0.52,
             size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_rect(s, x, 4.15, 2.1, 1.3, fill_color=WHITE)
    add_text(s, desc, x + 0.05, 4.18, 2.0, 1.25,
             size=12, color=DGRAY, align=PP_ALIGN.CENTER)
    if i < 4:
        add_text(s, "→", x + 2.1, 3.9, 0.4, 0.5,
                 size=18, bold=True, color=AMBER, align=PP_ALIGN.CENTER)

add_text(s, "Rubric: Problem clarity  ·  Solution design  ·  Business value  ·  Responsible AI awareness  ·  Pitch quality",
         0.35, 5.65, 12.6, 0.5, size=12, color=DGRAY,
         align=PP_ALIGN.CENTER, italic=True)

add_rect(s, 0.35, 6.2, 12.6, 0.75, fill_color=NAVY)
add_text(s, "\"The hardest part of any AI project is defining the problem and designing the solution clearly.\nThat's exactly what this format tests — and what employers are hiring for.\"",
         0.55, 6.22, 12.2, 0.7, size=12, color=AMBER,
         align=PP_ALIGN.CENTER, italic=True)

# ── SLIDE 8: Why Now / Call to Action ────────────────────────
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, 13.33, 7.5, fill_color=NAVY)
add_rect(s, 0, 0, 0.35, 7.5, fill_color=AMBER)
add_rect(s, 0, 6.7, 13.33, 0.8, fill_color=RGBColor(0x0F, 0x1A, 0x33))

add_text(s, "Ready to Launch", 0.55, 0.9, 12.2, 0.9,
         size=36, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

points = [
    "Full 7-week syllabus with session-level detail — complete",
    "Hybrid assessment model: 2 exams + capstone pitch + reflections",
    "No coding required — accessible to all business concentrations",
    "All tools have free student tiers; AI Studio coordinated with IT",
    "AI Innovation Showcase creates a high-visibility department event",
    "Fills a genuine whitespace: no comparable course in peer programs",
]
for i, pt in enumerate(points):
    y = 1.9 + i * 0.72
    add_rect(s, 0.55, y + 0.08, 0.28, 0.28, fill_color=AMBER)
    add_text(s, pt, 1.0, y, 11.8, 0.65, size=16, color=LGRAY)

add_text(s, "Seeking department support to offer IDSC 4101 in [Semester Year].",
         0.55, 6.1, 12.2, 0.5, size=16, bold=True,
         color=AMBER, align=PP_ALIGN.LEFT)

add_text(s, "Questions welcome — [Your Name]  ·  [Email]",
         0.55, 6.78, 12.2, 0.4, size=12,
         color=RGBColor(0xAA, 0xBB, 0xCC),
         align=PP_ALIGN.LEFT, italic=True)

# ── Save ──────────────────────────────────────────────────────
prs.save("/workspace/IDSC4101_course_proposal.pptx")
print("Saved: /workspace/IDSC4101_course_proposal.pptx")
