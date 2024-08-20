import argparse


def get_lcs(s1, s2):
    ROWS, COLUMNS = len(s2), len(s1)
    if ROWS == 0 or COLUMNS == 0:
        return ""
    dp = [[""] * (COLUMNS + 1) for _ in range(ROWS + 1)]
    for row in range(1, ROWS + 1):
        for col in range(1, COLUMNS + 1):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + s1[col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[ROWS][COLUMNS]


def get_lcs_multiline(s1: list[str], s2: list[str]) -> list[str]:
    ROWS, COLUMNS = len(s2), len(s1)
    if ROWS == 0 or COLUMNS == 0:
        return []
    dp = [[[] for _ in range(COLUMNS + 1)] for _ in range(ROWS + 1)]
    for row in range(1, ROWS + 1):
        for col in range(1, COLUMNS + 1):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + [s1[col - 1]]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[ROWS][COLUMNS]


def _get_lcs_indexes(s1: list[str], s2: list[str]) -> list[tuple[int, int]]:
    ROWS, COLUMNS = len(s2), len(s1)
    if ROWS == 0 or COLUMNS == 0:
        return []
    dp = [[[] for _ in range(COLUMNS + 1)] for _ in range(ROWS + 1)]
    for row in range(1, ROWS + 1):
        for col in range(1, COLUMNS + 1):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + [(col - 1, row - 1)]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[ROWS][COLUMNS]


def get_diff(s1: list[str], s2: list[str]) -> tuple[list[str], list[str]]:
    indexes = _get_lcs_indexes(s1, s2)
    s1_common_indexes = {i[0] for i in indexes}
    s2_common_indexes = {i[1] for i in indexes}
    s1_diff = [s for idx, s in enumerate(s1) if idx not in s1_common_indexes]
    s2_diff = [s for idx, s in enumerate(s2) if idx not in s2_common_indexes]
    return (s1_diff, s2_diff)


def print_diff(s1: list[str], s2: list[str]) -> None:
    s1_diff, s2_diff = get_diff(s1, s2)
    for s in s1_diff:
        print(f"< {s}")
    print("---")
    for s in s2_diff:
        print(f"> {s}")


def read_file(filepath: str) -> list[str]:
    lines = []
    with open(filepath, "r", encoding="latin-1") as file_:
        for line in file_:
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='diff', description='Calculated difference between 2 files.',)
    parser.add_argument('file1')
    parser.add_argument('file2')
    args = parser.parse_args()
    print_diff(read_file(args.file1), read_file(args.file2))