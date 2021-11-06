class NameManager:
    # initialize the class
    def __init__(self):
        # need a list to story the names --> anything in init is defined as a variable
        self.name_list = []  # want this to be accessed by all functions and not be deleted

    # want to ba able to add a name
    def add_name(self, name):
        if not (name in self.name_list):
            # add the same to the end of the list
            self.name_list.append(name)
        else:
            print(f"{name} is already in the name list")

    # be able to remove a name
    def remove_name(self, name):
        # just take it out of the list
        # remeber, sometimes a user wants to remove a name that doesn't exist
        try:
            self.name_list.remove(name)
        except ValueError:
            print(f"{name} is not in the name list")
