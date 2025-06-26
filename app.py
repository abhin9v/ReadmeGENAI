import streamlit as st
from github_utils import fetch_repo_data
from generator import generate_readme_from_repo

st.title("📝 GenREADME from GitHub URL")

repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Generate README"):
    repo_data = fetch_repo_data(repo_url)
    if repo_data:
        with st.spinner("Generating README with Perplexity..."):
            readme = generate_readme_from_repo(repo_data)
            st.success("README generated successfully!")
            st.code(readme, language='markdown')
            st.download_button("Download README.md", readme, file_name="README.md")
    else:
        st.error("Could not fetch GitHub repository data. Check URL or repo privacy.")
