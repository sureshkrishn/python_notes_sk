#Disease Diagnosis using Exemplaer Based Learning
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# Each row represents a patient with features and a disease label (0: Healthy, 1: Disease A, 2: Disease B)
data = np.array([
    [65, 150, 120, "None"],
    [70, 160, 130, "A"],
    [75, 155, 140, "A"],
    [88, 170, 160, "B"],
    [80, 165, 150, "B"]
])

# New patient case for diagnosis
new_patient = np.array([72, 152, 128])

# Define a similarity metric (Euclidean distance)
def similarity(patient1, patient2):
    return euclidean_distances([patient1[:3]], [patient2[:3]])[0][0]

# Retrieve similar past cases
similar_cases = []
for patient in data:
    sim_score = similarity(new_patient, patient)
    similar_cases.append((patient, sim_score))

# Sort by similarity score
similar_cases.sort(key=lambda x: x[1])

# Adaptation and diagnosis (simple: choose the most similar case)
diagnosis = similar_cases[0][0][-1]

# Display results
print("Similar cases:")
for patient, score in similar_cases:
    print(f"Features: {patient[:3]}, Similarity: {score}, Diagnosis: {patient[-1]}")

print(f"Diagnosis for the new patient: {diagnosis}")