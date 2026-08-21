import json
import random

def generate_patient():
    return {
        "previous_pneumonia": random.choice([True, False]),
        "asthma": random.choice([True, False]),
        "smoker": random.choice([True, False]),
        "chronic_disease": random.choice([True, False])
    }

# Generate data for 500 patients
patients = [generate_patient() for _ in range(500)]

# Save to JSON file
with open("patients_data.json", "w") as f:
    json.dump(patients, f, indent=4)

print("Generated data for 500 patients and saved to patients_data.json")