#!/usr/bin/env python3
"""UK version: chat with, or test, a Glostudy bot on Claude.

Uses the same bot designs, knowledge and tests as try_bot.py (the China version on DeepSeek / Kimi / Qwen),
so one set of instructions drives both. Claude works in the UK but not in mainland China.

  pip install anthropic
  export ANTHROPIC_API_KEY=sk-ant-...      # from console.anthropic.com
  python3 ai-office/tools/try_bot_claude.py chat 1     # chat with bot 1 (customer service)
  python3 ai-office/tools/try_bot_claude.py test       # run tests/customer-service-tests.json on bot 1
  python3 ai-office/tools/try_bot_claude.py chat 4 --model claude-haiku-5-5   # cheaper model
"""
import argparse, json, os, sys

import anthropic

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from try_bot import read, system_prompt  # same prompts and knowledge as the China version

# Customer chat needs quick, short replies; the internal bots do more careful work.
EFFORT = {"1": "low", "2": "medium", "3": "medium", "4": "medium"}


def ask(client, args, system, messages):
    """One Claude turn. Returns (reply text, content blocks to append to the history)."""
    response = client.beta.messages.create(
        model=args.model,
        max_tokens=16000,
        system=system,
        messages=messages,
        cache_control={"type": "ephemeral"},  # the long prompt + knowledge is cached after the first turn
        output_config={"effort": EFFORT.get(args.bot, "medium")},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # if Claude declines a request, the API retries it on a fallback model
    )
    if response.stop_reason == "refusal":
        return "[Claude declined to answer this. Hand the conversation to a person.]", None
    text = "".join(b.text for b in response.content if b.type == "text")
    return text, response.content


def chat(client, args):
    system, messages = system_prompt(args.bot), []
    print(f"Bot {args.bot} on {args.model}. Type your message; empty line to quit.\n")
    while True:
        try:
            text = input("You > ").strip()
        except EOFError:
            break
        if not text:
            break
        messages.append({"role": "user", "content": text})
        reply, content = ask(client, args, system, messages)
        if content is None:
            messages.pop()  # drop the declined turn so the chat can go on
        else:
            messages.append({"role": "assistant", "content": content})  # keep all blocks, not just the text
        print(f"\nBot > {reply}\n")


def test(client, args):
    tests = json.loads(read("tests/customer-service-tests.json"))
    system, failed = system_prompt(args.bot), 0
    for t in tests:
        reply, _ = ask(client, args, system, [{"role": "user", "content": t["ask"]}])
        problems = [f"contains '{w}'" for w in t.get("must_not", []) if w in reply]
        problems += [f"missing '{w}'" for w in t.get("must", []) if w not in reply]
        failed += bool(problems)
        print(f"{'FAIL' if problems else 'ok  '} [{t['id']}] {t['ask']}")
        print(f"     expected: {t['expect']}")
        if problems:
            print(f"     problems: {', '.join(problems)}")
        print("     reply: " + reply.replace("\n", "\n            ") + "\n")
    print(f"{len(tests) - failed}/{len(tests)} passed the automatic checks. Read every reply too: the checks only catch obvious mistakes.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("mode", choices=["chat", "test"])
    p.add_argument("bot", nargs="?", default="1", help="1 customer service, 2 school research, 3 documents, 4 marketing")
    p.add_argument("--model", default="claude-opus-5-5")
    a = p.parse_args()
    c = anthropic.Anthropic()
    chat(c, a) if a.mode == "chat" else test(c, a)
