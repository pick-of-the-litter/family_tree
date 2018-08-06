WELCOME = "Welcome to the family, {}"
PERSON_EXISTS = "Sorry {} already exists!"
SPOUSE_EXISTS = "Sorry {} is already married!"
RELATIONSHIPS = set(["father", "mother", "grandfather", "grandmother",
                     "daughters", "sons", "brothers", "sisters",
                     "uncles", "aunts", "cousins", "grandsons",
                     "grandaughters", "wife", "husband"])


class Tree:
    """
       An object that represents a family tree and the actions
       that can be performed upon it.
    """

    data = {}

    def __init__(self, data):

        self.data = data

    def get_relationships(self, person, relation):
        """Query the different relationships in the family tree.

        Args:
            person (str): The person you are querying.
            relation (str): The type relationship.

        Returns:
            str: The persons relations of type that was input
                 i.e. Brothers=John,Joe
        """

        self.isvalid(person, relation)

        relations = self.data[person][relation]

        if type(relations) == list:
            relations = ",".join(sorted(relations)).replace(" ", "")

        return str.format("{0}={1}", relation.title(), relations.title())

    def add_spouse(self, husband, wife):
        """Create a new wife or spouse for an existing person.

        Args:
            husband (str): The husband you'd like to create or get married.
            wife (str): The wife you'd like to create or get married.

        Raises:
            ValueError: If both spouses already exist.
            ValueError: If Neither spouse exists.

        Returns:
            str: A welcome message including the name of the new spouse.
        """

        if set(("husband", "wife")) <= set(self.data.keys()):
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
            self.ismarried(husband)
            self.data[husband]["wife"] = wife
            self.data[wife] = {"husband": husband}
            return str.format(WELCOME, wife.title())

        if wife in self.data:
            self.ispresent(husband)
            self.ismarried(wife)
            self.data[wife]["husband"] = husband
            self.data[husband] = {"wife": wife}
            return str.format(WELCOME, husband.title())

    def add_child(self, child, parent , relation):
        """Add a new child to a mother and implicitly it's father as well.

        Args:
            child (str): The child you'd like to create.
            parent (str): The parent of the child.
            relation (str): The relationship - son or daughter

        Raises:
            ValueError: If `child` already exists.

        Returns:
            str: A welcome message including the child's name.
        """
   
        self.isvalid(parent, relation)

        if relation in self.data[parent]:
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
        """Check if a person is missing or the relationship input is valid.

        Args:
            person (str): The person input into the program.
            relation (str): The relationship type input into the program.

        Raises:
            ValueError: If `person` is missing from the data.
            ValueError: If `relation` is invalid.
        """

        self.ismissing(person)

        if relation not in RELATIONSHIPS:
            raise KeyError(str.format("Sorry, {} not a supported relationship type",
                             relation.title()))

    def ismissing(self, person):
        """Check if a person is missing from the data.

        Args:
            person (str): The person input into the program.

        Raises:
            ValueError: If `person` is missing from the data.
        """

        if person not in self.data:
            raise ValueError(str.format("{} is a not a member of this family.",
                             person.title()))

    def ispresent(self, person):
        """Check if a person is alread represented in the data.

        Args:
            person (str): The person input into the program.

        Raises:
            ValueError: If `person` is represented in the data.
        """

        if person in self.data:
            raise ValueError(str.format(PERSON_EXISTS, person.title()))

    def ismarried(self, person):
        """Check if a person is already married.

        Args:
            person (str): The person input into the program.

        Raises:
            ValueError: If `person` is already married.
        """

        for k in self.data[person].keys():
            if k in ["wife", "husband"]:
                raise ValueError(str.format(SPOUSE_EXISTS, person.title()))
