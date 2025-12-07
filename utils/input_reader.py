import inspect
import os
import sys

# Ensure repo root is in path for imports
_repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)

def read_puzzle_input(year=2024):
    """
    Read puzzle input file.
    
    Args:
        year: Optional year (e.g., 2024). If not provided, will be detected from directory structure.
              Can also be specified via CLI argument: --year YYYY or -y YYYY
    
    Returns:
        List of lines from the input file
    """
    # Check for sample flag
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        file = "sample"
        arg_offset = 1
    else:
        file = "input"
        arg_offset = 0
    
    # Check for year in CLI arguments
    if year is None:
        for i, arg in enumerate(sys.argv[1 + arg_offset:], start=1 + arg_offset):
            if arg in ("--year", "-y") and i + 1 < len(sys.argv):
                year = int(sys.argv[i + 1])
                break
    
    caller_frame = inspect.stack()[1]
    caller_path = os.path.dirname(caller_frame.filename)

    # Get the day folder name (e.g., "day01")
    folder_name = os.path.basename(caller_path)
    day_num = "".join(filter(str.isdigit, folder_name))

    if not day_num:
        raise ValueError(f"No numeric identifier found in folder name: {folder_name}")

    # Get the year folder name (e.g., "2024")
    if year is None:
        parent_path = os.path.dirname(caller_path)
        parent_name = os.path.basename(parent_path)
        # Check if parent is a year folder (4 digits)
        if parent_name.isdigit() and len(parent_name) == 4:
            year = int(parent_name)
        else:
            # Default to 2024 if not found
            year = 2024

    # Construct path: {year}/day{num:02d}/{file}.txt
    # Get the repo root directory (parent of utils)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(repo_root, f"{year}/day{int(day_num):02d}/{file}.txt")
    
    with open(input_path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines
