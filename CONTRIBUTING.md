# Contributing to Sparky-OS

Thank you for helping.
Sparky-OS holds the editions of SparkyLinux made by Daniel Ramos with Paweł "pavroo" Pijanowski: **Sparky Stereo OS 9 "Mashtabba"** and the business editions.
This page is the default for every repository in the organisation.
A repository can add its own rules in its own `CONTRIBUTING.md`, and those win for that repository.

**The short version: run it, measure it, say only what you measured, and be ready to defend every line you send.**

## Issues

- One problem per issue.
- Say what happens, why you think it is wrong, what you measured, and what you propose. Then stop.
- Put long logs and evidence in attachments, not in the body.
- Tell us your Sparky edition, kernel, desktop, and the hardware involved.
- Mark what you did not test as untested. A stated gap is cheap. A discovered one is expensive.
- Search first, but remember that a search is not proof. Never write "X does not support Y" because you could not find it. Fetch the code and run it first.

## Pull requests

- Small enough that a person can review it by hand. Several small pull requests beat one large one.
- Explain the problem and the **value**: the measured failure the change prevents, with the log or the observation. Do not shrink a real fix into "cleanup" or "compliance only".
- List how you tested it, on what, and what you could not test.
- Keep unrelated changes out. Do not reformat files you do not need to touch.
- Respond to review in your own words. See [AI-PROVENANCE.md](https://github.com/Sparky-OS/.github/blob/main/AI-PROVENANCE.md).
- A maintainer may ask for changes, extra tests or a smaller scope. That is normal and not a judgement of you.

## Testing before filing

- **Measured facts only.** A result exists when a log shows it, a person saw it, or a measurement recorded it. "It should work" is a prediction.
- Run the software on a reproducer before you claim anything about it. A throwaway container is cheap.
- For hardware claims, quote the tool output, for example `edid-decode` of the saved EDID bytes, not a summary of it.
- Check content, not status codes. A blocked page can answer HTTP 200 with a denial body.
- Test on hardware you own and are allowed to risk. Prefer a machine or a VM you can restore.
- Build against the real target (the kernel's own compiler and headers, a matching Debian testing container). Do not change a host system to make a build pass.

## The spec is the authority

For hardware and format work (HDMI, CTA, EDID, colour depth, stereoscopic packing, kernel and driver interfaces), **the specification decides, not our own hardware.**
Follow what the standard defines and what the sink declares, and do not cap the support at what your own devices happen to do.
Measurements on your own hardware stay labelled as measurements of that hardware.
Quote the clause, or leave the claim out.

## Packages and tools: Paweł's formula

Sparky tools are plain scripts with an `install.sh`, a `CHANGELOG` and a `copyright` file, packaged by hand.
Our packages follow his way first.
The full formula lives in the packaging skill described in [ai-skill/SKILL.md](https://github.com/Sparky-OS/.github/blob/main/ai-skill/SKILL.md). The essentials:

- **Layout of a tool repository:** `bin/`, `lang/`, `share/`, `install.sh` (with `uninstall`), `CHANGELOG`, `copyright`, `LICENSE` (GPLv3), `README.md` in his template. The folder name is the package name, with the `sparky-` prefix for ecosystem tools.
- **Control fields, in this order:** `Package`, `Version`, `Architecture`, `Maintainer`, `Installed-Size`, `Depends`, then `Recommends` / `Suggests` / `Conflicts` / `Replaces` if needed, `Section`, `Priority`, `Homepage`, `Description`.
- **Field style:** `Section` is a capitalised word such as `System` or `Utilities`. `Priority: optional`. `Architecture: all` for scripts. `Depends` in alphabetical order, with versions only when needed. `Description` is a short title line, then the body indented by two spaces. `Homepage: https://sparkylinux.org` without a trailing slash.
- **Versions:** small tools `0.MINOR.PATCH`, raised by one per change. Packages tied to the Sparky generation `YYYYMMDD~sparky9~0`, and `YYYYMMDD.1~sparky9~0` for a second build on the same day. Meta packages use the date alone. A rebuilt upstream package keeps the upstream version plus our suffix.
- **CHANGELOG:** newest first. A rule line of 79 dashes, then `  Version X (YYYY-MM-DD)`, the rule line again, then `  * ` bullets that are short, capitalised and have no full stop.
- **Commit message in a tool repository = the new version string**, for example `0.1.3` or `20261015~sparky9~0`. One commit per release: the CHANGELOG entry and the changed files together. Where the project's convention asks for a trailer, it goes after the version line (see [AI-PROVENANCE.md](https://github.com/Sparky-OS/.github/blob/main/AI-PROVENANCE.md)).
- **Strings and translations:** one sourced file per language under `lang/`, as `LOCAL1..n` variables, picked from the whole `LANG=xx_YY` value (not a substring match).
- **Privilege:** `remsu` plus one polkit policy per tool. Dialogs with `yad`. A root check at the top of scripts.

## Provenance and credits

- **Maintainer:** every package of ours names its real maintainer in `Maintainer:`. Packages made by Paweł keep his `Maintainer:` and are never modified in place. Ship ours beside them, use `dpkg-divert`, or send him a pull request.
- Where we modified someone else's package, their maintainer stays as `Original-Maintainer:` and their copyright file stays, with our credit appended in its own `Files:` block.
- Script headers keep the credit chain: the original author first, then ours, with dates.
- The product credit reads: "Sparky Stereo OS, an edition of SparkyLinux, created by Paweł "pavroo" Pijanowski and Daniel Ramos (Capitain Jack)".
- State one licence version consistently in a copyright file. Do not copy an inconsistency from an older file.
- **Never put another person's email address or contact details in a public file.** Names, handles and public profile links are fine. Mailing list archive links stay as citations.
- Never commit credentials, tokens, keys or passwords. When you inspect a configuration, extract host names only. Never print a credential file.
- Nothing enters a repository that we cannot redistribute: vendor firmware, vendor manuals and recovered bundles stay out.

## Translations

- **The order is English first, then Polish, then Brazilian Portuguese (pt-BR), then the others.** English is the reference text. Polish is Paweł's language, so it must be excellent and idiomatic, and he reviews it.
- Put each language in its own `lang/` file in the tool's existing format.
- A translation pull request changes the translation only. Credit the translator in the `copyright` file, in a `Files:` block for that language file.
- Translation with the help of a tool is a legitimate use. Say so once, as described in [AI-PROVENANCE.md](https://github.com/Sparky-OS/.github/blob/main/AI-PROVENANCE.md), and have a person who reads the language check it. For Polish that person is a fluent speaker, and Paweł approves it.

## Respect for SparkyLinux upstream

Sparky-OS is a guest in Paweł's house.

- **Send fixes to Paweł's repositories first** (the `sparkylinux` organisation), as a pull request in his style: small, one change, clear.
- Our forks carry only what upstream does not take, and they stay rebasable. We rebase onto upstream and do not diverge for taste.
- Never reuse his repository keys, suite names or branding for ours. Our repository has its own names and its own signing key.
- Release texts follow his tone: factual, plain, short sentences, no hype.
- Our editions are shipped "as is", built on Debian testing like most derivatives, with no paid support.

## Licence

By contributing you agree that your contribution is released under the licence of the repository you contribute to, and that you have the right to do so.
Sparky-OS repositories don't require a `Signed-off-by:` line, as Paweł's don't. Where a repository asks for one (the kernel and other projects with a Developer Certificate of Origin), **you** add it, and by doing so you certify the Developer Certificate of Origin (https://developercertificate.org/).
A tool never adds it for you.
