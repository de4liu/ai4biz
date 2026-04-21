# IDSC 4101: Agentic AI for Business Applications
## Week 3, Session 2 — AI in Operations, Finance, and HR + Capstone Team Formation
### Teaching Materials: Slide Deck + Activity Plan

**Session Duration:** 100 minutes
**Session Type:** Concept delivery (35 min) + Discussion (15 min) + Capstone team formation activity (40 min) + Debrief and close (10 min)
**Assumed Background:** Session 1 complete — students have practiced the ideation framework and can articulate AI opportunities with a value claim and risk assessment
**Tools Referenced:** SAP (operations AI), Workday AI, Blue Prism/UiPath (RPA), Gong, Salesforce Einstein — conceptual overview only

---

## SLIDE DECK

---

### SLIDE 1 — Title Slide

**Title:** AI Across the Organization — Operations, Finance, and HR
**Subtitle:** Where the Back Office Becomes the Competitive Advantage
**Course:** IDSC 4101: Agentic AI for Business Applications | Week 3, Session 2

**Speaker Notes:**
In Session 1 we focused on the customer-facing functions — marketing, sales, and customer experience — where AI is most visible and has the most public-facing examples. Today we go into the engine room: operations, finance, and HR. These functions are less glamorous but often represent the larger AI opportunity. Why? Because they involve enormous volumes of structured data, highly repetitive decision-making, and processes where errors have direct financial consequences. And critically: these are functions where the cost of human time is high and the tolerance for AI assistance is growing faster than most people realize. By the end of today's concept session you'll have a working mental model of AI's role in all six of the core business functions we've covered across Sessions 1 and 2. That foundation goes directly into your capstone team formation, which is the second half of today.

---

### SLIDE 2 — AI in Operations: The Invisible Engine

**Title:** Operations AI Is Already Running — Most Customers Just Don't See It

**Bullets:**
- Operations sits at the intersection of supply, demand, logistics, and quality — all data-rich, time-sensitive, and consequential
- **Demand forecasting:** AI analyzes historical sales, weather, local events, and macroeconomic signals to predict demand more accurately than statistical models alone. Excess inventory and stockouts are both expensive — AI reduces both.
- **Logistics optimization:** AI routes shipments dynamically based on real-time traffic, weather, carrier capacity, and cost — reducing delivery time and fuel cost simultaneously
- **Quality control and anomaly detection:** AI analyzes images or sensor data from a production line and flags defective units faster and more consistently than human inspectors
- **Supplier communication and procurement:** AI drafts RFQ responses, monitors supplier compliance, flags contract deviations, and summarizes supplier performance data for procurement reviews

**Speaker Notes:**
Operations is where AI has had the longest history — many of the optimization models embedded in supply chain software have used machine learning for over a decade. What is new is the accessibility: previously, deploying demand forecasting AI required a data science team and months of model development. Today, platforms like SAP, Oracle, and Microsoft Dynamics have AI forecasting built in — operations managers configure it rather than build it. The business case is also among the clearest: a 5% improvement in demand forecasting accuracy in a $500M company with 20% inventory costs can translate to millions in freed working capital. Operations is where AI stops being a "nice to have" and becomes a bottom-line argument.

---

### SLIDE 3 — Operations AI in Practice: Two Business Cases

**Title:** What Operations AI Looks Like When It Works

**Case 1 — Demand Forecasting at a Retail Chain:**
- Problem: A regional grocery chain was over-ordering perishables by an average of 12%, driving $3.2M per year in waste
- AI approach: integrated weather data, local event calendars, and promotional history into their existing inventory system using a third-party AI module
- Result: Forecast error dropped 34% in the first quarter; waste reduced by $1.1M annualized; implementation took 6 weeks with no custom code
- Key lesson: AI improved a decision that was already being made — it did not replace the process, it upgraded the inputs

**Case 2 — Quality Control in Manufacturing:**
- Problem: A mid-sized electronics manufacturer had a 2.3% defect escape rate — units leaving QC that customers later returned
- AI approach: Computer vision system deployed on existing production line cameras. AI trained on images of defective units; flags anomalies in real time.
- Result: Defect escape rate dropped to 0.4% in 90 days; customer returns down 65%; human inspectors redeployed to exception handling and root cause analysis
- Key lesson: AI did not eliminate QC jobs — it changed their content from inspection to investigation

