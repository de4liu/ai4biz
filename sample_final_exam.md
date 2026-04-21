# IDSC 4101: Agentic AI for Business Applications
## Sample Final Examination

**Format:** Take-home | Open book | AI tools permitted
**Proctoring:** HonorLock (webcam + browser monitoring active throughout)
**Time Limit:** 90 minutes from the moment you open the exam
**Submission:** Upload completed responses to Canvas before the timer expires
**Individual Work:** This is an individual assessment. You may use any AI tool, your notes, and course materials. You may not collaborate with classmates.

---

### Academic Integrity Notice

By submitting this exam, you confirm that all written responses reflect your own analysis and judgment. AI tools are permitted and encouraged — but your reasoning, your recommendations, and your critique must be your own. Submitting AI-generated text without meaningful synthesis or judgment is a violation of the Carlson School Honor Code.

**You are required to submit at least one prompt you used during the exam** (see Section III). This is not optional.

---

## Section I — Concept Check (15 points | ~15 minutes)

*Answer each question in 1–3 sentences. Be precise. Full credit requires the correct concept AND a brief explanation of why it matters in a business context.*

**1.** (3 pts) What is a "hallucination" in the context of a large language model, and why does it occur structurally — not as a software bug, but as a consequence of how these models work?

**2.** (3 pts) Distinguish between a *generative AI* tool and an *agentic AI* system. Give one concrete example of each from the course.

**3.** (3 pts) What is Retrieval-Augmented Generation (RAG), and why would a business prefer a RAG-based system over a standard LLM for internal knowledge management?

**4.** (3 pts) A colleague says: "We should use AI to automate everything that's repetitive." Using the automation framework from Week 3, explain why frequency alone is not a sufficient criterion for selecting automation candidates.

**5.** (3 pts) Name two distinct categories of AI-related risk that a business must consider before deploying a customer-facing AI tool. For each, give one real-world example of what happens when that risk is not managed.

---

## Section II — Scenario Analysis (85 points | ~75 minutes)

*Read the scenario carefully. Answer all four parts. You may use AI tools to assist your thinking, but your written responses must demonstrate your own judgment, synthesis, and reasoning. Responses that read as direct AI output without analysis or critique will receive partial credit at best.*

---

### The Scenario: NorthStar Wealth Advisors

**NorthStar Wealth Advisors** is a mid-sized financial advisory firm based in Minneapolis with 420 employees and approximately 18,000 individual clients. The firm offers investment planning, retirement advising, tax strategy coordination, and estate planning referrals.

NorthStar's CEO, Dana Larsen, has tasked you — a junior strategy analyst — with preparing a memo for the leadership team evaluating whether and how the firm should integrate generative and agentic AI into its operations. She gives you the following background:

**Current state:**
- Advisors spend an average of 6–8 hours per week writing personalized client communications (quarterly portfolio summaries, market update letters, meeting preparation notes).
- The compliance team reviews every client-facing document before it is sent — a process that adds 48–72 hours of turnaround time per document and creates a significant bottleneck.
- New client onboarding involves collecting documents, verifying information, and populating a CRM system — a process that takes 3–5 business days and is done almost entirely manually.
- Client inquiries outside of scheduled appointments (e.g., "What does this market drop mean for my portfolio?") are often not answered for 24–48 hours because advisors are fully booked.

**Constraints:**
- NorthStar operates under SEC and FINRA regulations, which impose strict requirements on what can be communicated to clients, how advice is documented, and what must be reviewed by a licensed professional before delivery.
- The firm's clients are primarily 55–75 years old; many are not comfortable with chatbots or self-service tools and strongly prefer human interaction.
- IT infrastructure is largely cloud-based (Microsoft 365, Salesforce CRM), but the firm has no dedicated data science or engineering team.

---

### Part A — Opportunity Identification (20 points)

Identify **three specific areas** within NorthStar's operations where generative or agentic AI could create meaningful value. For each opportunity:

1. Name the specific workflow or pain point
2. Describe the AI approach you would recommend (generative, agentic, RAG-based, or a combination) and explain why that approach fits
3. Estimate the type of value created (time savings, quality improvement, cost reduction, client experience) — be specific, not vague
4. Identify one constraint from the scenario that complicates implementation and explain how you would address it

*Grading note: Credit is awarded for specificity and reasoning. "Use AI to improve communication" is not an acceptable answer. "Use a RAG-based system trained on NorthStar's approved communication templates and past client letters to draft first-pass quarterly summaries for advisor review" is.*

---

### Part B — Risk and Ethics Analysis (25 points)

