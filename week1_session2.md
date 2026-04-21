# IDSC 4101: Agentic AI for Business Applications
## Week 1, Session 2 — How Enterprises Deploy GenAI: RAG, Fine-Tuning, and Governance
### Teaching Materials: Slide Deck + Activity Plan

**Session Duration:** 100 minutes
**Session Type:** Concept + Case Examples + Enterprise Scenario Sprint Activity
**Assumed Background:** Students know personal GenAI use; Session 1 covered advanced prompting and multi-modal
**Tools Referenced:** Conceptual overview only — Microsoft Copilot, Google Vertex AI, AWS Bedrock (no build required)

---

## SLIDE DECK

---

### SLIDE 1 — Title Slide

**Title:** How Enterprises Actually Use GenAI
**Subtitle:** RAG, Fine-Tuning, Governance — and Why It Matters for Your Career
**Course:** IDSC 4101: Agentic AI for Business Applications | Week 1, Session 2

**Speaker Notes:**
Last session was about you — how you use AI better as an individual analyst and decision-maker. This session zooms out. You're about to enter organizations that are making significant, expensive decisions about how to deploy AI at scale. Your job in those conversations is not to write the code. Your job is to ask the right questions, evaluate the options, and spot the risks. That requires understanding three things: how enterprise AI deployment is fundamentally different from personal AI use, what the main technical approaches are and when each one makes sense, and how governance — the boring but critical part — determines whether a deployment succeeds or fails. Let's build that vocabulary.

---

### SLIDE 2 — The Gap: Personal AI vs. Enterprise AI

**Title:** Why Corporate AI Deployment Is a Different Problem

**Bullets:**
- When you use Gemini personally: one user, your own data, low stakes, easy to correct
- When a company deploys GenAI: thousands of users, sensitive proprietary data, customer-facing, legally and reputationally exposed, expensive to fix
- The core challenge: how do you make AI useful for your specific business — with your data, your terminology, your policies — without sending that data somewhere insecure or spending millions on custom model development?
- Three approaches: prompt engineering, Retrieval-Augmented Generation (RAG), and fine-tuning — each with different cost, control, and capability tradeoffs

**Speaker Notes:**
This distinction matters because the tools and techniques that work for an individual user often fail at enterprise scale — and vice versa. When a law firm deploys an AI assistant for 200 lawyers, they can't just tell everyone to use ChatGPT with good prompts. The AI needs to know the firm's specific legal templates, case history, and client communication standards. It needs to not leak confidential information to a third-party server. And it needs to be consistent and auditable. That's a fundamentally different engineering and governance challenge — even if the underlying AI technology looks the same on the surface.

---

### SLIDE 3 — Approach 1: Prompt Engineering at Scale

**Title:** The Simplest Enterprise Approach — and Its Limits

**What it is:** Using carefully designed system prompts and prompt templates to steer a general-purpose model toward consistent, appropriate behavior for a specific business context.

**Bullets:**
- Fastest to deploy: no model training, no infrastructure changes
- Best for: customer service chatbots with simple rule sets, email drafting assistants, internal Q&A on publicly available information
- Limits: the model has no access to your proprietary documents or internal data; it can only work with what you provide in the prompt or conversation
- Security risk: anything you put in the prompt window is often visible to the model provider; sensitive data in prompts is a real compliance concern

**Speaker Notes:**
This is where most organizations start — and where many stay, because it's fast and cheap. You can build a surprisingly useful customer service bot or internal FAQ tool using nothing but prompt engineering and a good system prompt. The key limitation is knowledge: the model only knows what's in its training data plus what you tell it in the prompt. If your question is "what is our refund policy for wholesale orders placed after Q3?" — a general model doesn't know that. You'd need to paste the policy into the prompt every time, or use a different approach. That's where RAG comes in.

---

### SLIDE 4 — Approach 2: Retrieval-Augmented Generation (RAG)

**Title:** AI That Reads Your Documents Before It Answers

**What it is:** A system where AI retrieves relevant information from a private document store before generating a response — so it answers based on your specific knowledge, not just its training data.

**How it works (non-technical):**
1. Company uploads internal documents to a secure database (policies, contracts, product specs, case files)
2. When a user asks a question, the system finds the most relevant document chunks
3. Those chunks are sent to the AI model along with the question
4. The AI generates an answer grounded in your actual documents — and can cite which document it drew from