**Speaker Notes:**
Both of these cases share a pattern worth naming: AI was not the first thing implemented. In both cases, there was already a process — humans were already forecasting demand, humans were already doing quality control. AI improved an existing decision-making process by providing better data, better pattern recognition, or both. This is almost always the right framing for operations AI: not "AI instead of process," but "AI-upgraded process." The job change in Case 2 is worth dwelling on — human inspectors moved from standing at a line looking for defects to investigating why defects were occurring and fixing root causes. That is a higher-value, higher-skill job. It's also a harder job to do well. Change management and reskilling are as important as the AI deployment itself.

---

### SLIDE 4 — AI in Finance: From Reporting to Intelligence

**Title:** Finance Is Moving from Backward-Looking to Forward-Looking — AI Makes That Possible

**Bullets:**
- **Financial report summarization:** AI reads 10-Ks, earnings transcripts, and audit reports, extracts key figures, flags material changes, and produces a structured briefing — in minutes instead of hours
- **Anomaly detection in transactions:** AI flags unusual patterns in financial data — expense reports that exceed norms, transactions with unfamiliar vendors, revenue recognition patterns that diverge from historical precedent — for compliance and fraud detection
- **Automated client briefings:** In wealth management and investment banking, AI synthesizes portfolio performance, market conditions, and client-specific holdings into a personalized briefing draft — reviewed and finalized by the advisor
- **Regulatory document review:** AI reads regulatory filings, vendor contracts, and compliance documents and flags clauses that require legal review — reducing the time an attorney or compliance officer spends on first-pass reading
- **FP&A assistance:** AI models multiple financial scenarios simultaneously — what happens to margin if commodity costs rise 10%? — helping finance teams run analyses that previously took days in hours

**Speaker Notes:**
Finance is a function where the accuracy bar for AI output is extremely high, which creates a particular design challenge. A hallucinated figure in a marketing brief is embarrassing. A hallucinated figure in a financial report filed with the SEC is a material misstatement. This means finance AI almost universally operates with a mandatory human review step before any output becomes authoritative. The appropriate AI role in most finance contexts today is: accelerate the first-pass analysis, generate the structured summary, flag the anomalies — so that the human can spend their time on the judgment call rather than the data extraction. That's the augmentation model. The autonomous finance agent — one that approves a transaction or files a report without human sign-off — remains a high-bar, high-scrutiny deployment that requires explicit regulatory consideration. We'll come back to this in the Week 6 governance session.

---

### SLIDE 5 — Finance AI: The Audit and Compliance Opportunity

**Title:** Where Finance AI Is Moving Fastest — Compliance and Risk

**Bullets:**
- Compliance and audit are ideal AI territory: massive document volume, well-defined rules, high cost of human expert time, and low tolerance for missed issues
- **Contract analysis:** AI reads vendor, customer, and employment contracts, extracts key terms (payment terms, termination clauses, liability caps), and flags items that deviate from standard templates
- **Expense audit:** AI reviews expense submissions against policy, flags exceptions, categorizes spending, and routes for approval — eliminating most of the routine human audit work
- **Tax document processing:** AI extracts relevant figures from tax documents, cross-references them with prior-year filings, and flags discrepancies for CPA review
- **Real-time risk monitoring:** AI watches financial feeds and internal transaction data for signals that indicate elevated risk — currency exposure, counterparty concentration, covenant approach — and alerts finance teams before they become surprises

**Discussion question:** Where is the line between AI "flagging an issue for human review" and AI "making a compliance decision"? Who is responsible when an AI-flagged issue turns out to be a false positive — and the human dismissed it?

**Speaker Notes:**
The discussion question is deliberately provocative and it's worth three to four minutes of class time. The liability question — who is accountable when an AI system is in the decision loop — is one of the most important unresolved questions in enterprise AI right now. The answer in most organizations today is: the human who reviewed and approved the AI's output is accountable. But that puts enormous pressure on the human review step to be substantive rather than perfunctory. If the AI flags 200 items a day and the compliance officer rubber-stamps them because they trust the AI and don't have time to investigate each one, the accountability structure has collapsed in practice even if it's intact on paper. This is a governance design problem, not just a technology problem — and it's exactly the kind of thinking this course is trying to develop.

---

### SLIDE 6 — AI in HR: The People Function Gets Personal

**Title:** HR Handles the Most Human Problems in the Organization — AI Handles the Volume

