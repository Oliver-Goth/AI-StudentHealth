import pandas as pd
import requests

df = pd.read_csv("students_mental_health_survey.csv")
df.columns = df.columns.str.strip()

for index, row in df.head(5).iterrows():
    prompt = f"""You are a student mental health advisor. A student has the following profile:
- Stress Level: {row['Stress_Level']}
- Depression Score: {row['Depression_Score']}
- Anxiety Score: {row['Anxiety_Score']}
- Sleep Quality: {row['Sleep_Quality']}
- Social Support: {row['Social_Support']}
- Financial Stress: {row['Financial_Stress']}
- Uses Counseling Services: {row['Counseling_Service_Use']}
- Substance Use: {row['Substance_Use']}
- Has Chronic Illness: {row['Chronic_Illness']}

Based on this, give 2-3 bullet points of practical, compassionate mental health advice tailored to this student's situation."""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    })

    print(f"\n--- Student #{index + 1} ---")
    print("Prompt:\n", prompt)
    print("\nAdvice:\n", response.json()["response"])