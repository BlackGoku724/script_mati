from script_mati.scripts.script_2 import hello_world
import pytest

def test_hello_world_succes():
    response=hello_world('mati')
    assert response==0

@pytest.mark.xfail
def test_hello_world_error():
    response=hello_world('mati')
    assert response==1