**Bullets:**
- **Job description drafting:** AI generates first-draft JDs based on role parameters — title, level, team, key responsibilities — dramatically reducing the time an HRBP spends on posting new roles. Also useful for bias detection: AI can flag gendered or exclusionary language before the JD is published.
- **Resume screening augmentation:** AI pre-ranks applicants based on structured criteria — skills match, experience level, education — to reduce the first-pass screening burden. Critical caveat: AI resume screening has a documented history of replicating historical bias. Human oversight and regular auditing are mandatory, not optional.
- **Onboarding content generation:** AI creates role-specific onboarding materials — first-30-days plans, FAQ documents, benefit summaries, team intro templates — customized for the individual's role, location, and start date
- **Employee sentiment monitoring:** AI analyzes patterns in employee survey data, support ticket topics, and (where consented) communication patterns to surface early signals of disengagement or team friction
- **Learning and development personalization:** AI recommends training paths based on role, career goals, and skill gaps — making L&D less generic and more relevant to the individual

**Speaker Notes:**
HR AI is where the responsible AI conversation gets the most personal, literally. When AI is involved in hiring decisions, performance assessments, or monitoring employee sentiment, the ethical stakes are immediate and high. I want to flag the resume screening example specifically: there are well-documented cases of AI hiring tools trained on historical applicant data that learned to penalize candidates whose resumes contained signals associated with underrepresented groups — not because the AI was programmed to discriminate, but because historical hiring data reflected historical bias. The AI learned the pattern that was in the data. Amazon famously scrapped an AI recruiting tool in 2018 for exactly this reason. The lesson for this course: AI in HR is a high-leverage, high-risk application area. The ideation opportunity is real — but the responsible design requirements are more stringent here than almost anywhere else in the organization.

---

### SLIDE 7 — AI as a Force Multiplier: The Cross-Functional Theme

**Title:** AI Doesn't Replace Teams — It Changes What Teams Are For

**Bullets:**
- The pattern across all six functions: AI handles the high-volume, rule-based, data-heavy work — humans handle the judgment-intensive, relationship-driven, consequence-bearing work
- This is not headcount replacement — it is role transformation. The marketing team of 10 becomes a team of 6 who do what the team of 10 used to do, plus more strategic work that wasn't possible before.
- The organizations that get the most value from AI are not the ones that cut the most people — they're the ones that redeploy freed human capacity toward higher-value work
- Implication for you: your value as a future business leader is not in doing the high-volume work faster. It's in making the judgment calls, managing the AI systems, and deciding where the AI should and shouldn't be trusted.
- The fluency advantage: professionals who can evaluate AI outputs critically, spot failure modes, and design guardrails will outcompete those who only use AI as a productivity tool

**Speaker Notes:**
This is the "so what does this mean for me" slide and I want to make sure it lands clearly. Some students in this room are worried about AI replacing their future jobs. That is a legitimate concern — but it is not the right frame for building a career strategy. The right frame is: in five years, every business team will be AI-augmented. The question is whether you're the one who knows how to design and manage those augmented workflows, or the one who just uses the tool because your employer installed it. This course is training you to be the former. You will leave knowing how to identify AI opportunities, evaluate AI tools critically, design guardrails and escalation logic, and make responsible deployment decisions. Those are leadership-level skills, not user-level skills.

---

### SLIDE 8 — Capstone: What You're Building

**Title:** The Capstone Project — From Ideation to Pitch

**Overview:**
- **Teams:** 3–4 students, explicitly cross-major. Every team must have students from at least two different business concentrations.
- **Sector:** Each team is assigned (or selects) a sector — retail, healthcare, financial services, logistics/supply chain, hospitality, or a sector requested by the team (instructor approval required)
- **Deliverable:** An 8-minute pitch + 4-minute Q&A in Week 7, Session 2. No working prototype required — this is an ideation and strategy pitch, not a demo.
- **What a strong pitch includes:** A real business problem in the sector → an agentic AI solution design → the AI workflow (what the agent does, what tools it uses, where humans stay in the loop) → responsible AI analysis (bias, security, privacy, governance) → the business case (value created, cost or risk avoided)
- **The rubric:** Problem clarity (20%) | Solution design and workflow logic (30%) | Responsible AI analysis (25%) | Business case and pitch quality (25%)

**Speaker Notes:**
The capstone is the course's signature assignment. Everything from Week 3 forward is designed to build toward it: the functional AI knowledge from today, the agent design in Weeks 4–5, the responsible AI analysis in Week 6, and the strategy thinking in Week 7. Teams should leave today's session with a rough sector interest, an initial list of potential problem areas, and a clear sense of who is on their team. The cross-major requirement is deliberate: the best AI ideation happens when someone who understands the business problem works alongside someone who thinks about process design and someone who thinks about customer experience. Don't let students form teams with everyone from the same concentration — enforce this actively during formation.

