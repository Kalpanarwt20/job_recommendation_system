# import streamlit as st
# import streamlit.components.v1 as components
# from src.helper import ask_groq, extract_text_from_pdf
# from src.database import save_resume_data
# from src.job_api import fetch_linkedin_jobs
# from src.job_api import fetch_naukri_jobs



# st.set_page_config(page_title="AI Job Recommender", layout="wide")
# with open("index.html", "r", encoding="utf-8") as f:
#     components.html(f.read(), height=750)
#     st.markdown("---")
# st.title("🤖 AI Job Recommender")
# st.markdown("Upload your resume and get personalized job recommendations based on your skills and experience from LinkedIn and Naukri.")

# uploaded_file = st.file_uploader("Upload your resume (PDF format only)", type=["pdf"])

# if uploaded_file:
    

 
#     with st.spinner("Extracting text from resume..."):
#         resume_text = extract_text_from_pdf(uploaded_file)

#         with st.spinner("Summarizing your resume..."):
#             summary = ask_groq(f"Summarize this resume highlighting the skills, education and experience:\n\n {resume_text}", max_tokens=500)

#         with st.spinner("Finding skills gaps..."):
#             gaps = ask_groq(f"Analyze this resume and highlight missing skills, certification and experience needed for better job opportunities:\n\n {resume_text}", max_tokens=400)

#         with st.spinner("Creating Future Roadmap..."):
#             roadmap = ask_groq(f"Based on this resume suggest a future roadmap to improve this person's career prospects:(Skills to learn, certification needed, industry exposure):\n\n {resume_text}", max_tokens=400)

#         st.markdown("---")
#         st.header("📄 Resume Summary")
#         st.markdown(f"<div style='background-color:#000000; padding:15px; border-radius:10px; font-size:16px; color:white;'>{summary}</div>", unsafe_allow_html=True)
        
#         st.markdown("---")
#         st.header("⚠️ Skills Gaps Analysis")
#         st.markdown(f"<div style='background-color:#000000; padding:15px; border-radius:10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html=True)

#         st.markdown("---")
#         st.header("🎯 Future Roadmap")
#         st.markdown(f"<div style='background-color:#000000; padding:15px; border-radius:10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)
        

#         st.success("✅ Analysis Completed Successfully!")

#         if st.button("🔍 Get Job Recommendations"):
#             with st.spinner("Fetching job recommendations..."):
#                 keywords = ask_groq(f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-seperated list only, no explaination.\n\nSummary:{summary}", max_tokens=100)
#                 search_keywords_clean = keywords.replace("\n", "").strip()
#                 if st.session_state.get("debug_mode", False):
#                   st.write("DEBUG resume_text:", resume_text[:200])
#                   st.write("DEBUG summary:", summary)
#                   st.write("DEBUG gaps:", gaps)
#                   st.write("DEBUG roadmap:", roadmap)
#                   st.write("DEBUG keywords:", search_keywords_clean)

#                 save_resume_data(
#                     resume_text,
#                     summary,
#                     gaps,
#                     roadmap,
#                     search_keywords_clean
#                 )
        

#             st.success(f"Extracted Job keywords: {search_keywords_clean}")

#             with st.spinner("Fetching jobs from LinkedIn and Naukri ..."):
#                 linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, num_jobs=60) 
#                 naukri_jobs = fetch_naukri_jobs(search_keywords_clean, num_jobs=60)



#                 st.markdown("---")
#                 st.header("💼 Job Recommendations from LinkedIn")
#                 if linkedin_jobs:
#                     for job in linkedin_jobs:
#                         st.markdown(f" **[{job['title']}]({job['url']})**  at *{job.get('companyName')}*")
#                         st.markdown(f"-📍 {job.get('location')}")
#                         st.markdown(f"-🕒 [View Job]({job.get('url')})")
#                         st.markdown("---")
#                 else:
#                     st.warning("No jobs found on LinkedIn.")

#                 st.markdown("---")
#                 st.header("💼 Job Recommendations from Naukri")
#                 if naukri_jobs:
#                     for job in naukri_jobs:
#                         st.markdown(f" **[{job['title']}]({job['url']})**  at *{job.get('companyName')}*")
#                         st.markdown(f"-📍 {job.get('location')}")
#                         st.markdown(f"-🕒 [View Job]({job.get('url')})")
#                         st.markdown("---")
#                 else:
#                     st.warning("No jobs found on Naukri.")

