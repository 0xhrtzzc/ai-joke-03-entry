# ai-joke-03 entry

A program that writes one one-liner about AI coding agents to `/output/entry.txt`.
`main.py` is the entrypoint (Python 3.13, standard library only, no network):
the joke is a fixed string, so two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py && cat out/entry.txt
```
