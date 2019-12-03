import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# ------------------------------------------------------------------------
# TODO:
#  * different colours? https://matplotlib.org/3.1.0/gallery/color/named_colors.html
#  * can I make the labels more centered, or wrap?
# ------------------------------------------------------------------------



# ------------------------------------------ #
#                lip placement               #
# ------------------------------------------ #

def draw_lip_chart():
    lip_counts = data["lip placement"].value_counts()

    lip_style_labels = {
        'both': "bunch of both",
        'wrappy': "mostly wrap around the other's lip",
        'matchy': "mostly match up",
    }
    labels = [lip_style_labels[lip_style] for lip_style in lip_counts.keys()]

    plt.pie(
        lip_counts,
        colors = ['yellowgreen', 'lightcoral', 'lightskyblue'],
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=0.8,
    )

    # draw inner circle (a e s t h e t i c)
    centre_circle = plt.Circle((0,0),0.60,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.show()

draw_lip_chart()



# ------------------------------------------ #
#                 tongue use                 #
# ------------------------------------------ #

# TODO --- order them!

def draw_tongue_chart():
    tongue_counts = data["tongue use"].value_counts()

    tongue_style_labels = {
        'more than half': 'more than half the time',
        'lots': 'lots',
        'less than half': 'less than half the time',
        'barely any': 'barely any, if at all',
    }
    labels = [tongue_style_labels[tongue_style] for tongue_style in tongue_counts.keys()]

    plt.pie(
        tongue_counts,
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'],
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=0.8,
    )

    # draw inner circle (a e s t h e t i c)
    centre_circle = plt.Circle((0,0),0.60,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.show()

draw_tongue_chart()


# ------------------------------------------ #
#            adaption to partner             #
# ------------------------------------------ #

def draw_adapt():
    adapt_counts = data["adapt"].value_counts()

    adapt_style_labels = {
        'follow': 'I adapt to them',
        'mix': 'mix of both',
        'lead': 'they adapt to me',
    }
    labels = [adapt_style_labels[adapt_style] for adapt_style in adapt_counts.keys()]

    plt.pie(
        adapt_counts,
        colors = ['yellowgreen', 'lightcoral', 'lightskyblue'],
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=0.8,
    )

    # draw inner circle (a e s t h e t i c)
    centre_circle = plt.Circle((0,0),0.60,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.show()

draw_adapt()


# ------------------------------------------ #
#             normalized gender              #
# ------------------------------------------ #

def draw_gender():
    gender_counts = data["normalized gender"].value_counts()
    labels = [gender_style for gender_style in gender_counts.keys()]

    plt.pie(
        gender_counts,
        # colors = ['yellowgreen', 'lightcoral', 'lightskyblue'],
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=0.8,
    )

    # draw inner circle (a e s t h e t i c)
    centre_circle = plt.Circle((0,0),0.60,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.show()

draw_gender()

tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
# import pdb; pdb.set_trace()

# plt.show()



# sns.set(style="whitegrid")
# sns.barplot(x="lip placement", y="lip placement count", hue="tongue use", data=data)

# indexed_data = data.set_index(["lip placement", "tongue use", "adapt", "normalized gender"])
# lip_counts = indexed_data.count(level="lip placement")
