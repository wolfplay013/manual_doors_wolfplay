from .functions import show_output

# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py

# def after_load_location_file(location_table: list) -> list:
#    return location_table

def after_load_location_file(location_table: list) -> list:

    door_sanity = []
    temporary_count = 1

    while temporary_count != 101:
        if temporary_count < 50:
            doorsanity_region = "The Hotel 0"
        elif 50 <= temporary_count < 100:
            doorsanity_region = "The Hotel 1"
        else:
            doorsanity_region = "The Hotel 2"
        door_sanity.append({
                'name': f'Door {"%04d" % temporary_count} - The Hotel',
                'region': doorsanity_region,
                'category': ["Doorsanity (Hotel)", "doorsanity"]
            })
        temporary_count = temporary_count + 1

    while temporary_count != 201:
        if temporary_count < 142:
            doorsanity_region = "The Mines 0"
        elif 142 <= temporary_count < 200:
            doorsanity_region = "The Mines 1"
        else:
            doorsanity_region = "The Mines 2"
        door_sanity.append({
                'name': f'Door {"%04d" % temporary_count} - The Mines',
                'region': doorsanity_region,
                'category': ["Doorsanity (Mines)", "doorsanity"]
            })
        temporary_count = temporary_count + 1
    temporary_count = 1
    while temporary_count != 201:
        if temporary_count % 5 == 0:
            rooms_categories = ["Doorsanity (Rooms)", "doorsanity"]
        else:
            rooms_categories = ["Doorsanity (Rooms)", "doorsanity", "notsimple_doorsanity"]
        door_sanity.append({
                'name': f'A-{"%04d" % temporary_count} - The Rooms',
                'region': "The Rooms",
                'category': rooms_categories
            })
        temporary_count = temporary_count + 1
    while temporary_count != 1001:
        if temporary_count % 5 == 0:
            rooms_categories = ["Doorsanity (Rooms)", "doorsanity", "veryhigh_doorsanity"]
        else:
            rooms_categories = ["Doorsanity (Rooms)", "doorsanity", "notsimple_doorsanity", "veryhigh_doorsanity"]
        door_sanity.append({
                'name': f'A-{"%04d" % temporary_count} - The Rooms',
                'region': "The Rooms",
                'category': rooms_categories
            })
        temporary_count = temporary_count + 1
    temporary_count = -50
    while temporary_count != 0:
        door_sanity.append({
            'name': f'Door {"%02d" % temporary_count} - The Backdoor',
            'region': 'The Backdoor',
            'category': ["Doorsanity (Backdoor)", "doorsanity"]
        })
        temporary_count = temporary_count + 1 

    location_table.extend(door_sanity)

    return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

# called when an external tool (eg Univeral Tracker) ask for slot data to be read
# use this if you want to restore more data
# return True if you want to trigger a regeneration if you changed anything
def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> bool:
    return False
