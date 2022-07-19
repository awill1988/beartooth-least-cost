from typing import FrozenSet, Tuple


def locations() -> FrozenSet[Tuple[str, Tuple[float, float]]]:
    """
    Provides all relevant Beartooth Least Cost Path Ultra Marathon coordinate locations.

    :returns: A set of the 10 highest points
    """

    # https://beartoothleastcostpath.github.io/2022-06-21-How-to-Participate
    return frozenset(
        [
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Granite_Peak_(Montana)&params=45.163426647_N_109.807456247_W_type:mountain_region:US-MT_scale:100000
                "Granite Peak",
                (45.163427, -109.807456),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Mount_Wood_(Montana)&params=45_16_31_N_109_48_48_W_type:mountain_region:US
                "Mount Wood",
                (45.275278, -109.813333),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Castle_Mountain_(Carbon_County,_Montana)&params=45_05_56_N_109_37_50_W_type:mountain_region:US-MT_scale:100000
                "Castle Mountain",
                (45.098889, -109.630556),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Whitetail_Peak&params=45_05_20_N_109_35_16_W_type:mountain_region:US-MT_scale:100000
                "Whitetail Peak",
                (45.088889, -109.587778),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Castle_Rock_Spire&params=45_05_50_N_109_38_35_W_type:mountain_region:US-MT_scale:100000
                "Castle Rock Spire",
                (45.097222, -109.643056),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Silver_Run_Peak&params=45_07_16_N_109_32_43_W_type:mountain_region:US-MT_scale:100000
                "Silver Run Peak",
                (45.121111, -109.545278),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Tempest_Mountain&params=45_10_01_N_109_47_31_W_type:mountain_region:US-MT_scale:100000
                "Tempest Mountain",
                (45.166944, -109.791944),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Mount_Peal&params=45_09_39_N_109_46_22_W_type:mountain_region:US-MT_scale:100000
                "Mount Peal",
                (45.160833, -109.772778),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Castle_Rock_Mountain&params=45_05_54_N_109_39_14_W_type:mountain_region:US-MT_scale:100000
                "Castle Rock Mountain",
                (45.098333, -109.653889),
            ),
            (
                # https://geohack.toolforge.org/geohack.php?pagename=Beartooth_Mountain&params=45_03_39_N_109_34_07_W_type:mountain_region:US-MT_scale:100000
                "Beartooth Mountain",
                (45.060833, -109.568611),
            ),
        ]
    )
