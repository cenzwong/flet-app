import ai21

def ai21_rewrite(text, intent):
    ai21.api_key = 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvvvv'
    r = ai21.Experimental.rewrite(
        text=text, 
        intent=intent
    )
    return r["values"]["suggestions"]