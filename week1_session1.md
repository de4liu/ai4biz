# IDSC 4101: Agentic AI for Business Applications
## Week 1, Session 1 — Course Orientation + Advanced Prompting for Business Judgment
### Teaching Materials: Slide Deck + Activity Plan

**Session Duration:** 100 minutes
**Session Type:** Orientation (20 min) + Concept + Live Demo + Prompt Audit Activity
**Assumed Background:** Students have used Gemini and basic prompt patterns (role prompting, step-by-step, examples) in a prior Carlson course
**Tools Used:** Google Gemini (advanced and multi-modal), Google AI Studio

---

## SLIDE DECK

---

### SLIDE 1 — Title Slide

**Title:** Beyond the Basics
**Subtitle:** Advanced Prompting for Business Judgment + Course Orientation
**Course:** IDSC 4101: Agentic AI for Business Applications | Week 1, Session 1

**Speaker Notes:**
Welcome. You've already used Gemini. You know what a prompt is. You've probably written a few hundred of them. This course starts where that left off — and moves fast. Today we cover three things: a quick orientation to where we're going over seven weeks, a significant upgrade to how you prompt for business decisions (not just drafts), and a live demo of multi-modal AI that most of you haven't seen before. Let's get into it.

---

### SLIDE 2 — Where This Course Goes

**Title:** Seven Weeks — One Clear Arc

**Bullets:**
- **Week 1:** Advanced GenAI — multi-modal, RAG concepts, enterprise deployment (today and next session)
- **Weeks 2–3:** AI for business — workflow automation, no-code tools, functional applications across every major
- **Weeks 4–6:** Agentic AI — three full weeks on autonomous systems, multi-agent architectures, and real deployment
- **Week 7:** Strategy, ethics, capstone presentations
- The course builds a complete picture: from tool user → workflow designer → agent architect → strategic evaluator

**Speaker Notes:**
Here's the honest pitch for why this course is structured the way it is. You already know how to use AI personally. What you don't yet know is how businesses deploy it at scale, how autonomous AI agents work and fail, and how to make strategic decisions about AI adoption. That's the gap this course closes. We move quickly through what you already know and spend the most time — three full weeks — on agentic AI, which is where the real business transformation is happening right now and where no other course in this program goes.

---

### SLIDE 3 — Assessments at a Glance

**Title:** How You'll Be Assessed

**Bullets:**
- Weekly reflection posts (individual, 200–300 words) — 20%
- Build sprints and in-class activities (team) — 25%
- Industry case analyses (team) — 20%
- Capstone pitch — AI solution for a real sector (cross-major team, 3–4 members) — 25%
- Final exam — take-home, open-book, AI tools allowed, HonorLock proctored, 90 minutes — 10%
- **Capstone teams:** Must include at least 3 different declared majors. Team registration due Week 2.

**Speaker Notes:**
A few things worth flagging. First: AI tools are explicitly allowed in almost every assessment in this course, including the final exam. That's intentional — you're being graded on judgment, not memorization. Second: the capstone team requirement for cross-major composition is serious. A Finance + Marketing + SCO team will produce a genuinely stronger pitch than three Finance students. I'll explain the team formation process in Week 3. For today, just know it's coming and start thinking about who you want to work with across majors.

---

### SLIDE 4 — The Gap Between "Using AI" and "Using AI Well"

**Title:** You Know How to Use AI. Here's What Most People Still Get Wrong.

**Bullets:**
- Most users treat AI as an answer machine — they ask, they accept, they move on
- Sophisticated users treat it as a thinking partner — they direct, they push back, they verify, they synthesize
- The gap is not technical. It's in how you frame the problem, constrain the output, and evaluate the result.
- Today: three techniques that separate casual users from people who use AI to make better decisions

**Speaker Notes:**
Let me be direct about what I mean. I've seen students — and professionals — use AI to produce a polished-looking output and submit it without reading it carefully. That's not sophisticated AI use. That's faster bad work. The people who get genuine value from these tools are the ones who treat the AI like a smart but fallible analyst: they give it a strong brief, they push back on the first answer, they ask it to show its reasoning, and they synthesize its output with their own judgment. Those are learnable behaviors. That's what today is about.

---

### SLIDE 5 — Advanced Technique 1: Chain-of-Thought Prompting

**Title:** Make It Show Its Work

**What it is:** Instructing the AI to reason step by step before reaching a conclusion — surfacing the reasoning process, not just the answer.

**Example prompt:**
> "Before you give me a recommendation, walk through your reasoning step by step. First, identify the key variables. Second, evaluate the tradeoffs. Third, state your recommendation and explain why it outweighs the alternatives."

**When to use it:**
- Complex decisions with multiple competing factors
- Any analysis where you want to audit the logic, not just accept the conclusion
- Building a recommendation you'll need to defend to someone else

