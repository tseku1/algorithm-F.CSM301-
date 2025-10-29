from pathlib import Path
from typing import List
import sys

def read_file(path: str) -> List[str]:
    try:
        if path is None or str(path).strip() == "":
         raise ValueError("Файлын зам хоосон байна.")
        
        p = Path(path)

        if not p.exists():
            raise FileNotFoundError(f"Файл олдсонгүй: {p.resolve()}")

        if p.is_dir():
            raise IsADirectoryError(f"Заасан зам файл биш (хавтас): {p.resolve()}")

        if not p.stat().st_mode & 0o444:
            raise PermissionError(f"Файлыг унших зөвшөөрөл алга: {p.resolve()}")

        with p.open("r", encoding="utf-8") as fh:
            return [line.rstrip("\n") for line in fh.readlines()]
    except UnicodeDecodeError as ude:
        raise ude
    except OSError as e:
        raise e


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) != 1:
        print("Ашиглалт: python app.py <file-ийн_зам>", file=sys.stderr)
        sys.exit(1)

    try:
        lines = read_file(argv[0])
        print(f"Амжилттай уншлаа, мөрийн тоо: {len(lines)}")
        for i, line in enumerate(lines[:5]):
            print(f"{i+1}: {line}")
    except ValueError as e:
        print("Input error:", e, file=sys.stderr)
        sys.exit(2)
    except FileNotFoundError as e:
        print("Error: File not found.", e, file=sys.stderr)
        sys.exit(3)
    except IsADirectoryError as e:
        print("Error: Path is a directory or other file system issue.", e, file=sys.stderr)
        sys.exit(4)
    except PermissionError as e:
        print("Error: No permission to read the file.", e, file=sys.stderr)
        sys.exit(5)
    except UnicodeDecodeError:
        print("Error: File contains invalid UTF-8 or corrupted encoding.", file=sys.stderr)
        sys.exit(6)
    except OSError as e:
        print("IO Error:", e, file=sys.stderr)
        sys.exit(7)


if __name__ == "__main__":
    main()
