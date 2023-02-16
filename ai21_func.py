# import ai21

# def ai21_rewrite(text, intent):
#     ai21.api_key = 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvvvv'
#     r = ai21.Experimental.rewrite(
#         text=text, 
#         intent=intent
#     )
#     return r["values"]["suggestions"]

import requests

def ai21_rewrite(text, intent):
    api_key = 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvvvv'
    r = requests.post(
        "https://api.ai21.com/studio/v1/experimental/rewrite",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "text": text,
            "intent": "general"
        }
    )
    return r.json()["suggestions"]