**Speaker Notes:**
This is the single most powerful technique for business analysis use cases. Here's why: when you ask for a conclusion without reasoning, you get a polished answer with no visible logic. You can't evaluate it. You can't push back on it. You can't tell whether the AI made a reasonable assumption or a completely wrong one. When you force it to reason step by step, two things happen: the output is usually better — because the model is more careful when it knows it has to show its work — and errors become visible earlier, before they compound into a wrong recommendation. Use this whenever the stakes of getting it wrong are real.

---

### SLIDE 6 — Advanced Technique 2: Structured Output Prompting

**Title:** Tell It Exactly What Shape You Want

**What it is:** Specifying the format of the output — not just the content — so it fits directly into your workflow.

**Example prompt:**
> "Analyze this company's competitive position. Output your analysis as a structured table with four columns: Competitive Advantage, Strength (High/Medium/Low), Supporting Evidence, and Key Risk. Do not write prose — table only."

**When to use it:**
- When you need output you can paste into a slide or spreadsheet directly
- When you're comparing multiple options and want them in a consistent format
- When you want to force the AI to be specific rather than vague

**Formats to request:** Tables, scored lists, JSON, bullet hierarchies, numbered criteria, side-by-side comparisons

**Speaker Notes:**
This sounds simple, but it changes the game for business use. When you get unstructured prose, you have to do all the work of organizing it. When you specify the structure upfront — a table, a scored list, a decision matrix — the AI fills in that structure and you get output you can actually use immediately. The other benefit: structured output forces the AI to be concrete. It's much harder to give a vague, hedged answer when it has to fill in a cell that says "Strength: High/Medium/Low." Use this whenever you're producing something you'll need to present or share.

---

### SLIDE 7 — Advanced Technique 3: Adversarial Prompting

**Title:** Ask It to Argue Against Itself

**What it is:** Using the AI to actively challenge, stress-test, or find weaknesses in an idea, plan, or output — including its own previous response.

**Example prompt:**
> "You just gave me a recommendation to expand into the European market. Now I want you to argue against that recommendation as forcefully as you can. What are the strongest reasons this strategy could fail? What assumptions in your previous answer were most questionable?"

**When to use it:**
- Before presenting a recommendation to a senior leader or client
- When you want to pressure-test your capstone idea
- When you suspect the AI is being too agreeable (it frequently is)

**Speaker Notes:**
AI tools have a bias toward being helpful and agreeable. If you give them an idea, they tend to find reasons to support it. That's a problem if you're using them for analysis rather than just drafting. Adversarial prompting breaks that pattern. You're essentially asking the model to put on a different hat — the skeptic, the devil's advocate, the critic — and attack the very thing it just produced. This is one of the most practically useful techniques in a business context. I use it before every significant recommendation I write. It's the AI equivalent of asking a smart colleague "what am I missing?"

---

### SLIDE 8 — Live Demo: Multi-Modal Gemini

**Title:** When AI Can See — Multi-Modal Capabilities in Practice

**Bullets:**
- Gemini can now process: images, PDFs, spreadsheets, audio, and video (in addition to text)
- This changes what you can ask it to do — dramatically
- Business use cases: reading a competitor's slide deck, analyzing a chart from an earnings report, extracting data from a scanned form, summarizing an audio recording of a meeting
- Today's demo: I'll give Gemini a business dashboard image and a PDF excerpt — and ask it to synthesize both into an executive recommendation

**Speaker Notes:**
Most of you have been using Gemini as a text-in, text-out tool. What I'm about to show you is what happens when you hand it a business document it can actually read. I'm going to paste in an image of a sales performance dashboard and a two-page excerpt from a strategic planning document. Then I'm going to ask it to synthesize both and tell me what the leadership team should prioritize in Q2. Watch what it can do — and watch where it makes assumptions you'd want to verify.

[INSTRUCTOR ACTION: Prepare in advance — (1) a screenshot of a business dashboard (revenue by region, or similar — use a generic example), (2) a 1–2 page PDF excerpt from a publicly available strategy document or annual report. Upload both to Gemini. Prompt: "Here is a sales dashboard and an excerpt from our strategic plan. Based on both, identify the top two priorities leadership should address in Q2 and explain your reasoning." Walk through the output with students. Point out one assumption the AI made that a human reviewer would need to verify.]

---

### SLIDE 9 — What You Just Saw

**Title:** Three Observations From the Demo

**Bullets:**
- Multi-modal input dramatically expands what you can hand the AI — you're no longer limited to what you can type
- The AI made at least one visible assumption — it filled in a gap with plausible reasoning, not verified fact
- The chain-of-thought structure made that assumption visible — without it, we might have missed it
- Implication: multi-modal AI is powerful, but verification discipline matters more, not less, as inputs get richer

**Speaker Notes:**
The point of the demo is not to impress you with what Gemini can do. The point is to show you how these capabilities interact with the techniques we just covered. When you give AI richer inputs — images, documents, multiple sources — it has more to work with, but also more opportunities to make plausible-sounding errors. The chain-of-thought technique made it show its reasoning, which is what let us spot the assumption. That's the pattern: richer inputs + structured reasoning + human verification = genuinely useful analysis. Any one of those three without the others is less reliable.

