import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
plt.style.use("ggplot")

def generate_plot():
    years=[]
    moneys=[]
    kinds=[]
    data = json.load(open('data.json'))["fourth_slide"]
    for year, args in data["years"].items():
        for kind, money in args.items():
            years.append(year)
            kinds.append(kind)
            moneys.append(float(money))
    df = pd.DataFrame(dict(money=moneys, year=years, kind=kinds))

    sns.barplot(data=df, x="year", y="money", hue="kind")
    plt.savefig(data["path2plot"])

if __name__ == "__main__":

    generate_plot()