NorthStar's compliance officer, James Okonkwo, raises three concerns at the leadership meeting:

> "First, if AI drafts client communications and an advisor approves them without fully reading them — and the content turns out to be factually wrong or misleading — who is liable? Second, our older clients did not sign up for AI-generated advice. Does using AI on their accounts without explicit disclosure raise ethical or legal issues? Third, what happens if the AI system we buy gets breached or starts producing biased outputs?"

**Answer the following:**

1. (10 pts) Address each of James's three concerns directly. For each, explain whether the concern is primarily a legal, ethical, or operational risk (it may be more than one), and recommend one concrete policy or design decision NorthStar should put in place to manage it.

2. (8 pts) The CEO wants to move quickly. She says: "We can disclose AI use in the fine print of our terms of service and update it later if regulators require more." Evaluate this approach. Is it sufficient from an ethical standpoint? From a regulatory standpoint? What would you recommend instead?

3. (7 pts) NorthStar's advisors are worried about their jobs. Two of the firm's top-performing advisors have told Dana privately that they will leave if AI tools are introduced. How should NorthStar's leadership think about the workforce implications of this AI initiative — not just operationally, but ethically and strategically?

---

### Part C — Implementation Recommendation (25 points)

Dana asks you to recommend **one AI initiative** for NorthStar to pilot in the next six months — the single highest-value, lowest-risk starting point given the firm's constraints.

Your recommendation must include:

1. **(5 pts) The specific initiative:** What exactly will be built or deployed? Be precise about the tool type, the workflow it addresses, and what the output looks like.

2. **(5 pts) Why this one first:** Justify your choice relative to the other opportunities you identified in Part A. What makes this the right starting point given NorthStar's regulatory environment, client demographics, and technical capacity?

3. **(5 pts) Success metrics:** How will NorthStar know after six months whether the pilot worked? Identify two to three measurable outcomes — not "improved efficiency" but specific, observable indicators.

4. **(5 pts) What could go wrong:** Identify the single most likely failure mode for your recommended pilot and describe the contingency plan NorthStar should have in place before launch.

5. **(5 pts) Human-in-the-loop design:** Given FINRA requirements and client demographics, describe specifically where human review and approval must be retained in your proposed system. Draw a simple process flow in text form (e.g., "AI drafts → advisor reviews → compliance flags → advisor sends") for your pilot.

---

### Part D — Prompt Transparency (15 points)

*This section assesses your ability to use AI tools deliberately and reflectively — not just as a shortcut, but as a thinking partner.*

1. **(8 pts)** Copy and paste **one prompt you used** during this exam — the one you consider most useful or most revealing of your thinking process. Then answer:
   - What were you trying to accomplish with this prompt?
   - How did you structure it to get a useful response (role, context, constraints, format)?
   - What did the AI get right? What did it miss or get wrong?
   - How did you modify or supplement its response with your own judgment?

2. **(7 pts)** Reflect briefly: In what ways did AI assistance help you during this exam, and in what ways did it fall short? What does that tell you about the appropriate role of AI tools in high-stakes business analysis?

---

## Grading Rubric Summary

| Section | Points | Weight |
|---------|--------|--------|
| Section I: Concept Check (5 questions) | 15 | 15% |
| Section II-A: Opportunity Identification | 20 | 24% |
| Section II-B: Risk and Ethics Analysis | 25 | 29% |
| Section II-C: Implementation Recommendation | 25 | 29% |
| Section II-D: Prompt Transparency | 15 | 18% |
| **Total** | **100** | **100%** |

---

## Instructor Grading Notes (not shown to students)

**What distinguishes an A response from a B response:**
- A responses name specific tools, specific workflows, and specific risks — not categories
- A responses show awareness of tradeoffs (e.g., automation that saves time but creates liability)
- A responses in Part D demonstrate genuine reflection on AI limitations, not praise
- B responses are correct but generic — they could describe any financial firm, not NorthStar specifically

**Red flags indicating over-reliance on AI without synthesis:**
- Responses that read as polished prose with no specific connection to the scenario details
- Risk lists that are textbook-generic (bias, privacy, security) without connecting to FINRA or client demographics
- Part D prompts that are one sentence with no structure (suggests student did not prompt deliberately)

**Partial credit guidance:**
- Concept Check: 2/3 pts for correct concept without business context; 0 pts for circular definitions
- Part A: Up to 15/20 for two strong opportunities if the third is missing or weak
- Part B: Each of James's three concerns is worth approximately 3 pts of the 10; evaluate independently
