import DeckofcardsAPI #Proxy Class


def main():
    player_score = 0 # Total of each hand
    dealer_score = 0
    play = True     # To control when game ends
    res = "Y"
    
    #Proxy Class for a Deck of Cards
    dapi = DeckofcardsAPI.DeckofcardsAPI()
    results = dapi.get() # The dealer shuffles six decks of cards together
    deckid = results  # Unique ID for the six decks of cards
    print(f"Deck ID: {deckid}")

#    card = dapi.deal() # The dealer deals a card
#    cardvalue = card
#    print(f"{cardvalue}")

    print("\n** Welcome to Binghamton Resort Casino **")
    print("** The Blackjack table is now open! **\n")
    
    for i in range(0, 4):       # Start game by dealing a two card hand to Player and Dealer
        card = dapi.deal()      # The card comes off the deck...
        if card == "KING" or card == "QUEEN" or card == "JACK":  # convert face cards to value
            cardvalue = 10
        elif card =="ACE":
            cardvalue = 11
        else:
            cardvalue = int(card)   # card comes in as a string
        if i %2 == 0:       # Deal it to the Player
            player_score += cardvalue
            print("Card: ", card)
            print("The PLAYER received:", cardvalue, "and has a ", player_score, "\n")
        else:               # Deal it to the Dealer
            dealer_score += cardvalue
            print("Card: ", card)
            print("The DEALER received:", cardvalue, "and has a ", dealer_score, "\n")


    print("\nPlayer's Score: ", player_score, "| Dealer's Score", dealer_score)

    if (player_score == 21 and dealer_score == 21):
        play = False    # Sorry, game ends here
        print("You both hit Blackjack!")

    if (player_score == 21 and dealer_score < 21):
        play = False
        print("Congratulations! The PLAYER hit Blackjack!")

    if (player_score < 21 and dealer_score == 21):
        play = False
        print("Sorry, PLAYER! The DEALER hit Blackjack!")
    
    if play:        # PLAYER's turn to finish his hand
        while (res != "N" and player_score < 21):
            res = input("Would PLAYER like a hit? (Y/N)")
            res = res.upper()   # Accept upper or lowercase 
            if res == "Y":
                        card = dapi.deal()      # The card comes off the deck...
                        print("Card: ", card)
                        if card == "KING" or card == "QUEEN" or card == "JACK":  # convert face cards to value
                            cardvalue = 10
                        elif card =="ACE":  # Should the ACE be 1 or 11?
                            if player_score + 11 <= 21:  # 11 if it won't bust the hand
                                cardvalue = 11
                            else:
                                cardvalue = 1
                        else:
                            cardvalue = int(card)   # card comes in as a string
                        player_score += cardvalue
            print("The PLAYER received:", cardvalue, "and has a ", player_score, "\n")
            print("\nPlayer's Score: ", player_score, "| Dealer's Score", dealer_score)
    if (player_score == dealer_score):
        print("The PLAYER and DEALER have a tie.  Play again!")
        play = False
    if (player_score > 21 and dealer_score > 21):
        print("Sorry!  The PLAYER and DEALER both have busted hands.  Play again!")
        play = False
    if (player_score <= 21 and player_score > dealer_score):
        print("The PLAYER has won!  Play again!")
        play = False
    if (dealer_score <= 21 and dealer_score > player_score):
        print("The DEALER has won!  Play again!")
        play = False
    if (player_score > 21 and dealer_score <= 21):
        print("Sorry!  The DEALER has won!  Play again!")
        play = False
               

main()
