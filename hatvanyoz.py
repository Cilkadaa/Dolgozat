def hatvanyoz(tomb, hatvany):
    if not isinstance(tomb, list) or not isinstance(hatvany, int):
        return []
    return [elem ** hatvany for elem in tomb]
