# IDSC 4101: Generative and Agentic AI for Business
## 7-Week Session Schedule

---

### How to Read This Schedule

Each week has a unifying theme and two 100-minute sessions. **Session 1** typically introduces concepts and tools through demonstration and guided exploration. **Session 2** builds on that foundation with a hands-on activity, case discussion, or team build sprint. Readings listed under each week should be completed **before** Session 1 unless otherwise noted. Tools are introduced progressively — do not worry about mastering earlier tools before new ones appear; the course is designed to layer skills.

The arc of the course follows a deliberate progression:

- **Weeks 1–2:** What is generative AI, and how does it already show up in your life? (Personal productivity lens)
- **Weeks 3–4:** How do businesses use this? What can I build for a team or organization? (Workflow and business application lens)
- **Weeks 5–6:** What are AI agents, and how do businesses deploy them as workers, assistants, and decision-makers? (Agentic and automation lens)
- **Week 7:** Where is this going, and what does it mean for how I work, lead, and make decisions? (Strategy, ethics, and responsibility lens)

---

## Week 1: Welcome to the AI Era — What Is Generative AI and Why Does It Matter?

**Theme:** Orientation, curiosity, and first contact with generative AI tools.

**Session 1 — The New Landscape (Day 1)**

*Topics:*
- Course orientation: what we will build, what we will understand, how we will be assessed
- What generative AI actually is — and is not: distinguishing it from search engines, calculators, and traditional software
- A brief, non-technical mental model: how AI learns from text and generates responses (no math; think of it as a very well-read assistant that predicts what to say next)
- The generative AI moment: why 2022–2025 was a hinge point in technology history
- Live demo: instructor uses Gemini live in class to answer a business question, draft a memo, and make a factual error — students observe and discuss

*Activity:* "First Contact" — students open Gemini for the first time and complete three tasks: ask a question in their area of interest, give the AI a bad prompt, then a better one, and compare outputs. No setup beyond a Google account.

*Discussion:* What surprised you? What did it get right? What did it get wrong?

*Tools Introduced:* Google Gemini (conversational interface)

**Session 2 — Personal AI: Making Your Own Work Life Better**

*Topics:*
- Generative AI as a personal productivity tool — not a replacement for thinking, but an accelerant
- Use cases every business student can use today: drafting emails, summarizing documents, preparing for interviews, building study guides, researching companies before a job application
- Prompting as communication: the difference between a bad prompt and a great one is not magic — it is clarity, context, and specificity
- Introduction to prompt patterns: role prompting, step-by-step instructions, asking for multiple options, giving examples

*Activity:* "Upgrade Your Workflow" — each student picks one recurring task from their academic or personal life (weekly recap email, meeting agenda, study notes, cover letter draft) and uses Gemini to build a reusable prompt template for it. Students share their best templates with the class.

*Readings (before Session 1):*
- Mollick, E. "Using AI to Make Work More Meaningful" — *Harvard Business Review*, 2024
- Assigned briefing: "What is a Large Language Model?" (NotebookLM-generated summary, provided via LMS — students will evaluate it critically in class)

*Assignment Due:* None (week 1 is orientation)

---

## Week 2: Going Deeper — Understanding AI Well Enough to Use It Confidently

**Theme:** Building just enough conceptual foundation to be an informed, critical user — not a builder of models, but someone who understands why AI behaves the way it does.

**Session 1 — Why Does AI Do That?**

*Topics:*
- Tokens, context windows, and why AI "forgets" things in long conversations
- Hallucination: what it is, why it happens structurally, and how to reduce it — this is not a bug to be fixed, it is a feature of how the technology works
- Temperature and creativity: why AI gives different answers to the same question
- Multimodal AI: what changes when AI can see images, read PDFs, and hear audio
- Model differences: what it means when a tool says it uses a "more capable" or "faster" model, and how to think about choosing tools

*Activity:* "Break the AI" — structured red-teaming exercise. Teams are given a list of prompting strategies (adding false context, asking the AI to roleplay, pushing it toward confident wrong answers) and test Gemini's behavior. Teams report findings. Discussion: what does this tell us about how to use AI responsibly?

