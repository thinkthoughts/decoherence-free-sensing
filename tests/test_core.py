import numpy as np

from dfs_sensing.core import common_phase, differential_phase, lieb_mattis_qfi


def test_phase_definitions():
    assert differential_phase(3.0, 1.0) == 1.0
    assert common_phase(3.0, 1.0) == 2.0


def test_lieb_mattis_qfi():
    assert np.isclose(lieb_mattis_qfi(10), (100 + 40) / 3)
