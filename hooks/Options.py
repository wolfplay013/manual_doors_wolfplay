# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class option_WelcomeBack(DefaultOnToggle):
    """Welcome Back
    Join another day.

    This achievement should be disabled when you are playing in a sync."""
    display_name = "Welcome Back"

class option_BuddySystem(DefaultOnToggle):
    """Buddy System
    Play a run with a friend.

    This achievement should be disabled when you are not playing / don't want to play doors with someone."""
    display_name = "Buddy System"

class option_Betrayal(DefaultOnToggle):
    """Betrayal
    Steal a hiding spot from someone right before they die.

    This achievement should be disabled when you are not playing / don't want to play doors with someone."""
    display_name = "Betrayal"

class option_HundredOfMany(Choice):
    """Hundred Of Many
    Encounter your hundredth death.

    This achievement should be disabled when you are playing in a sync, or when you have death link enabled, or when you just don't like tedious tasks.
    If 'with_death_item' is chosen, you unlock an additional item that give you 10 deaths for this achievement. These are balanced to require 9 Death Packs."""
    display_name = "Hundred Of Many"
    option_with_death_item = 0
    option_enabled = 1
    option_disabled = 2
    default = option_with_death_item

class option_ErrorAchievement(DefaultOnToggle):
    """Error
    Enounter the Glitch.

    This achievement should be disabled when you are not playing / don't want to play doors with someone."""
    display_name = "Error"

class option_MeetJack(DefaultOnToggle):
    """Meet Jack
    Enounter Jack.

    This achievement should be disabled when you are playing in a sync, or when you just don't want to grind for a 1 in 200 chance."""
    display_name = "Meet Jack"

class option_TrialAndError(DefaultOnToggle):
    """Trial And Error
    Encounter and survive an activated Glitch Fragment.

    This achievement should be disabled when you are not playing / don't want to play doors with someone."""
    display_name = "Trial And Error"

class option_HelpingHand(DefaultOnToggle):
    """Helping Hand
    Knock Giggle off of another player's face.

    This achievement should be disabled when you are not playing / don't want to play doors with someone."""
    display_name = "Helping Hand"

class option_A1000(DefaultOnToggle):
    """A-1000
    Reach the end of The Rooms.

    This achievement may take hours to complete, and should be disabled when you are playing in a sync, or when you don't want to spend a lot of time on a single check."""
    display_name = "A-1000"

class option_HotelHell(DefaultOnToggle):
    """Hotel Hell
    Escape The Hotel with at least a 150% bonus using Modifiers.

    This achievement can be quite difficult, reccomended to disable this if you have never done Hotel Hell."""
    display_name = "Hotel Hell"

class option_AHardPlace(DefaultOnToggle):
    """A Hard Place
    Escape The Mines with at least a 150% bonus using Modifiers.

    This achievement can be quite difficult, reccomended to disable this if you have never done A Hard Place."""
    display_name = "A Hard Place"

class option_VoidRelated(DefaultOnToggle):
    """It Stares Back & Lost In The Dark
    
    These achievements are grouped together due to being very similar. Lost In The Dark can be disabled through the Crucifix achievement setting.
    Technically possible alone, however this achievement should be disabled when you are not playing / don't want to play doors with someone."""
    display_name = "Void Related Achievements"

class option_SallyRelated(DefaultOnToggle):
    """Playtime & Playtime's Over
    
    These achievements are grouped together due to being very similar. Playtime's Over can be disabled through the Crucifix achievement setting.
    Very RNG-heavy achievements."""
    display_name = "Sally Related Achievements"

class option_AllCrucifix(DefaultOnToggle):
    """Every entity achievement related to the Crucifix.

    Enables all 23 crucifix achievements that are related to an entity. This setting does not disable Evil Be Gone.
    This setting can be disabled when you are in a Sync, due to it being just so time-wasting."""
    display_name = "All Entity Crucifix Achievements"

class option_IndividualFloorKeys(Toggle):
    """Individual Floor Keys
    
    Legacy option, changes the progression of the game in a way where you can access The Mines before The Hotel.
    Every floor exceept for subfloors get 3 keys, with the exception of The Hotel which skips the first key.
    Key #1 unlocks the floor itself, Key #2 unlocks the midway point, Key #3 unlocks the last door."""
    display_name = "Individual Floor Keys"

class option_Doorsanity(Toggle):
    """Doorsanity
    
    Gives a check for every door that you open up.
    Includes 450 checks by default, however this can be modified to be lower or higher through settings.
    Disabling Floor 2 will disable all 100 checks for that floor."""
    display_name = "Doorsanity"

class option_DoorSanityRoomsType(Choice):
    """The Rooms can be customisable to be less severe. Disabling the A-1000 achievement can also make this shorter.
        all_checks: Adds all checks possible, 1 check per 1 door. Stops at 200 checks if the A-1000 achievement is disabled.
        limited_checks: Limits the amount of checks so that it's more fair, 1 check per 5 doors. Stops at 40 checks if the A-1000 achievement is disabled.
        no_check: Disables all checks in The Rooms subfloor."""
    display_name = "Checks in The Rooms on Doorsanity"
    option_all_checks = 0
    option_limited = 1
    option_no_checks = 2
    default = option_limited

class option_AprilFools(Toggle):
    """Strange Achievements

    Legacy setting that adds the 2025 april fools update, Adds unobtainable or scrapped achievements."""
    display_name = "April Fools 2025"

class option_DisableFloor2(DefaultOnToggle):
    """Floor 2

    Legacy option, allows you to disable Floor 2 achievements and items if set to false."""
    display_name = "Floor 2"

class FillerTrapPercent(Range):
    """How many fillers will be replaced with traps. 0 means no additional traps, 100 means all fillers are traps."""
    range_start = 0
    range_end = 100
    default = 15

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["welcome_back"] = option_WelcomeBack
    options["buddy_system"] = option_BuddySystem
    options["betrayal"] = option_Betrayal
    options["hundred_of_many"] = option_HundredOfMany
    options["error"] = option_ErrorAchievement
    options["meet_jack"] = option_MeetJack
    options["trial_and_error"] = option_TrialAndError
    options["helping_hand"] = option_HelpingHand
    options["a_1000"] = option_A1000
    options["hotel_hell"] = option_HotelHell
    options["a_hard_place"] = option_AHardPlace
    options["void_related"] = option_VoidRelated
    options["sally_related"] = option_SallyRelated
    options["all_crucifix"] = option_AllCrucifix
    options["individual_floor_keys"] = option_IndividualFloorKeys
    options["doorsanity"] = option_Doorsanity
    options["rooms_doorsanity"] = option_DoorSanityRoomsType
    options["floor_2"] = option_DisableFloor2
    options["unused_achievements"] = option_AprilFools
    options["filler_traps"] = FillerTrapPercent

    return options
# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
