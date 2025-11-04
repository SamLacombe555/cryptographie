import pytest
import crypto as crypt

@pytest.mark.parametrize("mots, longueur", [
    (["banane", "orange", "pomme"], 3),
    (["banane", "orange", "pomme", "sadlhaosd", "aksdas"], 5),
    (["banane", "orange"], 2),
    ([], 0)
])
def test_hasher_mots(mots, longueur):

    dict_hash = crypt.hasher_mots(mots)

    assert isinstance(dict_hash, dict)
    assert len(dict_hash) == longueur
    if len(dict_hash) != 0:
        assert len(dict_hash[mots[0]]) == 3


@pytest.mark.parametrize("initial, nb_cesar, chaine_attendue",[
    ("abcde", 2, "cdefg"),
    ("abcde", 0, "abcde"),
    ("abcde", 10, "klmno"),
    ("abcde", 26, "abcde"),
    ("cdefg", -2, "abcde"),
    ("zoo", 13, "mbb")
])
def test_chiffrement_cesar(initial, nb_cesar, chaine_attendue):

    chaine_cesar = crypt.chiffrement_cesar(initial, nb_cesar)

    assert isinstance(chaine_cesar, str)
    assert len(chaine_cesar) == len(initial)
    assert chaine_cesar == chaine_attendue