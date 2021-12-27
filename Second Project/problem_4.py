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
    
    if group is None:
        return -1
    if (not group.get_users()) and (not group.get_groups()):
        return -2

    if user in group.get_users():
        return True

    for _group in group.get_groups():
        return is_user_in_group(user, _group)

    return False

# test case 1: None values
print(is_user_in_group('sub_child_user', None))
#returns -1

# test case 2: Empty Group
empty_group = Group('empty')
print (is_user_in_group('sub_child_user', empty_group))
# returns -2

# test case 3: 
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print (is_user_in_group('sub_child_user', parent))
# returns True

print (is_user_in_group(67588, child))
# return False

