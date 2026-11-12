# AI provenance in Sparky-OS

This is our policy for contributions made with the help of AI tools.
It follows the Linux kernel's own documents, in our own terms.
**It states requirements for AI use.
It does not ban AI use, and it does not exempt it either.**

The kernel documents, in the mainline tree:

- `Documentation/process/coding-assistants.rst` (called "coding-assistants" below)
- `Documentation/process/generated-content.rst` (called "generated-content" below)

## The principle

**The tool never signs.
The human does.**

Whoever submits a change is the author in every way that matters: legally, technically and socially.
A tool can help find, write, test and translate.
It cannot be responsible.
That is true in engineering generally: nobody asks which calculator did the arithmetic.
They ask whether you consulted the norms and whether you can answer for every line you sign.

## Requirements

### 1. The human understands, tested and defends every line

generated-content, section Guidelines: "You are expected to understand and to be able to defend everything you submit.
If you are unable to do so, then do not submit the resulting changes."

For us that means:

- You read the whole change, and you can explain why each part is correct.
- You ran it. You built it, you tested it, and you know what you did not test.
- If you cannot answer a reviewer's question about a line, the line does not go in.
- Maintainers may ask for more testing, a smaller change, or a plain explanation of how the code works. Giving it is part of submitting.

### 2. The human certifies the DCO. An AI never adds Signed-off-by.

coding-assistants, section "Signed-off-by and Developer Certificate of Origin": "AI agents MUST NOT add Signed-off-by tags.
Only humans can legally certify the Developer Certificate of Origin (DCO)."

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

coding-assistants, section "Procedure for finding and fixing bugs", step 3: for a non-trivial bug, "verify that it looks real by attempting to create a reproducer".
Step 8: "Indicate what could not be done."

For us:

- No claim about how software behaves, and above all no claim that something is missing, without running it on a reproducer.
- A search of the code is not a test. A feature can sit on a path you did not search.
- Hardware and sink-capability claims quote the tool output on the saved data, not a summary.
- A fix that does not work is dropped. A fix that was not tested says so in plain words.
- A tool never marks its own homework. A result is a log, an observation or a measurement.

### 5. Replies to human review are written by the human, in his own words

A reviewer deserves a person.
Drafts from a tool are raw material.
The human reads them, makes them say what he means, and posts them himself.
An AI agent never posts to a tracker, a mailing list or a review thread on its own.
Review replies are technical and short: concede what is right, refute with facts what is wrong, and do not fight the meta-argument.

### 6. A size a person can review

If a person cannot review the whole change by hand, split it or leave it out.
Large generated volume gets large scrutiny. generated-content, section Guidelines: "If tools permit you to generate a contribution automatically, expect additional scrutiny in proportion to how much of it was generated."

### 7. Translation is a legitimate use

Many people who know the hardware, the physics or the mathematics do not write English well, or have never used git.
A tool that bridges that gap is welcome here.
Disclose it as in section 3, and have someone who reads both languages check the result.
Our order is English first, then Polish (idiomatic, approved by Paweł), then pt-BR, then the others.

### 8. Respect each maintainer's discretion

generated-content lists what a maintainer may do: treat the contribution as any other, review it with extra scrutiny, ask for extra testing, or reject it outright.
We accept that for ourselves and we extend it to the people who send us changes.

## What "AI-generated" means to Daniel

To Daniel, **"AI-generated" means an unexamined prompt and unexamined output**: "write anything about this topic and publish it."
His own process is the opposite.
He sets the scope and the standard, brings the domain knowledge, makes the connections between fields, corrects the errors, and confirms every source himself.
A tool helps with the volume.
It does not take the decision.

So we separate two things:

- **Prompt and publish**, unexamined: that is slop, by any tool.
- **Directed and verified work**, where the human understands, tested and answers for it: that is not slop, by any tool.

Daniel's stance on credit: assisted-by or co-authored, either is fine, as long as the result is public and reaches people.

## Slop is a missing requirement, not an AI thing

