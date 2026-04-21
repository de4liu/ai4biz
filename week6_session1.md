# Week 6, Session 1 — AI-Native Products and Business Models
### IDSC 4101: Agentic AI for Business Applications
**Session type:** Lecture + real-world case walk-through + AI Product Pitch activity
**Assignment released:** Conceptual Exam 2 (take-home, open-note, individual) — released end of session, due 48 hours later

---

## SLIDE DECK

---

### SLIDE 1 — Title Slide

**Title:** Building for Real
**Subtitle:** AI-Native Products, Business Models, and the Ideation Toolkit
**Course:** IDSC 4101: Agentic AI for Business Applications | Week 6, Session 1

**Speaker Notes:**
Five weeks ago we started with the question: what is generative AI, and why does it matter? You've since built agents, stress-tested them, and deployed a working one. Today we zoom out to the business level — not what a single agent does, but how AI is reshaping what products look like, what business models are possible, and how you think about building something new in this environment. This session is the bridge between the technical literacy you've built and the strategic thinking you'll need in the capstone and in your careers. We're going to look at companies that are fundamentally different because AI is at their core — not bolted on, not a feature — and we're going to work through the product thinking loop that lets you design at that level. The session ends with a pitch. Let's go.

---

### SLIDE 2 — The Distinction That Changes Everything

**Title:** AI-Enhanced vs. AI-Native — Why It Matters

**Definitions:**

**AI-Enhanced:**
An existing product or workflow that uses AI to do something faster, cheaper, or better than before.
The underlying product logic is unchanged. AI is an accelerant.
*Example:* A law firm that uses an AI tool to summarize case documents instead of having associates do it manually. Same product (legal services), same business model (hourly billing), faster execution.

**AI-Native:**
A product or business that would not exist — or would not be viable — without AI at its core.
The product logic is designed around AI capability from the start. AI is not an accelerant; it is the architecture.
*Example:* A contract review platform that offers unlimited document analysis for a flat monthly fee. This pricing only works because the marginal cost of each analysis is near zero. Without AI, this business model is impossible.

**Why the distinction matters:**
AI-enhanced companies face competition risk: if AI is just a feature, a competitor can add the same feature. AI-native companies face architectural risk: if the AI fails or degrades, the entire product fails. Different risks, different strategic questions.

**Speaker Notes:**
Take a moment with this distinction because it reframes a lot of the business conversation around AI. When you read that "Company X is adding AI," the first question to ask is: enhanced or native? Is this a feature on top of an existing product, or is this a fundamental redesign of what the product does and how it makes money? Most current deployments are enhanced — AI is being layered onto existing systems. Native is rarer and harder to build, but it's where the most durable competitive advantage sits. For the capstone, you'll be designing in native territory: an AI solution that has a business model only possible because of AI. Keep that in mind as we go through today's examples.

---

### SLIDE 3 — Four Business Model Patterns Enabled by AI

**Title:** What AI Makes Possible That Wasn't Before

**Pattern 1: Mass Personalization**
Delivering individualized experiences at scale — without the per-unit cost of human customization.
*Example:* A learning platform that generates a unique curriculum for each student based on their pace, gaps, and goals. Previously required a human tutor. Now scalable to millions.
*Business model implication:* Subscription pricing at consumer scale, with engagement metrics (completion rate, test scores) as the value signal.

**Pattern 2: AI-as-a-Service (AIaaS)**
Packaging AI capability as a product sold to other businesses via API or platform.
*Example:* An AI that reads insurance claims documents and extracts structured data. Sold to 50 insurers who each connect it to their own systems.
*Business model implication:* Per-call or per-document pricing; volume discounts; very high margins at scale once the model is trained.

**Pattern 3: Outcome-Based Pricing**
Charging customers for results rather than inputs — made viable because AI can deliver measurable outcomes consistently and cheaply enough to absorb the risk.
*Example:* An AI recruiting tool that charges per successful hire, not per job posting or per resume screened.
*Business model implication:* Seller takes on more risk but earns more per unit; requires very high confidence in AI performance and clear outcome definition.

**Pattern 4: Data Flywheel**
Each customer interaction generates data that improves the AI, which improves the product, which attracts more customers, which generates more data.
*Example:* A fraud detection system that gets more accurate as it processes more transactions across more clients.
*Business model implication:* First-mover advantage compounds; late entrants face a data gap that's hard to close; winner-take-most dynamics in some markets.

