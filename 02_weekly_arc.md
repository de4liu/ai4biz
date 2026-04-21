# IDSC 4101: Agentic AI for Business Applications
## 7-Week Session Schedule

---

### How to Read This Schedule

Each week has a unifying theme and two 100-minute sessions. **Session 1** typically introduces concepts and tools through demonstration and guided exploration. **Session 2** builds on that foundation with a hands-on activity, case discussion, or team build sprint. Readings listed under each week should be completed **before** Session 1 unless otherwise noted. Tools are introduced progressively — do not worry about mastering earlier tools before new ones appear; the course is designed to layer skills.

The arc of the course follows a deliberate progression:

- **Week 1:** Advanced GenAI foundations — multi-modal capabilities, RAG concepts, and enterprise deployment. Assumes prior basic prompting experience; moves fast into business-critical depth.
- **Weeks 2–3:** AI for business — workflow automation, no-code tools, and functional applications across marketing, finance, operations, and HR.
- **Weeks 4–6:** Agentic AI — three full weeks on autonomous systems, multi-agent architectures, human-in-the-loop design, failure modes, and real business deployment.
- **Week 7:** Strategy, ethics, and synthesis — responsible AI, organizational decision-making, and capstone presentations.

---

## Week 1: Beyond the Basics — Advanced GenAI and Enterprise Foundations

**Theme:** Fast-paced elevation from personal prompting (covered in prior coursework) to advanced techniques, multi-modal capabilities, RAG concepts, and how enterprises actually deploy generative AI at scale. Course orientation embedded in Session 1.

**Session 1 — Course Orientation + Advanced Prompting for Business Judgment**

*Topics:*
- Course orientation (20 min): arc, assessments, tools, capstone overview — assumes students have used Gemini and basic prompting before
- Advanced prompt techniques: chain-of-thought prompting, prompt chaining across tasks, structured output prompting (requesting JSON, tables, or scored formats), adversarial prompting (deliberately stress-testing AI outputs)
- Framing shift: prompting not for drafts, but for decisions — how to use AI as an analytical partner, not just a writing tool
- Multi-modal Gemini: what changes when AI can read images, PDFs, spreadsheets, and audio — live demo using a business document and an image of a dashboard

*Activity:* "Prompt Audit" — students receive a weak business prompt and its output. In pairs, they diagnose what is missing (context, constraints, format, reasoning instruction) and rebuild it using at least two advanced techniques. Before/after comparison shared with class.

*Tools Introduced/Deepened:* Google Gemini (advanced and multi-modal use), Google AI Studio (prompt experimentation)

**Session 2 — How Enterprises Deploy GenAI: RAG, Fine-Tuning, and Governance**

