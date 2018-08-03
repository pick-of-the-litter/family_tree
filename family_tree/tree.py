

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

    def add_spouse(self, husband, wife):

        print(str.format("{0} - {1} - {2}", husband, wife, self.data.keys()))

        if husband in self.data.keys():
            if wife in self.data.keys():
                raise ValueError(str.format("Both {0} and {1} already exist in your family tree.", husband, wife))

        if not {p for p in set(self.data) if p in (husband, wife)}:
            raise ValueError(str.format("Neither {0} and {1} exist in your family tree.", husband, wife))

        if husband in self.data:
            self.data[husband]["wife"] = wife
            self.data[wife] = {"husband": husband}

        if wife in self.data:
            self.data[wife]["husband"] = husband
            self.data[husband] = {"wife": wife}

    def isvalid(self, person, relation):

        if person not in self.data:
            raise ValueError(str.format("{} is a not a member of this family.", person))

        if relation not in self.relationships:
            raise KeyError(str.format("Sorry, {} not a supported relationship type", relation))

