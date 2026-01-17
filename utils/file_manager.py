from pathlib import Path

class FileManager:
    @staticmethod
    def read_lines(path: Path) -> list[str]:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]

    @staticmethod
    def write_lines(path: Path, lines: list[str]):
        with open(path, "w", encoding="utf-8") as f:
            f.writelines([f"{line}\n" for line in lines])

    @staticmethod
    def append_line(path: Path, line: str):
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"{line}\n")