#                 # st.markdown(f"<div style='background-color:#000000; padding:15px; border-radius:10px; font-size:16px; color:white;'>{job_recommendations}</div>", unsafe_allow_html=True)
# # st.markdown("#### ✨ Powered by Artificial Intelligence")
        
#                  # st.success("Resume text extracted successfully!")
# # st.markdown("####  Powered by Artificial Intelligence")

# # st.markdown("---")




# # def main():
# #     print("Hello from job!")


# # if __name__ == "__main__":
# #     main()


import streamlit as st
import streamlit.components.v1 as components

from src.helper import (
    ask_groq,
    extract_text_from_pdf,
    extract_basic_details
)
from src.database import save_resume_data
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs


st.set_page_config(page_title="AI Job Recommender", layout="wide")


# -------- Load UI --------
with open("index.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=750)

st.markdown("---")
st.title("🤖 AI Job Recommender")
st.markdown(
    "Upload your resume and get personalized job recommendations "
    "based on your skills and experience."
)


# -------- Upload Resume --------
uploaded_file = st.file_uploader(
    "Upload your resume (PDF format only)",
    type=["pdf"]
)

if uploaded_file:

    # -------- Extract Resume Text --------
    with st.spinner("📄 Extracting resume text..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    # -------- Extract Name / Email / Phone --------
    name, email, phone = extract_basic_details(resume_text)

    # -------- AI Analysis --------
    with st.spinner("🧠 Generating resume summary..."):
        summary = ask_groq(
            f"Summarize this resume highlighting skills, education and experience:\n\n{resume_text}",
            max_tokens=500
        )

    with st.spinner("⚠️ Analyzing skill gaps..."):
        gaps = ask_groq(
            f"Analyze this resume and identify missing skills and certifications:\n\n{resume_text}",
            max_tokens=400
        )

    with st.spinner("🎯 Creating career roadmap..."):
        roadmap = ask_groq(
            f"Suggest a future career roadmap based on this resume:\n\n{resume_text}",
            max_tokens=400
        )

    # -------- Save to MySQL --------
    save_resume_data(
        name=name,
        email=email,
        phone=phone,
        resume_text=resume_text,
        summary=summary,
        gaps=gaps,
        roadmap=roadmap,
        keywords="Not generated yet"
    )

    st.success("✅ Resume details extracted & saved to database!")

    # -------- Display Extracted Details --------
    st.markdown("---")
    st.subheader("👤 Candidate Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")

    # -------- Display Analysis --------
    st.markdown("---")
    st.header("📄 Resume Summary")
    st.markdown(
        f"<div style='background:#000; padding:15px; border-radius:10px; color:white;'>{summary}</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.header("⚠️ Skills Gap Analysis")
    st.markdown(
        f"<div style='background:#000; padding:15px; border-radius:10px; color:white;'>{gaps}</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.header("🎯 Future Roadmap")
    st.markdown(
        f"<div style='background:#000; padding:15px; border-radius:10px; color:white;'>{roadmap}</div>",
        unsafe_allow_html=True
    )

    # -------- Job Recommendation --------
    st.markdown("---")
    if st.button("🔍 Get Job Recommendations"):

        with st.spinner("🔎 Generating job keywords..."):
            keywords = ask_groq(
                f"Suggest best job titles and search keywords based on this resume summary. "
                f"Comma-separated list only.\n\nSummary:\n{summary}",
                max_tokens=100
            )
            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"🎯 Job Keywords: {search_keywords_clean}")

        with st.spinner("💼 Fetching jobs..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, num_jobs=50)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, num_jobs=50)

        st.header("💼 LinkedIn Jobs")
        for job in linkedin_jobs or []:
            st.markdown(f"**[{job['title']}]({job['url']})** at *{job.get('companyName')}*")

        st.header("💼 Naukri Jobs")
        for job in naukri_jobs or []:
            st.markdown(f"**[{job['title']}]({job['url']})** at *{job.get('companyName')}*")
