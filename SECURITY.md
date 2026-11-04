# Security policy

This page is the default for every repository in the Sparky-OS organisation.
A repository can add its own `SECURITY.md`, and that one wins for that repository.

## What is covered

The code and packages we write: Sparky Stereo OS 9 "Mashtabba", its build tree, its libraries and its tools.
Only the latest commit of a repository's default branch and the packages published from it are supported.

A fork of another project carries that project's code.
A flaw in the project's own code belongs to the project: report it there, following its rules, and tell us the link so we can carry the fix.
A flaw that only our changes introduce, or only our build carries, is ours: report it here.

## How to report a vulnerability

Report it privately.
Please do not open a public issue or pull request for it.

1. Open the repository on GitHub, choose the Security tab, then "Report a vulnerability".
2. If that button is not offered, open an issue that says only that you have a security report for this repository, with no details.
   We will answer there and arrange a private way to receive it.

## What a report carries

A report that a maintainer can act on the same day carries:

- what fails and where (file, function, version or commit);
- the steps to reproduce it, with the smallest case that shows it;
- the fix, as a patch against the current default branch, and the test that fails before the fix and passes after it;
- anything you did not verify, marked as not verified.

State facts and leave the severity to us.
Only the people who run the code know how it is deployed and what an attacker would need.

If an AI tool found the problem or wrote the patch, say so, and confirm that a person reproduced the failure and read every line.
[AI-PROVENANCE.md](https://github.com/Sparky-OS/.github/blob/main/AI-PROVENANCE.md) explains how we treat AI-assisted work.
We do not turn away a verified report because of the tool behind it.
We do turn away an unverified one, and a batch of findings sent at once is read one finding at a time.

## What happens next

We acknowledge a report, say whether we can reproduce it, and keep the reporter informed.
We publish the fix before we publish the details, and we credit the reporter by the name they choose.

## Sources

The guidance above follows OpenSSF's [Securing Open Source in the Age of AI: A Practical Guide](https://openssf.org/resources/securing-open-source-in-the-age-of-ai-a-practical-guide/) (Chris Aniszczyk, Christopher "CRob" Robinson and David A. Wheeler, May 2026): the Maintainers Guide, "Security Policy" and "Reporting Guidelines", and the Researchers' Guide.
