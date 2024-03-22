import pytest



def test_sub1():
    assert 2 + 2 == 3


@pytest.mark.smoke
def test_sub2():
    assert 2 - 2 == 0
    
@pytest.mark.reg
def test_sub3():
    assert 2 - 2 == 0
    
@pytest.mark.reg
def test_sub4():
    assert 2 - 2 == 0
    
@pytest.mark.skip(reason="Not implemented yet")
def test_subtraction():
    assert 2 - 1 == 1
