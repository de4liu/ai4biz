# IDSC 4101: Agentic AI for Business Applications
## Week 2, Session 2 — Build Sprint: Your First Automation
### Teaching Materials: Slide Deck + Activity Plan

**Session Duration:** 100 minutes
**Session Type:** Brief concept (20 min) + Build Sprint (60 min) + Demo and Debrief (20 min)
**Assumed Background:** Session 1 complete — students understand automation framework; Zapier accounts created
**Tools Used:** Zapier (or Make), Relevance AI (introduction)

---

## SLIDE DECK

---

### SLIDE 1 — Title Slide

**Title:** Build Sprint 1
**Subtitle:** Your First Working AI Automation — From Zero to Running
**Course:** IDSC 4101: Agentic AI for Business Applications | Week 2, Session 2

**Speaker Notes:**
Today is a build day. We will spend the majority of this session with you actually building something that works — not watching me build it, not planning to build it, but building it. The goal by the end of this session is that every student has a running Zapier automation with at least two connected apps and an AI step in the middle. That is achievable in 60 minutes. I will give you a brief concept overview, show you the anatomy of what you're building, and then you work. I circulate. Peer help is encouraged. Let's go.

---

### SLIDE 2 — Quick Recap: The Automation Framework

**Title:** Before You Build — What Makes This Worth Building?

**Bullets:**
- From Session 1: the best automation candidates are **high frequency + meaningful effort + high standardizability**
- Today's build should target one of those candidates — either from the Lakeside Wellness audit or a real task from your own academic or professional life
- If you're stuck choosing: pick something you actually do repeatedly. Real problems produce better builds and better learning.
- You are not graded on complexity. You are graded on whether it runs and whether you can explain the design logic.

**Speaker Notes:**
Before anyone opens Zapier, I want you to spend two minutes writing down the task you're going to automate. Not the tool — the task. What is the trigger? What does the AI step do to the input? What is the output and where does it go? If you can answer those three questions, you're ready to build. If you can't, that's the first thing we fix — not in Zapier, on paper. The tool should implement your design. Your design should not be discovered by clicking around in Zapier.

---

### SLIDE 3 — The Anatomy of a No-Code Workflow

**Title:** Four Building Blocks — Know These Before You Touch the Tool

**Bullets:**
- **Trigger:** The event that starts the workflow. Examples: new form submission, new email received, new row added to a spreadsheet, scheduled time (every Monday at 8am), new file uploaded to a folder.
- **Action:** What happens after the trigger — or after a previous step. Examples: send an email, add a row to a spreadsheet, post to Slack, create a calendar event, call an AI model.
- **Filter / Condition:** A decision point. "Only continue if the email subject contains the word 'urgent'." Filters let your automation behave differently based on what it sees.
- **AI Step:** You call a language model (Gemini, or whichever model your Zapier plan supports) with a prompt that processes the previous step's data and produces structured output for the next step.

**The template:** Trigger → AI Step → Filter (optional) → Action → Action

**Speaker Notes:**
These four building blocks are all you need to understand to build almost anything in Zapier. The most important thing to internalize is the data flow: each step passes its output to the next step. When you call Gemini in the AI step, you pass it data from the trigger — the form response text, the email body, whatever the trigger captured. Gemini produces output. That output is what the next step acts on. If your AI step produces freeform prose, the next step can't parse it reliably. If your AI step produces structured output — "Category: Billing | Priority: High | Summary: Customer cannot access account" — the next step can route, filter, and act on each field independently. This is why structured output prompting from Week 1 matters so much in a workflow context.

---

### SLIDE 4 — Build Options: Choose Your Challenge

**Title:** Pick One of These — or Bring Your Own

**Option A — The Inquiry Handler (Beginner):**
Trigger: New Google Form submission (customer message form)
AI Step: Gemini categorizes the inquiry and drafts a 2-sentence response
Action: Post to a Slack channel (or send an email) with the category and draft

**Option B — The Feedback Summarizer (Intermediate):**
Trigger: New row added to a Google Sheet (e.g., customer feedback responses)
AI Step: Gemini reads the feedback, extracts a sentiment score (Positive/Neutral/Negative), and writes a one-sentence summary
Action: Add a new row to a separate Google Sheet with the original feedback, sentiment score, and summary

