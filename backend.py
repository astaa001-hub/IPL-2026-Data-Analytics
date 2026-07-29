import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

def load_data():
    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")
    return matches, deliveries


# ==========================================
# DATASET OVERVIEW
# ==========================================

def dataset_overview():

    matches, deliveries = load_data()

    return {
        "matches_shape": matches.shape,
        "deliveries_shape": deliveries.shape,

        "matches_columns": matches.columns.tolist(),
        "deliveries_columns": deliveries.columns.tolist(),

        "matches_missing": matches.isnull().sum(),
        "deliveries_missing": deliveries.isnull().sum(),

        "matches_head": matches.head(),
        "deliveries_head": deliveries.head(),

        "matches": matches,
        "deliveries": deliveries
    }


# ==========================================
# TEAM PERFORMANCE
# ==========================================

def team_performance():

    matches, deliveries = load_data()

    # Matches Won
    team_wins = matches["winner"].value_counts()

    # Matches Played
    played_team1 = matches["team1"].value_counts()
    played_team2 = matches["team2"].value_counts()

    matches_played = played_team1.add(
        played_team2,
        fill_value=0
    )

    # Win Percentage
    win_percentage = (
        team_wins / matches_played * 100
    ).round(2)

    summary = pd.DataFrame({

        "Matches Played": matches_played,

        "Matches Won": team_wins,

        "Win %": win_percentage

    }).fillna(0)

    summary = summary.sort_values(
        by="Win %",
        ascending=False
    )

    return summary
# ==========================================
# TOSS ANALYSIS
# ==========================================

def toss_analysis():

    matches, deliveries = load_data()

    toss_wins = matches["toss_winner"].value_counts()

    toss_impact = (
        matches["toss_winner"] == matches["winner"]
    ).value_counts()

    return toss_wins, toss_impact


# ==========================================
# ORANGE CAP
# ==========================================

def orange_cap():

    matches, deliveries = load_data()

    # Runs
    runs = deliveries.groupby("striker")["runs_of_bat"].sum()

    # Balls
    balls = deliveries.groupby("striker").size()

    # Fours
    fours = deliveries[
        deliveries["runs_of_bat"] == 4
    ].groupby("striker").size()

    # Sixes
    sixes = deliveries[
        deliveries["runs_of_bat"] == 6
    ].groupby("striker").size()

    # Strike Rate
    strike_rate = ((runs / balls) * 100).round(2)

    orange = pd.DataFrame({

        "Runs": runs,

        "Balls": balls,

        "4s": fours,

        "6s": sixes,

        "Strike Rate": strike_rate

    }).fillna(0)

    orange = orange.sort_values(
        by="Runs",
        ascending=False
    )

    return orange.head(10)


# ==========================================
# PURPLE CAP
# ==========================================

def purple_cap():

    matches, deliveries = load_data()

    wickets = deliveries[

        deliveries["player_dismissed"].notna()

        &

        (~deliveries["wicket_type"].isin([
            "run out",
            "retired hurt",
            "obstructing the field"
        ]))

    ]

    purple = wickets.groupby("bowler").size()

    purple = purple.sort_values(
        ascending=False
    )

    return purple.head(10)
# ==========================================
# HIGHEST TEAM SCORES
# ==========================================

def highest_team_scores():

    matches, deliveries = load_data()

    # Total runs on each ball
    deliveries["total_runs"] = (
        deliveries["runs_of_bat"] +
        deliveries["extras"]
    )

    team_scores = deliveries.groupby(
        ["match_no", "innings", "batting_team"]
    )["total_runs"].sum()

    highest = (
        team_scores
        .sort_values(ascending=False)
        .head(10)
    )

    return highest


# ==========================================
# DASHBOARD SUMMARY
# ==========================================

def dashboard_summary():

    matches, deliveries = load_data()

    total_matches = len(matches)

    total_teams = len(
        pd.unique(
            pd.concat([
                matches["team1"],
                matches["team2"]
            ])
        )
    )

    total_players = deliveries["striker"].nunique()

    total_runs = deliveries["runs_of_bat"].sum()

    total_wickets = deliveries["player_dismissed"].notna().sum()

    return {
        "matches": total_matches,
        "teams": total_teams,
        "players": total_players,
        "runs": total_runs,
        "wickets": total_wickets
    }