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

class achievement_Events(Toggle):
    """Enables every non-secret event achievement. If the achievements listed below are no longer active, disable this option or update your manual if it's possible.
    
    Silent Night
    Complete the Vision of Cringle's Workshop during the 2025 holidays."""

class achievement_BuddySystem(DefaultOnToggle):
    """Buddy System (Multiplayer Achievement)
    Play a run with a friend."""
    display_name = "Buddy System"

class achievement_BackFromTheDead(DefaultOnToggle):
    """Back From The Dead (Paid Achievement)
    Revive yourself."""
    display_name = "Back From The Dead"


class achievement_WelcomeBack(DefaultOnToggle):
    """Welcome Back (Secret Achievement)
    Join another day."""
    display_name = "Welcome Back"

class achievement_Betrayal(DefaultOnToggle):
    """Betrayal (Secret Achievement / Multiplayer Achievement)
    Steal a hiding spot from someone right before they die."""
    display_name = "Betrayal"

class achievement_TenOfMany(DefaultOnToggle):
    """Ten Of Many (Secret Achievement)
    Encounter your tenth death."""
    display_name = "Ten Of Many"

class achievement_HundredOfMany(Choice):
    """Hundred Of Many (Secret Achievement)
    Encounter your hundredth death.
    If 'with_death_item' is chosen, an additional item will be added that gives you 10 deaths for this achievement."""
    display_name = "Hundred Of Many"
    option_with_death_item = 0
    option_enabled = 1
    option_disabled = 2
    default = option_with_death_item

class achievement_Doh(DefaultOnToggle):
    """D'oh! (Secret Achievement)
    Eat a Donut."""
    display_name = "D'oh!"

class achievement_FeedTheBirds(DefaultOnToggle):
    """Feed the Birds (Secret Achievement)
    Feed a Caw Bread!"""
    display_name = "Feed The Birds"

class achievement_YouFinallyTurnGreen(DefaultOnToggle):
    """You Finally Turn Green (Secret Achievement)
    Drink a Gween Soda and finally turn green."""
    display_name = "You Finally Turn Green"

class achievement_HelpingHand(DefaultOnToggle):
    """Helping Hand (Multiplayer Achievement)
    Knock Giggle off of another player's face."""
    display_name = "Helping Hand"

class achievement_ItStaresBack(DefaultOnToggle):
    """It Stares Back (Secret Achievement / Multiplayer Achievement)
    Encounter the Void."""
    display_name = "It Stares Back"

class achievement_MeetTimothy(DefaultOnToggle):
    """Meet Timothy (Secret Achievement)
    Encounter Timothy while looting."""

class achievement_Error(DefaultOnToggle):
    """Error (Secret Achievement / Multiplayer Achievement / Rare Achievement)
    Enounter the Glitch."""
    display_name = "Error"

class achievement_MeetJack(DefaultOnToggle):
    """Meet Jack (Secret Achievement / Rare Achievement)
    Enounter Jack."""
    display_name = "Meet Jack"

class achievement_TrialAndError(DefaultOnToggle):
    """Trial And Error (Secret Achievement / Multiplayer Achievement / Rare Achievement)
    Encounter and survive an activated Glitch Fragment."""
    display_name = "Trial And Error"

class achievement_SecretCrucifix(DefaultOnToggle):
    """Every secret Crucifix achievement. (Secret Achievement)
    Use a crucifix against every entity except for Rush, Ambush, Figure, & Seek."""
    display_name = "All Entity Crucifix Achievements"

class achievement_HotelHell(DefaultOnToggle):
    """Hotel Hell (Difficult Achievement)
    Escape The Hotel with at least a 150% bonus using Modifiers."""
    display_name = "Hotel Hell"

class achievement_AHardPlace(DefaultOnToggle):
    """A Hard Place (Difficult Achievement)
    Escape The Mines with at least a 150% bonus using Modifiers."""
    display_name = "A Hard Place"

class achievement_A1000(DefaultOnToggle):
    """A-1000 (Secret Achievement / Long Achievement)
    Reach the end of The Rooms."""
    display_name = "A-1000"

class achievement_BattleMode(DefaultOnToggle):
    """Battle Mode
    Enables all Battle Mode-exclusive items and achievements."""
    display_name = "Battle Mode"

class achievement_BattleModeSecret(DefaultOnToggle):
    """Secret Battle Mode Achievements (Secret Achievement)
    Enables all secret Battle Mode achievements, disabling this will also remove hard achievements."""
    display_name = "Battle Mode Secret Achievements"

class achievement_BattleModeCool(DefaultOnToggle):
    """Hard Battle Mode Achievements (Secret Achievement / Hard Achievement)
    Enables only the hard Battle Mode achievements. (Winner Winner, In Plain Sight 2, High Roller, Battler)"""
    display_name = "Battle Mode Hard Achievements"

class achievement_DailyRuns(DefaultOnToggle):
    """Daily Runs
    Enables all Daily Runs achievements."""
    display_name = "Daily Runs"

class option_IndividualFloorKeys(Toggle):
    """Individual Floor Keys
    Experimental option, changes the progression of the game in a way where you can access The Mines before The Hotel.
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
    """The Rooms can be customised to be less severe. Disabling the A-1000 achievement can also make this shorter.
        all_checks: Adds all checks possible, 1 check per 1 door. Stops at 200 checks if the A-1000 achievement is disabled.
        limited_checks: Limits the amount of checks so that it's more fair, 1 check per 5 doors. Stops at 40 checks if the A-1000 achievement is disabled.
        no_check: Disables all checks in The Rooms subfloor."""
    display_name = "Checks in The Rooms on Doorsanity"
    option_all_checks = 0
    option_limited = 1
    option_no_checks = 2
    default = option_limited

class FillerTrapPercent(Range):
    """How many fillers will be replaced with traps. 0 means no additional traps, 100 means all fillers are traps."""
    range_start = 0
    range_end = 100
    default = 15

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["buddy_system"] = achievement_BuddySystem
    options["back_from_the_dead"] = achievement_BackFromTheDead
    options["welcome_back"] = achievement_WelcomeBack
    options["betrayal"] = achievement_Betrayal
    options["ten_of_many"] = achievement_TenOfMany
    options["hundred_of_many"] = achievement_HundredOfMany
    options["doh"] = achievement_Doh
    options["feed_the_birds"] = achievement_FeedTheBirds
    options["you_finally_turn_green"] = achievement_YouFinallyTurnGreen
    options["helping_hand"] = achievement_HelpingHand
    options["it_stares_back"] = achievement_ItStaresBack
    options["meet_timothy"] = achievement_MeetTimothy
    options["error"] = achievement_Error
    options["meet_jack"] = achievement_MeetJack
    options["trial_and_error"] = achievement_TrialAndError
    options["a_1000"] = achievement_A1000
    options["hotel_hell"] = achievement_HotelHell
    options["a_hard_place"] = achievement_AHardPlace
    options["battle_mode"] = achievement_BattleMode
    options["battle_mode_secrets"] = achievement_BattleModeSecret
    options["battle_mode_hard_secrets"] = achievement_BattleModeCool
    options["daily_runs"] = achievement_DailyRuns

    options["all_crucifix"] = achievement_SecretCrucifix
    options["individual_floor_keys"] = option_IndividualFloorKeys
    options["doorsanity"] = option_Doorsanity
    options["rooms_doorsanity"] = option_DoorSanityRoomsType
    options["filler_traps"] = FillerTrapPercent
    # options["event_achievements"] = achievement_Events

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
