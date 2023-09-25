import pandas as pd
import cohere
from cohere.custom_model_dataset import InMemoryDataset

co = cohere.Client("API_KEY_HERE")

data = pd.read_csv('./quotes.csv')

d = []

for i in range(len(data['author'])):
    if not (str(data['author'][i]) == 'nan' or str(data['quote'][i]) == 'nan' or str(data['category'][i]) == 'nan'):
        d.append(('quote like '+data['author'][i]+' on '+data['category'][i], data['quote'][i]))

dataset = InMemoryDataset(training_data=d)

finetune_model = co.create_custom_model('quote_textgenerator', model_type='GENERATIVE', dataset=dataset)
