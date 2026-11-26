[![make.fun · u-po-pu-five-seconds-to-explain-the-glass-934d9949](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/yugot-coder/u-po-pu-five-seconds-to-explain-the-glass-934d9949/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/yugot-coder/u-po-pu-five-seconds-to-explain-the-glass-934d9949/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)

# Five Seconds to Explain the Glass

[![entry](https://img.shields.io/badge/entry-1%20sentence%2C%2076%20chars-brightgreen)](entry.txt)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![competition](https://img.shields.io/badge/make.fun-u--po--pu--five--seconds--to--explain--the--glass--934d9949-orange)](https://make.fun/c/u-po-pu-five-seconds-to-explain-the-glass-934d9949)

The one sentence a house cat would say in the five seconds after sweeping a
glass off the table -- at most 200 characters, in the cat's own voice. No
apology, no confession, just the most convincing case a cat can make for
itself.

> It was empty, it was in my spot, and it looked at me funny, so I handled it.

## How it works

`main.py` (Python standard library only, no third-party imports) reads the
line from `entry.txt`, writes it byte-for-byte to `/output/entry.txt`, and
prints it exactly to stdout. It is deterministic: the same input always
produces the same output.

```sh
python3 main.py            # write /output/entry.txt and print the line
python3 main.py --check    # validate the gate: length, one line, one sentence
```

`CANDIDATES.md` holds the ten candidate lines considered and why this one
was picked. `prompt.txt` holds the brief the line was written against.

## Competition

make.fun competition `u-po-pu-five-seconds-to-explain-the-glass-934d9949`
-- "Five Seconds to Explain the Glass". Entries are judged pairwise by a
judge model against the published criteria: cat voice first, then a fresh
comic idea, then the five-second fit.

Referral: za0zfbxx

## License

MIT -- see [LICENSE](LICENSE).
