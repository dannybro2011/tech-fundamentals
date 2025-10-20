import re  # regex module for checking weird characters in name
import json  # for saving game data to a JSON file

def main():
    display_title()  # show the opening narration and instructions
    decision = start()  # ask if the user wants to play

    while decision == 'yes':  # keep looping as long as they wanna play
        player_name = name()  # grab and validate player name
        one, x = breakfast()  # get breakfast choice key and description
        two, y = lunch()  # same for lunch
        three, z = dinner()  # same for dinner
        title = outcome(one, two, three)  # generate kitty title from choices
        print(f'what a day you\'ve had , {player_name} The {title} cat!')  # print final line
        summary(player_name, title, x, y, z)  # save it to JSON

        # ask if they wanna play again
        decision = input('Enter YES to play another day or NO to exit:\n').strip().lower()
        while decision not in ('yes', 'no'):  # reprompt if they typed bull
            decision = input('Invalid input. Enter YES or NO:\n').strip().lower()

def display_title():
    print('Hello kitty! Welcome to your CATVENTURE!\n')
    print('In this story, you are a fatty kitty who gets to decide on what they want for breakfast, lunch, and dinner!')
    print('when prompted, pick between 3 choices for breakfast, lunch, and dinner by typing "A", "B", or "C" respectively\n')

def start():
    print('Would you like to start the Catventure game?')
    decision = input('Enter YES to begin the game or NO to exit:\n').strip().lower()
    while decision not in ('yes', 'no'):  # validate user input
        decision = input('Invalid input. Enter YES or NO:\n').strip().lower()
    return decision  # give that value back to main()

def name():
    while True:
        user_input = input('Whose Catventure is this? what\'s your name?\n')
        pattern = r"(?=.*[!@#$%^&*()])"  # looking for special chars
        match = re.match(pattern, user_input)
        if match:  # found something invalid
            print('choose only alphabeNumberical names -- no special characters!')
            continue  # try again
        else:
            print(f'Welcome! {user_input}!')
            break  

    return user_input

def breakfast():
    # the choices, with label as key and full story as value
    meal = {
        'A': 'Broke into the pantry and ate dad\'s bread',
        'B': 'Parkoured up the fridge to sneak some Pate sticks',
        'C': 'Had some kibble from the automated feeder'
    }

    while True:
        choice = input('You just woke up from a catnap, your catTummy growls "BREAKFAST TIME", are you going to: \nA. break into the pantry and eat dad\'s bread? \nB. parkour up the fridge to sneak a pate stick? \nC. wait for the kibble to dispense then eat it?\n').upper().strip()
        if choice not in ('A', 'B', 'C'):
            print('input only "A", "B", or "C", try again:\n')
            continue

        match choice:
            case 'A':
                return 'A', meal['A']
            case 'B':
                return 'B', meal['B']
            case 'C':
                return 'C', meal['C']

def lunch():
    meal = {
        'A': 'Broke into the pantry and ate dad\'s chips',
        'B': 'Parkoured up the fridge to sneak some pill pockets',
        'C': 'Had some kibble from the automated feeder'
    }

    while True:
        choice = input('You just got done terrorizing the local couch, your catTummy growls "LUNCH TIME", are you going to: \nA. break into the pantry and eat dad\'s chips? \nB. parkour up the fridge to sneak a pill pocket? \nC. wait for the kibble to dispense then eat it?\n').upper().strip()
        if choice not in ('A', 'B', 'C'):
            print('input only "A", "B", or "C", try again:\n')
            continue

        match choice:
            case 'A':
                return 'A', meal['A']
            case 'B':
                return 'B', meal['B']
            case 'C':
                return 'C', meal['C']

def dinner():
    meal = {
        'A': 'Broke into the pantry and ate dad\'s jerky',
        'B': 'Parkoured up the fridge to sneak some fish lollipop',
        'C': 'Had some kibble from the automated feeder'
    }

    while True:
        choice = input('You got done window gazing at loud moving objects, your catTummy growls "DINNER TIME", are you going to: \nA. break into the pantry and eat dad\'s jerky? \nB. parkour up the fridge to sneak a fish lollipop? \nC. wait for the kibble to dispense then eat it?\n').upper().strip()
        if choice not in ('A', 'B', 'C'):
            print('input only "A", "B", or "C", try again:\n')
            continue

        match choice:
            case 'A':
                return 'A', meal['A']
            case 'B':
                return 'B', meal['B']
            case 'C':
                return 'C', meal['C']

def outcome(one, two, three):
    # building the final title based on behavior
    choices = [one, two, three]  # these are just A, B, or C
    title = []  # hold labels like 'Sneaky', 'Gluttonous', 'Angelic'

    for i in choices:
        match i.upper():
            case 'A':
                if 'Gluttonous' not in title:
                    title.append('Gluttonous')
            case 'B':
                if 'Sneaky' not in title:
                    title.append('Sneaky')
            case _:
                if 'Angelic' not in title and one != 'A' and two != 'B':
                    title.append('Angelic')

    return ', '.join(title)  # join and make title

def summary(player_name, title, x, y, z):
    # store this session’s summary data in a JSON file
    player_data = {
        'name': player_name,
        'title': title,
        'meals': [x, y, z]
    }

    try:
        with open('Catventure_summary.json', 'w') as file:
            json.dump(player_data, file, indent=4)
    except Exception as e:
        print(f'an error occurred during file writing: {e}')

if __name__ == '__main__':
    main()  # start 