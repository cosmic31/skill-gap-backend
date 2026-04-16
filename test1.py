# -------------------------------
# Recommendation Evaluation
# -------------------------------

def precision_at_k(recommended, relevant, k):
    recommended_k = recommended[:k]
    correct = len(set(recommended_k) & set(relevant))
    return correct / k


def coverage(missing_skills, skills_with_resources):
    if len(missing_skills) == 0:
        return 0
    return len(skills_with_resources) / len(missing_skills)


# Example for Data Analyst Resume
missing_skills = ["excel", "statistics", "machine learning"]

# system recommendations returned:
recommended_resources = [
    "tableau course",
    "excel course",
    "python blog",
    "ml repo"
]

# relevant resources (determine manually)
relevant_resources = [
    "excel course",
    "ml repo"
]

print("Precision@4:", precision_at_k(recommended_resources, relevant_resources, 4))
print("Coverage:", coverage(missing_skills, relevant_resources))
