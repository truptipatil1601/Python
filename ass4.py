def check_age(age):
    if age < 18:
        return "You are a minor."
    elif 18 <= age <= 65:
        return "You are an adult."
    else:
        return "You are a senior citizen."