**Speaker Notes:**
These four patterns are not exhaustive — they're the most common and the most useful for understanding what's actually different about AI-native companies. What I want you to take away is not the pattern names but the underlying logic: AI reduces marginal cost toward zero (enables mass personalization and AIaaS), AI improves measurably over time (enables data flywheels), and AI can be confident enough to take on outcome risk (enables outcome-based pricing). Each pattern is only possible because of something AI does that traditional software does not. When you're designing your capstone pitch, ask yourself: which of these patterns does your solution enable? If the answer is none, you may be building AI-enhanced, not AI-native.

---

### SLIDE 4 — Company Walk-Through: Three AI-Native Examples

**Title:** What AI-Native Actually Looks Like

**Example 1: Harvey (AI for Law)**
*What it is:* An AI platform trained on legal documents that helps lawyers research, draft, and review legal work.
*Why it's native:* The core product is AI reasoning over legal content — not a search engine, not a document management system. Without the AI, there is no product.
*Business model:* Enterprise subscription; priced per attorney per year.
*The strategic bet:* Legal work has historically been priced by the hour, which creates an incentive to go slow. Harvey is betting that outcome quality — not speed — will eventually be the primary value driver, and that firms willing to rebuild around AI output will outcompete those that don't.

**Example 2: Glean (Enterprise Search and AI Assistant)**
*What it is:* An AI that searches across all of a company's internal tools — Slack, Google Drive, Salesforce, GitHub — and answers employee questions using the company's own knowledge.
*Why it's native:* The product value comes from AI synthesis across fragmented sources. A traditional search tool returns links. Glean returns answers with citations.
*Business model:* Enterprise subscription; priced per seat.
*The data flywheel:* The more employees use it, the better Glean understands what knowledge matters in that company. That organizational knowledge graph becomes a switching cost.

**Example 3: Nabla (AI for Healthcare Documentation)**
*What it is:* An AI scribe that listens to a physician-patient conversation and automatically generates clinical notes.
*Why it's native:* Clinical documentation takes physicians 2–3 hours per day on average. Nabla removes that entirely. The business model — subscription per physician — only works because the AI is accurate enough and fast enough to replace a human task completely.
*Business model:* Subscription per provider; outcome framing (hours saved, burnout reduction).
*The responsible AI dimension:* Clinical notes go into patient records. Accuracy is non-negotiable. Nabla has invested heavily in accuracy guarantees and human review workflows — an example of AI-native design that builds guardrails into the core product.

**Speaker Notes:**
Walk through these examples at moderate pace — students will have questions. The most useful question to invite is: "What's the failure mode of this business?" For Harvey, it's regulatory: if courts decide AI-generated legal work requires human sign-off on every clause, the economics change. For Glean, it's data privacy: enterprise clients may not want their internal knowledge indexed by a third-party system. For Nabla, it's accuracy: one documented case of a clinical error traced to an AI note could damage the brand permanently. In each case, the failure mode is a business design question, not a technical one. That's the pattern.

---

### SLIDE 5 — The Ideation Toolkit: From Problem to Product

**Title:** How to Think Like an AI Product Designer

**The four-step product thinking loop:**

**Step 1: Start with the user problem**
Not "what can AI do?" but "what does someone need that they can't get easily today?"
Good problems: too much information to process, too much repetitive work to do, too much variability in outcomes that should be consistent, too little access to expertise that should be accessible.
*Diagnostic question:* What does the person currently do manually, slowly, or at high cost?

**Step 2: Map the AI capability**
What type of AI system addresses this problem? (generative text, classification, retrieval, reasoning, vision, speech)
Does the capability exist and is it good enough? (accuracy, speed, cost per call)
*Diagnostic question:* Which AI capability closes the gap between what exists today and what the user needs?

**Step 3: Design the workflow**
How does the AI fit into the user's process? What triggers it? What does it produce? Where does a human still need to be?
This is the agent design thinking from Weeks 4–5, applied at product scale.
*Diagnostic question:* Draw the before-and-after workflow. What did the human do before? What does the AI handle now? What does the human still do?

**Step 4: Define the value proposition and business model**
Who pays, how much, and why? Which of the four patterns applies? What's the pricing unit?
*Diagnostic question:* Why would someone pay for this instead of doing it the old way — and how much is the old way actually costing them?

**Speaker Notes:**
This loop is the ideation framework for the capstone. Students who come to capstone with a vague "AI solution for healthcare" idea will struggle. Students who can articulate a specific user problem, a specific AI capability that addresses it, a workflow design, and a pricing rationale will have a strong pitch. We'll practice the loop in the activity today — each team runs their product concept through all four steps before pitching. The pitch is only 2 minutes, but the thinking behind it should be grounded in all four.

