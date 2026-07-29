import streamlit as st

from backend import (
    dataset_overview,
    team_performance,
    toss_analysis,
    orange_cap,
    purple_cap,
    highest_team_scores,
    dashboard_summary
)

# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------

st.set_page_config(
    page_title="IPL 2026 Data Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🏏 IPL Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dataset Overview",
        "🏆 Team Performance",
        "🎯 Toss Analysis",
        "🟠 Orange Cap",
        "🟣 Purple Cap",
        "💥 Highest Team Scores",
        "ℹ About"
    ]
)

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------

if page == "🏠 Home":

    st.title("🏏 IPL 2026 DATA ANALYTICS DASHBOARD")

    st.markdown(
        """
Welcome to the IPL 2026 Data Analytics Project.

This dashboard analyzes IPL 2026 data using:

- Python
- Pandas
- Streamlit
- Matplotlib

Use the sidebar to explore different analyses.
"""
    )

    summary = dashboard_summary()

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Matches", summary["matches"])
    c2.metric("Teams", summary["teams"])
    c3.metric("Players", summary["players"])
    c4.metric("Runs", summary["runs"])
    c5.metric("Wickets", summary["wickets"])

    # -------------------------------------------------
# DATASET OVERVIEW
# -------------------------------------------------

elif page == "📊 Dataset Overview":

    st.title("📊 Dataset Overview")

    data = dataset_overview()

    # Matches Dataset
    st.header("📁 Matches Dataset")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", data["matches_shape"][0])

    with col2:
        st.metric("Columns", data["matches_shape"][1])

    st.subheader("Column Names")
    st.dataframe(
        data["matches_columns"],
        use_container_width=True
    )

    st.subheader("Missing Values")

    missing_matches = (
        data["matches_missing"]
        .reset_index()
        .rename(columns={
            "index": "Column",
            0: "Missing Values"
        })
    )

    st.dataframe(
        missing_matches,
        use_container_width=True
    )

    st.subheader("First 5 Rows")

    st.dataframe(
        data["matches_head"],
        use_container_width=True
    )

    st.divider()

    # Deliveries Dataset

    st.header("🏏 Deliveries Dataset")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("Rows", data["deliveries_shape"][0])

    with col4:
        st.metric("Columns", data["deliveries_shape"][1])

    st.subheader("Column Names")

    st.dataframe(
        data["deliveries_columns"],
        use_container_width=True
    )

    st.subheader("Missing Values")

    missing_deliveries = (
        data["deliveries_missing"]
        .reset_index()
        .rename(columns={
            "index": "Column",
            0: "Missing Values"
        })
    )

    st.dataframe(
        missing_deliveries,
        use_container_width=True
    )

    st.subheader("First 5 Rows")

    st.dataframe(
        data["deliveries_head"],
        use_container_width=True
    )

# -------------------------------------------------
# TEAM PERFORMANCE
# -------------------------------------------------

elif page == "🏆 Team Performance":

    st.title("🏆 Team Performance")

    summary = team_performance()

    st.subheader("Team Performance Table")

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.subheader("🏆 Matches Won")

    st.bar_chart(summary["Matches Won"])

    st.subheader("📈 Win Percentage")

    st.bar_chart(summary["Win %"])

    # -------------------------------------------------
# TOSS ANALYSIS
# -------------------------------------------------

elif page == "🎯 Toss Analysis":

    st.title("🎯 Toss Analysis")

    toss_wins, toss_impact = toss_analysis()

    st.subheader("Toss Wins by Team")
    st.dataframe(toss_wins, use_container_width=True)

    st.bar_chart(toss_wins)

    st.divider()

    st.subheader("Match Wins After Winning Toss")
    st.dataframe(toss_impact, use_container_width=True)

    st.bar_chart(toss_impact)


# -------------------------------------------------
# ORANGE CAP
# -------------------------------------------------

elif page == "🟠 Orange Cap":

    st.title("🟠 Orange Cap")

    orange = orange_cap()

    st.subheader("Top 10 Run Scorers")

    st.dataframe(
        orange,
        use_container_width=True
    )

    st.bar_chart(orange)


# -------------------------------------------------
# PURPLE CAP
# -------------------------------------------------

elif page == "🟣 Purple Cap":

    st.title("🟣 Purple Cap")

    purple = purple_cap()

    st.subheader("Top 10 Wicket Takers")

    st.dataframe(
        purple,
        use_container_width=True
    )

    st.bar_chart(purple)


# -------------------------------------------------
# HIGHEST TEAM SCORES
# -------------------------------------------------

elif page == "💥 Highest Team Scores":

    st.title("💥 Highest Team Scores")

    scores = highest_team_scores()

    st.subheader("Top 10 Highest Innings")

    scores_df = scores.reset_index()
    scores_df.columns = ["Match", "Innings", "Team", "Runs"]

    st.dataframe(scores_df, use_container_width=True)

    st.bar_chart(
        scores_df.set_index("Team")["Runs"]
    )


# -------------------------------------------------
# ABOUT
# -------------------------------------------------

elif page == "ℹ About":

    st.title("ℹ About This Project")

    st.markdown("""
## IPL 2026 Data Analytics Dashboard

### Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib

### Features

- Dataset Overview
- Team Performance
- Toss Analysis
- Orange Cap Analysis
- Purple Cap Analysis
- Highest Team Scores

### Developed By

B.Tech CSE (AI) Student

### Purpose

This project analyzes IPL 2026 match and ball-by-ball data using Python and presents the results through an interactive Streamlit dashboard.
""")