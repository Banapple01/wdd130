"""
File: game.py
Author: Jonathan Wright

Purpose: Choose, Champion!.
"""

act1 = input("\nIt's summer. You walk down the street from your house and see a nice dog. Do you want to PET Or KICK the dog? ").lower()
act2 = ''

if(act1 == 'pet'):
    act2 = input("\nYou pet the dog. But it turns out to be a raccoon. \nYou keep walking down the street and see someone getting mugged by a raccoon. \nDo you HELP or keep WALKING? ").lower()
    while act2 != 'help' or act2 != 'walking':
        print("\nChoose a given option.\n")
        act2 = input("\nYou pet the dog. But it turns out to be a raccoon. \nYou keep walking down the street and see someone getting mugged by a raccoon. \nDo you HELP or keep WALKING? ").lower()
    if(act2 == 'help'):
        act3 = input("\nYou help by equipping a baseball bat and threatening the person. They drop their wallet and run. \nBefore you can haggle with the raccoon it picks up the wallet and runs. \nDo you CHASE after it? or SCREAM at it and keep walking? ").lower()
        if(act3 == 'chase'):
            print("\nYou chase after it, ashamed of your terrible mugging skills. \nTHE END")
        elif(act3 == 'scream'):
            print("\nYou scream some profanities at it before considering your terrible life choices. \nYou repent and decide to become a super hero. Naming yourself 'Raccoon Man(or Woman)'. \nYou perform many righteous deeds including taking down the raccoon syndicate. \nTHE END")
        else:
            print("you spontaneously combust.")
    elif(act2 == 'walking'):
        act3 = input("\nYou keep walking down the street, you monster. \nTwo raccoons come up to you. \nDo they MUG you? Or give you HUGS? ").lower()
        if(act3 == 'mug'):
            print("\nThey mug you. \nTHE END")
        elif(act3 == 'hugs'):
            print("\nThey give you hugs. Spreading their diseases all over you. \nYou later die of covid because the hospital needed some money. \nTHE END")
        else:
            print("you spontaneously combust.")
elif(act1 == 'kick'):
    act2 = input("\nYou kick that dog with the fury of 10,000 suns. By doing so you invoke the rath of the Dog King. \nHe appears out of thin air to give you a beat down. Do you FIGHT or RUN? ").lower()
    while act2 != 'fight' or act2 != 'run':
        print("\nChoose a given option.\n")
        act2 = input("\nYou kick that dog with the fury of 10,000 suns. By doing so you invoke the rath of the Dog King. \nHe appears out of thin air to give you a beat down. Do you FIGHT or RUN? ").lower()
    if(act2 == 'fight'):
        act3 = input("\nYou and the Dog King engage in an epic anime battle with many charging up screaming episodes before the finally. \nThe Dog King gets you into a choke hold. Do you TAP out or FIGHT on? ").lower()
        if(act3 == 'tap'):
            print("\nYou tap out but the Dog King does not believe you deserve mercy. He chokes you out. \nYou wake up in the hospital with every bone in your body broken, wondering why people care more about dogs than other people. \nTHE END")
        elif(act3 == 'fight'):
            print("\nYou fight his choke hold with every fiber of your body. Slowly ripping his arm from your throat. \nYou explain to the Dog King that the dog you kicked had an incurable disease and you granted it mercy. \nThe Dog King doesn't believe you and you're forced to kill him to survive. Your last words to him being 'You are a bad dog.' \nAfter the fight you're left wondering why people care more about dogs than other people.\nTHE END")
        else:
            print("you spontaneously combust.")
    elif(act2 == 'run'):
        act3 = input("\nYou run. But the Dog King catches up to you and gives you a beat down. Do you say SORRY or GIT gud? ").lower()
        if(act3 == 'sorry'):
            print("\nHe calls you a bad human and sprays you in the face with a spray bottle. \nTHE END")
        elif(act3 == 'git'):
            print("\nHe gives you an even worse beat down. \nTHE END")
        else:
            print("you spontaneously combust.")
else:(
    print("You Lose")
)