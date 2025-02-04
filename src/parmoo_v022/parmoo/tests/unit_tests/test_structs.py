# This is an archival version of ParMOO v0.4.1 for INFORMSJoC; users should
# to obtain the latest ParMOO source at https://github.com/parmoo/parmoo
#

def test_AcquisitionFunction():
    """ Test that the AcquisitionFunction ABC raises a TypeError"""

    from parmoo.structs import AcquisitionFunction
    import pytest

    with pytest.raises(TypeError):
        AcquisitionFunction(0, 0, 0, 0)


def test_GlobalSearch():
    """ Test that the GlobalSearch ABC raises a TypeError"""

    from parmoo.structs import GlobalSearch
    import pytest

    with pytest.raises(TypeError):
        GlobalSearch(0, 0, 0, 0)


def test_SurrogateFunction():
    """ Test that the SurrogateFunction ABC raises a TypeError"""

    from parmoo.structs import SurrogateFunction
    import pytest

    with pytest.raises(TypeError):
        SurrogateFunction(0, 0, 0, 0)


def test_SurrogateOptimizer():
    """ Test that the SurrogateFunction ABC raises a TypeError"""

    from parmoo.structs import SurrogateOptimizer
    import pytest

    with pytest.raises(TypeError):
        SurrogateOptimizer(0, 0, 0, 0)


if __name__ == "__main__":
    test_AcquisitionFunction()
    test_GlobalSearch()
    test_SurrogateFunction()
    test_SurrogateOptimizer()