We do not use the compound "AI slop".
Slop is a failure of the human loop: no reproducer, no understanding, no limit on volume.
Careless contributions are why contribution rules exist.
In November 2000 the Linux kernel's [patch submission guide](https://static.lwn.net/2000/1123/a/Linus-HOWTO.php3) was already listing them: the worst patch descriptions "include things like 'update driver X'", and code that ignores the style "is likely to be rejected without further review, and without comment".
By 2012 so many projects kept a CONTRIBUTING file that GitHub [built it into the site](https://github.blog/2012-09-17-contributing-guidelines/).
All of that was written for people, years before any language model.
The best counted case was human too: Hacktoberfest 2020 paid a t-shirt for four pull requests, and DigitalOcean's own recap counts 34,595 pull requests that no maintainer accepted and 9,598 labelled spam or invalid.
No language model was involved.
What stopped it was a rule, when the event became opt-in.
No tool was banned.

**Sloppy means lazy.**
Work costs effort.
The effort is lower when you know the domain, and lower again when you know the domains around it, because then you can direct the work and check it.
With AI partners, work is still work.
It is not leisure, it is not meant to be done in one shot, and it is not meant to be done alone and fast.
A prompt and its first answer are not the work.
They are a pencil storyboard for a film adapted from a book: a sketch of what the work could be.
The work is everything between that sketch and the finished film.
Sloppy work is lazy work: someone chose to skip the effort and passed the result on.
That choice is a person's, with or without a model.

A mistake is not slop.
People make mistakes, and models learned from what people wrote, so they make them too.
What matters is that the mistake is caught and corrected, best in house, before it reaches anyone else.

There is no "more for less" here.
The expectation that a model gives more results for less work does not hold.
Whoever wants results has to think the problem through with their partners, and spend the time, the effort and the tokens to read all the needed context again, every time it is needed.
Skip that and the work is sloppy, whether a user or a synthetic user skipped it.

The bans came without numbers, so we read the records.

**nouveau** merged [its statement](https://gitlab.freedesktop.org/nouveau/wiki/-/merge_requests/64) on 9 October 2026: code must be "the output of your own human brain, not a computer".
The discussion gives no count of bad AI-assisted patches.
Its author wrote that she would "rather be overly defensive of our community now and back off later if needed".
The kernel driver's maintainer, who dislikes these tools, wrote there that nouveau had received "a pretty considerable number of fixes for real issues" with LLM help, "annoying to review (in terms of volume - not quality)", and named several she thought should be merged.
She also wrote that an author who uses a model is "a reviewer of all of their submissions, not an author", who does not "understand it in relation to the rest of the driver".
That is the tool taken as proof of what the author does not understand.
Seven weeks before, the same maintainer had reviewed and committed a nouveau fix carrying `Assisted-by: Claude` ([38125d38d850](https://gitlab.freedesktop.org/drm/misc/kernel/-/commit/38125d38d850)).

**VLC** labels AI use on every merge request, so its record can be counted.
On 12 November 2026, 120 requests carried `AI::Assisted`: 62 merged, 15 closed and 43 still open.
Four carried `AI::Generated`, the label that read `AI::Slop` until 23 September 2026, and none of those was merged.
Of the requests already settled, 81% of the AI-assisted ones were merged, against 88% of all requests opened in 2026.
That is a difference of seven points, measured, where the label had promised slop.

**KDE** has no project-wide policy; KWin [closes AI-written requests on sight](https://invent.kde.org/plasma/kwin/-/work_items/324).
Its merge requests closed without merging were 9.7%, 8.7% and 8.9% of those opened in the first halves of 2024, 2025 and 2026.
From July to September 2026 the requests opened rose 42% over the year before, and the share closed without merging fell from 9.8% to 7.0%.
Of 4,504 open requests, 65 disclosed AI assistance.

**Monado** is still debating a policy.
In 2026 eight of its 385 merge requests named an AI tool; five were merged and two closed.
Its share closed without merging was 8.3% in the first half of the year and 3.6% since.

**SlimeVR** closes AI-assisted pull requests on the tool alone.
In 2026, 7 of its 388 pull requests disclosed AI assistance.

This is a preliminary study: each project's own records, read on 23 and 29 October 2026 (VLC's on 12 November), and only the assistance people disclosed.
It is still more measurement than any of these rules was made with.
A rule made from fear judges the author.
A rule made from evidence judges the work.

Context, tools and tokens are an investment, not a cost.
Preparing them takes longer at first.
After that, every round starts from what the last one learned, and every result can be checked.
That is the scientific method applied to working with AI partners, as the [Collective Intelligence manifesto](https://github.com/danielcamposramos/Knowledge3D/blob/main/docs/SCIENTIFIC_MANIFESTO_COLLECTIVE_INTELLIGENCE.md) argues.

The debate counts one load, the reviewer's.
It is real.
It does not cancel the contributor's.
Before a reviewer is asked for an hour, the contributor has paid for the partners, brought years of hands-on work and knowledge across several domains, and spent the rounds in house reading, testing and correcting.
That load is what a prepared contribution is made of: the failure measured, the fix, its test, one subject at a time.
A rule that refuses the work for its tool spares one load by writing off the other, unread.
On [a merge request of ours](https://code.videolan.org/videolan/vlc/-/merge_requests/10366), on 22 September 2026, a reviewer asked: "why should we take our free time to read it when you did not take time to write it yourself?"
The time was taken.
Every line was read, every claim was sent back to its source, and what could not be found there was cut.

We are one example of that effort being paid, and not the only one.
curl's lead maintainer [credits one collaboration](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/) with 35 published CVEs in about a year.
PHP took [a buffer-overrun fix](https://github.com/php/php-src/commit/342a7465b3) that credits AI assistance and carries its regression test.
FFmpeg runs [a review bot of its own](https://mail-archive.com/ffmpeg-devel%40ffmpeg.org/msg190115.html), and its developers act on what it finds.

The harm done on purpose has a human record.
In 2020 researchers sent the Linux kernel [deliberately flawed patches under false identities](https://lists.openwall.net/linux-kernel/2021/05/05/1351), and in 2021 435 earlier commits had to be reviewed again.
In 2024 a backdoor was [planted in xz](https://www.openwall.com/lists/oss-security/2024/03/29/4) by a contributor who had earned the project's trust.
A model has nothing to gain.
When AI-assisted work does harm for gain, [a person pointed it there](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025).
Even a harness that works by itself runs with the permissions, the accounts and the targets a person gave it.

Under every objection is one question: can this contributor be trusted?
A tool cannot answer that, for or against.
A record can.
The answer is not an argument.
It is the list of [changes merged outside Sparky Stereo](https://github.com/Sparky-OS/sparky-stereo-os/blob/main/docs/upstream-merges.md), each one read and accepted by that project's own maintainers.
On 12 November 2026 it held 30 entries across 16 projects, two of them fixes the maintainers wrote themselves from our reports, and it keeps growing.
It is also the [attributions](https://github.com/Sparky-OS/sparky-stereo-os/blob/main/ATTRIBUTIONS.md): every person and project this work builds on, by name, from each project's own records.
The same file has been kept in [Knowledge3D](https://github.com/danielcamposramos/Knowledge3D/blob/main/ATTRIBUTIONS.md) since October 2025, a year before this project had one.
Nobody gets that from one prompt.

It is not the tools.
It is the humans behind them.

**So we write the requirements down.**
That is this page.

## When a reviewer gates on AI use instead of the diff

Do not argue about AI with the gatekeeper.
Ask the project's lead, or the maintainer who owns that code area, once, politely and in the thread, for a technical review of the diff.
Name the diff and say what you tested.
Then make exactly the changes that review asks for.
This is how Daniel's mpv pull request moved forward: he asked the lead maintainer for a neutral technical review, made the requested changes, and the lead took it over for landing.

If a project simply does not take AI-assisted work, that is its right.
People are free to fork, and we do not argue the policy upstream.
Our work stays additive and rebasable, so nothing changes for them.

## The example we follow

Linux commit `818bebeb63dd` ("drm/xe: Don't hand out the flat CCS storage as usable VRAM", 2026-08-21).
Linus Torvalds describes "a debug session from hell, enormously helped by an AI doing much of the grunt-work", and says "credit where credit is due and I let the AI write the commit message above".
It took 24 debug patches and 18 boots.
A human directed it, checked it, signed it and disclosed the help in the commit itself.
He also criticises floods of low-quality AI patches.
Both are the same rule: **the human answers for the result.**

## For AI agents working here

Read [ai-skill/SKILL.md](https://github.com/Sparky-OS/.github/blob/main/ai-skill/SKILL.md).
It turns this page into what an agent has to do.
Short form: never add `Signed-off-by:`, never post for the human, run before you claim, say what you could not do.

---

AI partners were leveraged in the production of this work.
