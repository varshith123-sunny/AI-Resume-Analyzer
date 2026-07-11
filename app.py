import streamlit as st
from analyzer import read_resume, analyze_resume
from prompts import PROMPT

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and receive AI-powered feedback.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            resume_text = read_resume(uploaded_file)
            result = analyze_resume(resume_text, PROMPT)

        st.success("Analysis Complete!")

        if "response" in result:
            st.markdown(result["response"])
        else:
            st.subheader("📊 Overall Score")
            st.progress(result["overall_score"] / 100)
            st.write(result["overall_score"])

            st.subheader("🎯 ATS Score")
            st.progress(result["ats_score"] / 100)
            st.write(result["ats_score"])

            st.subheader("💪 Strengths")
            for item in result["strengths"]:
                st.write("✅", item)

            st.subheader("⚠️ Weaknesses")
            for item in result["weaknesses"]:
                st.write("❌", item)

            st.subheader("🛠️ Missing Skills")
            for item in result["missing_skills"]:
                st.write("•", item)

            st.subheader("💼 Recommended Job Roles")
            for item in result["recommended_job_roles"]:
                st.write("➡️", item)

            st.subheader("📁 Suggested Projects")
            for item in result["recommended_projects"]:
                st.write("📌", item)

            st.subheader("🎓 Certifications")
            for item in result["recommended_certifications"]:
                st.write("🏅", item)

            st.subheader("🚀 Improvements")
            for item in result["improvements"]:
                st.write("✔️", item)

            st.subheader("📅 30-Day Roadmap")
            for item in result["roadmap"]:
                st.write(item)