---

### SLIDE 9 — Capstone: Sector Options and Selection

**Title:** Choose Your Sector — Where Does the AI Opportunity Interest You Most?

**Available Sectors:**

| Sector | Sample AI Problem Areas |
|--------|------------------------|
| Retail | Personalized recommendations, inventory optimization, returns fraud detection |
| Healthcare | Patient intake automation, prior authorization, clinical documentation |
| Financial Services | Fraud detection, loan processing, wealth management personalization |
| Logistics / Supply Chain | Route optimization, demand sensing, supplier risk monitoring |
| Hospitality / Travel | Dynamic pricing, guest experience personalization, staff scheduling |
| Open Sector | Propose a sector with a clear AI problem (instructor approval required) |

**Selection process:**
- Teams self-select sector preference today
- Instructor confirms and resolves conflicts (first-come-first-served, with limits on popular sectors)
- No more than two teams per sector

**Speaker Notes:**
The sector list is designed to cover the range of business concentrations in the room. Students in finance will naturally gravitate toward financial services; operations students toward logistics; marketing students toward retail or hospitality. That's fine — but the team composition requirement means a finance student's capstone team still needs to include someone from a different concentration who challenges their framing. Open sector is available for teams with a genuine passion for a sector not listed — a student who has worked in healthcare or has family in logistics often produces the most credible pitches because they bring domain knowledge that the course can't replicate. Encourage it where genuine, but require a brief one-paragraph proposal before approving.

---

### SLIDE 10 — Capstone Team Formation: Ground Rules

**Title:** Team Formation Rules — Non-Negotiable

**Rules:**
1. **Cross-major required:** Every team must include students from at least two different declared concentrations (accounting, finance, marketing, management, supply chain, MIS/IDSC, etc.). Teams that are concentration-homogeneous will be reassigned by the instructor.
2. **Size:** 3–4 students per team. No teams of 2. No teams of 5.
3. **Commitment:** Once teams are confirmed at the end of today's session, they are locked. Changes require instructor approval with a written explanation.
4. **Contribution equality:** Each team member must be able to explain every part of the final pitch. Capstone Q&A questions will be directed to individual team members at the instructor's discretion.
5. **Sector assignment:** Finalized today. If two teams want the same sector, the team that submitted their composition to the instructor first gets priority.

**Why cross-major?**
AI solutions fail in business not because the AI is bad — they fail because the team building the solution didn't understand the problem well enough, the workflow context, and the human factors involved. A team with diverse business knowledge builds better solutions. That is not a pedagogical preference — it is what practitioner research consistently shows.

**Speaker Notes:**
Be clear and firm on the cross-major rule. Students often want to work with their friends, who are typically in the same concentration. That's understandable — but it produces worse pitches and worse learning. The most common capstone failure mode is a team that designs a technically interesting AI solution for a problem that doesn't actually exist in the sector the way they described it. Cross-major teams catch this earlier because they bring more diverse domain knowledge. A finance student who has done an internship in a bank will tell the marketing student "actually, the compliance process doesn't work the way you're describing" — and the pitch gets better. That friction is the point.

---

### SLIDE 11 — Team Formation Activity: What to Do Right Now

**Title:** 40 Minutes — Form Your Team and Start the Problem Discovery

**Phase 1 — Open networking (10 minutes):**
- Stand up. Find two or three people from different concentrations who you want to work with.
- Confirm your concentrations are different before you commit.
- If you don't know someone's concentration — ask.
- Instructor announces: "If you're still looking for a team at the 8-minute mark, come to the front — I will help you form a team."

**Phase 2 — Team registration (5 minutes):**
- Every team: record team members + concentrations + first and second sector preference on the team registration form (paper distributed in class or Google Form link on Canvas)
- Submit to instructor — sector assignment confirmed on the spot where possible

**Phase 3 — Sector brainstorm (25 minutes):**
- Teams meet together for the first time. Assign a note-taker.
- Task: Generate a list of 3–5 specific AI problem areas in your assigned sector.
- For each problem: one sentence on what the AI would need to do, and one sentence on what value it would create.
- At the end: agree on your top 1–2 problems to investigate before Week 4.

**Deliverable from today:** A completed team registration form and a brief brainstorm document (can be a shared Google Doc) listing 3–5 problem areas. No submission required — just have it ready when you leave.

