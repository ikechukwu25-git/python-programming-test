"""Run every program in folder order (interactive prompts are skipped)."""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).parent
failed = 0
for folder in sorted(p for p in root.iterdir() if p.is_dir() and p.name[:2].isdigit()):
    for script in sorted(folder.glob("*.py")):
        result = subprocess.run([sys.executable, str(script)], stdin=subprocess.DEVNULL,
                                capture_output=True, text=True)
        status = "PASS" if result.returncode == 0 else "FAIL"
        failed += result.returncode != 0
        print(f"[{status}] {folder.name}/{script.name}")
        if result.returncode:
            print(result.stderr)
print("\nAll programs ran successfully." if not failed else f"\n{failed} program(s) failed.")
