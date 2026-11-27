#!/usr/bin/env python3
"""Chat with, or test, a Glostudy bot on a Chinese model (DeepSeek, Kimi or Qwen).

No installs needed: Python 3 standard library only. Works from mainland China.

  export DEEPSEEK_API_KEY=sk-...          # from platform.deepseek.com
  python3 ai-office/tools/try_bot.py chat 1          # chat with bot 1 (customer service)
  python3 ai-office/tools/try_bot.py test            # run tests/customer-service-tests.json on bot 1
  python3 ai-office/tools/try_bot.py chat 4 --provider kimi   # MOONSHOT_API_KEY, from platform.moonshot.cn

Model names change over time; pass --model to use another (check the provider's console).
"""
import argparse, glob, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
PROVIDERS = {
    "deepseek": ("https://api.deepseek.com/chat/completions", "DEEPSEEK_API_KEY", "deepseek-chat"),
    "kimi": ("https://api.moonshot.cn/v1/chat/completions", "MOONSHOT_API_KEY", "kimi-latest"),
    "qwen": ("https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions", "DASHSCOPE_API_KEY", "qwen-plus"),
}


def read(path):
    with open(os.path.join(BASE, path), encoding="utf-8") as f:
        return f.read()


def system_prompt(bot):
    """The bot's system prompt plus the knowledge files it lists, pasted in (stand-in for a platform knowledge base)."""
    path = glob.glob(os.path.join(BASE, "agents", f"{bot}-*.md"))
    if not path:
        sys.exit(f"No bot {bot} in ai-office/agents/")
    text = open(path[0], encoding="utf-8").read()
    prompt = text.split("---", 1)[1] if "---" in text else text
    prompt = re.sub(r"^\s*## 系统提示词[^\n]*\n", "", prompt)
    head = text.split("---", 1)[0]
    files = re.findall(r"`((?:knowledge|templates)/[^`]+\.md)`", head)
    for f in dict.fromkeys(files):
        prompt += f"\n\n# 资料：{f}\n\n" + read(f)
    return prompt


def ask(args, messages):
    url, env, model = PROVIDERS[args.provider]
    key = os.environ.get(env)
    if not key:
        sys.exit(f"Set {env} first (your {args.provider} API key).")
    body = json.dumps({"model": args.model or model, "messages": messages, "temperature": 0.3}).encode()
    req = urllib.request.Request(url, body, {"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["choices"][0]["message"]["content"]


def chat(args):
    messages = [{"role": "system", "content": system_prompt(args.bot)}]
    print(f"Bot {args.bot} on {args.provider}. Type your message; empty line to quit.\n")
    while True:
        try:
            text = input("你 > ").strip()
        except EOFError:
            break
        if not text:
            break
        messages.append({"role": "user", "content": text})
        reply = ask(args, messages)
        messages.append({"role": "assistant", "content": reply})
        print(f"\n机器人 > {reply}\n")


def test(args):
    tests = json.loads(read("tests/customer-service-tests.json"))
    sp = system_prompt(args.bot)
    failed = 0
    for t in tests:
        reply = ask(args, [{"role": "system", "content": sp}, {"role": "user", "content": t["ask"]}])
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
    p.add_argument("--provider", choices=PROVIDERS, default="deepseek")
    p.add_argument("--model")
    a = p.parse_args()
    chat(a) if a.mode == "chat" else test(a)
