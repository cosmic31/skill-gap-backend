def get_required_skills(job_role, df):
    row = df[df["job_role"].str.lower() == job_role.lower()]
    if row.empty:
        return []
    return [s.strip() for s in row.iloc[0]["required_skills"].split(",")]


def find_missing(found, required):
    return [skill for skill in required if skill not in found]
