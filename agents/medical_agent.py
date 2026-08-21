def medical_agent(xray_prob,history_prob):

    final_risk = (0.8 * xray_prob) + (0.2 * history_prob)

    if final_risk > 0.65:

        diagnosis = "High Pneumonia Risk"

    elif final_risk > 0.40:

        diagnosis = "Moderate Pneumonia Risk"

    else:

        diagnosis = "Low Pneumonia Risk"

    explanation = f"""
    X-ray probability: {xray_prob:.2f}
    History risk: {history_prob:.2f}

    AI agent combined both signals to compute final risk.
    """

    return final_risk,diagnosis,explanation