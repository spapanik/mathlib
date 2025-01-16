import pytest

from mathlib import physics


def test_float() -> None:
    assert pytest.approx(float(physics.G), rel=1e-15) == 6.67430e-11
