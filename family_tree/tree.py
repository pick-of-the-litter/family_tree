WELCOME = "Welcome to the family, {}"
PERSON_EXISTS = "Sorry {} already exists!"
RELATIONSHIPS = set(["father", "mother", "grandfather", "grandmother",
                     "daughters", "sons", "brothers", "sisters",
                     "uncles", "aunts", "cousins", "grandsons",
                     "grandaughters", "wife", "husband"])


class Tree:

    data = {}

    def __init__(self, data):

        self.data = data

    def get_relationships(self, person, relation):

        self.isvalid(person, relation)

        relations = self.data[person][relation]

        if type(relations) == list:
            relations = ",".join(sorted(relations)).replace(" ", "")

        return str.format("{0}={1}", relation.title(), relations.title())

    def add_spouse(self, husband, wife):

        if husband in self.data.keys():
            if wife in self.data.keys():
                raise ValueError(str.format(
                    "Both {0} and {1} already exist in your family tree.",
                    husband.title(), wife.title()))

        if husband not in self.data.keys():
            if wife not in self.data.keys():
                raise ValueError(str.format(
                    "Neither {0} and {1} exist in your family tree.",
                    husband.title(), wife.title()))

        if husband in self.data:
            self.ispresent(wife)
            self.data[husband]["wife"] = wife
            self.data[wife] = {"husband": husband}
            return str.format(WELCOME, wife.title())

        if wife in self.data:
            self.ispresent(husband)
            self.data[wife]["husband"] = husband
            self.data[husband] = {"wife": wife}
            return str.format(WELCOME, husband.title())

    def add_child(self, child, parent , relation):
   
        self.isvalid(parent, relation)
        if child in self.data[parent][relation]:
            raise ValueError(str.format(PERSON_EXISTS, child.title()))

        spouse_name = ""
        spouse_relation = ""
        parents = [parent]

        spouse_relation = [x for x in self.data[parent].keys()
                           if x in ["husband", "wife"]]

        if spouse_relation:
            spouse_name = self.data[parent][spouse_relation[0]]
            parents.append(spouse_name)

        for p in parents:
            if relation in self.data[p]:
                self.data[p][relation].append(child)
            else:
                self.data[p][relation] = [child]

        return str.format(WELCOME, child.title())

    def isvalid(self, person, relation):

        if person not in self.data:
            raise ValueError(str.format("{} is a not a member of this family.",
                             person.title()))

        if relation not in RELATIONSHIPS:
            raise KeyError(str.format("Sorry, {} not a supported relationship type",
                             relation.title()))

    def ispresent(self, person):

        if person in self.data:
            raise ValueError(str.format(PERSON_EXISTS, person))
