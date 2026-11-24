import os

PART_A = "A Wi-Fi router on tiny legs that follows you from room to room so the signal never dies the moment "
PART_B = "you settle on the sofa with your laptop and a deadline."

SENTENCE = PART_A + PART_B

assert "\n" not in SENTENCE and len(SENTENCE) == 154

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
