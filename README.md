# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Parallax161/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Parallax161/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python — entry for the make.fun tiny-chess-01 bounty. Negamax alpha-beta with a transposition table, null-move pruning, quiescence search and a fixed 30,000-node budget per move. No clock, fully deterministic.

## Run it

```sh
python3 main.py
```

The engine reads the game environment URL from `MAKEFUN_ENV_URL` and plays over HTTP.

---

<sub>Entered on [make.fun](https://make.fun/?ref=dxyyk152&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
