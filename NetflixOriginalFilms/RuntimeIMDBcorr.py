import pandas as pd

#read Runtime, Year, and IMDB Scores from csv
fields = ['Runtime','Year', 'IMDB Score']
data = pd.read_csv(r'D:\\Projects\\NetflixOriginalFilms\\NetflixOriginalsCSV.csv', usecols = fields, encoding = 'latin1')

#Finding correlation between Runtime/Year/IMDB Scores
corr = data.loc[:,fields].corr()

print(corr)