*Session 2 — NotebookLM: AI as a Research and Knowledge Partner**

*Topics:*
- Introduction to NotebookLM: AI that reads your documents and lets you ask questions about them
- Use cases: summarizing a 40-page report, extracting key arguments from a case study, generating a briefing document for a client meeting, building a study guide from lecture notes
- Limits: NotebookLM only knows what you give it — and it can still be wrong about what it reads
- Ideation use case: using AI to pressure-test a business idea by uploading competitor websites, industry reports, and your own notes

*Activity:* "The Analyst Sprint" — each student uploads a set of documents relevant to their concentration (a 10-K, a case study, an industry report — provided) to NotebookLM and builds a one-page executive briefing by querying the AI. Teams compare their briefings and identify discrepancies.

*Tools Introduced:* Google NotebookLM, Google AI Studio (first look — used for prompt experimentation)

*Readings (before Session 1):*
- Assigned article: "The Hallucination Problem and What to Do About It" — *MIT Technology Review*, 2024
- Optional: Suleyman, M. *The Coming Wave*, Chapter 1 (recommended text)

*Assignment Due:* **Reflection Post 1** — 200–300 words: Describe one moment this week when the AI surprised you (positively or negatively). What does that surprise tell you about how the tool works?

---

## Week 3: AI for Teams — Automating the Work Nobody Wants to Do

**Theme:** From personal tools to team workflows. Students learn to connect AI to the systems businesses already use — without writing code.

**Session 1 — Workflow Thinking: What Gets Automated and What Does Not**

*Topics:*
- The automation opportunity: which business tasks are repetitive, rule-based, and time-consuming enough to automate?
- A framework for identifying automation candidates: frequency × effort × standardizability
- Introduction to no-code workflow builders: what they are, how they work visually, what they can connect (email, spreadsheets, CRMs, Slack, databases, AI models)
- Demonstration: building a simple Zapier workflow that takes a form submission, passes it to Gemini for a summary, and emails the result — live in class, no code

*Activity:* "Automation Audit" — in teams, students map the workflows of a hypothetical small business (provided scenario) and identify the top 3 candidates for AI-assisted automation. Teams present their reasoning using the frequency × effort × standardizability framework.

*Session 2 — Build Sprint: Your First Automation**

*Topics:*
- Getting set up with Zapier or Make (students choose their preferred platform)
- The anatomy of a no-code workflow: triggers, actions, filters, and AI steps
- Common business automations: lead qualification, meeting follow-up drafting, customer feedback summarization, content repurposing, invoice processing
- Relevance AI: building AI-powered assistants that follow business-specific rules

*Activity:* **Build Sprint 1** — each student builds a working automation connecting at least two tools with an AI step in the middle. Examples: a Google Form that summarizes responses with Gemini and posts to a shared Slack channel; an email inbox watcher that drafts replies using AI. Instructor circulates; peer help encouraged.

*Tools Introduced:* Zapier (or Make), Relevance AI (introduction)

*Readings (before Session 1):*
- McKinsey & Company: "The State of AI in 2025" — assigned excerpt (provided via LMS)
- Case study: "Automation at Scale: How [Company] Redesigned Its Customer Service Workflow" (HBS case — to be confirmed)

*Assignment Due:* **Reflection Post 2** — 200–300 words: What workflow did you build? What broke, and how did you fix it? What would you automate next?

---

## Week 4: Business Applications by Function — AI Across the Organization

**Theme:** Industry and functional applications. Students explore how AI is being used in their own concentration areas and develop an ideation vocabulary for new applications.

**Session 1 — AI in Marketing, Sales, and Customer Experience**

