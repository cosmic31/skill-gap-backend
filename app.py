from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import datetime
import json
from bson import json_util

from modules.pdf_extract import extract_text
from modules.preprocessing import clean_text
from modules.skill_extractor import extract_skills
from modules.gap_analysis import get_required_skills, find_missing
from modules.recommender import recommend_resources
from modules.db import save_result
from modules.market_analysis import get_demand_supply

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "https://skill-gap-frontend-eight.vercel.app"}})

# ==============================
# LOAD DATASETS
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

job_roles_df = pd.read_csv(os.path.join(DATA_DIR, "job_roles.csv"))
resources_df = pd.read_csv(os.path.join(DATA_DIR, "courses.csv"))

# Normalize skills list
skills_list = (
    resources_df["skill"]
    .dropna()
    .str.lower()
    .unique()
    .tolist()
)

# ==============================
# ANALYZE ROUTE
# ==============================
@app.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        # -------- Validate input --------
        if "resume" not in request.files:
            return jsonify({"error": "Resume file missing"}), 400

        file = request.files["resume"]
        job_role = request.form.get("job_role", "").strip()

        if job_role == "":
            return jsonify({"error": "Job role missing"}), 400

        # -------- Resume Processing --------
        text = extract_text(file)
        cleaned = clean_text(text)

        # -------- Skill Extraction --------
        extracted = extract_skills(cleaned, skills_list)

        # -------- Gap Analysis --------
        required = get_required_skills(job_role, job_roles_df)
        missing = find_missing(extracted, required)

        # -------- Recommendations --------
        recommendations = recommend_resources(missing, resources_df)

        # -------- Demand vs Supply (NEW) --------
        market_data = get_demand_supply(job_role)

        # -------- Debug Logs --------
        print("DEBUG: extracted skills ->", extracted)
        print("DEBUG: required skills  ->", required)
        print("DEBUG: missing skills   ->", missing)
        print("DEBUG: market data      ->", market_data)

        # -------- Final Record --------
        record = {
            "candidate_name": request.form.get("candidate_name", "Unknown"),
            "job_role": job_role,
            "extracted_skills": extracted,
            "missing_skills": missing,
            "recommendations": recommendations,
            "market_analysis": market_data,
            "timestamp": datetime.datetime.utcnow()
        }

        # -------- Save to MongoDB --------
        save_result(record)

        # -------- Safe JSON Response --------
        safe_json = json.loads(json_util.dumps(record))
        return jsonify(safe_json), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)