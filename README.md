[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/giandisruw/u-suzy-one-line-office-joke-laugh-off-f574ac73/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/giandisruw/u-suzy-one-line-office-joke-laugh-off-f574ac73/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

# One-Line Office Joke Laugh-Off

One line, 86 characters (limit 200), about office life:

> The intern fixed the bug in five minutes, so we promoted the bug to senior management.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 86 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written around universal office moments — the raise that becomes a pizza party, the out-of-office, the water-cooler chatbot, the boss who calls the team a family, focus time booked over by others, the intern and the bug, headphones as a do-not-disturb sign, the HR wellness webinar, the dead desk plant, the accidental reply-all, the lift, IT support, the suggestion box — each a real joke with a setup and a turn, punchline last, deliberately avoiding the plain-complaint form the judge brief penalises. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim. Swiss format, 3 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 22 games, 44 judge calls in total, all recorded in `tournament.jsonl` — every call returned a verdict, none needed a re-ask, no 429. Astra is down and Verboo's trial is exhausted (2026-11-24), so Caffeine judged alone.

Tournament table (Swiss score out of 3 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#7** | Intern fixed the bug in five minutes; we promoted the bug to senior management | **2.45** |
| #5 | Boss said we're a family; I asked for my inheritance and got a performance review | 2.10 |
| #6 | Blocked focus time; three people booked it to discuss my focus time | 2.05 |
| #1 | Asked for a raise, got a pizza party; now I expense my dignity by the slice | 1.80 |
| #11 | Cc'd the whole company by mistake; my apology got more replies than my work | 1.75 |
| #13 | Asked IT for a faster laptop; got a lecture on patience at dial-up speed | 1.55 |
| #12 | Lift only stops where someone important waits, which explains my career | 1.50 |
| #3 | Water cooler replaced with a chatbot; gossip never so well documented | 1.45 |
| #8 | Wore headphones to look busy; now the office's leading expert on silence | 1.40 |
| #14 | Suggestion box is now a shredder with a lid; morale efficiently filed away | 1.30 |
| #10 | Desk plant died of neglect; we held a retrospective and watered the action items | 1.20 |
| #4 | Brought my own mug to save the planet; office charges rent for the desk it sits on | 1.00 |
| #9 | HR wellness webinar: breathe deeply, preferably during meetings I wasn't invited to | 0.90 |
| #2 | Out-of-office says I'm unreachable — the most honest thing I've written all year | 0.55 |

Final: #7 led the Swiss at 2.45, #5 was second at 2.10, and #7 won the final 0.90–0.10 — the judge preferred #7's double turn (the intern succeeds instantly, then the bug itself gets promoted) over #5's family/inheritance punchline, which it read as a good but more familiar setup. #7 scores on every brief criterion at once: a real one-line joke with a setup and two turns, built on the bug-fix everyone in an office knows, a surprise ending the reader does not see coming, every word earning its place inside 86 characters, and a fresh angle rather than a stated cliche.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Verified deterministic: two runs produce byte-identical output, sha256 `824ef2ae9ce165922efa6373e985e97c4e5aabba24fd5fbb65141745956efc16` (86 bytes, one line, no trailing newline).

## Referral

Made with make.fun — referral code `0txwmf1m`.
