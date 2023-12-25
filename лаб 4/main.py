import pandas as pd
import re
import plotly.graph_objects as go

df = pd.read_csv("doubles3.csv")

def parse_score(score):
    scores = re.findall("\d{1,2}-\d{1,2}", score)
    
    total = 0

    for score in scores:
        splitted = score.split("-")
        total += int(splitted[0]) + int(splitted[1])

    return total

df["score_total"] = df["score"].apply(lambda x: parse_score(x))

scores = df["score_total"]
scores = scores[scores > 0].value_counts()

scores = scores[scores > 0]

fig = go.Figure(data=[go.Bar(x = scores.index.to_list(), y = scores.to_list())])
fig.write_html("tennis_scores.html")


df["team1"] = df["winner1_name"] + "/" + df["winner2_name"]
df["team2"] = df["loser1_name"] + "/" +df["loser2_name"]

scores = pd.DataFrame(df[["team1", "score_total"]])
scores.columns = ["team2",  "score_total"]

scores_all = scores.merge(df["team2"])
scores_all = scores_all.groupby("team2").sum()

print(scores_all.nlargest(10, 'score_total'))