**Speaker Notes:**
Circulate actively during all three phases. Phase 1 is the hardest for introverted students — watch for students standing alone at the 5-minute mark and facilitate introductions. Phase 2 is administrative but important — get the forms in hand so you can resolve sector conflicts before the next class. Phase 3 is where the real work starts: listen to the brainstorms. Common early problems are scope (teams that pick a problem too big — "AI will transform all of healthcare" — or too small — "AI will help my uncle's restaurant make better reservations"). Intervene early on both ends. The sweet spot is a problem that is specific enough to design an AI solution for, but significant enough that a business would actually invest in solving it.

---

### SLIDE 12 — What Makes a Strong Capstone Problem?

**Title:** The Three Filters for a Good Capstone Problem

**Filter 1 — Specificity:**
Not: "AI can help retailers with inventory"
Yes: "An agentic AI system that monitors real-time point-of-sale data and supplier lead times, and automatically generates reorder recommendations with a human approval step — reducing stockouts by 20% without increasing safety stock"

**Filter 2 — Significance:**
Would a real business with this problem spend meaningful money and time to solve it? If the problem costs the business nothing to have and causes no customer pain, it's not a strong capstone problem.

**Filter 3 — Designability:**
Can you design an agentic AI solution with specific tools, a clear human-in-the-loop moment, and a responsible AI analysis — without writing code? If the solution is too vague to design at that level of specificity, the problem needs to be narrowed.

**The test:** Write your problem in one sentence. If a VP in that sector read your sentence and said "yes, this actually costs us time and money," you have a real problem. If they said "I'm not sure what you mean," you need to be more specific.

**Speaker Notes:**
The one-sentence test is useful — write it on the board and make teams try it before they leave. "An agentic AI system that [does what specifically] for a [type of business] in the [sector], enabling [business outcome] by [mechanism]." If a team can fill in all those blanks with specific, non-generic language, they have a strong capstone problem. If they're still using words like "optimize," "improve," or "streamline" without explaining how — they need to go narrower. A common example of a problem that fails filter 3: "AI that transforms the patient experience in healthcare." That's a vision statement, not a design problem. A problem that passes all three: "An AI intake agent that collects patient symptom history and insurance information before a primary care appointment, reduces average intake time from 22 minutes to 4 minutes, and flags potential contraindications for the physician to review before entering the exam room." That's specific, significant, and designable.

---

### SLIDE 13 — Assignments, Deadlines, and Looking Ahead

**Title:** What's Due and What's Coming

**Bullets:**
- **Before Week 4, Session 1:** Reflection Post 3 (200–300 words on Canvas) — one functional AI application, the highest-value use case, and the most significant risk to manage before deployment
- **Before Week 4, Session 1:** Team composition confirmed via registration form + sector assigned by instructor
- **Ongoing from Week 4:** Capstone teams should begin researching their sector problem in parallel with course content — Weeks 4–6 directly apply to capstone design
- **Week 4:** The shift to agentic AI — what agents are, how they reason, and what makes them different from everything we've studied so far. This is the transition point of the course.
- **Midterm exam (take-home, open-book, HonorLock, individual):** Released after Week 4, Session 2, due before Week 5, Session 1. Covers GenAI foundations through agentic AI basics.

**Speaker Notes:**
A note on the capstone timeline: teams sometimes wait until Week 7 to start seriously working on the pitch. That is too late. The teams that produce the strongest pitches spend Weeks 4–6 actively applying the agentic AI content to their specific sector problem — sketching agent designs as we learn agent design, running failure mode analysis as we learn about failure modes, doing the responsible AI analysis in real time as we cover governance. The course content is scaffolded to support the capstone. Use that scaffolding. Come to Week 4 already knowing your sector problem well enough to think about agent design. The goal for the next two weeks: know your problem so well that when we cover agentic AI design, you're immediately thinking about how it applies to your capstone.

---

### SLIDE 14 — Week 3 Synthesis: What You Now Know

**Title:** From Six Functions to One Framework

**Bullets:**
- You can now look at any of the six core business functions and apply the four-question ideation test (frequency, standardizability, live data, error cost)
- You understand that AI's dominant role across functions today is augmentation — accelerating and improving human decision-making, not replacing it
- You can distinguish between the AI automation opportunity (routine, rule-based, data-heavy tasks) and the AI-augmented judgment opportunity (complex decisions where AI provides inputs but humans own the outcome)
- You understand that responsible AI design is function-specific: the guardrails for a marketing content generator are different from the guardrails for an HR screening tool
- You have a capstone team, a sector, and a starting list of problem areas — you are ready for Week 4

