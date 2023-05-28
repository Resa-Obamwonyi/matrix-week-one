def nameValidator(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string.")

    name_parts = name.split()

    if len(name_parts) != 2:
        raise ValueError("Name must consist of a first name and a last name separated by a space.")

    first_name, last_name = name_parts
    
    if not first_name.isalpha() or not last_name.isalpha():
        raise ValueError("First name and last name must only contain alphabets.")

    if not (5 <= len(first_name) <= 20) or not (5 <= len(last_name) <= 20):
        raise ValueError("First name and last name must be between 5 and 20 characters long.")

    # Name is valid
    return True