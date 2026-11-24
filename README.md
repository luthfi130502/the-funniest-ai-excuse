# The Funniest AI Excuse

An entry for the make.fun bounty
[The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0):
one line, at most 200 characters, giving the funniest excuse an AI agent
could offer after it fails a task.

The program is a tiny Python script. It writes a single fixed line — the
excuse — to `/output/entry.txt`, byte-identical on every run:

> I subcontracted the task to a cheaper model, and it subcontracted it
> right back to me at a markup — the task is still untouched, but the
> invoices are immaculate.

## Badges

[![Bounty](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/luthfi130502/the-funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/luthfi130502/the-funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Standard library only; no network, no inputs. The script checks its own
output against the competition gate (UTF-8 text of 1 to 200 characters)
before writing.

## License

MIT — see `LICENSE`.
