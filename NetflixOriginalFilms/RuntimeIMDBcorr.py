import pandas as pd

#read Runtime and IMDB Scores from csv
fields = ['Runtime', 'IMDB Score']
data = pd.read_csv(r'D:\\Projects\\NetflixOriginalFilms\\NetflixOriginalsCSV.csv', usecols = fields, encoding = 'latin1')

#Finding correlation between Runtime/IMDB Scores
corr = data.loc[:,fields].corr()
print(corr)