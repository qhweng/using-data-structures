class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is "" or group is "":
        return False
    
    if user in group.get_users():
        return True

    for a_group in group.get_groups():
        if is_user_in_group(user, a_group):
            return True

    return False


def test():
    parent = Group("parent")
    child = Group("child")
    child2 = Group("child2")
    sub_child = Group("subchild")
    sub_child2 = Group("subchild2")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    
    sub_child_user2 = "sub_child_user2"
    sub_child2.add_user(sub_child_user2)

    child2.add_group(sub_child2)
    parent.add_group(child2)

    # Test normal cases
    assert is_user_in_group(sub_child_user, parent) is True
    assert is_user_in_group(sub_child_user, child) is True
    assert is_user_in_group("child_user", child) is False
    assert is_user_in_group(sub_child_user2, parent) is True

    # Test empty strings/inputs
    assert is_user_in_group("", parent) is False
    assert is_user_in_group(sub_child_user, "") is False
    assert is_user_in_group("", "") is False

    print("Finished testing")

test()
