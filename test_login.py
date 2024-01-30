import pytest

@pytest.mark.skip
def testlogin():
    print("Login Sucessfully")

def testlogoff():
    print("Log Out Sucessfully")

@pytest.mark.sanity
def testcalculation():
    assert 2+2==4
# line added in feature abc
#updated file for feature abc