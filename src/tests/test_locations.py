from lib import geo


def test_locaitons():
    all = geo.locations()
    assert all is not None
    assert len(all) == 10
    assert type(all) is frozenset
    for location in all:
        assert type(location[0]) is str
        assert type(location[1]) is tuple
        assert type(location[1][0]) is float
        assert type(location[1][1]) is float
