import requests
import json

class DeckofcardsAPI:

    def __init__(self, count=6):
        self.url = f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={count}' # url for creating new deck

    def get(self):  # Combine six decks of cards and shuffle them
        r = requests.get(self.url)
        #response is a json dictonary of values after .json() call
        response = r.json()
        #check to make sure I got a unique ID returned.  It will be used to access deck of cards
        if response.get('deck_id'):
            self.id = response['deck_id']
            return response['deck_id']
        else:
            return None

    """
This function calls url and is sent a unique deck id so that no one can acesss this url.
No args
No return
"""

    def deal(self):
        print("dealing...")
        # url for dealing one card at a time from the previously created/shuffled deck
        self.url_deal = f'https://deckofcardsapi.com/api/deck/{self.id}/draw/?count=1'
        d = requests.get(self.url_deal)
        dealt = d.json()
        if dealt.get('cards'):  # If we have a good response, return the card's value
            self.d = dealt['cards'][0]['value']
            return dealt['cards'][0]['value']
        else:
            return None        

    """
This functions is called whenever a card is needed for the player and dealer. 
No args
No return
"""