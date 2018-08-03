

class Tree:

    relationships = set(["father", "mother", "grandfather", "grandmother",
    "daughters", "sons", "brothers", "sisters", "uncles", "aunts", "cousins",
    "grandsons", "grandaughters", "wife", "husband"])

    data = {}

    def __init__(self, data):

        self.data = data

    def get_relationships(self, person, relation):

        self.isvalid(person, relation)

        relations = self.data[person][relation]

        if type(relations) == list:
            relations =  ",".join(sorted(relations)).replace(" ", "")

        return str.format("{0}={1}", relation.title(), relations.title())

    def isvalid(self, person, relation):

        if person not in self.data:
            raise ValueError(str.format("{} is a not a member of this family.", person))

        if relation not in self.relationships:
            raise KeyError(str.format("Sorry, {} not a supported relationship type", relation))

