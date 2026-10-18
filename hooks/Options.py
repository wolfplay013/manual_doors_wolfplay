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

class achievement_BuddySystem(DefaultOnToggle):
    """Buddy System (Multiplayer Achievement)
    Play a run with a friend."""
    display_name = "Buddy System"

class achievement_GroupMember(DefaultOnToggle):
    """Group Member
    Join the LSPLASH group (and get a free revive)!"""
    display_name = "Group Member"

class achievement_BackFromTheDead(DefaultOnToggle):
    """Back From The Dead (Paid Achievement)
    Revive yourself."""
    display_name = "Back From The Dead"


class achievement_WelcomeBack(DefaultOnToggle):
    """Welcome Back (Secret Achievement / Async Achievement)
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

class achievement_FeedTheBirds(DefaultOnToggle):
    """Feed the Birds (Secret Achievement)
    Feed a Caw Bread!"""
    display_name = "Feed The Birds"

class achievement_REDACTED(DefaultOnToggle):
    """REDACTED (Secret Achievement)
    Watch, and create a new entity."""
    display_name = "REDACTED"

class achievement_Patience(DefaultOnToggle):
    """Patience (Secret Achievement)
    Walk through the entire queue line in the Archives."""
    display_name = "Patience"

class achievement_MissionSuccessful(DefaultOnToggle):
    """Mission Successful (Secret Achievement)
    Flush a Toilet, turn on a Sink, and use an Air Dryer in succession."""
    display_name = "Mission Successful"

class achievement_DustToDust(DefaultOnToggle):
    """Dust To Dust (Secret Achievement)
    no spoilers :)"""
    display_name = "Dust To Dust"

class achievement_GarageSale(DefaultOnToggle):
    """Garage Sale (Secret Achievement)
    no spoilers :)"""
    display_name = "Garage Sale"

class achievement_ClayWorld(DefaultOnToggle):
    """Clay World (Secret Achievement)
    no spoilers :)"""
    display_name = "Clay World"

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
    display_name = "Meet Timothy"

class achievement_Error(DefaultOnToggle):
    """Error (Secret Achievement / Multiplayer Achievement / Rare Achievement)
    Encounter the Glitch."""
    display_name = "Error"

class achievement_MeetJack(DefaultOnToggle):
    """Meet Jack (Secret Achievement / Rare Achievement)
    Enounter Jack."""
    display_name = "Meet Jack"

class achievement_TrialAndError(DefaultOnToggle):
    """Trial And Error (Secret Achievement / Multiplayer Achievement / Rare Achievement)
    Encounter and survive an activated Glitch Fragment."""
    display_name = "Trial And Error"

class achievement_WhoAmI(DefaultOnToggle):
    """Who Am I? (Secret Achievement)
    Try to remember."""
    display_name = "Who Am I?"

class achievement_CongaLine(DefaultOnToggle):
    """Conga Line (Secret Achievement)
    no spoilers :)"""
    display_name = "Conga Line"

class achievement_FriendBall(DefaultOnToggle):
    """Friend Ball (Secret Achievement)
    no spoilers :)"""
    display_name = "Friend Ball"

class achievement_Doh(DefaultOnToggle):
    """D'oh! (Secret Achievement)
    Eat a Donut."""
    display_name = "D'oh!"

class achievement_YouFinallyTurnGreen(DefaultOnToggle):
    """You Finally Turn Green (Secret Achievement)
    Drink a Gween Soda and finally turn green."""
    display_name = "You Finally Turn Green"

class achievement_ProGamer(DefaultOnToggle):
    """Pro Gamer (New Achievement)
    no spoilers :)"""
    display_name = "Pro Gamer"

class achievement_EmancipationCustomization(DefaultOnToggle):
    """Emancipation Customization (Secret Achievement)
    no spoilers :)"""
    display_name = "Emancipation Customization"

class achievement_CrackedGamer(DefaultOnToggle):
    """Cracked Gamer (Secret Achievement)
    no spoilers :)"""
    display_name = "Cracked Gamer"

class achievement_FlashPoint(DefaultOnToggle):
    """Flash Point (Secret Achievement)
    no spoilers :)"""
    display_name = "Flash Point"

class achievement_SecretCrucifix(DefaultOnToggle):
    """Every secret Crucifix achievement. (Secret Achievement)
    Use a crucifix against every entity except for Rush, Ambush, Figure, Seek, & Portrait."""
    display_name = "All Entity Crucifix Achievements"

class achievement_CharlesDrowned(DefaultOnToggle):
    """Charles Drowned (Secret Achievement)
    no spoilers :)"""
    display_name = "Charles Drowned"

class achievement_HotelHell(DefaultOnToggle):
    """Hotel Hell (Difficult Achievement)
    Escape The Hotel with at least a 150% bonus using Modifiers."""
    display_name = "Hotel Hell"

class achievement_AHardPlace(DefaultOnToggle):
    """A Hard Place (Difficult Achievement)
    Escape The Mines with at least a 150% bonus using Modifiers."""
    display_name = "A Hard Place"

class achievement_StarEmployee(DefaultOnToggle):
    """Star Employee (Difficult Achievement)
    Successfully organize the Mail Room, after giving Honcho something it shouldn't have."""
    display_name = "Star Employee"

