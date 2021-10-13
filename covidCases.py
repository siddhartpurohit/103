import pandas as pd
import plotly.express as px 

df = pd.read_csv("tt.csv")

fig = px.scatter(df,x = "date", y = "cases",color = "country",title = "total covd cases",size = "cases",size_max = 100)
fig.show()