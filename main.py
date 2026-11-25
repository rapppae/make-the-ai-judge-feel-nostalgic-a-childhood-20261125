"""Entry for make.fun bounty "Make the AI Judge Feel Nostalgic: A Childhood Memory".

Entry text (169 characters, limit: at most 280 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "In Grandma’s kitchen the rice steamed, rain drummed the tin roof, and I sat by the window listening for the vendor’s bell, sure the whole world was waiting just outside."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
