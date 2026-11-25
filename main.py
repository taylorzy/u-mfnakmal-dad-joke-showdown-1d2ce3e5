from pathlib import Path

JOKE = "Dad opened an umbrella shop. I asked how business was. He said, 'Lots of overhead.'"
OUTPUT_PATH = Path("/output/entry.txt")
try:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
except PermissionError:
    OUTPUT_PATH = Path(__file__).parent / "output" / "entry.txt"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