---

### SLIDE 6 — Vendor Evaluation: Choosing an AI Platform

**Title:** How Do You Choose an AI Platform? Five Questions.

**The context:**
Most businesses deploying AI are not building their own models. They're selecting platforms — foundation model providers, workflow tools, enterprise AI suites. The decision is consequential: switching costs are high once a platform is embedded in production.

**Five questions to evaluate any AI vendor:**

**1. Data privacy and ownership**
What happens to your data when you send it to this system? Is it used to train the model? Who owns the outputs? This is especially critical for healthcare, legal, financial services, and any proprietary business information.
*Red flag:* Vague data processing agreements or opt-out mechanisms that are hard to find.

**2. Cost at scale**
What does this cost per call, per user, per document at the volume you actually plan to run?
Many AI products are cheap at demo scale and expensive at production scale. Run the math before committing.
*Red flag:* Pricing that only makes sense at low volume, with no published enterprise tier.

**3. Customizability**
Can you fine-tune the model on your data? Can you constrain its behavior? Can you integrate it with your existing systems?
*Red flag:* "Black box" platforms where you can't see or influence what the AI is doing or why.

**4. Reliability and SLA**
What's the uptime guarantee? What happens when the model is degraded or unavailable? Do you have a fallback?
*Red flag:* No published SLA, or SLA with too many carve-outs for "AI-specific" failures.

**5. Vendor lock-in risk**
If you need to switch platforms in 18 months, what does that cost? Is your data portable? Is your workflow logic platform-specific?
*Red flag:* Proprietary data formats, no export capability, deep platform-specific customization that doesn't transfer.

**Speaker Notes:**
These five questions apply to every AI procurement decision a company makes, from a $500/month tool to a multi-million dollar enterprise platform. Students will be in meetings where these decisions get made — often with insufficient rigor — within the first few years of their careers. Being the person who asks "what's the data processing agreement say?" or "have we run the unit economics at production volume?" is genuinely valuable and genuinely rare. This is not technical knowledge — it's business judgment applied to technology procurement. Emphasize that.

---

### SLIDE 7 — Activity: AI Product Pitch

**Title:** Your Turn — Pitch an AI-Native Product

**The task:**
Teams have 15 minutes to design and pitch a hypothetical AI-native product or service. Use the four-step ideation toolkit. Then pitch in 2 minutes.

**Pitch structure (2 minutes, all four components):**
1. **The problem** — one sentence. Who has this problem? What is it costing them?
2. **The AI capability** — one sentence. What type of AI system addresses it?
3. **The workflow** — one diagram or two sentences. What did the process look like before? What does the AI handle now?
4. **The business model** — one sentence. Who pays, how much, and why?

**Peer evaluation:**
After each pitch, the class votes (show of hands or quick poll):
- Feasibility: *Could this be built with today's AI?* (Yes / Probably / Unlikely)
- Impact: *Is the user problem real and significant?* (High / Medium / Low)

**Instructor feedback focuses on:**
- Is the problem specific enough? (vague: "helps businesses with marketing" vs. specific: "generates personalized email sequences for B2B sales reps based on prospect LinkedIn profiles and recent news")
- Is the AI capability plausible? (hallucination risk, accuracy requirements, data availability)
- Is the business model viable? (who really pays, is the cost-to-value ratio defensible)

**Speaker Notes:**
This activity is explicitly preparation for the capstone. Teams that use this session to develop and stress-test a real capstone idea are getting two sessions of capstone work done today. Encourage that explicitly: "If your team has a capstone direction, use this pitch to pressure-test it. I'll give you the same feedback I'd give on a capstone draft." The peer voting is fast and low-stakes — its purpose is to get the class engaged with each pitch, not to rank teams. After the votes, give your instructor feedback in 60 seconds or less per team: one thing that works, one thing that needs sharpening, one question to resolve before the capstone. Keep the energy up — 2-minute pitches move fast.

---

### SLIDE 8 — Common Pitfalls in AI Product Thinking

**Title:** What Goes Wrong — and How to Avoid It

**Pitfall 1: Solving for AI, not for the user**
The product is designed around what AI can do, not what a user actually needs.
*Sign:* "We'll use AI to analyze data and provide insights." (What data? What insights? For whom? What decision does it support?)
*Fix:* Start with the user's job-to-be-done, then work backward to the AI capability.

