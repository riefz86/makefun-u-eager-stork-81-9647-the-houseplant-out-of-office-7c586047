"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt. The fern was last watered in March, is still alive,
and is still judging you, so your "urgent" email can wait.
"""

import os

LINE = "Auto-reply: last watered in March, still alive, still judging you. Your 'urgent' email can wait. — Fern"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
