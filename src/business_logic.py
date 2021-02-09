def add_two(user_input):
    if "number" in user_input and isinstance(user_input["number"], int):
        return user_input["number"] + 2

    return None
