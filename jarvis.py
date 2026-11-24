import os, json, urllib.request

API_KEY = os.environ["ANTHROPIC_API_KEY"]

def ask(history):
    data = json.dumps({
        "model": "claude-sonnet-5-5",
        "max_tokens": 500,
        "system": "You are JARVIS, a helpful assistant. Keep answers short.",
        "messages": history,
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        headers={
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)["content"][0]["text"]

history = []
print("JARVIS ready. Type quit to stop.")
while True:
    text = input("You: ")
    if text.lower() == "quit":
        break
    history.append({"role": "user", "content": text})
    reply = ask(history)
    history.append({"role": "assistant", "content": reply})
    print("JARVIS:", reply)
  