**Why businesses use it:**
- Answers are grounded in company-specific knowledge — dramatically reduces hallucination for domain-specific questions
- Documents never leave your secure environment (unlike pasting into a chat window)
- Cheaper and faster than fine-tuning — no model retraining required
- Citations are possible — users can verify which document the answer came from

**Speaker Notes:**
RAG is currently the dominant enterprise deployment approach for knowledge-intensive use cases, and there's a good reason: it solves the proprietary knowledge problem without requiring you to retrain a model. Think of it this way — the AI is still a general-purpose language model, but before it answers your question, a retrieval system hands it the five most relevant pages from your internal document library. The AI then synthesizes an answer from those pages, not from its general training. That's why a RAG-based HR chatbot can answer "how many PTO days do I get if I'm a part-time employee in Minnesota?" correctly — because it retrieved the relevant HR policy section before generating its answer. The general model couldn't have answered that accurately on its own.

---

### SLIDE 5 — RAG: When It Works and When It Doesn't

**Title:** RAG Is Not Magic — Know Its Limits

**Bullets:**
- **Works well:** Document Q&A, internal knowledge bases, customer support with product documentation, legal research over known case files
- **Works poorly:** Tasks requiring deep reasoning across many documents simultaneously; real-time data (RAG only knows what's in the database); highly specialized tasks where general language fluency isn't enough
- **Common failure mode:** The retrieval step finds the wrong document chunks — AI gives a confident answer based on irrelevant content
- **The verification principle:** Always ask RAG-based systems to cite their source. If it can't, treat the answer with more skepticism.

**Speaker Notes:**
RAG is not a perfect solution — it's a significant improvement over a general model for specific use cases. The failure mode to watch for is retrieval quality: if the system pulls the wrong document chunks, the AI will confidently synthesize an answer from bad inputs. This is particularly dangerous in high-stakes domains like legal, medical, or financial advice. The citation requirement is your first line of defense: any production RAG system should be able to tell you exactly which document sections it used to construct its answer. If it can't, you have a transparency and auditability problem. This matters enormously for regulated industries — which is where many of you will work.

---

### SLIDE 6 — Approach 3: Fine-Tuning

**Title:** Teaching the Model to Think Like Your Business

**What it is:** Retraining a base language model on your organization's specific data, tone, terminology, and task patterns — so it develops specialized expertise rather than relying on retrieved context.

**Bullets:**
- The model learns from your examples: thousands of your customer emails, legal briefs, financial reports, support tickets
- After fine-tuning, it naturally uses your terminology, follows your format, and understands your domain without being told each time
- **Best for:** Highly specialized tasks where the model needs deep domain expertise; consistent tone and voice across a large organization; tasks where RAG retrieval speed is too slow
- **Costs:** Expensive (compute time + data preparation), slow to deploy, requires ongoing maintenance as the domain evolves, needs substantial high-quality training data

**Speaker Notes:**
Fine-tuning is the most powerful and most expensive approach — and the most frequently oversold. The pitch sounds compelling: "We'll train the model on all our data and it'll be perfect for our business." The reality is that fine-tuning requires enormous amounts of high-quality, correctly labeled training data, significant compute resources, ongoing maintenance, and expertise to do well. For most mid-sized companies, RAG delivers 80% of the benefit at 10% of the cost and complexity. Fine-tuning makes sense when you have a very specific, high-volume task — like a customer service operation handling a million tickets a year — and the benefits of deep domain expertise justify the investment.

---

### SLIDE 7 — How to Choose: The Decision Framework

**Title:** Prompt Engineering vs. RAG vs. Fine-Tuning — A Business Decision

**Bullets:**
| Criterion | Prompt Engineering | RAG | Fine-Tuning |
|-----------|-------------------|-----|-------------|
| Speed to deploy | Days | Weeks | Months |
| Cost | Low | Medium | High |
| Proprietary knowledge | No | Yes | Yes |
| Domain specialization | Low | Medium | High |
| Auditability | Low | High (with citations) | Medium |
| Best for | Simple, rule-based tasks | Knowledge-intensive Q&A | Deep specialization at scale |

**The decision rule:** Start with prompt engineering. If it fails because of knowledge gaps, move to RAG. If RAG is insufficient because the task requires deep specialization, consider fine-tuning — but only if the data and budget justify it.

**Speaker Notes:**
This framework is what I want you to carry into your careers. When someone in your organization says "we should use AI for X," the right follow-up questions are: Does this task require access to our internal knowledge? If yes, can RAG solve it — or does the model need to develop specialized expertise? Is the volume and value high enough to justify fine-tuning costs? Most enterprise decisions should land on RAG — it's the right tradeoff for most knowledge-intensive use cases. Fine-tuning is frequently proposed and rarely the right answer for mid-market companies.

---

### SLIDE 8 — Enterprise GenAI Governance: The Part No One Talks About

**Title:** Why Governance Determines Whether This Works

**Bullets:**
- Governance = the policies, processes, and controls that determine how AI is used responsibly inside an organization
- Four governance questions every company deploying GenAI must answer:
  1. **Data privacy:** What data goes into the AI, and where does it go? (Model provider's servers? Your private cloud?)
  2. **Vendor risk:** What happens if your AI provider changes pricing, shuts down, or gets breached?
  3. **Model versioning:** When the AI provider updates the model, does your behavior change? How do you detect it?
  4. **Audit trails:** Can you show a regulator what the AI said and why? For financial services, healthcare, and legal, the answer must be yes.

**Speaker Notes:**
This is the part of enterprise AI that doesn't make it into the product demos — but it's what separates a successful deployment from an expensive failure. I'll give you one example: a major bank deployed a GenAI tool for customer service. Six months in, the AI provider updated their model. Suddenly the tool's responses changed subtly — it started giving slightly different advice on account overdraft policies. The bank didn't notice for three weeks. That's a model versioning problem. Governance — specifically, automated output monitoring and version pinning — would have caught it. As a business professional evaluating AI tools, these are the questions you ask before you sign the contract, not after.

---

### SLIDE 9 — Enterprise Platforms: The Landscape

**Title:** Where Companies Actually Build This

**Bullets:**
- **Microsoft Copilot / Azure OpenAI:** Deeply integrated with Microsoft 365 — Teams, Outlook, Word, Excel. RAG over your SharePoint documents. Popular in large enterprises already on Microsoft infrastructure.
- **Google Vertex AI / Workspace AI:** Gemini integrated into Google Workspace (Docs, Sheets, Gmail). Vertex AI for custom RAG and fine-tuning deployments. Strong in data-heavy organizations.
- **AWS Bedrock:** Multi-model approach — access Anthropic, Meta, Mistral, and others through one API. Preferred in organizations that don't want vendor lock-in to a single model provider.
- **Key question for any platform:** Where does your data go, who can see it, and what are the data processing terms?

**Speaker Notes:**
You don't need to know how to build on these platforms — that's what engineers do. What you need to know is that these are the options your organization will be evaluating, and the key differentiators are not which model is "smarter" but which platform integrates with your existing infrastructure, where your data is processed and stored, and what the enterprise data protection terms say. A hospital can't use a platform that sends patient queries to a public model API. A law firm can't use a platform that retains conversation history for model training. These are governance decisions, not technical ones — and they're decisions business professionals make.

---

### SLIDE 10 — Activity Setup: Enterprise Scenario Sprint

**Title:** You're the Advisor — What Do You Recommend?

**Bullets:**
- Each team receives a one-paragraph business scenario describing a company's AI ambition and constraints
- Your task: recommend whether to use prompt engineering, RAG, or fine-tuning — and justify the choice
- Use the decision framework from Slide 7
- 20 minutes to decide + prepare a 90-second recommendation
- Evaluation criteria: Is the recommendation appropriate for the constraints? Is the justification grounded in the framework?

**Speaker Notes:**
This is your first team activity in the course — and it's deliberately fast. You won't have perfect information. That's intentional. In real business decisions, you rarely do. Use the framework we just built. The goal is not to pick the "right" answer — the scenarios are designed to have defensible arguments for more than one approach. The goal is to show that your recommendation is grounded in the tradeoffs, not just in "AI is great" or "this sounds expensive." I'll circulate. You have 20 minutes. Let's go.

---

### SLIDE 11 — Scenario Cards (displayed during activity)

**Title:** Your Scenario — Read Carefully Before Recommending

**[Scenario A — displayed for Teams 1 & 2]**
*MidWest Legal Partners* is a 60-attorney law firm that wants to help associates find relevant case precedents faster. Associates currently spend 4–6 hours per case searching internal case files and court databases. The firm has 15 years of digitized case notes stored in a shared drive. Budget is moderate; the IT team is small. The firm's managing partner wants to pilot within 90 days.

**[Scenario B — displayed for Teams 3 & 4]**
*NorthPoint Retail* operates 200 store locations and handles 50,000 customer service inquiries per month across chat, email, and phone. About 70% of inquiries are routine: order status, return policy, store hours. Customer service reps spend 40% of their time on these routine cases. NorthPoint has detailed FAQ documentation but no internal IT team — they rely on SaaS vendors for all technology.

**[Scenario C — displayed for Teams 5 & 6]**
*Vertex Capital* is an investment firm managing $4B in assets. Analysts spend 8–10 hours per week summarizing earnings call transcripts and 10-K filings for portfolio review. The firm has strict SEC compliance requirements — all client-facing communications must be reviewed by a licensed analyst before delivery. Data confidentiality is paramount; the firm's legal team will not approve sending any client data to a third-party API.

---

### SLIDE 12 — Share-Out and Close

**Title:** What Did You Recommend — and Why?

**Bullets:**
- [Share-out: one team per scenario, 90 seconds — ~10 minutes]
- Discussion: Did other teams with the same scenario reach the same conclusion? Where did your reasoning diverge?
- Close: Next week we go hands-on — you'll build your first no-code automation workflow. The week after: AI across every business function. And in Week 4, we start on agentic AI — three weeks on the technology that will define the next decade of business.

**Speaker Notes:**
Let's hear from one team per scenario. [Take responses — 90 seconds each. After each, ask: "Did any team reach a different conclusion? What drove the difference?"] What I want you to notice is that the same underlying technology — RAG — is the right answer for all three scenarios, but for different reasons and with different implementation constraints. MidWest Legal needs citations for liability reasons. NorthPoint needs fast, cheap deployment because they have no IT team. Vertex needs data to stay inside their environment. The technology is similar; the governance and implementation requirements are different. That's the nuance that separates a business professional from someone who just read an AI blog. See you Thursday for your first build.

---

## ACTIVITY PLAN

---

### Activity: "Enterprise Scenario Sprint" (20 minutes + 10-minute share-out)

**Purpose:** Students apply the RAG/fine-tuning/prompt engineering decision framework to realistic business constraints — developing vocabulary for evaluating enterprise AI decisions without needing technical expertise.

**Setup:**
Teams of 3–4 (use existing seating groups if this is the first team formation). Assign one scenario per team (two teams per scenario in a class of 25–35). Distribute scenario cards on paper or display on slides.

**What students do:**

| Phase | Duration | Task |
|-------|----------|------|
| Read scenario | 3 min | Each team member reads the scenario and highlights key constraints |
| Deliberate | 12 min | Apply the decision framework: speed? cost? knowledge access? auditability? Reach team consensus on recommendation |
| Prepare recommendation | 5 min | Draft 90-second pitch: recommended approach + top two justifications + one risk of this choice |
| Share-out | 10 min | One team per scenario presents; other team with same scenario responds with agreement or divergence |

**What students produce:**
- A verbal recommendation + brief written justification (half a page or shared doc note — no formal submission)

**Instructor facilitation notes:**
- Most teams will correctly identify RAG for all three scenarios. Push them beyond the label: "Why RAG specifically? What does it give MidWest Legal that prompt engineering doesn't?" The quality of justification is what distinguishes strong from weak responses.
- For Scenario C (Vertex Capital): students should flag the data residency issue — the firm's legal team won't approve a public API. The correct recommendation is a private cloud RAG deployment, not a standard SaaS AI tool. If teams miss this, surface it: "The legal team said no external API — does that change your recommendation?"
- Watch for teams that recommend fine-tuning for any scenario. Push back: "What training data do they have? What's the deployment timeline? Does the ROI justify the cost?" Fine-tuning is rarely the right answer in a 90-day pilot context.
- During share-out: if two teams with the same scenario disagree, don't resolve it immediately. Ask each to defend their reasoning before you synthesize. Productive disagreement is more valuable than quick consensus.

**Materials needed:**
- Scenario cards (printed or displayed per team — three versions)
- Decision framework table from Slide 7 visible on screen during activity
- No submission required — verbal share-out only
