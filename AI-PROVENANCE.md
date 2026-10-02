# AI provenance in Sparky-OS

This is our policy for contributions made with the help of AI tools.
It follows the Linux kernel's own documents, in our own terms.
**It states requirements for AI use. It does not ban AI use, and it does not exempt it either.**

The kernel documents, in the mainline tree:

- `Documentation/process/coding-assistants.rst` (called "coding-assistants" below)
- `Documentation/process/generated-content.rst` (called "generated-content" below)

## The principle

**The tool never signs. The human does.**

Whoever submits a change is the author in every way that matters: legally, technically and socially.
A tool can help find, write, test and translate. It cannot be responsible.
That is true in engineering generally: nobody asks which calculator did the arithmetic. They ask whether you consulted the norms and whether you can answer for every line you sign.

## Requirements

### 1. The human understands, tested and defends every line

generated-content, section Guidelines: "You are expected to understand and to be able to defend everything you submit. If you are unable to do so, then do not submit the resulting changes."

For us that means:

- You read the whole change, and you can explain why each part is correct.
- You ran it. You built it, you tested it, and you know what you did not test.
- If you cannot answer a reviewer's question about a line, the line does not go in.
- Maintainers may ask for more testing, a smaller change, or a plain explanation of how the code works. Giving it is part of submitting.

### 2. The human certifies the DCO. An AI never adds Signed-off-by.

coding-assistants, section "Signed-off-by and Developer Certificate of Origin": "AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the Developer Certificate of Origin (DCO)."

- Where a repository uses `Signed-off-by:`, the human adds his own, after reviewing the change.
- An agent working in a repository never writes that line, for anyone.
- By signing, the human takes full responsibility for the licence compliance and the content.

### 3. Disclose once, where the format asks

coding-assistants, section Attribution: contributions "should include an Assisted-by tag", in the form `Assisted-by: LLM [TOOL1] [TOOL2]`, listing specialised tools such as `coccinelle` or `sparse` and not basic ones such as git, gcc or editors.

Our rules:

- **Kernel and kernel-style repositories:** `Assisted-by:` trailers in the commit, as the kernel asks.
- **Repositories where `Co-Authored-By:` is the convention:** use that trailer, with the model's name.
- **Everywhere else:** one plain line at the end of the description, in the project's own place. For example: "AI partners were leveraged in the production of this work."
- **Say it once.** Not in the commit, again in the description, and again in the first comment. The same statement repeated reads as spam to maintainers and to filters, and it weakens the disclosure instead of strengthening it. Comments and follow-ups carry only new content.
- If a project has its own AI policy, read it first and follow it. If it asks for no mention, honour that, and tell the maintainers when they ask.
- Never tick a box that says "not AI-generated" if tools wrote meaningful parts.

generated-content, section "In Scope", also lists the tool uses to disclose: new functions written by a chatbot, files generated and cleaned up by hand, changelogs written by a tool, and **a changelog "translated from another language"**.
It lists as out of scope: spelling and grammar fixes, completion of trivial boilerplate, purely mechanical renames and reformatting.
We follow the same line, and the same advice: "If in doubt, choose transparency".

### 4. Verified by running, before any claim

coding-assistants, section "Procedure for finding and fixing bugs", step 3: for a non-trivial bug, "verify that it looks real by attempting to create a reproducer". Step 8: "Indicate what could not be done."

For us:

- No claim about how software behaves, and above all no claim that something is missing, without running it on a reproducer.
- A search of the code is not a test. A feature can sit on a path you did not search.
- Hardware and sink-capability claims quote the tool output on the saved data, not a summary.
- A fix that does not work is dropped. A fix that was not tested says so in plain words.
- A tool never marks its own homework. A result is a log, an observation or a measurement.

### 5. Replies to human review are written by the human, in his own words

A reviewer deserves a person.
Drafts from a tool are raw material. The human reads them, makes them say what he means, and posts them himself.
An AI agent never posts to a tracker, a mailing list or a review thread on its own.
Review replies are technical and short: concede what is right, refute with facts what is wrong, and do not fight the meta-argument.

### 6. A size a person can review

If a person cannot review the whole change by hand, split it or leave it out.
Large generated volume gets large scrutiny. generated-content, section Guidelines: "If tools permit you to generate a contribution automatically, expect additional scrutiny in proportion to how much of it was generated."

### 7. Translation is a legitimate use

Many people who know the hardware, the physics or the mathematics do not write English well, or have never used git.
A tool that bridges that gap is welcome here.
Disclose it as in section 3, and have someone who reads both languages check the result. Our order is English first, then Polish (idiomatic, approved by Paweł), then pt-BR, then the others.

### 8. Respect each maintainer's discretion

generated-content lists what a maintainer may do: treat the contribution as any other, review it with extra scrutiny, ask for extra testing, or reject it outright.
We accept that for ourselves and we extend it to the people who send us changes.

## What "AI-generated" means to Daniel

To Daniel, **"AI-generated" means an unexamined prompt and unexamined output**: "write anything about this topic and publish it."
His own process is the opposite.
He sets the scope and the standard, brings the domain knowledge, makes the connections between fields, corrects the errors, and confirms every source himself.
A tool helps with the volume. It does not take the decision.

So we separate two things:

- **Prompt and publish**, unexamined: that is slop, by any tool.
- **Directed and verified work**, where the human understands, tested and answers for it: that is not slop, by any tool.

Daniel's stance on credit: assisted-by or co-authored, either is fine, as long as the result is public and reaches people.

## Slop is a missing requirement, not an AI thing

We do not use the compound "AI slop". Slop is a failure of the human loop: no reproducer, no understanding, no limit on volume.
The largest slop event in open source history was human: Hacktoberfest 2020 paid a t-shirt for four pull requests, and DigitalOcean's own recap counts 34,595 pull requests that no maintainer accepted and 9,598 labelled spam or invalid. No language model was involved.
What stopped it was a rule, when the event became opt-in. No tool was banned.
**So we write the requirements down.** That is this page.

## When a reviewer gates on AI use instead of the diff

Do not argue about AI with the gatekeeper.
Ask the project's lead, or the maintainer who owns that code area, once, politely and in the thread, for a technical review of the diff.
Name the diff and say what you tested.
Then make exactly the changes that review asks for.
This is how Daniel's mpv pull request moved forward: he asked the lead maintainer for a neutral technical review, made the requested changes, and the lead took it over for landing.

If a project simply does not take AI-assisted work, that is its right. People are free to fork, and we do not argue the policy upstream. Our work stays additive and rebasable, so nothing changes for them.

## The example we follow

Linux commit `818bebeb63dd` ("drm/xe: Don't hand out the flat CCS storage as usable VRAM", 2026-08-21). Linus Torvalds describes "a debug session from hell, enormously helped by an AI doing much of the grunt-work", and says "credit where credit is due and I let the AI write the commit message above".
It took 24 debug patches and 18 boots. A human directed it, checked it, signed it and disclosed the help in the commit itself.
He also criticises floods of low-quality AI patches. Both are the same rule: **the human answers for the result.**

## For AI agents working here

Read [ai-skill/SKILL.md](https://github.com/Sparky-OS/.github/blob/main/ai-skill/SKILL.md). It turns this page into what an agent has to do.
Short form: never add `Signed-off-by:`, never post for the human, run before you claim, say what you could not do.

---

AI partners were leveraged in the production of this work.
