import streamlit as st
from crew import crew_workflow
import pandas as pd
import openai

st.title("Company Competitor, Service Analysis, and SWOT Agent")

url = st.text_input("Enter the company URL:")

if st.button("Analyze Competitors, Services, and SWOT"):
    if url:
        result = crew_workflow(url)
        if "error" in result:
            st.error(result["error"])
        else:
            st.write(f"**Company Name**: {result['company_name']}")

            st.subheader("Extracted Services")
            st.write(result["services"])

            st.subheader("Competitors")
            competitors_list = result["competitors"].split("\n")
            for competitor in competitors_list:
                if ":" in competitor:
                    name, link = competitor.split(":", 1)
                    st.write(f"{name.strip()} ({link.strip()})")
                else:
                    st.write(competitor)

            st.subheader("SWOT Analysis - Company")
            if isinstance(result["swot"], pd.DataFrame):
                swot_text = ""
                for index, row in result["swot"].iterrows():
                    swot_text += f"{row['Category']}:\n " + "\n ".join(row['Details']) + "\n\n"
                st.text(swot_text.strip())
            else:
                st.error(result["swot"])

            st.subheader("SWOT Analysis - First Competitor")
            if result["competitor_swot"]:
                st.text(result["competitor_swot"])
            else:
                st.write("No competitor found for SWOT analysis.")
    else:
        st.error("Please enter a URL.")