---

### SLIDE 10 — Google AI Studio: Your Prompting Workbench

**Title:** AI Studio — Where You Go to Experiment Deliberately

**Bullets:**
- AI Studio (aistudio.google.com) lets you: set system instructions, compare prompts side-by-side, adjust temperature, test structured outputs, save prompt templates
- More powerful than the Gemini chat interface for iterative prompt development
- Today's activity uses Gemini — but in future sessions, AI Studio is your go-to for serious prompt development
- Quick walkthrough: system prompt field, temperature slider, output format settings

**Speaker Notes:**
Quick two-minute orientation before the activity. AI Studio is where you go when you want to develop a prompt seriously — not just try something once. The system prompt field is particularly powerful: it lets you set a persistent context or persona that applies to every message in the conversation. The temperature slider controls how creative vs. deterministic the output is — low temperature for analysis, higher for brainstorming. We'll use this more in coming weeks. For today, just know it exists and take a look at it on your own after class.

---

### SLIDE 11 — Activity: Prompt Audit (25 minutes)

**Title:** Prompt Audit — Fix What's Broken

**Setup:**
You will receive a weak business prompt and its actual output. Your job is not to write a better prompt about the same topic — your job is to diagnose exactly why this prompt underperforms and rebuild it using at least two of the three techniques from today.

**Steps:**
1. **(5 min)** Read the weak prompt and its output. Identify what's missing: reasoning instruction? Format constraint? Adversarial check? Specificity?
2. **(12 min)** Rebuild the prompt in Gemini. Use at least two techniques from today. Run it and compare the output.
3. **(8 min)** Document your diagnosis and your rebuilt prompt — one slide or half a page: what was wrong, what you changed, what improved.

**Share-out:** Two or three pairs present their before/after comparison to the class.

---

### SLIDE 12 — Debrief and Close

**Title:** What Changed?

**Bullets:**
- [Share-out: 2–3 pairs, 3 minutes each — ~10 minutes]
- Discussion prompts: What technique made the biggest difference? Did the output surprise you? Where would you still want a human to verify?
- Close: You now have three tools that move you from casual user to analytical user. Next session: how enterprises actually deploy GenAI at scale — RAG, fine-tuning, and governance.

**Speaker Notes:**
Let's hear from a few pairs. I'm specifically interested in which technique changed the output the most — because that tells us something about what the original prompt was missing. [Take 2–3 responses. Synthesize briefly.] What I'm hearing consistently is that structured output and chain-of-thought make the biggest difference for analysis tasks — because they force the AI to be explicit rather than fluent. Next session we zoom out completely: you've been using AI as an individual. Companies deploy it differently. We're going to look at how — and why it matters for how you evaluate AI decisions in your career.

---

## ACTIVITY PLAN

---

### Activity: "Prompt Audit" (25 minutes + 10-minute share-out)

**Purpose:** Students practice diagnosing weak prompts and rebuilding them with advanced techniques — shifting from intuitive to deliberate prompt design.

**Instructor preparation:**
Prepare 2–3 weak prompts with their actual Gemini outputs printed or posted on slides. Suggested examples:
- **Weak prompt A:** "Analyze this company's strategy." Output: generic 5-paragraph essay with no structure or specificity.
- **Weak prompt B:** "Should we expand to Europe?" Output: list of pros and cons with no reasoning chain, no evidence, no recommendation.
- **Weak prompt C:** "Write a memo about our Q3 results." Output: blank-filling template with obvious placeholders and no analytical insight.

Assign one weak prompt per pair. Pairs with the same prompt compare results during share-out.

**What students do:**

| Phase | Duration | Task |
|-------|----------|------|
| Read and diagnose | 5 min | Identify what's missing from the weak prompt and its output |
| Rebuild and run | 12 min | Write improved prompt using ≥2 advanced techniques; run in Gemini |
| Document | 8 min | Before/after: what changed in the prompt, what changed in the output |
| Share-out | 10 min | 2–3 pairs present; class identifies which technique had the most impact |

**What students produce:**
- A documented before/after prompt card (kept personally; instructor collects one strong example per weak prompt type for the class library)

**Instructor facilitation notes:**
- During rebuild phase: watch for students who simply add more words to the original prompt. Redirect: "What *type* of instruction is missing — reasoning, format, or adversarial check?" Length is not the issue; structure is.
- Common error: students use chain-of-thought but forget to constrain the output format, getting verbose prose they can't use. Prompt them to combine techniques.
- During share-out: ask students to read their rebuilt prompt aloud before showing the output. This makes the technique visible, not just the result.
- If time allows: take one strong rebuilt prompt and ask the class "what would you still want to verify before using this output in a real decision?" This bridges to Session 2's enterprise governance content.

**Materials needed:**
- Weak prompt examples prepared by instructor (printed or on LMS)
- Slide 11 displayed during activity
- Optional: shared Google Doc for collecting strong rebuilt prompts
