<img alt="cc-by-nc-sa-4.0" src="https://img.shields.io/badge/License-cc--by--nc--sa--4.0-critical"></a>
[![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)
<a href="https://pypi.org/project/nlp-pandas"><img alt="PyPI" src="https://img.shields.io/badge/pypi-supported-yellow"></a>
<img alt="textreader" src="https://img.shields.io/badge/nlpPandas-v.1.0.0-informational"></a>
<img alt="Dev Status" src="https://img.shields.io/badge/Status-Stable-success"></a>

# nlpPandas
nlpPandas does basic processing to an NLP dataset. Input a Pandas dataframe and output preprocessed dataframe.

## Usage

```python
>>> import nlp-pandas

>>> nlpPandas = nlp-pandas.pass_data(data = some_df, target_column = some_column)


"""
- preprocessor "strong": remove nan, lowercase, remove special characters, remove numbers, remove website links, remove emails, remove nextline (\n), remove repeating whitespace
- preprocessor "base": remove nan, remove website links, remove emails, remove nextline (\n), remove repeating whitespace, *give whitespace number ("3boys"->"3 boys")
- preprocessor "weak": remove nan, remove website links, remove emails, remove nextline (\n), remove repeating whitespace, *give whitespace number ("3boys"->"3 boys")
- preprocessor "custom": under dev
"""
>>> nlpPandas.use_preprocessor(preprocessor = "base")


"""
- analyzer (under dev) "base": give each word count (returns dictionary)
"""
>>> nlpPandas.use_analyzer(analyzer = "base")
```

## Install

### Install using pip
```shell
pip install nlpPandas
```