**Option C — The Meeting Prep Bot (Intermediate):**
Trigger: New calendar event created with a keyword (e.g., "client meeting") in the title
AI Step: Gemini generates a meeting preparation checklist based on the event title, attendees, and description
Action: Create a Google Doc with the checklist, or send it to yourself via email

**Bring Your Own:** If you identified a real automation candidate in Session 1 or from your own work — build that instead. Check with instructor first to confirm it's buildable in Zapier.

**Speaker Notes:**
Choose based on your confidence level, not your ambition. Option A is the most constrained and most reliable — fewest moving parts, most forgiving if something breaks. Option B introduces data transformation, which is a more realistic enterprise use case. Option C requires calendar integration, which has a few more setup steps but produces something genuinely useful. If you bring your own: show me your design before you start building. I've seen students spend 30 minutes building something that wasn't automatable in Zapier. Two minutes of design review prevents that.

---

### SLIDE 5 — Setting Up Your AI Step in Zapier

**Title:** The Zapier AI Step — What You Need to Know

**Bullets:**
- In Zapier, the AI step is accessed through "AI by Zapier" or through direct integrations with Google Gemini, OpenAI, or Anthropic (depending on your plan)
- You write a prompt that uses data from previous steps — Zapier lets you insert "variables" from the trigger or earlier steps directly into the prompt
- **Key: your prompt should produce structured, parseable output** — not a paragraph. Tell the AI what format to use.
- Example prompt structure: "You are a customer service analyst. Classify the following customer message into one of these categories: [Billing / Technical / General / Complaint]. Then write a 2-sentence professional response. Format your output exactly as: Category: [X] | Response: [Y]. Customer message: {{trigger.message}}"
- The {{trigger.message}} is Zapier's variable syntax — it inserts the actual content from the trigger into your prompt at runtime

**Speaker Notes:**
The variable syntax is the key technical thing to understand in Zapier. When you write {{trigger.message}}, Zapier replaces that placeholder with the actual message text from the form submission when the Zap runs. This is how data flows through the automation — each step can reference the output of any previous step. The structured output prompt pattern is critical: if you get freeform text from the AI, you can still read it as a human, but downstream steps can't parse it reliably. Enforce your format in the prompt. Test it by running a sample and confirming the output looks exactly like you specified.

---

### SLIDE 6 — Error Handling: What To Do When It Breaks

**Title:** When Your Zap Doesn't Work (It Will) — Here's the Playbook

**Bullets:**
- **Step 1:** Check the Zap history — Zapier logs every run and shows you exactly which step failed and what the error message was
- **Step 2:** Run a test on the failing step — Zapier lets you test each step individually with sample data
- **Step 3:** If the AI step produced unexpected output — your prompt format is the most likely culprit. Add more explicit formatting instructions.
- **Step 4:** If a connection step failed — check authentication. App integrations require permission grants; they expire or need re-authorization.
- **Step 5:** If the trigger didn't fire — check that the Zap is turned ON (the toggle in the upper right) and that the trigger app has the right permissions

**The mindset:** Debugging is part of the build. A broken Zap is not failure — it's information. Read the error message, test the step, fix one thing at a time.

**Speaker Notes:**
I want to say this clearly before the build starts: your Zap will probably break at least once. That is normal. That is expected. That is part of learning to build automations. The skill I want you to develop is not "how do I build something that never breaks" — it's "how do I read an error and fix it efficiently." Zapier's error logs are quite readable. The most common errors are: authentication expired (re-connect the app), AI step output doesn't match what the next step expects (fix your prompt format), and trigger didn't fire because the Zap was toggled off. Check those three things first before asking for help.

---

### SLIDE 7 — Introduction to Relevance AI

**Title:** Beyond Simple Automations: AI Assistants with Business Rules

**Bullets:**
- Relevance AI is a no-code platform for building AI-powered business tools — think of it as Zapier's AI step, but with much more control
- You can build: AI assistants that follow specific business rules, multi-step AI workflows, and tools that combine web search, document reading, and AI generation
- Key use case: building an internal AI assistant that knows your company's products, policies, and FAQs — without sending data to a general-purpose API
- Today: introduction only — we explore Relevance AI more deeply in the agentic AI weeks (Weeks 4–6)
- Action for today: create a free account at relevanceai.com and explore the template library

