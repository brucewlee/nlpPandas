import helper
import pandas as pd

nlp_pandas = helper.pass_data(pd.read_csv('sampler/onestopenglish.csv'),target_column="text")

new_df = nlp_pandas.use_preprocessor("base")
new_df.to_csv("processed_onestopenglish.csv", index = False)
print(new_df.text[0])

output = nlp_pandas.use_analyzer("base")