*Topics:*
- From personal tools to enterprise systems: why individual Gemini use and enterprise AI deployment are fundamentally different problems
- Retrieval-Augmented Generation (RAG): what it is, why businesses use it, and when it outperforms a standard LLM — explained conceptually, no code (think: AI that reads your company's documents before answering)
- Fine-tuning vs. RAG vs. prompt engineering: how businesses choose an approach based on cost, control, and use case
- Enterprise GenAI governance: data privacy, vendor risk, model versioning, audit trails — what responsible enterprise deployment looks like in practice
- Real examples: how a law firm, a hospital, and a retailer have each deployed GenAI differently and why

*Activity:* "Enterprise Scenario Sprint" — teams receive a one-paragraph description of a mid-sized company's AI ambition and constraints. They recommend whether to use RAG, fine-tuning, or prompt engineering — and justify the choice using the framework from the lecture. Teams present their recommendation in 90 seconds.

*Tools Introduced:* Conceptual overview of RAG architecture (no build required); reference to enterprise platforms (Microsoft Copilot, Google Vertex AI, AWS Bedrock) as examples

*Readings (before Session 1):*
- Mollick, E. "Using AI to Make Work More Meaningful" — *Harvard Business Review*, 2024
- Assigned briefing: "What is RAG and Why Does It Matter?" — instructor-curated summary (provided via LMS)

*Assignment Due:* **Reflection Post 1** — 200–300 words: Describe one advanced prompting technique you tried this week that you had not used before. What changed in the output quality, and why do you think it worked?

---

## Week 2: AI for Teams — Automating the Work Nobody Wants to Do

**Theme:** From individual tools to team workflows. Students learn to identify automation opportunities and connect AI to the systems businesses already use — without writing code.

**Session 1 — Workflow Thinking: What Gets Automated and What Does Not**

*Topics:*
- The automation opportunity: which business tasks are repetitive, rule-based, and time-consuming enough to automate?
- A framework for identifying automation candidates: frequency × effort × standardizability
- Introduction to no-code workflow builders: what they are, how they work visually, what they can connect (email, spreadsheets, CRMs, Slack, databases, AI models)
- Demonstration: building a simple Zapier workflow that takes a form submission, passes it to Gemini for a summary, and emails the result — live in class, no code
- Where GenAI fits in a workflow vs. where it does not: structured vs. unstructured tasks, reversible vs. irreversible actions

*Activity:* "Automation Audit" — in teams, students map the workflows of a hypothetical small business (provided scenario) and identify the top 3 candidates for AI-assisted automation. Teams present their reasoning using the frequency × effort × standardizability framework.

*Tools Introduced:* Zapier (or Make) — visual introduction

**Session 2 — Build Sprint: Your First Automation**

*Topics:*
- The anatomy of a no-code workflow: triggers, actions, filters, and AI steps
- Common business automations: lead qualification, meeting follow-up drafting, customer feedback summarization, content repurposing, invoice processing
- Relevance AI: building AI-powered assistants that follow business-specific rules
- Error handling and guardrails in automated workflows: what happens when AI produces a bad output mid-workflow?

*Activity:* **Build Sprint 1** — each student builds a working automation connecting at least two tools with an AI step in the middle. Examples: a Google Form that summarizes responses with Gemini and posts to a shared Slack channel; an email inbox watcher that drafts replies using AI. Instructor circulates; peer help encouraged.

*Tools Introduced:* Zapier (or Make), Relevance AI (introduction)

*Readings (before Session 1):*
- McKinsey & Company: "The State of AI in 2025" — assigned excerpt (provided via LMS)
- Case study: "Automation at Scale: How [Company] Redesigned Its Customer Service Workflow" (HBS case — to be confirmed)

*Assignment Due:* **Reflection Post 2** — 200–300 words: What workflow did you build? What broke, and how did you fix it? What would you automate next?

---

## Week 3: Business Applications by Function — AI Across the Organization

**Theme:** Industry and functional applications. Students explore how AI is reshaping their own concentration areas and develop an ideation vocabulary for spotting and pitching new AI opportunities.

**Session 1 — AI in Marketing, Sales, and Customer Experience**

*Topics:*
- AI in marketing: content generation, audience segmentation, personalization at scale, A/B testing with AI assistance
- AI in sales: lead scoring, outreach personalization, call summarization, pipeline forecasting
- AI in customer experience: chatbots vs. AI agents, sentiment analysis, support ticket routing
- The "ideation mindset": how to look at a business function and ask "where is the AI opportunity?" — not "how do I build it?" but "what would it need to do and what value would it create?"
- Guest perspective (video or live): practitioner in marketing or sales describing their AI toolkit

*Activity:* "Function Mapping" — each student maps their intended career function and identifies 3 concrete AI use cases. They pitch the highest-impact one to a partner, who challenges it with a "what could go wrong?" critique.

**Session 2 — AI in Operations, Finance, and HR + Capstone Team Formation**

*Topics:*
- AI in operations: demand forecasting, logistics optimization, quality control flagging, supplier communication
- AI in finance: financial report summarization, anomaly detection, automated client briefings, regulatory document review
- AI in HR: job description writing, resume screening augmentation, onboarding content generation, employee sentiment monitoring
- Cross-functional theme: AI as a force multiplier — small teams doing more, not headcount replacement (nuanced discussion)
- Capstone team formation: cross-major teams of 3–4, sector assignment process explained

*Activity:* Capstone team formation and sector brainstorm. Teams meet for the first time, review their assigned sector, and identify 3 potential AI problem areas to investigate. Team composition approved by instructor before Week 4.

*Readings (before Session 1):*
- Assigned report: "AI Adoption by Business Function" — Deloitte AI Institute excerpt (provided via LMS)
- Assigned article: "AI Won't Replace Humans — But Humans with AI Will Replace Humans Without AI" — *HBR*, 2023

*Assignment Due:* **Reflection Post 3** — 200–300 words: Pick one functional AI application from this week. What is the highest-value use case, and what is the most significant risk a business would need to manage before deploying it?

---

## Week 4: Agentic AI — What Agents Are and How They Think

**Theme:** Crossing from generative AI (AI that responds) to agentic AI (AI that plans, acts, and loops). Students learn what agents are, how they reason, and how to evaluate them as business tools — not just as technology.

**Session 1 — What Is an AI Agent?**

*Topics:*
- The key difference: generative AI responds; agentic AI plans, takes actions, and loops back on its own outputs
- Agent anatomy without code: goals, tools, memory, and reasoning loops — explained through analogy and diagram
- Types of agents students will encounter in business: task agents, research agents, customer-facing conversational agents, multi-agent systems (one agent orchestrates others)
- Agentic AI design patterns: reflection (agent checks its own output), tool use (agent calls external systems), planning (agent breaks a goal into steps), handoff (agent routes to human or another agent)
- Real business examples: AI SDR that researches and drafts outreach; AI operations agent that monitors inventory and flags exceptions; AI onboarding agent that answers new employee questions

*Activity:* "Agent Blueprint" — teams sketch an agent for a business use case they find compelling. They define: What is the agent's goal? What tools does it need? When should it hand off to a human? What could go wrong? Blueprint shared with class; instructor gives feedback on each.

**Session 2 — Failure Modes, Guardrails, and Human-in-the-Loop Design**

*Topics:*
- Why agentic AI fails: goal misspecification, tool misuse, compounding errors, reward hacking — with real business examples
- The human-in-the-loop spectrum: fully autonomous vs. human-supervised vs. human-approved — how organizations decide where to draw the line
- Guardrails: what they are, how to define them without code (scope restrictions, escalation rules, audit trails)
- Regulatory and liability implications of autonomous AI actions: who is responsible when an agent does something wrong?
- Case study: an agentic AI deployment that went wrong — class analysis of what the failure point was and what design choice could have prevented it

*Activity:* "Failure Mode Analysis" — each team takes their agent blueprint from Session 1 and runs it through a structured failure analysis: What are the top 3 ways this agent could cause harm or produce a bad outcome? What guardrail would address each? Teams document and present.

*Readings (before Session 1):*
- Assigned article: "The Rise of AI Agents in Enterprise" — *MIT Technology Review*, 2025 (provided via LMS)
- Assigned briefing: "Agentic AI: Opportunities and Risks for Business" — instructor-curated (provided via LMS)

*Assignment Due:* **Midterm Conceptual Exam (take-home, open-book, HonorLock, individual)** — released after Session 2, due before Week 5 Session 1. Format: 4 case-based short-answer questions testing conceptual understanding of GenAI foundations, workflow automation, and agentic AI basics. AI tools allowed. Approximately 90 minutes.

---

## Week 5: Building Agents — No-Code Agent Construction and Multi-Agent Systems

**Theme:** From understanding agents to building them. Students construct working agents using no-code platforms and explore how multiple agents collaborate in enterprise-grade systems.

**Session 1 — Build Sprint: Your First Agent**

*Topics:*
- Introduction to n8n and Voiceflow: what each is best for (n8n for workflow-based agents; Voiceflow for conversational agents)
- Building a simple agent: a customer FAQ bot that can look up answers, escalate when it does not know, and log interactions
- Live demo: instructor builds a working agent from scratch in class — students observe before building their own
- Connecting agents to external tools: how agents call APIs, read databases, or trigger other workflows without code

*Activity:* **Build Sprint 2** — teams build a working agent using n8n or Voiceflow. Suggested builds: a customer service agent for a fictional business, a meeting scheduler agent, or a research agent that searches and summarizes. Teams demo their agent to another team at the end of the session. Instructor circulates and troubleshoots.

*Tools Introduced:* n8n, Voiceflow

**Session 2 — Multi-Agent Systems: When One Agent Is Not Enough**

*Topics:*
- What is a multi-agent system? Orchestrators, subagents, and how tasks are delegated between agents
- Business cases for multi-agent architectures: complex research pipelines, customer service escalation chains, automated financial reporting workflows
- How agents communicate: handoff protocols, shared memory, and output chaining
- The coordination problem: what can go wrong when multiple agents work together — and how organizations design for it
- Emerging platforms: overview of Microsoft Copilot Studio, Salesforce Agentforce, and Google Agentspace as enterprise multi-agent environments (conceptual, no build)

*Activity:* "Multi-Agent System Design" — teams design a multi-agent system for their capstone sector. They map: which agent does what, what triggers each handoff, where human oversight enters, and what the failure scenario looks like. Output: a one-page system diagram (text-based or drawn).

*Readings (before Session 1):*
- Assigned article: "Multi-Agent AI Systems Are Coming to the Enterprise" — *MIT Technology Review* or equivalent, 2025 (provided via LMS)

*Assignment Due:* **Reflection Post 4** — 200–300 words: What does your agent do? What design decision did you make about what it should NOT be allowed to do autonomously — and why?

---

## Week 6: Agentic AI in the Real World — Products, Business Models, and Responsible Deployment

**Theme:** From building agents to deploying them responsibly. Students examine how companies embed agentic AI into products and business models, evaluate vendor platforms, and learn to identify and mitigate the risks that come with autonomous AI systems.

**Session 1 — AI-Native Products and Agentic Business Models**

*Topics:*
- What makes a product "AI-native" vs. "AI-enhanced"? — and why it matters for competitive strategy
- Business model patterns enabled by agentic AI: mass personalization at scale, AI-as-a-service, outcome-based pricing, autonomous operations
- Startup and enterprise examples: companies whose core value proposition depends on agentic AI (not just GenAI)
- The ideation toolkit: from user problem → agent capability → workflow design → value proposition — thinking like an AI product designer without writing code
- Vendor evaluation for agentic platforms: key questions on data privacy, cost at scale, customizability, reliability, and vendor lock-in risk
- Guest perspective (live or video): practitioner who has deployed an agentic AI system in a business context

*Activity:* "Agentic Product Pitch" — teams pitch a hypothetical AI-native product or service built around an agentic system (2 minutes each). Peers vote on feasibility and impact. Instructor gives targeted feedback on product thinking and agentic design logic.

**Session 2 — Responsible Agentic AI: Ethics, Security, and Governance**

*Topics:*
- Why responsible AI matters more for agents than for GenAI tools: agents act, not just generate — mistakes compound
- Bias and fairness in agentic systems: where bias enters, and how to spot warning signs without being a data scientist
- Security risks specific to agents: prompt injection attacks, tool misuse, data exfiltration through agent actions
- Data privacy in agentic systems: what data agents access, where it goes, what enterprise data governance must address
- Regulatory landscape: EU AI Act classification of autonomous systems, U.S. executive orders, FINRA/SEC implications for financial agents (high-level)
- Principles for responsible deployment: NIST AI Risk Management Framework — conceptual overview applied to agentic contexts

*Activity:* "Red Team the Agent" — teams swap their multi-agent system designs from Week 5 and spend 20 minutes identifying the top 3 ethical, security, or reliability risks in the other team's system. They present findings; original teams respond with a revised guardrail recommendation.

*Readings (before Session 1):*
- Assigned briefing: NIST AI Risk Management Framework — Executive Summary (provided via LMS)
- Assigned article: "When AI Agents Go Wrong: Case Studies in Autonomous System Failure" — instructor-curated (provided via LMS)

*Assignment Due:* **Reflection Post 5** — 200–300 words: What is the biggest responsible AI risk in your team's capstone project, and what specific design choice — in the agent's guardrails, handoff rules, or data access — would you make to mitigate it?

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
- **Final Exam (take-home, open-book, AI tools allowed, HonorLock proctored, individual)** — released after Session 1, 90-minute window. Format: short concept check (15%) + scenario-based analysis on AI strategy, agentic systems, governance, and ethics (85%). Includes a required prompt transparency section.
- **Capstone Team Deliverable** — slide deck submitted to LMS before Session 2.

---


