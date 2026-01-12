import unittest
from pathlib import Path

from Database.Database import find_root


class TestDatabase(unittest.TestCase):

    def test_find_root(self):
        root = find_root()
        self.assertTrue(Path(root).resolve().exists())
        self.assertTrue(Path(root).resolve().is_dir())
        self.assertTrue(Path(root / "rental_config.json").exists())


if __name__ == '__main__':
    unittest.main()