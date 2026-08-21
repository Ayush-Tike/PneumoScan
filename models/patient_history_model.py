def to_bool(value):

    if isinstance(value,bool):
        return value

    if isinstance(value,str):
        return value.lower() in ["true","1","yes"]

    return False


def analyze_history(history):

    risk = 0

    previous_pneumonia = to_bool(
        history.get("previous_pneumonia") or
        history.get("previous pneumonia")
    )

    asthma = to_bool(history.get("asthma"))

    smoker = to_bool(history.get("smoker"))

    chronic = to_bool(
        history.get("chronic_disease") or
        history.get("chronic disease")
    )

    if previous_pneumonia:
        risk += 0.35

    if asthma:
        risk += 0.20

    if smoker:
        risk += 0.20

    if chronic:
        risk += 0.25

    return min(risk,1.0)