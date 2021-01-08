def save_user(**user):
    print(user)


save_user(id=1, name="ilia", age=31)


def save_user(**user):
    print(user["name"])


save_user(id=1, name="ilia", age=31)


def save_user(**user):
    print(user["name"])


save_user(id=1, name="ilia", age=31)
