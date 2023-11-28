import pandas as pd

def get_transaction_categories(user_data):
    company_categories = {
        'Eating out': ['Tiger Tiger', 'Nandos', 'Pizza Express', 'The Royal Oak', 'Honest Burgers', 'Wetherspoon', 'Dominos'],
        'Coffee': ['Nero', 'Costa Coffee'],
        'Healthcare and Wellbeing': ['Pure gym', 'Boots', 'Lloyds pharmacy', 'Tony and Guy'],
        'Travel': ['TFL'],
        'Retail shops': ['Zara', 'Next', 'Amazon', 'Waitrose', 'Disney shop', 'John Lewis', 'New look', 'River Island', 'Asos', 'RayBan', 'HnM', 'B&Q', 'The Griffin', 'The Newman Arms', 'Trotters'],
        'Supermarkets': ['Tesco', 'Waitrose'],
        'Insurance and finance': ['Halifax', 'Churchill', 'Lloyds Bank'],
        'Bills': ['Virgin Media', 'Amazon prime', 'Netflix', 'Octopus energy','O2'],
        'Transfer to accounts': ['11234567', '111345678','11234678']
    }
    user_data['category'] = user_data['third_party_name'].map({company: category for category, companies in company_categories.items() for company in companies})
    user_data.to_csv("./user_data.csv")
    return user_data

def neg_amounts(df):
    df["transaction_amount"]*=-1
    return df

def preprocess(df):
    df = get_transaction_categories(df)
    df = neg_amounts(df)
    return df