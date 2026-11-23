"""Public tests for Lab 08. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab08 as lab  # noqa: E402

def test_vote():
    assert list(lab.majority_vote([[1, 0], [1, 1], [0, 1]])) == [1, 1]
