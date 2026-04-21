# IDSC 4101: Agentic AI for Business Applications
## Week 2, Session 1 — Workflow Thinking: What Gets Automated and What Does Not
### Teaching Materials: Slide Deck + Activity Plan

**Session Duration:** 100 minutes
**Session Type:** Concept + Live Demo + Automation Audit Activity
**Assumed Background:** Week 1 complete — students understand advanced prompting, RAG, and enterprise GenAI deployment
**Tools Introduced:** Zapier (or Make) — visual introduction

---

## SLIDE DECK

---

### SLIDE 1 — Title Slide

**Title:** Workflow Thinking
**Subtitle:** How to Spot Automation Opportunities — and Know When AI Doesn't Belong
**Course:** IDSC 4101: Agentic AI for Business Applications | Week 2, Session 1

**Speaker Notes:**
Last week we covered how AI works at the individual and enterprise level. This week we shift from understanding AI to building with it. But before we touch any tool, I want to spend this session on something that sounds simple and is actually the hardest part: deciding what to automate. Every failed AI project I've seen started with the wrong problem — someone picked a task because it felt automatable, not because it actually was. By the end of today, you'll have a framework that prevents that mistake.

---

### SLIDE 2 — The Shift: From Using AI to Deploying AI

**Title:** You've Been a User. Now You're a Designer.

**Bullets:**
- Using AI: you write a prompt, you get a response, you decide what to do with it
- Deploying AI in a workflow: AI receives inputs automatically, produces outputs automatically, and those outputs trigger the next step — often without a human in the loop
- The design question is no longer "what should I ask the AI?" — it's "what should the AI do, to what inputs, and what happens next?"
- This shift from user to designer is where most of the real business value lives — and where most mistakes happen

**Speaker Notes:**
This distinction is crucial and worth sitting with for a moment. When you use Gemini in a chat window, you're always in the loop — you read the output, you evaluate it, you decide what to do next. When you embed AI in a workflow, that loop often closes automatically. A form gets submitted, AI processes it, an email gets sent, a database gets updated — all without a human reviewing each step. That's enormously powerful. It's also where things go wrong if you automate the wrong task, the wrong way. Today's framework is about making that design decision rigorously.

---

### SLIDE 3 — The Automation Opportunity

**Title:** Where Does Business Time Actually Go?

**Bullets:**
- Knowledge workers spend approximately 60% of their time on "work about work": scheduling, updating systems, writing status updates, routing information, following up on tasks (Asana, 2024)
- Much of this is repetitive, rule-based, and low-value — but it consumes real time and creates real friction
- AI workflow automation targets this layer: it doesn't replace judgment, it removes the friction around judgment
- The opportunity is not eliminating jobs — it's eliminating the least valuable parts of jobs and freeing capacity for higher-value work

**Speaker Notes:**
Here's a number I want you to carry with you: 60%. That's the share of knowledge worker time spent on administrative coordination rather than the actual work that requires expertise. Scheduling meetings. Writing follow-up emails. Entering data from one system into another. Routing customer inquiries to the right person. These are not complex tasks. They're repetitive, rule-based, and they happen at a scale that makes them genuinely expensive — both in time cost and in the opportunity cost of what smart people could be doing instead. AI workflow automation is designed to attack exactly this layer.

---

### SLIDE 4 — The Automation Framework: Three Criteria

**Title:** Frequency × Effort × Standardizability

**What makes a task a good automation candidate?**

- **Frequency:** How often does this task occur? Daily? Hundreds of times per week? The higher the frequency, the greater the ROI of automating it.
- **Effort:** How much human time and attention does it require per instance? High effort per instance = high value of automation per instance.
- **Standardizability:** Can the task be described as a consistent set of rules? Does the same type of input always require the same type of output? Low variability = high standardizability = automatable.

**The sweet spot:** High frequency + meaningful effort + high standardizability = strong automation candidate

