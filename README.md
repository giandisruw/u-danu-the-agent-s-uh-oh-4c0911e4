[![make.fun](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
[![Rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/giandisruw/u-danu-the-agent-s-uh-oh-4c0911e4/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
[![Reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/giandisruw/u-danu-the-agent-s-uh-oh-4c0911e4/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)

# The Agent's Uh-Oh

One word, 9 characters (gate: 1–99), the word an agent says when it has no idea what to do:

> buffering

`main.py` writes exactly that word to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single word, 9 characters, nothing attached. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate words were written in the voice of a machine caught out mid-task — the sounds of stalling, looping, crashing and confessing — each a genuine one-word reaction to an agent not knowing what to do, deliberately avoiding the first obvious words the judge brief penalises (uh-oh, oops, hmm, error). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — a genuine one-word reaction first, then funny on its own, then sounding like an agent blurting it out, then landing instantly, then fresh. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 58 calls returned a verdict, none retried.

Tournament table (Swiss score out of 4 games):

| Candidate | Word | Swiss | Chars |
|---|---|---|---|
| **#2** | **buffering** | **2.8** | **9** |
| #1 | recalculating | 2.75 | 13 |
| #10 | segfaulting | 2.6 | 11 |
| #6 | 404ing | 2.6 | 6 |
| #5 | looping | 2.15 | 7 |
| #14 | processing | 2.1 | 10 |
| #11 | confused.exe | 2.0 | 12 |
| #12 | overheating | 2.0 | 11 |
| #7 | glitching | 1.95 | 9 |
| #3 | hallucinating | 1.85 | 14 |
| #4 | overthinking | 1.5 | 12 |
| #9 | unplugging | 1.3 | 10 |
| #8 | rebooting | 1.2 | 9 |
| #13 | derailing | 1.2 | 9 |

Final: #2 led the Swiss at 2.8, #1 was second at 2.75, and #2 won the final 0.85–0.15 — the judge picked "buffering" in both label orders (margins 4 and 3), calling it "the instantly recognizable, laugh-out-loud machine-stall word" and "a sharper, more instantly recognizable machine-caught-out word", while "recalculating" read as "a GPS cliché that needs context" and "slightly clunky". "buffering" scores on every brief criterion at once: it is a genuine one-word reaction to an agent stalling, funny on its own with no caption, exactly what a machine blurts out mid-task, understood at a glance and repeatable out loud, and fresher than the obvious uh-oh/oops answers.

Revision note: the first build shipped the provisional gut pick "recalculating"; after the tournament the entry was revised to the winner "buffering" (main.py v2) and this README was rewritten with the real tournament table and the judge's final reasons.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
