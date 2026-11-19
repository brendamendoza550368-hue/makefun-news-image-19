# makefun-news-image-19

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/brendamendoza550368-hue/makefun-news-image-19/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/brendamendoza550368-hue/makefun-news-image-19/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

## The day in one picture

Thursday 19 November 2026, folded into six panels under a single date line:

- **Shenzhen summit.** Donald Trump, Xi Jinping and Vladimir Putin sat down together for the first three-way meeting of its kind, talking Ukraine, Iran and nuclear risk, and left with a joint statement.
- **GTA VI day.** After thirteen years of waiting, the game launched worldwide at midnight local time, topped Metacritic at 99 and became the most pre-ordered release in history.
- **Iran warning.** Trump threatened to "wipe out" Iran if a dirty bomb were used, while missile fire crossed the Gulf and a tower in Riyadh was hit.
- **Myanmar ruling.** The International Court of Justice found Myanmar responsible for state-sponsored genocide against the Rohingya, a first for the court.
- **Crimea Bridge.** Russia said Ukraine struck the bridge for the third time in a week, with a span down and smoke over the strait.
- **Arctic pact.** Denmark's parliament voted 109-0 to back the Greenland security agreement with the United States.

## How the entry works

`main.py` copies `entry.png` into the folder named by `MAKEFUN_OUTPUT_DIR` (default `/output`) and checks the copy against the original with a SHA-256 digest, so the bytes the judge opens are exactly the bytes committed here.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
