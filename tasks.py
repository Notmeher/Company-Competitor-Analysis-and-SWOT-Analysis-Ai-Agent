import openai
from dotenv import load_dotenv
import os
import pandas as pd
from tools import fetch_company_details

# Load environment variables and set OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Task to fetch company details
def scraping_task(inputs):
    url = inputs.get("url")
    if not url:
        return {"error": "No URL provided."}
    return fetch_company_details(url)

# Task to analyze services and identify competitors
def analysis_task(inputs):
    company_name = inputs.get("company_name")
    body_text = inputs.get("body_text")
    if not company_name or not body_text:
        return {"error": "Missing company details for analysis."}

    try:
        # Extract services
        services_prompt = (
            f"Analyze the following text and identify sections related to services, products, or solutions for the company. "
            f"Extract the most relevant service keywords (technologies, services, or domains):\n\n{body_text}"
        )
        services_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": services_prompt}],
            temperature=0.7
        )
        extracted_services = services_response["choices"][0]["message"]["content"].strip()

        # Identify competitors
        competitors_prompt = (
            f"List the top competitors of {company_name} that offer services like {extracted_services}. Include their website links."
        )
        competitors_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": competitors_prompt}],
            temperature=0.7
        )
        competitors = competitors_response["choices"][0]["message"]["content"].strip()

        return {"services": extracted_services, "competitors": competitors}
    except Exception as e:
        return {"error": f"An error occurred during competitor analysis: {str(e)}"}

# Task to perform SWOT analysis
def swot_task(inputs):
    company_name = inputs.get("company_name")
    body_text = inputs.get("body_text")
    if not company_name or not body_text:
        return {"error": "Missing company details for SWOT analysis."}

    try:
        swot_prompt = (
            f"Using the following company name and text, perform a SWOT analysis "
            f"(Strengths, Weaknesses, Opportunities, and Threats):\n\nCompany Name: {company_name}\n\nText: {body_text}"
        )
        swot_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": swot_prompt}],
            temperature=0.7
        )
        swot_analysis = swot_response["choices"][0]["message"]["content"].strip()

        swot_sections = swot_analysis.split('\n\n')
        swot_data = []

        for section in swot_sections:
            lines = section.split('\n')
            if len(lines) > 1:
                swot_data.append({'Category': lines[0], 'Details': lines[1:]})

        return pd.DataFrame(swot_data)
    except Exception as e:
        return {"error": f"An error occurred during SWOT analysis: {str(e)}"}
