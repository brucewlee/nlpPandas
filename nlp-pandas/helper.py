import pandas as pd
from collections import defaultdict
import logging
logging.basicConfig(level = logging.INFO)

class pass_data():
    def __init__(self, data: object, target_column: str):
        self.target_column = target_column
        self.data = data

    def use_preprocessor(self, preprocessor: str = "base", custom: list = None):
        if preprocessor == "strong":
            output = self.preprocessor_strong()
        elif preprocessor == "base":
            output = self.preprocessor_base()
        elif preprocessor == "weak":
            output = self.preprocessor_weak()
        return output

    def use_analyzer(self, analyzer: str = "base", custom: list = None):
        if analyzer == "base":
            output = self.analyzer_base()
        return output

    def preprocessor_strong(self):
        self.remove_nan()
        self.lowercase()
        self.remove_special_characters()
        self.remove_numbers()
        self.remove_website_links()
        self.remove_emails() 
        #self.give_whitespace_sentence()
        self.remove_nextline()
        self.remove_repeating_whitespace()
        return self.data
    
    def preprocessor_base(self):
        self.remove_nan()
        self.remove_website_links()
        self.remove_emails()
        self.give_whitespace_number()
        self.remove_nextline()
        #self.give_whitespace_sentence()
        self.remove_repeating_whitespace()
        return self.data

    def preprocessor_weak(self):
        self.remove_nan()
        self.give_whitespace_number()
        #self.give_whitespace_sentence()
        self.remove_nextline()
        self.remove_repeating_whitespace()
        return self.data

    def analyzer_base(self):
        analyzed_dict = defaultdict()
        analyzed_dict["each_word_counter"] = self.each_word_counter()
        return analyzed_dict

    """Preprocessor"""
    def remove_nan(self):
        self.data[self.target_column] = self.data[self.target_column].dropna()

    def lowercase(self):
        logging.info("Converting dataframe to lowercase")
        self.data[self.target_column] = self.data[self.target_column].apply(lambda x: x.lower())

    def remove_special_characters(self):
        logging.info("Removing special characters from dataframe")
        self.data[self.target_column] = self.data[self.target_column].replace(r'[^A-Za-z0-9 ]+', '', regex=True)

    def remove_numbers(self):
        logging.info("Removing numbers from dataframe")
        self.data[self.target_column] = self.data[self.target_column].str.replace(r'\d+',"", regex=True)
    
    def remove_website_links(self):
        logging.info("Removing website links from dataframe")
        self.data[self.target_column] = self.data[self.target_column].str.replace(r"http\S+", "", regex=True)

    def remove_emails(self):
        logging.info("Removing emails from dataframe")
        self.data[self.target_column] = self.data[self.target_column].str.replace(r"\S*@\S*\s?", "", regex=True)

    def give_whitespace_number(self):
        logging.info("Give whitespace when character comes right after number, vice versa")
        self.data[self.target_column] = self.data[self.target_column].str.replace(r'(?<=([a-z])|\d)(?=(?(1)\d|[a-z]))', ' ', regex=True)

    """
    def give_whitespace_sentence(self):
        logging.info("Give whitespace after sentence markers")
        # replace more than 1 space with 1 space
        self.data[self.target_column] = self.data[self.target_column].str.replace(r"(?<=[.,;:!?])(?=[^\d])", r"\1\2 ", regex=True)
    """
    def remove_nextline(self):
        logging.info("Removing nextline from dataframe")
        self.data[self.target_column] = self.data[self.target_column].str.replace(r"\n", " ", regex=True)

    def remove_repeating_whitespace(self):
        logging.info("Removing repeating whitespace from dataframe")
        # replace more than 1 space with 1 space
        self.data[self.target_column] = self.data[self.target_column].str.replace(r"\s\s+", "", regex=True)

    """Analyzer"""
    def each_word_counter(self) -> dict:
        logging.info("Counting each word")
        return dict(self.data[self.target_column].str.split().explode().value_counts())
    