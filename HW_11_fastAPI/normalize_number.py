def normalize_phone(value):
    new_value = (
        value.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if new_value.isdigit():
        if len(new_value) == 12:
            new_value = "+" + new_value

        elif len(new_value) == 10:
            new_value = "+38" + new_value
        elif len(new_value) == 7:
            new_value = "+38044" + new_value
        else:
            new_value = None

    return new_value