**Speaker Notes:**
I'm introducing Relevance AI today so you have it in your toolkit, but we're not building with it yet — that comes in the agentic weeks. What I want you to notice is that Relevance AI sits in a different category than Zapier: Zapier is primarily about connecting applications and automating data flows; Relevance AI is primarily about building AI tools that follow your specific business logic. The line between them blurs as both platforms add features, but the mental model is useful: Zapier for integration automation, Relevance AI for AI-native business tools. We'll build agents in Relevance AI in Weeks 5 and 6.

---

### SLIDE 8 — Build Sprint Begins

**Title:** 60 Minutes — Build Something That Works

**Rules of the sprint:**
- Choose your option (or bring your own — instructor approved)
- Design on paper or a doc FIRST — trigger, AI step, action, output
- Build in Zapier
- Test with real (or sample) data
- When it runs successfully: add one refinement (better prompt, add a filter, add a second action)
- If it's not running by minute 45: flag the instructor — we triage together

**Peer collaboration:** Encouraged. If your neighbor's Zap works and yours doesn't, ask what they did differently. If yours works first, help your neighbor.

**The bar:** By end of sprint, every student should be able to show a Zap history with at least one successful run.

**Speaker Notes:**
Alright. Design first — two minutes on paper — then build. I'm circulating. If you're stuck for more than five minutes on the same problem, flag me — don't spend 20 minutes debugging alone. The most common points where students get stuck: the trigger not firing (check that your Zap is ON and that you've submitted a real test input), the AI step returning weird formatting (refine the prompt to be more explicit), and the output action not receiving the right data (check that you're mapping the AI output field correctly to the next step). Let's go.

[INSTRUCTOR ACTION: Circulate continuously during the 60-minute build. Keep a mental list of the most common errors and address them with the whole class if three or more students hit the same issue. At minute 45: quick show of hands — who has a successful run? For those who don't, offer a 5-minute triage at the front of the room while others continue refining.]

---

### SLIDE 9 — Demo Time

**Title:** Show What You Built (5 minutes each — 3–4 volunteers)

**Bullets:**
- Walk us through: What problem did you automate? What is the trigger? What does the AI step do? What is the output?
- Trigger the Zap live — show the actual run in Zapier history
- What was the hardest part to get working?
- What would you add if you had another hour?

**Speaker Notes:**
[Call on 3–4 volunteers — prioritize students who built different options so the class sees range. For each demo: let them trigger the Zap live if possible, show the run history, and walk through the structure. After each demo, ask the class: "What did they do that you hadn't thought of?" The goal is peer learning — students often solve problems in ways the instructor wouldn't have suggested.]

---

### SLIDE 10 — What You Built — Patterns and Principles

**Title:** What Your Builds Have in Common

**Bullets:**
- Every working automation follows the same structure: trigger → process → act
- The AI step is a translator: it converts unstructured input into structured, actionable output
- The quality of the AI step depends entirely on prompt quality — this is Week 1's lesson in practice
- The weakest point in most automations is the AI step's output format — inconsistent formatting breaks downstream steps
- Human review gates add reliability without sacrificing speed — next week we look at how to decide when to include them

**Speaker Notes:**
Let me synthesize what I observed during the build. The students who got running fastest were the ones who designed on paper first — they knew exactly what trigger they were using, what they wanted the AI to produce, and where it was going. The students who struggled longest were building and designing simultaneously, discovering in step 5 that the architecture they chose in step 1 wouldn't work. That's a design lesson, not a Zapier lesson. For next week's build — we're building agents, which are more complex — the design phase will be even more important. Think about the design before you think about the tool.

---

### SLIDE 11 — Reflection Post 2 and Looking Ahead

**Title:** What's Due and What's Coming

**Bullets:**
- **Due before Week 3, Session 1:** Reflection Post 2 (200–300 words on Canvas)
  - What workflow did you build? What broke, and how did you fix it? What would you automate next?
- **Week 3:** AI across every business function — marketing, sales, finance, operations, HR. Guest perspective from a practitioner.
- **Week 3, Session 2:** Capstone team formation. Start thinking about cross-major teammates.
- **Weeks 4–6:** Agentic AI — agents that plan, act, and coordinate. Everything we built today is the foundation.

**Speaker Notes:**
The reflection post is due before Week 3. I want three things: what you built (specific), what broke (specific), and what you would automate next (and why it meets the framework criteria — don't just say "I'd automate my email"). The reflection is where learning consolidates — take it seriously. Week 3 is functional — we look at AI across every area of business. Useful for thinking about your capstone sector and for the team formation conversation in Session 2. Come with a sense of what sector or business problem interests you. And one more note: the automation you built today is a building block. In Weeks 4–6 we add reasoning, planning, and multi-step decision-making to what you just built. Everything connects.

---

### SLIDE 12 — Debrief and Close

**Title:** Lessons From the Build

**Bullets:**
- Design before you build — always
- Structured output prompting is not optional in a workflow — it's the difference between a reliable automation and a fragile one
- Debugging is a skill, not a failure — read the error, test the step, fix one thing at a time
- The human review gate is a feature, not a limitation — use it until you trust the AI step's output quality
- You now have a working automation. That's a real capability. Build on it.

**Speaker Notes:**
I want to close with something that I think is undersaid in most AI courses: building something that works is satisfying in a way that watching a demo never is. You now have a running automation. It connects real apps. It calls a real AI model. It produces real output. That is not a toy — that is a prototype of something a business could actually use. Next week we zoom out to the business landscape — how AI is reshaping every functional area — and you'll start to see where the automations you just built fit in a larger strategic picture. See you Tuesday.

---

## ACTIVITY PLAN

---

### Activity: Build Sprint 1 (60 minutes + 20-minute demo and debrief)

**Purpose:** Students build a working AI-powered automation from scratch — moving from workflow design concept to a tested, running Zap. The sprint develops hands-on fluency with no-code tools and reinforces structured output prompting in a practical context.

**Pre-session requirements:**
- Students must have a Zapier account (free tier) created before class — reminded via Canvas after Session 1
- Google account required (for Gmail/Sheets/Forms triggers)
- Slack account recommended (for output demos) — free tier is sufficient

**What students do:**

| Phase | Duration | Task |
|-------|----------|------|
| Choose option and design | 5 min | Select build option (A, B, C, or own); write trigger → AI step → action on paper |
| Build in Zapier | 45 min | Connect trigger app, configure AI step with structured prompt, connect output action |
| Test and refine | 10 min | Run with real or sample data; fix prompt format if AI output is inconsistent; add one refinement |
| Demo | 5 min/volunteer | 3–4 students show live Zap run and walk through design logic |
| Debrief | 5 min | Instructor synthesizes patterns observed; preview Week 3 |

**What students produce:**
- A running Zapier automation with at least one successful run in the Zap history
- No formal submission — Zap history is the artifact; students screenshot it for their reflection post

**Instructor facilitation notes:**
- Minute 0–5: enforce the design-on-paper requirement. Walk through the room and confirm every student has written their trigger, AI step, and output before they open Zapier.
- Minute 5–45: circulate constantly. The most common support needs: (1) AI step variable mapping — show students how to insert {{trigger.field}} into their prompt; (2) Zapier plan limitations — free tier restricts some app integrations; direct students to Google Forms + Gemini + Gmail as the most reliable free-tier combination; (3) Zap is not firing — check toggle is ON and that a real test input was submitted.
- Minute 45: quick audit — hands up if you have a successful run. Students without one get 5 minutes of targeted triage. Students with a successful run add a refinement (filter, second action, or improved prompt).
- Demo selection: prioritize variety. Try to show Option A, Option B, and one "bring your own." Ask student to trigger the Zap live if possible — live runs are more engaging and more instructive than screenshots.
- Reflection post: remind students that the reflection requires specific details — what broke, how they fixed it. Vague reflections ("it was hard but I figured it out") do not receive full credit.

**Common build issues and solutions:**
| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| AI step returns inconsistent format | Prompt doesn't enforce structure | Add explicit format instruction: "Output ONLY: Category: [X] \| Draft: [Y]" |
| Zap not triggering | Zap is toggled off | Check toggle in upper right of Zap editor |
| App connection fails | Auth expired or wrong account | Re-connect app, confirm correct Google/Slack account |
| Filter step blocking all runs | Filter condition too narrow | Test with sample data that matches the filter condition |
| Output action not receiving AI data | Wrong field mapped | In action step, re-map the field to the AI step's output variable |

**Materials needed:**
- Build option slides displayed throughout sprint (Slide 4)
- Zapier account — instructor demo account separate from personal
- Slack workspace (instructor-created for class, or use Canvas notifications as fallback output)
- Google Form pre-built by instructor for Option A (share link on Canvas before class)