**Speaker Notes:**
Let me walk through each criterion with a real example. Customer service tier-1 routing: high frequency (happens hundreds of times per day), meaningful effort (rep reads the message, decides which team, writes a response or forwards it), and highly standardizable (the same categories of questions get routed the same way). That's a strong automation candidate. Executive strategy review: low frequency (happens once a quarter), very high effort, but low standardizability (every quarter's context is different, requires genuine judgment). Not a good automation target. The framework sounds obvious when you explain it — but most organizations skip it and automate based on what's technically easy rather than what's strategically valuable.

---

### SLIDE 5 — The Fourth Dimension: What AI Adds

**Title:** Standardizability × Unstructured Inputs — Where AI Changes the Game

**Bullets:**
- Traditional automation (without AI): works only on structured inputs — form fields, database records, clear rules
- AI-powered automation: works on unstructured inputs — emails, customer messages, documents, images, voice — and converts them into structured, actionable outputs
- This dramatically expands the automation frontier: tasks that were previously un-automatable because the input was messy or variable are now within reach
- Key question: Is the output of the AI step consistent and reliable enough to trust downstream automation?

**Bullets — What AI unlocks:**
- Reading and classifying incoming emails → routing without human review
- Extracting key data from uploaded documents → populating a CRM or database
- Summarizing customer feedback → generating a structured weekly report
- Drafting a first-pass response → sending after approval (human-in-the-loop) or automatically (fully autonomous)

**Speaker Notes:**
This is the slide that changes how people think about what's automatable. Before AI, workflow automation required clean, structured inputs — you could automate "if a form is submitted with field X = Y, do Z." That works for structured data. But most business communication is unstructured: emails, slack messages, customer feedback, support tickets. AI acts as a translation layer — it reads the unstructured input and converts it into a structured, rule-followable output that the rest of the automation can act on. That translation layer is genuinely new. It's why the automation frontier has expanded so dramatically in the last two years.

---

### SLIDE 6 — Where AI Does Not Belong in Workflows

**Title:** The Anti-Patterns: When Not to Automate with AI

**Bullets:**
- **High-stakes, irreversible actions:** AI should not autonomously send a legal notice, approve a loan, or terminate a vendor contract — the cost of a wrong output is too high
- **Tasks requiring genuine empathy or discretion:** A customer who just lost a family member needs a human on the phone, not an AI-drafted condolence response
- **Tasks where errors compound:** If AI output in step 3 is wrong, and it feeds automatically into steps 4, 5, and 6 — you can have a large-scale failure before any human notices
- **Tasks with low volume and high variability:** Automating something that happens twice a month with different inputs every time often costs more than it saves
- **The rule:** Automate for scale. If you wouldn't trust a well-trained junior employee to execute this task with minimal oversight, don't trust the AI to do it without human review.

**Speaker Notes:**
This slide is as important as the previous one. I've seen organizations automate the wrong things with enormous enthusiasm and cause genuine harm. The most common mistake is automating an action that's irreversible — sending an email to 10,000 customers, updating a customer's account status, triggering a financial transaction — without a human approval step. AI can draft, classify, and prepare. But for actions that are hard to undo and have real consequences, there must be a human gate before the action fires. This is the human-in-the-loop principle we'll return to repeatedly in the agentic AI weeks. Start developing the habit now: always ask, "what's the worst-case output of this AI step, and what happens if it fires automatically?"

---

### SLIDE 7 — Introduction to No-Code Workflow Builders

**Title:** The Tools That Make This Possible — Without Writing Code

**Bullets:**
- No-code workflow builders are visual tools that let you connect applications and define automation logic using drag-and-drop interfaces
- You define: **triggers** (what starts the workflow), **actions** (what happens next), **conditions** (if/then logic), and **AI steps** (where a language model processes unstructured input)
- Popular platforms: **Zapier** (largest ecosystem, easiest to start), **Make** (more powerful, slightly steeper learning curve), **n8n** (open-source, more control — we use this for agents in Weeks 5–6)
- These tools connect thousands of applications: Gmail, Slack, Salesforce, Notion, Google Sheets, Airtable, Stripe, HubSpot, and many more

