def szepTomb(tomb):
    if not isinstance(tomb, list):
        return False
    if len(tomb) == 0:
        return True
    return all(isinstance(elem, type(tomb[0])) for elem in tomb)
