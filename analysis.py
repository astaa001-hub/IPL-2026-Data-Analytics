import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# ============================================
# IPL 2026 DATA ANALYTICS PROJECT
# ============================================

# ============================================
# Load Dataset
# ============================================

df = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# ============================================
# Dataset Overview
# ============================================

print("=" * 50)
print("IPL 2026 DATA ANALYTICS PROJECT")
print("=" * 50)

print("\nDataset Shape")
print(df.shape)

print("\nFirst 5 Rows")
print(df.head())

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nMissing Values")
print(df.isnull().sum())    

# ============================================
# EXPLORATORY DATA ANALYSIS (EDA)
# ============================================

# ============================================
# ANALYSIS 1 - TEAM PERFORMANCE
# ============================================

print("\n" + "=" * 50)
print("TEAM PERFORMANCE")
print("=" * 50)

# Match Wins
team_wins = df["winner"].value_counts()

# Matches Played
played_as_team1 = df["team1"].value_counts()
played_as_team2 = df["team2"].value_counts()

matches_played = played_as_team1.add(played_as_team2, fill_value=0)

# Win Percentage
win_percentage = ((team_wins / matches_played) * 100).round(2)

# Team Performance Summary
team_summary = pd.DataFrame({
    "Matches Played": matches_played,
    "Matches Won": team_wins,
    "Win Percentage": win_percentage
}).fillna(0)

team_summary = team_summary.sort_values(
    by="Win Percentage",
    ascending=False
)

print(team_summary)

# ============================================
# GRAPH 1 - MATCH WINS
# ============================================

plt.figure(figsize=(10,5))

team_wins.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Matches Won by Each Team")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("graphs/match_wins.png")
plt.show()

# ============================================
# GRAPH 2 - WIN PERCENTAGE
# ============================================

plt.figure(figsize=(10,5))

team_summary["Win Percentage"].plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Team Win Percentage")

plt.xlabel("Teams")

plt.ylabel("Win Percentage")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/win_percentage.png")

plt.show()

# ============================================
# ANALYSIS 2 - TOSS WINNERS
# ============================================

toss_wins = df["toss_winner"].value_counts()

print("\n" + "=" * 50)
print("TOSS WINNERS")
print("=" * 50)
print(toss_wins)
# ============================================
# GRAPH 3 - TOSS WINS
# ============================================

plt.figure(figsize=(10,5))

toss_wins.plot(kind="bar")

plt.title("Toss Wins by Team")

plt.xlabel("Teams")

plt.ylabel("Number of Toss Wins")

plt.savefig("graphs/toss_wins.png")

plt.show()

# ============================================
# ANALYSIS 3 - TOSS IMPACT
# ============================================

toss_match = df["toss_winner"] == df["winner"]

print(toss_match)

result = toss_match.value_counts()

print(result)
# ============================================
# GRAPH 4 - TOSS IMPACT
# ============================================

plt.figure(figsize=(5,4))

result.plot(kind="bar")

plt.title("Did Toss Winner Win the Match?")

plt.xlabel("Result")

plt.ylabel("Matches")

plt.savefig("graphs/toss_impact.png")

plt.show()

# ============================================
# ANALYSIS 4 - MOST SIXES
# ============================================

sixes = deliveries[deliveries["runs_of_bat"] == 6]

most_sixes = sixes.groupby("striker").size()

most_sixes = most_sixes.sort_values(ascending=False)

top10_sixes = most_sixes.head(10)

print(top10_sixes)
# ============================================
# GRAPH 5 - MOST SIXES
# ============================================

plt.figure(figsize=(10,5))

top10_sixes.plot(kind="bar")

plt.title("Top 10 Players with Most Sixes")

plt.xlabel("Batsman")

plt.ylabel("Number of Sixes")

plt.xticks(rotation=45)

plt.savefig("graphs/most_sixes.png")

plt.show()