**Pitfall 2: Ignoring the accuracy threshold**
Every AI product has a required accuracy level — the minimum performance needed for the product to be useful and safe. Many teams don't name it.
*Sign:* "The AI will summarize documents." (How accurately? What happens when it's wrong? Who checks?)
*Fix:* State the required accuracy explicitly. Design the human-in-the-loop step for the cases where accuracy falls short.

**Pitfall 3: "The AI will figure it out"**
Treating the AI as a black box that magically handles complexity without designing the workflow.
*Sign:* The workflow diagram has "AI does its thing" as a step.
*Fix:* Draw the observe-think-act loop. Name the tools. Name the handoff points.

**Pitfall 4: Underpricing the trust problem**
Users may not trust AI outputs in high-stakes contexts, regardless of accuracy. The product design needs to address trust, not just performance.
*Sign:* The pitch assumes users will act on AI outputs without question.
*Fix:* Design the UI and workflow to show provenance — where did the AI get this? What is it confident about? Where should you verify?

**Speaker Notes:**
These pitfalls are drawn from real capstone projects and real commercial AI product failures. Pitfall 4 — the trust problem — is the one students most consistently underweight. In a B2C context especially, users who don't trust an AI tool will abandon it even if it's highly accurate. The design response is transparency and auditability: showing sources, flagging low-confidence outputs, making it easy to verify. That's not a technical feature — it's a design principle. It connects directly to the responsible AI content in Session 2.

---

### SLIDE 9 — The Capstone Connection

**Title:** What Week 6 Means for Your Capstone

**What your capstone pitch needs:**
1. A specific, named user problem (not "AI for healthcare" — a specific job-to-be-done)
2. An AI capability that addresses it (generative, retrieval, classification, agentic — which one and why)
3. A workflow design (before/after — where does AI slot in, where does the human stay)
4. A business model (who pays, what pricing pattern, what's the unit economics argument)
5. A responsible AI analysis (Session 2 content — what are the top 3 risks and how are they addressed)

**Timeline:**
- Today: AI Product Pitch (practice run — instructor feedback on product thinking)
- Session 2: Red Team the Product (responsible AI analysis — your product, by another team)
- Week 7: Capstone presentations

**Speaker Notes:**
Be direct about this connection. The Week 6 activities are not abstract exercises — they're structured capstone development. Students who treat the AI Product Pitch as a throwaway activity will come to Week 7 underprepared. The pitch feedback you give today is the same feedback they'll get on the capstone. And the Red Team analysis in Session 2 — where another team stress-tests their product on responsible AI grounds — is a preview of the kind of scrutiny a real AI product faces from investors, regulators, and customers. Use the energy of this session to motivate the quality of capstone thinking.

---

### SLIDE 10 — Conceptual Exam 2 Overview

**Title:** Conceptual Exam 2 — Releasing Today

**Format:**
- Take-home, open-note, open-tool
- Individual — no collaboration
- 3 case-based short-answer questions
- Covers: AI strategy, governance, ethics, and responsible deployment
- Approximately 90 minutes of work
- Due: 48 hours after release

**What it tests:**
- Can you evaluate an AI product or deployment on strategy, governance, and ethics grounds?
- Can you identify risks, name the frameworks that apply, and propose design responses?
- Can you distinguish AI-enhanced from AI-native, and apply the ideation toolkit to a new scenario?

**Speaker Notes:**
Release via LMS immediately after class. Walk through the format in 60 seconds — the written instructions cover details. Remind students: this exam tests judgment applied to scenarios, not recall of definitions. A student who can name the NIST AI RMF but can't apply it to a specific case scenario will not score well. A student who can describe a concrete responsible AI risk in a given deployment, identify which framework element applies, and propose a design response will score very well. The exam rewards the same thinking we're practicing in the Red Team activity tomorrow.

---

### SLIDE 11 — Readings Reminder + Close

**Title:** Before Session 2 — Do the Readings

**Required before Session 2:**
- NIST AI Risk Management Framework — Executive Summary (provided via LMS, ~15 pages)
- "When AI Gets It Wrong: Case Studies in AI Failure" — instructor-curated (provided via LMS)

**Why the readings matter for Session 2:**
The Red Team activity asks you to identify the top 3 responsible AI risks in another team's product. Students who have read the NIST framework have a vocabulary and a structure for doing that analysis. Students who haven't will produce vague, generic risk lists. The quality difference in the activity is significant.

**Closing thought:**
Every AI product you've seen this week — Harvey, Glean, Nabla, whatever your team pitched today — will eventually face a session like the one we're running tomorrow. A regulator, an investor, a journalist, or a competitor will ask: what are the risks? What could go wrong? How did you design for it? Today you pitched. Tomorrow you find out what you missed.

**Speaker Notes:**
End the session on that note — it creates genuine anticipation for Session 2. The Red Team activity is one of the most engaging in the course precisely because teams feel protective of their product ideas and challenged by having their work critiqued. Channel that energy into productive preparation: the teams that do the readings and think critically about their own product's weaknesses before Session 2 will have more interesting exchanges.

---

### SLIDE 12 — Session Summary

**Title:** What We Covered Today

**Bullets:**
- AI-enhanced vs. AI-native: a distinction that changes strategic analysis
- Four business model patterns: mass personalization, AIaaS, outcome-based pricing, data flywheel
- Three AI-native company examples: Harvey, Glean, Nabla
- The ideation toolkit: user problem → AI capability → workflow design → business model
- Five vendor evaluation questions: data privacy, cost at scale, customizability, reliability, lock-in risk
- Four pitfalls in AI product thinking
- Conceptual Exam 2 released — due in 48 hours

**Coming up in Session 2:**
Responsible AI in practice — bias, hallucination, data privacy, regulatory landscape, and the Red Team activity.

**Speaker Notes:**
Quick summary close. The content today was dense and conceptual — make sure students leave with the ideation toolkit internalized. If you have 90 seconds, ask the class: "What's one AI-native product idea that came out of the pitch activity that you'd actually want to use?" That question surfaces genuine enthusiasm and ends the session on a positive, forward-looking note.

---

## ACTIVITY PLAN

---

### Activity: "AI Product Pitch" (15 minutes prep + 2 minutes per team pitch + 1 minute peer feedback each)

**Purpose:**
Apply the four-step ideation toolkit (user problem → AI capability → workflow design → business model) to a hypothetical AI-native product. Practice pitching at speed. Receive instructor feedback on product thinking quality in preparation for the capstone.

**Team configuration:**
Same course teams. Each team pitches once.

**What students do:**

| Phase | Duration | Task |
|-------|----------|------|
| Ideation sprint | 15 min | Teams apply the four-step toolkit to design a hypothetical AI-native product. Document all four components — problem, capability, workflow, business model. Assign a spokesperson. |
| Pitches (all teams) | 2 min × number of teams | Each team pitches. Peer vote on feasibility and impact immediately after each pitch. Instructor gives 60-second feedback. |

**What students produce:**
- A 4-component product concept (problem, capability, workflow, business model) — retained for the Session 2 Red Team swap
- The spoken pitch is the deliverable; no written submission required today

**Instructor facilitation notes:**

*During the ideation sprint (15 minutes — circulate):*

Most teams will start with the AI capability ("what if we used AI to...") rather than the user problem. Redirect immediately: "Who has this problem? What are they doing instead today? What does it cost them in time, money, or quality?" Forcing the user-problem-first frame almost always produces a sharper product concept.

Watch for over-broad problem statements: "small businesses waste time on administrative tasks" is not specific enough. Push for: "small business owners spend on average 6 hours per week manually entering receipts into accounting software." That specificity makes the AI capability choice obvious and the business model defensible.

Teams that are using their actual capstone direction: encourage them. Give them the same feedback quality you'd give on a capstone draft. This is not a separate exercise — it's integrated capstone development.

*During pitches:*

Time each pitch strictly at 2 minutes. Start timing when the spokesperson begins speaking. At 2 minutes, say "time" and give your feedback. Students who run long on the pitch get less instructor feedback — that's an appropriate consequence and mirrors real pitch environments.

Peer vote structure: after each pitch, ask for a show of hands: "Feasibility — could this be built with today's AI? Thumbs up if yes, thumbs sideways if probably, thumbs down if unlikely." Repeat for impact. Read the room and comment briefly: "Interesting split on feasibility — who thinks it's unlikely and why?" Keep it fast.

Your 60-second instructor feedback for each pitch:
1. One specific thing that works in the product thinking (not generic praise)
2. One specific thing to sharpen (not generic critique — name the component: "the business model needs a pricing unit")
3. One question the team should resolve before the capstone (the kind a skeptical investor would ask)

After all pitches: tell teams to save their product concept. In Session 2, they'll swap with another team for the Red Team analysis.

**Materials needed:**
- Slide 7 (activity card) displayed during ideation sprint
- No handout required
- Peer voting: show of hands, or a quick poll tool if the class uses one
- Teams should retain their product concept notes for Session 2 swap
