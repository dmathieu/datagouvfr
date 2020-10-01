# Data Gouv FR

This project will load data from [data.gouv.fr](https://www.data.gouv.fr/fr/)'s
Open Data and inject it into ElasticSearch, so it can then be
consumed/displayed within Kibana.

## Usage

You need [ElasticSearch and Kibana](https://www.elastic.co/guide/en/kibana/current/install.html) installed locally.
You also need Python 3.x installed, as well a pipenv.

You will also need an API key from [data.gouv.fr's API](https://doc.data.gouv.fr/).

```
pipenv install
DATA_GOUV_API_KEY=<your API key> python main.py
```

This will inject all the datasets configured in [config.json](config.json) into
Elastic, with one dataset for each index.

Once all the data is injected, it will be available to be used within Kibana.
