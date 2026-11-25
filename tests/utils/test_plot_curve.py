import os
import tempfile
import unittest
from importlib.util import find_spec
from pathlib import Path

from rlcard.utils.utils import plot_curve


@unittest.skipUnless(find_spec('matplotlib'), 'Plotting requires matplotlib')
class TestPlotCurve(unittest.TestCase):

    def test_save_with_or_without_parent_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            os.chdir(directory)
            try:
                Path('results.csv').write_text('episode,reward\n1,0.5\n')
                for target in ('curve.png', 'figures/curve.png'):
                    with self.subTest(target=target):
                        plot_curve('results.csv', target, 'random')
                        self.assertTrue(Path(target).read_bytes().startswith(b'\x89PNG'))
            finally:
                os.chdir(previous)
