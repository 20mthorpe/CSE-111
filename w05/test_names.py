from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name("Mary", "Thorpe") == "Thorpe; Mary"
    assert make_full_name("Inigo", "Montoya") == "Montoya; Inigo"
    assert make_full_name("Ann", "Wei") == "Wei; Ann"
    assert make_full_name("La-ah", "Brown") == "Brown; La-ah"

def test_extract_family_name():

    assert extract_family_name("Thorpe; Mary") == "Thorpe"
    assert extract_family_name("Montoya; Inigo") == "Montoya"
    assert extract_family_name("Wei; Ann") == "Wei"
    assert extract_family_name("Brown; La-ah") == "Brown"

def test_extract_given_name():

    assert extract_given_name("Thorpe; Mary") == "Mary"
    assert extract_given_name("Montoya; Inigo") == "Inigo"
    assert extract_given_name("Wei; Ann") == "Ann"
    assert extract_given_name("Brown; La-ah") == "La-ah"


pytest.main(["-v", "--tb=line", "-rN", __file__])