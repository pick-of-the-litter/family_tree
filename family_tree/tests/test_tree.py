import pytest
from .context import tree


@pytest.fixture
def populated_tree():
	'''return a populated tree'''
	f = {
	"amy": {
	    "father": "brian",
	    "mother": "shelly",
	  },
	"alex": {
		"father": "evan",
		"mother": "diana",
		"wife": "nancy",
		"sisters": ["nisha"],
		"brothers": ["john","joe"],
		"cousins": ["peter, steve"],
		"aunts": ["jane"],
		"uncles": ["bob"],
		"grandfather": "jack",
		"grandmother": "helen",
		"grandsons": ["jon", "billy"],
		"grandaughters": ["trish"],
		},
	 "john": {
		"father": "evan",
		"mother": "diana",
		"sisters": ["nisha"],
		"brothers": ["alex","joe"],
		},
	}

	return tree.Tree(f)


@pytest.mark.parametrize("name, relation, result", [
	("alex", "father", "Father=Evan"),
	("alex", "mother", "Mother=Diana"),
	("alex", "wife", "Wife=Nancy"),
	("alex", "grandmother", "Grandmother=Helen"),
	("alex", "grandfather", "Grandfather=Jack"),
	])
def test_singular_relationship(populated_tree, name, relation, result):

	assert populated_tree.get_relationships(name, relation) == result


@pytest.mark.parametrize("name, relation, result", [
	("alex", "brothers", "Brothers=Joe,John"),
	("alex", "sisters", "Sisters=Nisha"),
	("alex", "cousins", "Cousins=Peter,Steve"),
	("alex", "aunts", "Aunts=Jane"),
	("alex", "uncles", "Uncles=Bob"),
	("alex", "grandsons", "Grandsons=Billy,Jon"),
	("alex", "grandaughters", "Grandaughters=Trish"),
	])
def test_plural_relationships(populated_tree, name, relation, result):

	assert populated_tree.get_relationships(name, relation) == result

def test_person_doesnt_exist(populated_tree):

	with pytest.raises(ValueError):
		populated_tree.get_relationships("tina", "mother")

def test_relationship_missing(populated_tree):

	with pytest.raises(KeyError):
		populated_tree.get_relationships("john", "stepson")

def test_add_spouse_wife(populated_tree):

	assert populated_tree.add_spouse("john", "kelly") == str.format(tree.WELCOME, "Kelly")
	assert populated_tree.data["john"]["wife"] == "kelly"
	assert populated_tree.data["kelly"]["husband"] == "john"

def test_add_spouse_husband(populated_tree):

	assert populated_tree.add_spouse("phillip", "amy") == str.format(tree.WELCOME, "Phillip")
	assert populated_tree.data["phillip"]["wife"] == "amy"
	assert populated_tree.data["amy"]["husband"] == "phillip"

def test_add_spouse_neither_person_exists(populated_tree):

	with pytest.raises(ValueError):
	    populated_tree.add_spouse("unknown", "annon")


def test_add_spouse_both_people_exist(populated_tree):

	with pytest.raises(ValueError):
	    populated_tree.add_spouse("alex", "amy")
