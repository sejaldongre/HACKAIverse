# main.py
import streamlit as st
import json
import os

st.title("HackAIverse: Shaping Tomorrow with AI Agents")

# Choose mode
option = st.sidebar.selectbox("Choose Task", ["Add Problem", "Register Team", "Upload Project", "Judging Panel", "View Data"])

# Save data to JSON file
def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Load data from JSON file
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return []

if option == "Add Problem":
    st.header("📌 Add a Problem Statement")
    title = st.text_input("Title")
    description = st.text_area("Description")

    if st.button("Save Problem"):
        problems = load_data("problems.json")
        
        # Check for duplicates
        duplicate = any(p['title'].strip().lower() == title.strip().lower() for p in problems)

        if duplicate:
            st.warning("This problem statement already exists!")
        else:
            problems.append({"title": title, "description": description})
            save_data("problems.json", problems)
            st.success("Problem Saved!")

    st.subheader("Existing Problems")
    for p in load_data("problems.json"):
        st.markdown(f"**{p['title']}**: {p['description']}")

elif option == "Register Team":
    st.header("👥 Register Your Team")
    team_name = st.text_input("Team Name")
    members = st.text_input("Team Members (comma-separated)")
    email = st.text_input("Email")

    if st.button("Register Team"):
        teams = load_data("teams.json")
        teams.append({
            "team_name": team_name,
            "members": members.split(","),
            "email": email
        })
        save_data("teams.json", teams)
        st.success("Team Registered!")

elif option == "Upload Project":
    st.header("📤 Upload Project Link")
    team = st.text_input("Team Name")
    project_link = st.text_input("GitHub/Drive Link")

    if st.button("Submit Project"):
        projects = load_data("projects.json")
        projects.append({"team": team, "link": project_link})
        save_data("projects.json", projects)
        st.success("Project Submitted!")

elif option == "Judging Panel":
    st.header("🧑‍⚖️ Enter Scores")
    team = st.text_input("Team to Score")
    usefulness = st.slider("Usefulness", 1, 10)
    creativity = st.slider("Creativity", 1, 10)
    teamwork = st.slider("Teamwork", 1, 10)

    if st.button("Submit Score"):
        scores = load_data("scores.json")
        scores.append({
            "team": team,
            "usefulness": usefulness,
            "creativity": creativity,
            "teamwork": teamwork
        })
        save_data("scores.json", scores)
        st.success("Score Submitted!")
