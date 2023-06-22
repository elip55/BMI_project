
from functions import bald_eagle, metric

user = input('Do you use metric or imperial?  Type "lame" for metric and "USA" for imperial. ')
if user == 'USA' or user == 'usa':
    bald_eagle()
if user == 'lame':
    metric()
