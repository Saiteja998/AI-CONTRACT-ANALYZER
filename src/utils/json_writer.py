import json
from pathlib import Path


def save_json(result: dict, filename: str):

    output_dir = Path("data/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / filename

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print(f"\nResult saved to: {output_file}")