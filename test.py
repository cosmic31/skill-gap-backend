# -------------------------------
# Evaluation Metrics for Skill Extraction
# Precision, Recall, F1 for all resumes
# -------------------------------

def precision(actual, extracted):
    if len(extracted) == 0:
        return 0
    return len(set(actual) & set(extracted)) / len(extracted)

def recall(actual, extracted):
    if len(actual) == 0:
        return 0
    return len(set(actual) & set(extracted)) / len(actual)

def f1_score(p, r):
    if (p + r) == 0:
        return 0
    return 2 * (p * r) / (p + r)


# -------------------------------
# Resume 1 – Data Analyst
# -------------------------------
actual_1 = ["python", "sql", "excel", "tableau", "statistics", "powerbi", "data visualization", "machine learning"]
extracted_1 = ["python", "sql", "tableau", "powerbi", "data visualization"]

p1 = precision(actual_1, extracted_1)
r1 = recall(actual_1, extracted_1)
f1_1 = f1_score(p1, r1)

print("Resume 1 – Data Analyst:")
print("Precision:", round(p1, 3))
print("Recall:", round(r1, 3))
print("F1 Score:", round(f1_1, 3))
print("-" * 50)


# -------------------------------
# Resume 2 – Financial Analyst
# -------------------------------
actual_2 = ["excel", "financial modeling", "forecasting", "reporting", "sql"]
extracted_2 = ["excel", "financial modeling", "forecasting", "reporting", "sql"]

p2 = precision(actual_2, extracted_2)
r2 = recall(actual_2, extracted_2)
f1_2 = f1_score(p2, r2)

print("Resume 2 – Financial Analyst:")
print("Precision:", round(p2, 3))
print("Recall:", round(r2, 3))
print("F1 Score:", round(f1_2, 3))
print("-" * 50)


# -------------------------------
# Resume 3 – Analyst (NaN Case)
# -------------------------------
actual_3 = ["excel", "analytics", "communication", "reporting"]
extracted_3 = []   # system couldn't extract anything

p3 = precision(actual_3, extracted_3)
r3 = recall(actual_3, extracted_3)
f1_3 = f1_score(p3, r3)

print("Resume 3 – Analyst (NaN Case):")
print("Precision:", round(p3, 3))
print("Recall:", round(r3, 3))
print("F1 Score:", round(f1_3, 3))
print("-" * 50)
