from openai import OpenAI
import pandas as pd
CHATBOT_CONTEXT = "You are to return python code ONLY (nothing else) - preferably a single line when possible. Your code should be functions that are run on a dataframe called transactions_df wih columns date, transaction_amount, third_party, transaction_category"


def query(input_string, client):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": CHATBOT_CONTEXT},
            {"role": "user", "content": input_string}
        ]
    )
    return completion.choices[0].message.content 


if __name__ == "__main__":
    transactions_df = pd.read_csv("user_data.csv")
    transactions_df = transactions_df.rename(columns= {"amount":"transaction_amount"})
    client = OpenAI()
    input_string = "Return ONLY code (nothing else) that would find the total amount spent. Store this in a variable res"
    command = query(input_string, client)
    exec(command)
    print(res)

