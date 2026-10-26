import sys
from pathlib import Path


def main():
    if len(sys.argv) > 1 and sys.argv[1].strip():
        raw_input = sys.argv[1].strip()
    else:
        try:
            raw_input = input(
                "Enter path under src (e.g. arrays/contains_duplicate): "
            ).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            return

    if not raw_input:
        print("Error: No path provided.")
        return

    # normalize path and strip leading 'src/' or 'tests/'
    path_obj = Path(raw_input)
    parts = list(path_obj.parts)

    if parts and parts[0] in ("src", "tests"):
        parts = parts[1:]

    if not parts:
        print("error: invalid path.")
        return

    filename = parts[-1].removeprefix("test_")
    if not filename.endswith(".py"):
        filename += ".py"

    stem = Path(filename).stem
    sub_dirs = parts[:-1]
    rel_dir = Path(*sub_dirs) if sub_dirs else Path(".")

    src_file = Path("src") / rel_dir / filename
    test_file = Path("tests") / rel_dir / f"test_{filename}"

    # ensure parent directories exist
    src_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.parent.mkdir(parents=True, exist_ok=True)

    # compute import path for the test file
    import_parts = ["src"] + list(sub_dirs) + [stem]
    import_module = ".".join(import_parts)

    # template contents
    src_template = """# add problem description (optional)
class Solution:
    def solve(self):
        pass
"""

    test_template = f"""import pytest
from assertpy import assert_that

from {import_module} import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "expected",
        [
            None,
        ],
    )
    def test_solution(self, expected):
        result = Solution().solve()
        assert_that(result).is_equal_to(expected)
"""

    created_any = False

    if src_file.exists():
        print(f"skipped (already exists): {src_file}")
    else:
        src_file.write_text(src_template)
        print(f"created: {src_file}")
        created_any = True

    if test_file.exists():
        print(f"skipped (already exists): {test_file}")
    else:
        test_file.write_text(test_template)
        print(f"created: {test_file}")
        created_any = True

    if created_any:
        print("\nready! run tests with: make test")


if __name__ == "__main__":
    main()