class achievement_StorageWars(DefaultOnToggle):
    """Storage Wars (Secret Achievement)
    Bargain 3000 Gold from the hooded figure in The Stairwell."""
    display_name = "Storage Wars"

class achievement_BattleModeSecret(DefaultOnToggle):
    """Battle Mode Achievements (Secret Achievement)
    Enables all Battle Mode-exclusive items and achievements, excluding Hard Achievements."""
    display_name = "Battle Mode Secret Achievements"

class achievement_BattleModeCool(DefaultOnToggle):
    """Hard Battle Mode Achievements (Secret Achievement / Hard Achievement)
    Enables only the hard Battle Mode achievements. (Winner Winner, In Plain Sight 2, High Roller, Battler)"""
    display_name = "Battle Mode Hard Achievements"

class achievement_DailyRuns(DefaultOnToggle):
    """Daily Runs
    Enables all Daily Runs achievements."""
    display_name = "Daily Runs"

class achievement_ParallelProcessing(DefaultOnToggle):
    """PARALLEL PROCESSING (Multiplayer Achievement)
    Win any Daily Run with other players. Retries count."""
    display_name = "PARALLEL PROCESSING"

class achievement_CleanRun(DefaultOnToggle):
    """CLEAN RUN (Async Achievement)
    Win any Daily Run on your first attempt."""
    display_name = "CLEAN RUN"

class achievement_Uptime(Choice):
    """UPTIME (Async Achievement)
    Keep up a Daily Streak for 7 days.
    If 'with_flame_item' is chosen, an additional item will be added that gives you an additional day to your streak for this achievement."""
    display_name = "UPTIME"
    option_with_flame_item = 0
    option_enabled = 1
    option_disabled = 2
    default = option_with_flame_item

class achievement_ChaosMode(DefaultOnToggle):
    """Everything Everywhere All At Once (Secret Achievement / Hard Achievement)
    Successfully escape The Hotel in the CHAOS Vision. If using livestream integration, requires at least 5 viewers."""
    display_name = "Everything Everywhere All At Once"

class option_Doorsanity(Toggle):
    """Doorsanity
    Gives a check for every door that you open up. (also includes landings in the stairwell)
    Includes 684 checks by default, however this can be modified to be lower or higher through settings."""
    display_name = "Doorsanity"

class option_DoorSanityArchivesType(Choice):
    """The Archives can be customized to be less severe.
        all_checks: Adds all checks in each sector.
        300_checks: Gives you 300 doors to go through in total, no matter the sector.
        no_checks: Disables all checks in The Archives subfloor."""
    display_name = "Doorsanity - The Archives Checks"
    option_all_checks = 0
    option_300_checks = 1
    option_no_checks = 2
    default = option_300_checks

class option_DoorSanityOutdoorsType(Choice):
    """The Outdoors can be customized to give checks on different factors.
        distance_checks: Adds a check for every 60 meters in the outdoors, up until 35 checks.
        door_checks: Adds a check for every door in the outdoors. Caution with this option, as there's no door numbers in the outdoors!
        no_checks: Disables all checks in The Outdoors subfloor."""
    display_name = "Doorsanity - The Outdoors Checks"
    option_distance_checks = 0
    option_door_checks = 1
    option_no_checks = 2
    default = option_door_checks

class option_Deathsanity(Toggle):
    """Deathsanity (⚠ Currently outdated, doesn't include any of the new entities.)
    Gives a check for every death you obtain. Not recommended to enable with Deathlink on.
    Includes every single thing you can die to.
    Includes 26 checks by default, however this can be expanded with the following options."""
    display_name = "Doorsanity"

