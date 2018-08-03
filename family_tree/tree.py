

class Tree:

	_relationships = set(["father", "mother", "grandfather", "grandmother",
	"daughter", "son", "brother", "sister", "uncle", "aunt", "cousin",
	"grandson", "grandaughter"])

	data = {}

	def __init__(self, data):

		self.data = data

	def get_relationships(self, person, relation):

		relations = self.data[person][relation]

		if type(relations) == list:
			relations =  ",".join(sorted(relations))

		return str.format("{0}={1}", relation.title(), relations.title())
