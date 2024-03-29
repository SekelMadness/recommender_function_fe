# Recommender system application
This app can give you the Top 5 recommendations lists of articles on globo.com per user.

# Context
This was a `kaggle competition` held several years ago.
See [News Portal User Interactions by Globo.com](https://www.kaggle.com/datasets/gspmoreira/news-portal-user-interactions-by-globocom#clicks_sample.csv) for much more detailed documentation.

# About the app
It is in fact a python `BayesianPersonalizedRanking` model. First time serverless Azure function.

# Librairies
You need to install first some python librairies:

```
azure-functions
```

# Goal
As you know now, our main objective is to predict a ratings (implicit way chosen) of globo's `clicks dataset`.

## Target
* clicks user-item related
* ratings
* top 5 recommendations

## Recommandations
I strongly recommand you to install packages from the `requirements.txt`.

# Tests section
None