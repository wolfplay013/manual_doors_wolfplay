from typing import Optional, TYPE_CHECKING, Any
from BaseClasses import MultiWorld, Item, Location # pyright: ignore[reportMissingImports]

if TYPE_CHECKING:
    from ..Items import ManualItem
    from ..Locations import ManualLocation

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "ManualItem") -> Optional[bool]:

    options = multiworld.worlds[player].options
    
    if not options.hundred_of_many == "with_death_item":
        if "HundredOfMany" in item["category"]:
            return False
        else:
            return None
    
    if not options.uptime == "with_flame_item":
        if "UptimeFlame" in item["category"]:
            return False
        else:
            return None

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "ManualLocation") -> Optional[bool]:
    options = multiworld.worlds[player].options

    if not options.doorsanity:
        if "doorsanity" in location["category"]:
            return False

    if "Doorsanity (Mines)" in location["category"]:
        # if not options.floor_2:
        #    return False
        # else:
        return True

    if "Doorsanity (Rooms)" in location["category"]:
        if not options.a_1000 and "veryhigh_doorsanity" in location["category"]:
            return False
        else:
            if options.rooms_doorsanity == "all_checks":
                return True
            elif options.rooms_doorsanity == "limited":
                if not "notsimple_doorsanity" in location["category"]:
                    return True
                else:
                    return False
            elif options.rooms_doorsanity == "no_checks":
                return False
            
    if not options.deathsanity:
        if "disable_Deathsanity" in location["category"]:
            return False

    if "deathsanity_glitch" in location["category"]:
        if options.glitch_deathsanity == "disabled":
            return False
        elif options.glitch_deathsanity == "simple":
            if not "deathsanity_simpleglitch" in location["category"]:
                return False
        elif options.glitch_deathsanity == "complex":
            if not "deathsanity_complexglitch" in location["category"]:
                return False
        elif options.glitch_deathsanity == "default":
            if "deathsanity_complexglitch" in location["category"]:
                return False
            elif "deathsanity_simpleglitch" in location["category"] and not options.trial_and_error:
                return False

    if "deathsanity_special" in location["category"]:
        if not options.special_deathsanity:
            return False
        else:
            return True
    
    if "single_death" in location["category"]:
        if not options.duplicate_deathsanity == 1:
            return False
        else:
            return True
    
    if "multi_death" in location["category"]:
        if options.duplicate_deathsanity == 1:
            return False
        else:
            if "death_no_3" in location["category"]:
                if options.duplicate_deathsanity >= 3:
                    return True
                else:
                    return False
            elif "death_no_2" in location["category"]:
                if options.duplicate_deathsanity >= 2:
                    return True
                else:
                    return False

    if "single_subdeath" in location["category"]:
        if not options.duplicate_subfloor_deathsanity == 1:
            return False
        else:
            return True
    
    if "multi_subdeath" in location["category"]:
        if options.duplicate_subfloor_deathsanity == 1:
            return False
        else:
            if "subdeath_no_3" in location["category"]:
                if options.duplicate_subfloor_deathsanity >= 3:
                    return True
                else:
                    return False
            elif "subdeath_no_2" in location["category"]:
                if options.duplicate_subfloor_deathsanity >= 2:
                    return True
                else:
                    return False

    if "Goal" in location["category"]:
        if options.goal_floor == "the_rooms":
            if not "roomsgoal" in location["category"]:
                return False
        elif options.goal_floor == "the_outdoors":
            if not "outdoorsgoal" in location["category"]:
                return False
        elif options.goal_floor == "the_backdoor":
            if not "backdoorgoal" in location["category"]:
                return False
        elif options.goal_floor == "the_hotel":
            if not "hotelgoal" in location["category"]:
                return False
        elif options.goal_floor == "the_mines":
            if not "minesgoal" in location["category"]:
                return False

    if "Goal" in location["category"]:
        if options.goal_extra_modifier == "0percent":
            if not "0modifier" in location["category"]:
                return False
        if options.goal_extra_modifier == "50percent":
            if not "50modifier" in location["category"]:
                return False
        if options.goal_extra_modifier == "100percent":
            if not "100modifier" in location["category"]:
                return False
        if options.goal_extra_modifier == "150percent":
            if not "150modifier" in location["category"]:
                return False
        if options.goal_extra_modifier == "chaosmode":
            if not "chaosmodemodifier" in location["category"]:
                return False

    return None
            
# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None