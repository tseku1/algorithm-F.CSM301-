# test_fileReader_unittest.py
import unittest
from pathlib import Path
import os
import stat
from fileReader import read_file

class TestReadFile(unittest.TestCase):

    def test_null_path_raises_value_error(self):
        with self.assertRaises(ValueError):
            read_file(None)

    def test_empty_path_raises_value_error(self):
        with self.assertRaises(ValueError):
            read_file("   ")

    def test_non_existing_raises_file_not_found(self):
        tmp_path = Path("temp_test_dir")
        tmp_path.mkdir(exist_ok=True)
        nonexist = tmp_path / "does_not_exist.txt"
        with self.assertRaises(FileNotFoundError):
            read_file(str(nonexist))
        tmp_path.rmdir()

    def test_directory_path_raises_is_a_directory(self):
        tmp_path = Path("temp_test_dir")
        tmp_path.mkdir(exist_ok=True)
        with self.assertRaises(IsADirectoryError):
            read_file(str(tmp_path))
        tmp_path.rmdir()

    def test_valid_file_reads_all_lines(self):
        tmp_path = Path("temp_test_file.txt")
        tmp_path.write_text("one\n two\nthree\n", encoding="utf-8")
        lines = read_file(str(tmp_path))
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0], "one")
        self.assertEqual(lines[2], "three")
        tmp_path.unlink()

    # def test_permission_error(self):
    #     tmp_path = Path("secret.txt")
    #     tmp_path.write_text("data\n", encoding="utf-8")
    #     tmp_path.chmod(0)
    #     try:
            
    #         with self.assertRaises(PermissionError):
    #             read_file(str(tmp_path))
    #     finally:
    #         tmp_path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    #         tmp_path.unlink()

    def test_malformed_encoding(self):
        tmp_path = Path("bad.txt")
        tmp_path.write_bytes(b"\xff\xfe\xff")
        with self.assertRaises(UnicodeDecodeError):
            read_file(str(tmp_path))
        tmp_path.unlink()

if __name__ == "__main__":
    unittest.main()