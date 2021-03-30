import os
import unittest
import subprocess
import shlex


class SlugifyTest(unittest.TestCase):
    def test_slugify(self):
        text = "Lorem ipsum dolor sit amet, consectetur's adipiscing elit"
        expected = "lorem-ipsum-dolor-sit-amet-consectetur-s-adipiscing-elit"
        res = subprocess.check_output(
            [
                "/bin/bash",
                "slugify.sh",
                text,
            ]
        ).strip().decode()
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