**Speaker Notes:**
Close the loop explicitly. Week 1 was about understanding GenAI deeply — beyond the basics. Week 2 was about building with GenAI — connecting it to workflows and automations. Week 3 was about seeing where AI fits across the business landscape — and starting to think like an AI strategist, not just an AI user. Week 4 is the pivot: we move from generative AI that produces outputs when asked, to agentic AI that plans, acts, and loops. Everything you've learned in Weeks 1–3 is the foundation for what comes next. The agent sessions are harder conceptually — but you're ready for them. See you next week.

---

## ACTIVITY PLAN

---

### Activity: Capstone Team Formation and Sector Problem Brainstorm

**Purpose:** Students form cross-major teams of 3–4, select a sector, and complete their first structured brainstorm of the AI problem space within that sector. This activity transitions the course from individual skill-building to team-based project work and directly scaffolds the capstone pitch in Week 7.

**Duration:** 40 minutes
- Open networking: 10 minutes
- Team registration: 5 minutes
- Sector brainstorm: 25 minutes

**Materials:**
- Team registration form (paper or Google Form — pre-loaded on Canvas before class)
- Sector options slide (Slide 9) on screen throughout the activity
- Problem brainstorm template (optional — simple shared Google Doc structure)

**Brainstorm template structure (for team's shared doc):**
```
Team: [Names and concentrations]
Sector: [Assigned sector]
Problem 1: [One sentence — what the AI does + what value it creates]
Problem 2: ...
Problem 3: ...
Top choice: [Which problem do we most want to pursue and why?]
Open questions: [What do we need to learn about this sector to develop this further?]
```

**Facilitation notes:**

*Phase 1 — Open networking (10 minutes):*
Announce the rules before releasing students to network: cross-major required, 3–4 members, no concentration-homogeneous teams. Walk the room during networking. Identify students who seem isolated at the 5-minute mark and facilitate introductions. Have a list of concentration distributions for the class handy — if you know the room is 40% finance, watch for clumping. At the 8-minute mark, call any remaining unplaced students to the front and help them form a team from the remaining individuals.

*Phase 2 — Team registration (5 minutes):*
Collect forms quickly. Resolve sector conflicts on the spot — first registered gets first choice. Announce final sector assignments before Phase 3 begins. If more than two teams want the same sector, offer the waitlisted team the Open Sector option and encourage them to propose a variant of their preferred sector that doesn't overlap directly with the assigned teams.

*Phase 3 — Sector brainstorm (25 minutes):*
Teams work independently. Circulate continuously. The first 5–10 minutes are often slow — teams get to know each other before working. That's okay. By minute 15, every team should have at least 2 problem areas articulated at the sentence level. By minute 20, push teams toward narrowing: "Which of these is most specific? Which one would a VP in that sector definitely spend money on?" At minute 23, give a 2-minute warning — teams should have their top choice identified.

*Common issues and instructor responses:*

| Issue | Response |
|-------|----------|
| Team is all from one major | Separate and reassign members from different teams; explain the rule was announced at the start |
| Team picks a problem that is too broad | "Write it in one sentence. If you can't, it's too broad." Offer the specificity scaffold from Slide 12. |
| Team can't agree on a sector | Give them 2 minutes to each make a case, then flip a coin or have instructor decide — the sector matters less than the team dynamic at this stage |
| Team picks a sector they know nothing about | Valid — they'll research. But push them to identify one person who has any relevant exposure (internship, family connection, personal interest) to anchor the research |
| Student is still alone at 10-minute mark | Instructor forms the last team manually from remaining individuals — do not let students fall through the cracks |

**Instructor follow-up before Week 4:**
- Send confirmation emails to each team: confirmed team roster, confirmed sector, capstone rubric, and one suggested resource to begin sector research (e.g., McKinsey, Gartner, or Deloitte report on AI in their sector — instructor-curated)
- Post capstone rubric to Canvas before Week 4 begins
- Note any team composition concerns (teams that have conflict in the brainstorm phase often need early mediation — flag and monitor)

**Connection to capstone rubric:**
The problem statement that teams articulate today should evolve — but the core problem should not flip entirely between now and Week 7. If a team's problem changes dramatically between Week 3 and Week 6, that is a signal that they haven't committed to understanding their sector deeply. Instability in the problem statement often predicts a weak final pitch. Monitor team evolution across Weeks 4–6 and intervene if teams are drifting without a good reason.
