import requests

def search_vn(query: str, fields: str, extra_filter: list = None) -> dict:
    search_filter = ["search", "=", query]
    if extra_filter:
        filters = ["and", search_filter, extra_filter]
    else:
        filters = search_filter
    body = {
        "filters": filters,
        "fields": fields
    }
    response = requests.post(
        "https://api.vndb.org/kana/vn",
        json=body,
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return response.json()["results"]

def get_vn(vndbid: str, fields:str) -> dict:
    id_filter = ["id","=",vndbid]
    body = {
        "filters": id_filter,
        "fields": fields
    }

    response = requests.post(
        "https://api.vndb.org/kana/vn",
        json=body,
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return response.json()["results"]

print(get_vn("v67", "title"))