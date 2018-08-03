import pytest
from .context import tree


@pytest.fixture
def populated_tree():
	'''return a populated tree'''
	f = {
	"alex": {
		"father": "evan",
		"mother": "diana",
		"wife": "nancy",
		"sisters": ["nisha"],
		"brothers": ["john","joe"]
		},
	 "john": {
		"father": "evan",
		"mother": "diana",
		"sisters": ["nisha"],
		"brothers": ["alex","joe"]
		},
	}

	return tree.Tree(f)


@pytest.mark.parametrize("name, relation, result", [
	("alex", "father", "Father=Evan"),
	("alex", "mother", "Mother=Diana"),
	("alex", "wife", "Wife=Nancy"),
	])
def test_singular_relationship(populated_tree, name, relation, result):

	assert populated_tree.get_relationships(name, relation) == result


@pytest.mark.parametrize("name, relation, result", [
	("alex", "brothers", "Brothers=Joe,John"),
	("alex", "sisters", "Sisters=Nisha"),
	])
def test_plural_relationships(populated_tree, name, relation, result):

	assert populated_tree.get_relationships(name, relation) == result

# def test_person_doesnt_exist(populated_tree):

# 	relationship = Relationship("xyz", "mother")

# 	with pytest.raises(ValueError):
# 		populated_tree.validate(relationship)

# def test_relationship_missing(populated_tree):

# 	relationship = Relationship("alex", "cosuins")

# 	with pytest.raises(KeyError):
# 		populated_tree.validate(relationship)