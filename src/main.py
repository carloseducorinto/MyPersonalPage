import streamlit as st

# --- PAGE SETUP ---

about_page = st.Page(
    page = "../views/about_me.py",
    title = "About Me",
    icon= ":material/account_circle:",
    default=True,
)

first_project_page = st.Page(
    page = "../views/first_project.py",
    title="First Project",
    icon=":material/bar_chart:", 
)

second_project_page = st.Page(
    page = "../views/second_project.py",
    title="Second Project",
    icon=":material/smart_toy:", 
)

# --- Navigation Setup [Without Sessions]
#pg = st.navigation(pages=[about_page, first_project_page, second_project_page])


# --- Navigation Setup [With Sessions]

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects":[first_project_page, second_project_page],
    }
)



# --- Shared on All Pages 
st.logo("../assets/cadu_logo_v1.png") 
#st.sidebar.text('Made by Cadu Santos')

# --- Run Navigation
pg.run()