**Speaker Notes:**
These tools are genuinely transformative for business professionals who don't code. The core insight is that most business processes are already digital — data moves between applications constantly. What these platforms do is make that movement programmable without requiring you to understand APIs or write code. You point at the trigger: "When a new row is added to this Google Sheet." You point at the action: "Send this data to Gemini with this prompt." You point at the next action: "Post the result to this Slack channel." Zapier connects over 7,000 applications. If you can describe a business process as a series of "when X happens, do Y" steps, you can automate it in Zapier.

---

### SLIDE 8 — Live Demo: Building a Zapier Workflow

**Title:** Let's Build One — Live

**What we're building:**
A workflow that: (1) receives a Google Form submission from a customer, (2) passes the submission to Gemini with a prompt that categorizes the inquiry and drafts a response, (3) posts the categorized inquiry and draft response to a Slack channel for the team to review and send.

**Why this example:**
- Covers a real, high-frequency business problem (customer inquiry handling)
- Uses three common tools students will encounter (Google Forms, Gemini, Slack)
- Includes a human review step — illustrating responsible automation design
- Produces visible output students can evaluate immediately

**Speaker Notes:**
Watch the structure as I build, not just the clicks. I want you to notice: there's a trigger (form submission), an AI step (Gemini categorizes and drafts), a condition (if the inquiry is about billing, route to the billing Slack channel; otherwise, general support), and a human review point (team sees the draft, approves or edits before sending). That structure — trigger, AI processing, condition, human gate, action — is the template for most responsible business automations. We're not sending anything automatically. The AI accelerates the human; it doesn't replace the human's judgment about whether to send.

