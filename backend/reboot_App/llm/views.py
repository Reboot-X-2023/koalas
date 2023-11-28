from django.http import HttpResponse, HttpRequest
import json
import pandas as pd
from openai import OpenAI


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index2(request):
    return HttpResponse("Test")

def create_user_data(request):
    print(request.body)
    if request.method == 'POST':
        CHATBOT_CONTEXT = "You are to return python code ONLY (nothing else) - preferably a single line when possible. Your code should be functions that are run on a dataframe called transactions_df wih columns: "
        body = json.loads(request.body)
        print(body["test"])

        transactions_df = pd.read_csv("user_data.csv")
        transactions_df = transactions_df.rename(columns={"amount": "transaction_amount"})
        CHATBOT_CONTEXT += str(transactions_df.columns)
        # print(CHATBOT_CONTEXT)
        client = OpenAI()
        res = "No queries yet"
        while True:
            input_string = body["test"]
            input_string = "Return code ONLY (nothing else) that would answer the following query based on the transactions_df data: " + input_string + ". Store this in a variable called res"
            command = query(input_string, client)
            exec(command)
            # print(command)
            print(res)

        return HttpResponse(res)
    else:
        return HttpResponse("That's not a post request")

    return render(request, 'llm/create_user_data.html', {'form': form})

def query(input_string, client):
    CHATBOT_CONTEXT = "You are to return python code ONLY (nothing else) - preferably a single line when possible. Your code should be functions that are run on a dataframe called transactions_df wih columns date, transaction_amount, third_party, transaction_category"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": CHATBOT_CONTEXT},
            {"role": "user", "content": input_string}
        ]
    )
    return completion.choices[0].message.content