import inquirer
import os
import requests
import pandas as pd


def get_readwise_api_token():
    home_dir = os.path.expanduser("~")
    token_file = os.path.join(home_dir, ".readwise/token")

    with open(token_file, "r") as f:
        return f.read().strip()


def get_headers():
    header = {"Authorization": f"Token {get_readwise_api_token()}"}
    return header


def select_source():
    response = requests.get(
        url="https://readwise.io/api/v2/books/",
        headers=get_headers(),
    )

    data = response.json()
    df = pd.DataFrame(data["results"])

    # sort df by "last_highlight_at" column, newest first
    df = df.sort_values(by="last_highlight_at", ascending=False)
    choices = [
        (f"\"{row['title']}\" by {row['author']}", index) for index, row in df.iterrows()
    ]
    question = [inquirer.List("row", message="Select a source", choices=choices)]
    answer = inquirer.prompt(question)
    return {
        "title": df.loc[answer["row"]]["title"],
        "author": df.loc[answer["row"]]["author"],
        "id": int(df.loc[answer["row"]]["id"]),
    }


def get_highlights(source_id):
    querystring = {
        "book_id": source_id,
    }

    response = requests.get(
        url="https://readwise.io/api/v2/highlights/",
        headers=get_headers(),
        params=querystring,
    )

    data = response.json()
    return data["results"]
