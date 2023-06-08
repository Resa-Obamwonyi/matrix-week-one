# Question One
def nameValidator(name):
    try:
        s = name.partition(' ')
        if(not s[0].isalpha() or not s[1].isspace() or not s[-1].isalpha()):
            raise AssertionError
        if (not (len(s[0]) >= 5 and len(s[0]) <= 20) or not(len(s[-1]) >= 5 and len(s[-1]) <= 20)):
            raise Exception
        
    except AssertionError:
        return "Ensure your names are in alphabet and space in between first name and last name."

    except Exception:
        return "Names must include a minimum of 5 and a maximum of 20 characters."
    
    else:
        return f'Welcome {name}'


print(nameValidator("Test Here"))