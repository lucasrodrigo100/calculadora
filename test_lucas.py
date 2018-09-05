import pytest

from arquivo import soma, menos, this_num


def test_xyz():
        assert soma(1,1) == 2
        assert soma(2,2) == 4
        assert soma(2.4,  3.1) == 5.5
        assert soma( -2, -10) == -12


def test_usandostring():
        assert soma('1', '2') == 3
        assert soma('xyz',1) == None

def test_menos():
        assert menos(2,2) == 0