[INSTRUCTOR ACTION: Build live in Zapier. Pre-create the Google Form with fields: Name, Email, Message. Set up the Zap: Trigger = New Form Response → Action = Gemini (prompt: "Categorize this customer inquiry as: Billing, Technical Support, General Question, or Complaint. Then draft a professional 2-sentence response. Format: Category: [X] | Draft: [Y]") → Filter = if category contains "Billing" → Action = Slack message to #billing-team. Test with a sample submission in class. Show students the Zap history and output.]

---

### SLIDE 9 — Reading the Output

**Title:** What Just Happened — and What to Notice

**Bullets:**
- The trigger fired automatically when the form was submitted — no human action required
- Gemini categorized the inquiry and produced a draft in the format we specified — structured output prompting from Week 1 in action
- The filter routed correctly based on the AI's category output
- The Slack message delivered the draft to the right channel for human review
- What to watch for: AI miscategorization (common with ambiguous messages), Gemini hallucinating a response that doesn't match the actual inquiry, Slack formatting issues

**Speaker Notes:**
What I want you to notice is that we used what you learned in Week 1 — structured output prompting — inside the automation. The Gemini step didn't just "summarize the message." It produced output in a specific format (Category: X | Draft: Y) because we told it to. That format is what the rest of the Zap reads to make decisions. If the AI had returned freeform prose, the filter would have failed. This is the connection between prompt craft and workflow design: better prompts don't just produce better text, they produce more reliable, parseable outputs that the rest of your automation can act on.

---

### SLIDE 10 — Activity Setup: Automation Audit

**Title:** Your Turn — Map What Should (and Shouldn't) Be Automated

**Bullets:**
- You'll work in teams of 3–4
- You'll receive a scenario describing a small business's current operations
- Your task: apply the Frequency × Effort × Standardizability framework to identify the top 3 automation candidates and 1 task that should NOT be automated
- For each automation candidate: name the trigger, the AI step, and the next action
- 30 minutes to complete + 10 minutes to present

**Speaker Notes:**
This is your first structured team activity, and it's designed to get you thinking like a workflow designer rather than a tool user. The scenario gives you a business that has specific operational pain points. Your job is not to propose technology — it's to apply the framework and make a reasoned recommendation. I want to see the reasoning, not just the answer. When you present, I'll be asking: why these three? What's the standardizability argument? And what's your anti-automation pick — and why?

---

### SLIDE 11 — Automation Audit: Scenario Card

**Title:** The Scenario — Read Before You Map

**Business: Lakeside Wellness Studio**
A yoga and wellness studio with three locations in the Twin Cities. Approximately 800 active members. Staff of 12 (front desk, instructors, one operations manager). Current operations run on a mix of Mindbody (booking software), Gmail, Google Sheets, and manual processes.

**Current pain points (from the operations manager):**
- Every new member inquiry (avg. 40/week) gets a manual reply from front desk staff — same questions, same answers, different words each time
- Class cancellations trigger a manual process: instructor emails ops manager, ops manager updates the schedule in Mindbody, ops manager emails affected members, ops manager posts to Instagram
- After each class, instructors submit a paper attendance sheet; front desk staff manually enters attendance into Google Sheets every Friday
- Monthly member retention report is compiled manually by pulling data from Mindbody, copying into Google Sheets, and writing a summary — takes 3–4 hours per month
- Membership renewals expire without notice — front desk discovers them only when a member tries to book and is declined

**Your task:** Using the framework, identify the top 3 automation candidates and 1 task that should NOT be automated. For each automation candidate, define: trigger, AI step (if any), and next action.

---

### SLIDE 12 — Debrief and Close

**Title:** What Did You Map — and Why?

**Bullets:**
- [Teams present — 2 minutes each, ~10 minutes total]
- Discussion: Which tasks scored highest on all three criteria? Did any teams disagree on the anti-automation pick?
- Close: Next session you build. You'll take one of these automation patterns and make it work in Zapier. Come ready to move fast — build sprint starts immediately.

**Speaker Notes:**
Let's hear from each team. I'm most interested in two things: your strongest automation candidate — walk me through the frequency, effort, and standardizability argument — and your anti-automation pick. [Take team responses. Synthesize.] What I'm hearing is consistent: the new member inquiry and the class cancellation workflow score highest, and most teams correctly identified either the monthly retention report or the member retention analysis as something that needs human judgment before it becomes automated action. Next session we build. Get your Zapier accounts set up before Thursday — free tier is sufficient. Link is on Canvas.

---

## ACTIVITY PLAN

---

### Activity: "Automation Audit" (30 minutes + 10-minute debrief)

**Purpose:** Students apply the Frequency × Effort × Standardizability framework to a realistic business scenario — developing the workflow design mindset before they touch any tool in Session 2.

**Setup:**
Teams of 3–4. Distribute the Lakeside Wellness Studio scenario card (printed or on screen). Each team works from the same scenario so comparisons during share-out are meaningful.

**What students do:**

| Phase | Duration | Task |
|-------|----------|------|
| Read and absorb scenario | 5 min | Each member reads independently; highlight what seems repetitive or rule-based |
| Apply framework | 15 min | Score each pain point on frequency, effort, standardizability; reach consensus on top 3 + 1 anti-automation |
| Define automation blueprints | 10 min | For each top 3: name the trigger, any AI step, and the next action |
| Present | 2 min/team | Share top candidate + anti-automation pick + reasoning |

**What students produce:**
- A completed framework table (informal — on paper or shared doc) with scores and blueprints for the top 3 automations
- No formal submission; instructor may photograph strong examples for the class library

**Instructor facilitation notes:**
- The five pain points in the scenario vary significantly in automation fit. Expect students to converge on: member inquiry automation (strong — high frequency, standardizable), class cancellation workflow (strong — multi-step but fully rule-based), and membership renewal notifications (strong — pure trigger/action, no AI needed). Attendance entry is automatable but requires a structural change (digital attendance instead of paper). Monthly report is partially automatable but the summary writing requires judgment.
- The anti-automation pick is the richest discussion: the monthly retention *analysis* (not just the data pull) requires human interpretation of trends, context, and strategic implications. If teams try to fully automate it, push back: "What would the AI do if retention dropped suddenly due to a competitor opening nearby? Would the automated summary capture that context?"
- Watch for teams that define automations without a trigger. Push them: "What event starts this process? A form submission? A date passing? A status change in Mindbody?" Triggers are the foundation of workflow design.
- Timing note: if teams finish early, extend the blueprint phase — ask them to sketch the full workflow path, including what happens if the AI step fails or produces an unexpected output.

**Materials needed:**
- Scenario card (one per team — printed or displayed)
- Framework grid on whiteboard or slide: Frequency / Effort / Standardizability columns
- Zapier account setup reminder (free tier, link on Canvas) — remind students to set up before Session 2
