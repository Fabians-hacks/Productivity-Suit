import json
import requests
def get_quote():
    try:
        daily_quote = requests.get("https://api.quotable.io/quotes/random")
        daily_quote.raise_for_status()  # Wirft eine Ausnahme, wenn die Anfrage fehlgeschlagen ist
    except requests.exceptions.RequestException as e:
        return  (f"Es gab ein Problem mit der Anfrage: {e}")
    else:
        full_data = daily_quote.json()

        if isinstance(full_data, list):
            for item in full_data:
                quote = item.get('content')  # Verwendet get(), um None zurückzugeben, wenn 'content' nicht vorhanden ist

                if quote is None:
                    return ("Ein Element in der Liste hat nicht das erwartete Format.")
                else:
                    return (f"Zitat des Tages: {quote}")
        else:
            return ("Die Antwort hat nicht das erwartete Format.")
