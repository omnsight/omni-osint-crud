import json
import sys
from pathlib import Path

# Ensure src is in python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from omni_osint_crud.main import app


def export_openapi():
    output_dir = Path(__file__).parent.parent / "doc"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "openapi.json"

    print(f"Exporting OpenAPI to {output_file}...")

    with open(output_file, "w") as f:
        json.dump(app.openapi(), f, indent=2)

    print("Done.")


if __name__ == "__main__":
    export_openapi()
