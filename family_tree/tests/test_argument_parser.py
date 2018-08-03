import pytest
from .context import ap


def test_person_relation_pattern():

	assert ap.parse("person=ash relation=brothers") == { "person": "ash", "relation": "brothers" }

def test_mother_son_pattern():

	assert ap.parse("mother=jean son=ash") == { "mother": "jean", "son": "ash" }

def test_husband_wife_pattern():

	assert ap.parse("husband=steve wife=jean") == { "husband":"steve", "wife": "jean" }

def test_wife_husband_pattern():

	assert ap.parse("wife=jean husband=steve") == { "wife": "jean", "husband": "steve" }