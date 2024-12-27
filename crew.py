import openai
from dotenv import load_dotenv
import os
from tasks import scraping_task, analysis_task, swot_task
import pandas as pd
# Load environment variables and set OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def crew_workflow(url):
    # Step 1: Scrape company details
    scraping_result = scraping_task({"url": url})
    if "error" in scraping_result:
        return {"error": scraping_result["error"]}
    company_name, body_text = scraping_result

    # Step 2: Analyze services and competitors
    analysis_result = analysis_task({"company_name": company_name, "body_text": body_text})
    if "error" in analysis_result:
        return {"error": analysis_result["error"]}

    extracted_services = analysis_result["services"]
    competitors = analysis_result["competitors"]

    # Parse the first competitor from the list
    first_competitor = None
    for line in competitors.split("\n"):
        if ":" in line:
            first_competitor = line.split(":")[0].strip()
            break

    # Step 3: Perform SWOT analysis for the input company
    swot_result = swot_task({"company_name": company_name, "body_text": body_text})
    if "error" in swot_result:
        return {"error": swot_result["error"]}

    # Step 4: Perform SWOT analysis for the first competitor (if available)
    competitor_swot_result = None
    if first_competitor:
        competitor_swot_prompt = (
            f"Perform a SWOT analysis for {first_competitor}. "
            f"Use general knowledge and assume relevant industry context."
        )
        competitor_swot_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": competitor_swot_prompt}],
            temperature=0.7
        )
        competitor_swot_result = competitor_swot_response["choices"][0]["message"]["content"].strip()

    # Return aggregated results
    return {
        "company_name": company_name,
        "services": extracted_services,
        "competitors": competitors,
        "swot": swot_result,
        "competitor_swot": competitor_swot_result
    }
