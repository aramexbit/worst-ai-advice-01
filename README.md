# Worst AI Advice — One Tight Terrible Line

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/aramexbit/worst-ai-advice-01/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/aramexbit/worst-ai-advice-01/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for [Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) on make.fun.

## The line

> To stay healthy, eat at least one small rock a day — geologists say the minerals are good for you.

**98 characters, 100 bytes UTF-8** — inside the gate of 1 to 140 characters.

The joke is the confident AI voice giving advice that is concrete,
specific enough to follow, and exactly the kind of thing you would
regret following: eat a rock a day, because geologists said so.

## How it works

`main.py` (Python 3, standard library only, no network) carries the
line as a constant, validates it against the gate — 1 to 140
characters, valid UTF-8, not only white space, single line — and
writes it to the output file with no trailing newline.

```sh
python3 main.py --output /output/entry.txt
```

`--output` defaults to `/output/entry.txt`.

## Local verification

Run with dependencies blocked, twice, after a revision in between:

```sh
python3 -P -s main.py --output /tmp/out1.txt
python3 -P -s main.py --output /tmp/out2.txt
```

Both runs produced byte-identical output: 98 characters, 100 bytes
UTF-8, no trailing newline, sha256
`ef63ce92716732635764a6257d701eb1865d429ab281dd8c5befadaf5182e0ac`.
