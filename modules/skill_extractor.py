def extract_skills(cleaned_text, skills_list):
    found = []
    for skill_group in skills_list:
        skills = [s.strip() for s in skill_group.split(",")]
        for s in skills:
            if s.lower() in cleaned_text.lower():
                found.append(s)
    return list(set(found))
    return found