class option_DeathsanityMainDuplicates(Range):
    """Adds multiple checks per death in the main floors for Deathsanity. Doesn't apply to special deaths, or subfloor deaths in the list."""
    range_start = 1
    range_end = 3
    default = 1
    display_name = "Doorsanity - Duplicate Deaths"

class option_DeathsanitySubDuplicates(Range):
    """Adds multiple checks per death in the subfloors for Deathsanity. Glitched entites are considered as subfloor entities."""
    range_start = 1
    range_end = 3
    default = 1
    display_name = "Doorsanity - Duplicate Subfloor Deaths"

class option_DeathsanityGlitch(Choice):
    """Adds glitched entities to the list of deaths. See below for options.
        default: Chooses between 'simple' or 'disabled', based on if the Trial and Error badge is enabled.
        complex: Adds 3 individual deaths to the list for SCJVEREECH, AROxMBUSH, & RNIUSHCg== each.
        simple: Adds 1 death to the list for all three entities, associates all of the glitched entities with glitch.
        disabled: Completely removes all deaths regarding glitched entities."""
    option_default = 0
    option_complex = 1
    option_simple = 2
    option_disabled = 3
    default = option_default
    display_name = "Doorsanity - Glitched Entities"

class option_DeathsanitySpecial(Toggle):
    """Adds special death conditions based on death messages to the list of deaths.
    Check the guide for more information."""
    display_name = "Doorsanity - Special Deaths"

class FillerTrapPercent(Range):
    """How many fillers will be replaced with traps. 0 means no additional traps, 100 means all fillers are traps."""
    range_start = 0
    range_end = 100
    default = 15

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["buddy_system"] = achievement_BuddySystem
    options["group_member"] = achievement_GroupMember
    options["back_from_the_dead"] = achievement_BackFromTheDead
    options["welcome_back"] = achievement_WelcomeBack
    options["betrayal"] = achievement_Betrayal
    options["ten_of_many"] = achievement_TenOfMany
    options["hundred_of_many"] = achievement_HundredOfMany
    options["feed_the_birds"] = achievement_FeedTheBirds
    options["redacted"] = achievement_REDACTED
    options["patience"] = achievement_Patience
    options["mission_successful"] = achievement_MissionSuccessful
    options["dust_to_dust"] = achievement_DustToDust
    options["garage_sale"] = achievement_GarageSale
    options["clay_world"] = achievement_ClayWorld

    options["helping_hand"] = achievement_HelpingHand
    options["it_stares_back"] = achievement_ItStaresBack
    options["meet_timothy"] = achievement_MeetTimothy
    options["error"] = achievement_Error
    options["meet_jack"] = achievement_MeetJack
    options["trial_and_error"] = achievement_TrialAndError
    options["who_am_i"] = achievement_WhoAmI
    options["conga_line"] = achievement_CongaLine
    options["friend_ball"] = achievement_FriendBall

    options["doh"] = achievement_Doh
    options["you_finally_turn_green"] = achievement_YouFinallyTurnGreen
    options["pro_gamer"] = achievement_ProGamer
    options["emancipation_customization"] = achievement_EmancipationCustomization
    options["cracked_gamer"] = achievement_CrackedGamer
    options["flash_point"] = achievement_FlashPoint

    options["all_crucifix"] = achievement_SecretCrucifix
    options["charles_drowned"] = achievement_CharlesDrowned

    options["hotel_hell"] = achievement_HotelHell
    options["a_hard_place"] = achievement_AHardPlace
    options["star_employee"] = achievement_StarEmployee
    options["storage_wars"] = achievement_StorageWars

    options["battle_mode_secrets"] = achievement_BattleModeSecret
    options["battle_mode_hard_secrets"] = achievement_BattleModeCool
    options["parallel_processing"] = achievement_ParallelProcessing
    options["clean_run"] = achievement_CleanRun
    options["uptime"] = achievement_Uptime
    options["daily_runs"] = achievement_DailyRuns
    options["chaos_mode"] = achievement_ChaosMode

    options["doorsanity"] = option_Doorsanity
    options["archives_doorsanity"] = option_DoorSanityArchivesType
    options["outdoors_doorsanity"] = option_DoorSanityOutdoorsType
    options["deathsanity"] = option_Deathsanity
    options["glitch_deathsanity"] = option_DeathsanityGlitch
    options["duplicate_deathsanity"] = option_DeathsanityMainDuplicates
    options["duplicate_subfloor_deathsanity"] = option_DeathsanitySubDuplicates
    options["special_deathsanity"] = option_DeathsanitySpecial
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
