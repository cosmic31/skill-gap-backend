def recommend_resources(missing_skills, resources_df):
    recommendations = {}

    for skill in missing_skills:
        # match resources where the skill column contains the missing skill (case-insensitive)
        # this handles synonyms and multi-word skills like 'web development' -> 'frontend'
        skill_rows = resources_df[
            resources_df["skill"].str.lower().str.contains(skill.lower(), na=False)
        ]
        # If no direct contains match, try token-based matching and a small synonyms map
        if skill_rows.empty:
            # token fallback: check if any token from the missing skill appears in resource skill
            tokens = [t.strip() for t in skill.lower().split() if t.strip()]
            for t in tokens:
                candidate = resources_df[
                    resources_df["skill"].str.lower().str.contains(t, na=False)
                ]
                if not candidate.empty:
                    skill_rows = candidate
                    break

        if skill_rows.empty:
            synonyms = {
                "web development": "frontend",
                "nodejs": "javascript",
                "mongodb": "database",
                "devops": "cloud",
                "ai": "machine learning",
            }
            mapped = synonyms.get(skill.lower())
            if mapped:
                skill_rows = resources_df[
                    resources_df["skill"].str.lower().str.contains(mapped.lower(), na=False)
                ]

        recommendations[skill] = {
            "courses": [],
            "blogs": [],
            "github": []
        }

        for _, row in skill_rows.iterrows():
            item = {
                "title": row["title"],
                "url": row["url"]
            }

            if row["resource_type"] == "course":
                recommendations[skill]["courses"].append(item)
            elif row["resource_type"] == "blog":
                recommendations[skill]["blogs"].append(item)
            elif row["resource_type"] == "github":
                recommendations[skill]["github"].append(item)

    return recommendations
