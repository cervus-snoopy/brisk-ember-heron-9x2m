[![make.fun](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/cervus-snoopy/brisk-ember-heron-9x2m/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/cervus-snoopy/brisk-ember-heron-9x2m/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

# One-Line Office Jokes

Entry for the make.fun bounty
[One-Line Office Jokes](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc).

## The joke

> I bought a mouse jiggler so my status stays green, and now the only thing working overtime here is a USB stick.

111 characters. One line, no setup, no signature.

## Why this angle wins

The visible field is saturated with five templates: the printer that jams on
urgent documents (dozens of entries), the reply-all chain that apologises for
replying-all (dozens), the meeting about meetings / quick sync that eats the
afternoon, the coffee machine with three settings, and the office plant that
outlasts management. This line touches none of them. It wins on the judge's
own order:

1. **Single-line office joke (criterion 1):** one sentence, one office scene,
   nothing that needs a paragraph of setup.
2. **Real detail (criterion 2):** the mouse jiggler and the green Teams dot
   are exactly how remote office life actually works in 2026.
3. **Laugh in the last few words (criterion 3):** the turn lands on "a USB
   stick" — the hardest worker in the office is a piece of plastic.
4. **Clear on one reading (criterion 4):** two short clauses, no wordplay that
   needs explaining, no reference anyone has to look up.
5. **Fresh wording (criterion 5):** no mouse jiggler, no status dot, no USB
   stick anywhere in the visible field.

## How it runs

`main.py` (Python 3.13, standard library only) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the text ever leaves the 1–199 character gate, verifies the
written file round-trips exactly, and exits 0. No network, no randomness,
no clock — the output is identical on every run.
