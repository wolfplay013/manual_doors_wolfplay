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
def after_load_location_file(location_table: list) -> list:

    door_sanity = []
    temporary_count = 1

    # The Hotel (100 Doors)
    while temporary_count != 101:
        if temporary_count < 51:
            doorsanity_region = "The Hotel 0"
        else:
            doorsanity_region = "The Hotel 1"
        door_sanity.append({
                'name': f'Door {"%04d" % temporary_count} - The Hotel',
                'region': doorsanity_region,
                'category': ["Doorsanity - The Hotel", "doorsanity"]
            })
        temporary_count = temporary_count + 1

    # The Mines (100 Doors)
    while temporary_count != 201:
        if temporary_count < 151:
            doorsanity_region = "The Mines 0"
        else:
            doorsanity_region = "The Mines 1"
        door_sanity.append({
                'name': f'Door {"%04d" % temporary_count} - The Mines',
                'region': doorsanity_region,
                'category': ["Doorsanity - The Mines", "doorsanity"]
            })
        temporary_count = temporary_count + 1

    # The Archives (1300 Doors, All Sectors)
    temporary_count = 1
    sector_number = 65 # start from 65 (A in ASCII)
    while sector_number < 91: # ends at 90 (Z)
        rooms_categories = ["Doorsanity - The Archives", "doorsanity", "archives_allsectors"]
        door_sanity.append({
                'name': f'{chr(sector_number)}-{"%03d" % temporary_count} - The Archives',
                'region': "The Archives 1",
                'category': rooms_categories
            })
        if temporary_count != 50:
            temporary_count = temporary_count + 1
        else:
            temporary_count = 1
            sector_number = sector_number + 1

    # The Archives (300 Doors, Any Sectors)
    temporary_count = 1
    while temporary_count != 301:
        rooms_categories = ["Doorsanity - The Archives", "doorsanity", "archives_short"]
        door_sanity.append({
                'name': f'Door {"%03d" % temporary_count} - The Archives',
                'region': "The Archives 1",
                'category': rooms_categories
            })
        temporary_count = temporary_count + 1

    # The Backdoor (50 Doors)
    temporary_count = -50
    while temporary_count != 0:
        door_sanity.append({
            'name': f'Door {"%02d" % temporary_count} - The Backdoor',
            'region': 'The Backdoor 1',
            'category': ["Doorsanity - The Backdoor", "doorsanity"]
        })
        temporary_count = temporary_count + 1 

    # The Outdoors (35 Doors, Distance)
    temporary_count = 2220
    while temporary_count != 0:
        door_sanity.append({
            'name': f'{format(250+temporary_count, ",d")}m - The Outdoors',
            'region': 'The Outdoors 1',
            'category': ["Doorsanity - The Outdoors", "doorsanity", "outdoors_distance"]
        })
        temporary_count = temporary_count - 60

    # The Outdoors (35 Doors, Doors)
    temporary_count = 0
    while temporary_count != 36:
        door_sanity.append({
            'name': f'Door {"%02d" % temporary_count} - The Outdoors',
            'region': 'The Outdoors 1',
            'category': ["Doorsanity - The Outdoors", "doorsanity", "outdoors_doors"]
        })
        temporary_count = temporary_count + 1

    # The Stairwell (99 Doors)
    temporary_count = 1
    while temporary_count != 100:
        door_sanity.append({
            'name': f'Landing {"%02d" % temporary_count} - The Stairwell',
            'region': 'The Stairwell 1',
            'category': ["Doorsanity - The Stairwell", "doorsanity"]
        })
        temporary_count = temporary_count + 1

    location_table.extend(door_sanity)

    return location_table

# called after the events.json file has been loaded, before any processing has occurred
# If you need access to the events after processing, you should use the hooks in World.py
def after_load_event_file(event_table: list) -> list:
    return event_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the categories.json file has been loaded
def after_load_option_file(option_table: dict) -> dict:
    # option_table["core"] is the dictionary of modification of existing options
    # option_table["user"] is the dictionary of custom options
    return option_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
