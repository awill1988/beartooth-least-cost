from lib import geo
from shapely.geometry import Polygon


def test_waypoints():
    all = geo.waypoints()
    assert all is not None
    assert len(all) == 10
    assert type(all) is frozenset
    for peak in all:
        assert type(peak[0]) is str
        assert type(peak[1]) is tuple
        assert type(peak[1][0]) is float
        assert type(peak[1][1]) is float


def test_centroid():
    beartooth_mountains = geo.centroid()
    assert type(beartooth_mountains[0]) is str
    assert type(beartooth_mountains[1]) is tuple
    assert type(beartooth_mountains[1][0]) is float
    assert type(beartooth_mountains[1][1]) is float


def test_bbox():
    map_extent = geo.bbox()
    assert type(map_extent) is Polygon
