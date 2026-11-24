import os

SENTENCE = "A Wi-Fi router on tiny legs that follows you from room to room so the signal never dies the moment you settle on the sofa with your laptop and a deadline."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
