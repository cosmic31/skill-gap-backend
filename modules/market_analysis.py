import pandas as pd
import os

def get_demand_supply(job_role):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "job_market.csv")

    df = pd.read_csv(data_path)

    row = df[df["job_role"].str.lower() == job_role.lower()]

    if row.empty:
        return None

    demand = int(row["demand"].values[0])
    supply = int(row["supply"].values[0])
    ratio = round(demand / supply, 2)

    if ratio >= 1.2:
        status = "High Opportunity"
        insight = "Demand exceeds supply for this role, indicating strong career opportunities."
    elif ratio >= 0.9:
        status = "Balanced"
        insight = "Demand and supply are relatively balanced, indicating moderate competition."
    else:
        status = "Saturated"
        insight = "Supply exceeds demand, suggesting a saturated job market."

    return {
        "job_role": job_role,
        "demand": demand,
        "supply": supply,
        "ratio": ratio,
        "status": status,
        "insight": insight
    }
