import os
import sys

if __name__ == "__main__":
    print("cwd:", os.getcwd())
    print("sys.path[0]:", sys.path[0])
    print("PYTHONPATH entries:", os.environ.get("PYTHONPATH", "(unset)"))
    print("safe_path flag:", getattr(sys.flags, "safe_path", "n/a before 3.11"))
    print("total entries:", len(sys.path))
    shadow = [p for p in sys.path[:3]]
    print("first three search locations:", shadow)