# ============================================
# ANALYSIS 5 - ORANGE CAP LEADERBOARD
# ============================================

# Runs scored
runs = deliveries.groupby("striker")["runs_of_bat"].sum()

# Balls faced
balls = deliveries.groupby("striker").size()

# Number of fours
fours = deliveries[deliveries["runs_of_bat"] == 4].groupby("striker").size()

# Number of sixes
sixes = deliveries[deliveries["runs_of_bat"] == 6].groupby("striker").size()

# Strike Rate
strike_rate = ((runs / balls) * 100).round(2)

# Orange Cap Table
orange_cap = pd.DataFrame({
    "Runs": runs,
    "Balls": balls,
    "4s": fours,
    "6s": sixes,
    "Strike Rate": strike_rate
}).fillna(0)

orange_cap = orange_cap.sort_values(
    by="Runs",
    ascending=False
)

top10_orange = orange_cap.head(10)

print("\n" + "="*50)
print("ORANGE CAP LEADERBOARD")
print("="*50)

print(top10_orange)

# ============================================
# GRAPH 6 - ORANGE CAP
# ============================================

plt.figure(figsize=(10,5))

top10_orange["Runs"].plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Top 10 Orange Cap Players")

plt.xlabel("Players")

plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/orange_cap.png")

plt.show()

# ============================================
# ANALYSIS 6 - PURPLE CAP LEADERBOARD
# ============================================

# Count wickets taken by each bowler
wickets = deliveries[
    deliveries["player_dismissed"].notna() &
    (~deliveries["wicket_type"].isin(["run out", "retired hurt", "obstructing the field"]))
]

purple_cap = wickets.groupby("bowler").size()

purple_cap = purple_cap.sort_values(ascending=False)

top10_purple = purple_cap.head(10)

print("\n" + "="*50)
print("PURPLE CAP LEADERBOARD")
print("="*50)

print(top10_purple)

# ============================================
# GRAPH 7 - PURPLE CAP
# ============================================

plt.figure(figsize=(10,5))

top10_purple.plot(
    kind="bar",
    color="purple",
    edgecolor="black"
)

plt.title("Top 10 Wicket Takers")

plt.xlabel("Bowlers")

plt.ylabel("Wickets")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/purple_cap.png")

plt.show()

# ============================================
# ANALYSIS 7 - HIGHEST TEAM SCORES
# ============================================

# Total runs scored on each ball
deliveries["total_runs"] = deliveries["runs_of_bat"] + deliveries["extras"]

# Team score in each innings
team_scores = deliveries.groupby(
    ["match_no", "innings", "batting_team"]
)["total_runs"].sum()

# Top 10 highest team scores
top10_team_scores = team_scores.sort_values(
    ascending=False
).head(10)

print("\n" + "=" * 50)
print("HIGHEST TEAM SCORES")
print("=" * 50)

print(top10_team_scores)

# ============================================
# GRAPH 8 - HIGHEST TEAM SCORES
# ============================================

plt.figure(figsize=(12,6))

top10_team_scores.plot(
    kind="bar",
    color="green",
    edgecolor="black"
)

plt.title("Top 10 Highest Team Scores")

plt.xlabel("Match / Innings / Team")

plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/highest_team_scores.png")

plt.show()

# ============================================
# PROJECT CONCLUSION
# ============================================

print("\n" + "=" * 50)
print("PROJECT CONCLUSION")
print("=" * 50)

print("""
PROJECT SUMMARY

• Team performance was analyzed using matches won and win percentage.

• Toss statistics were studied to understand their impact on match outcomes.

• Batting performance was evaluated through sixes hit and the Orange Cap leaderboard.

• Bowling performance was analyzed using the Purple Cap leaderboard.

• Highest team totals highlighted the strongest batting innings of the tournament.

Overall, this project demonstrates how Python, Pandas and Matplotlib can transform raw IPL data into meaningful insights using data analytics techniques.
""")