*Topics:*
- AI in marketing: content generation, audience segmentation, personalization at scale, A/B testing with AI assistance
- AI in sales: lead scoring, outreach personalization, call summarization, pipeline forecasting
- AI in customer experience: chatbots vs. AI agents, sentiment analysis, support ticket routing
- The "ideation mindset": how to look at a business function and ask "where is the AI opportunity?" — not "how do I build it?" but "what would it need to do?"
- Guest perspective (video or live): practitioner in marketing or sales describing their AI toolkit

*Activity:* "Function Mapping" — each student maps their intended career function and identifies 3 concrete AI use cases. They pitch the highest-impact one to a partner, who challenges it with a "what could go wrong?" critique.

**Session 2 — AI in Operations, Finance, and HR**

*Topics:*
- AI in operations: demand forecasting, logistics optimization, quality control flagging, supplier communication
- AI in finance: financial report summarization, anomaly detection, automated client briefings, regulatory document review
- AI in HR: job description writing, resume screening augmentation, onboarding content generation, employee sentiment monitoring
- Cross-functional theme: AI as a force multiplier — small teams doing more, not headcount replacement (nuanced discussion)

*Activity:* **Midterm Exam Review Session** — instructor-led review of core concepts from weeks 1–4 using live class polling. Students submit 2 questions they are unsure about; instructor addresses top questions. Remainder of session: team capstone brainstorm — teams of 3–4 form and begin identifying their capstone business problem.

*Readings (before Session 1):*
- Assigned report: "AI Adoption by Business Function" — Deloitte AI Institute excerpt (provided via LMS)
- Assigned article: "AI Won't Replace Humans — But Humans with AI Will Replace Humans Without AI" — *HBR*, 2023

*Assignment Due:* **Midterm Conceptual Exam (take-home, open-note, individual)** — released after Session 2, due before Week 5 Session 1. Format: 4 case-based short-answer questions testing conceptual understanding of LLMs, workflow automation, and functional AI applications. No coding. Approximately 90 minutes.

---

## Week 5: Agentic AI — Building Systems That Act, Not Just Answer

**Theme:** Crossing from generative AI (AI that responds) to agentic AI (AI that acts). Students learn what agents are, how they reason, and how businesses are beginning to deploy them.

**Session 1 — What Is an AI Agent?**

*Topics:*
- The key difference: generative AI responds; agentic AI plans, takes actions, and loops back
- Agent anatomy without code: goals, tools, memory, reasoning loops — explained through analogy and diagram
- Types of agents students will encounter in business: task agents, research agents, customer-facing conversational agents, multi-agent systems (one agent manages others)
- Agentic AI design patterns: reflection (agent checks its own output), tool use (agent calls external systems), planning (agent breaks a goal into steps), handoff (agent routes to human or another agent)
- Real business examples: AI SDR (sales development representative) that researches, drafts, and sends outreach; AI operations agent that monitors inventory and flags exceptions; AI onboarding agent that answers new employee questions

*Activity:* "Agent Blueprint" — teams sketch an agent for a business use case they find interesting. They define: What is the agent's goal? What tools does it need access to? When should it hand off to a human? What could go wrong?

**Session 2 — Build Sprint: Your First Agent with n8n or Voiceflow**

*Topics:*
- Introduction to n8n and Voiceflow: what each is best for (n8n for workflow-based agents; Voiceflow for conversational agents)
- Building a simple agent: a customer FAQ bot that can look up answers, escalate when it does not know, and log interactions
- Introduction to the concept of "guardrails": how to scope what an agent is and is not allowed to do

*Activity:* **Build Sprint 2** — teams build a simple agent using n8n or Voiceflow. Suggested builds: a customer service agent for a fictional business, a meeting scheduler agent, or a research agent that searches and summarizes. Teams demo their agent to another team at the end of the session.

*Tools Introduced:* n8n, Voiceflow

*Readings (before Session 1):*
- Assigned article: "The Rise of AI Agents in Enterprise" — *MIT Technology Review*, 2025 (provided via LMS)

*Assignment Due:* **Reflection Post 3** — 200–300 words: What does your agent do? What decision did you make about what it should NOT be allowed to do, and why?

---

## Week 6: Building for Real — AI in Products, Ventures, and Business Models

**Theme:** From individual tools to business-level thinking. How do companies build AI into their products and business models? How do you think like an AI product designer without being an engineer?

**Session 1 — AI-Native Products and Business Models**

*Topics:*
- What makes a product "AI-native" vs. "AI-enhanced"?
- Business model patterns enabled by AI: mass personalization, AI-as-a-service, outcome-based pricing, data flywheels
- Startup and enterprise examples: companies that are fundamentally different because of generative AI at their core
- The ideation toolkit: from user problem → AI capability → workflow design → value proposition — walking through the product thinking loop without needing to write code
- Vendor evaluation: how do you choose an AI platform? Key questions: data privacy, cost at scale, customizability, reliability, vendor lock-in risk

*Activity:* "AI Product Pitch" — teams pitch a hypothetical AI-native product or service to the class (2 minutes each). Peers vote on feasibility and impact. Instructor gives feedback on product thinking.

**Session 2 — Responsible AI: Ethics, Security, and What Can Go Wrong**

*Topics:*
- Why responsible AI matters in practice, not just in principle: reputational, legal, and operational risks
- Bias and fairness: where bias enters AI systems and how to spot warning signs without being a data scientist
- Hallucination in business contexts: what happens when an AI gives a confident wrong answer in a customer-facing product
- Data privacy and security basics: what data goes into an AI tool, where it is stored, what your company's data policies should address
- Regulatory landscape: EU AI Act basics, U.S. executive orders, what compliance looks like for a business deploying AI (high-level)
- The human-in-the-loop principle: when to require human review before AI output becomes action
- Principles for responsible deployment: NIST AI Risk Management Framework (conceptual overview)

*Activity:* "Red Team the Product" — teams swap their AI product pitches from Session 1 and spend 20 minutes identifying the top 3 ethical, security, or reliability risks in the other team's product. They present their findings; original teams respond.

*Readings (before Session 1):*
- Assigned briefing: NIST AI Risk Management Framework — Executive Summary (provided via LMS)
- Assigned article: "When AI Gets It Wrong: Case Studies in AI Failure" — instructor-curated (provided via LMS)

*Assignment Due:* **Reflection Post 4** — 200–300 words: What is the biggest responsible AI risk in your team's capstone project, and what design choice would you make to mitigate it?

---

## Week 7: Strategy, Synthesis, and What Comes Next

**Theme:** Pulling it together. How do leaders make decisions about AI adoption? What does it mean to work, lead, and grow in an AI-augmented world?

**Session 1 — AI Strategy for Organizations**

*Topics:*
- How organizations think about AI: strategy vs. experimentation vs. transformation
- The AI adoption spectrum: augmentation, automation, and autonomy — and how organizations move along it
- Building an AI roadmap: how to identify priorities, evaluate tools, build for change management, and measure impact
- Common failure modes of enterprise AI: wrong problem, wrong tool, no change management, ignoring ethics — case examples
- The human side: what jobs change, which skills grow in value, how to position yourself as an AI-fluent professional

*Activity:* Final exam review session and capstone preparation time. Instructor-led Q&A on final exam format; teams finalize their presentations.

**Session 2 — Capstone Presentations and Course Synthesis**

*Topics (brief, 15 minutes):*
- Where generative and agentic AI are heading: multimodal agents, physical AI, AI-to-AI economies — brief horizon scan
- The mindset that matters most: curiosity, critical evaluation, and willingness to learn continuously

*Activity:* **Capstone Presentations** — each team presents their AI workflow or agent (8 minutes) followed by 4 minutes of Q&A from peers and instructor. Presentations are evaluated on: problem clarity, solution design, AI workflow logic, responsible AI considerations, and pitch quality.

*Assignment Due:*
- **Final Conceptual Exam (take-home, open-note, individual)** — released after Session 1, due 48 hours later. Format: 3 case-based questions on AI strategy, governance, and ethics. No coding. Approximately 90 minutes.
- **Capstone Team Deliverable** — slide deck submitted to LMS before Session 2.

---


