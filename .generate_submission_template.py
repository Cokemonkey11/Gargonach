#!/usr/bin/env python
import sys
import textwrap


MAP_NAME           = "Gargonach"
AUTHOR             = "Cokemonkey11"


INTRODUCTION = (

    """

        Gargonach is my entry for the solo mini-mapping contest #7, whose theme
        was "Boss Fight". This map is inspired from a boss in the original Half-
        Life story called "Gonarch". The game centers around killing him with
        your main character, Don Rogo, using various paladin spells and by
        completing intermediate goals to ease your mission.

    """,

    """

        For centuries Gargonach rained terror on the world of Azeroth,
        unleashing his Nerubian warriors on the alliance's pitiful creatures so
        limited in magic and technology. No warrior could match the sheer
        brutality of an inter-dimensional species, controlling the elements, and
        the forces of the Universe. No one until Don Rogo.

    """,
)


SCREENSHOTS = (
    ("Divine Shield Spell", "https://i.imgur.com/KLXhNJu.png"),
)


ABILITIES = (
    (
        "https://i.imgur.com/xSoqYuZ.png",
        (
            "Don Rogo: Your hero.",
        )
    ),
    (
        "https://i.imgur.com/7NdWrM3.png",
        (
            "Attack: In Gargonach, Don Rogo will only attack when ordered to.",
        )
    ),
    (
        "https://i.imgur.com/uyLf194.png",
        (
            "Hammerthrow: Don Rogo throws his weapon in the target direction. He must pick it back up before attacking again.",
        )
    ),
    (
        "https://i.imgur.com/aYJ1lvl.png",
        (
            "Divine Shield: Creates a temporary shield which is impassible by evil attacks.",
        )
    ),
    (
        "https://i.imgur.com/t7CdGmv.png",
        (
            "Lighthopping: Jumps in the target direction in two delayed bursts of light.",
        )
    ),
    (
        "https://i.imgur.com/GGa2U3X.png",
        (
            "Ragnorak: After channeling for a short time, Thor's hammer falls from the sky, dealing massive damage and stunning enemy ground units.",
        )
    ),
)

REPOSITORY_URI = "https://bitbucket.org/Cokemonkey11/gargonach/"

CHANGELOG = (
    (
        "0.1.1",
        "28 Mar 2021",
        (
            "Crypt crabs now pursue the player.",
            "Crypt crabs can now die in lava.",
            "Crypt crabs now have a timed life.",
            "Gargonach's 'smokestack' ability now does 50% more damage (300).",
            "Gargonach's 'smokestack' ability now knocks up with more power.",
            "Gargonach's 'smokestack' ability has improved effects and sounds.",
            "Don Rogo can no longer die during the Victory special-effects.",
            "Removed the incomplete change-log from the quests menu.",
        )
    ),
    (
        "0.1.0",
        "22 June 2019",
        (
            "Gargonach's attacks no longer register as hit if you're airborne.",
            "Gargonach now has another attack in its repertoire: spawn crabs.",
            "Reworked healing fountain to provide more gameplay interaction.",
            "The map triggers are now fully translated to WurstScript.",
            "The map now uses the wurstStdLib2.",
            "Minor cosmetic tooltip improvements.",
        )
    ),
    (
        "0.0.9",
        "16 August 2016",
        (
            "The map triggers are now fully translated to WurstScript compliant Jurst.",
            "Fixed issue #13 which deselected Don Rogo during revive animation.",
            "Fixed issue #12 which allowed the player to select the revive animation sprites.",
            "Fixed issue #17 which allowed the player to select the hammer after using Hammerthrow.",
            "Fixed issue #15 which allowed the player to select the Shield blobs when using Divine Shield.",
            "Made Gargonach's Smokestack ability stronger (#18).",
            "Adjusted which Don Rogo spells provide a stun effect.",
            "The map now uses a black fog mask (#19).",
            "Minor QoL terrain improvements.",
            "Fixed issue #16 which allowed players to spam the Hammerthrow ability over and over without cooldown.",
            "Ragnorak no longer affects structures.",
            "Fountain now heals significantly slower.",
            "Fountain wisps are less goofy looking.",
        )
    ),

    (
        "0.0.8",
        "22 May 2012",
        (
            "First patch fixing a bug with don rogo attack spell and lighthopping tooltip.",
            "Fixed some pathing blocker positions.",
            "Small interface change.",
        )
    ),

    (
        "0.0.7",
        "17 May 2012",
        (
            "Initial version uploaded to hiveworkshop.com as contest entry.",
        )
    ),
)

HOSTING      = False
CONTRIBUTING = "I will merge atomic, well-formed pull-requests if they are consistent with my design policies and issue tracker."

def write(st):
    sys.stdout.write(st)


def print_section_header(title):
    write("[R][H3][color=#CCAA00]" + title + "[/color][/H3][R]\n")


def get_paragraph(paragraph):
    p = paragraph.strip().replace('\n', ' ').replace('\t', '')
    return textwrap.fill(p, width=90) + "\n\n"


def print_paragraph(paragraph):
    write(get_paragraph(paragraph))


def print_header():
    write("[CENTER]\n[TABLE]\n[CENTER]\n[H3][color=#60A600]")
    write(MAP_NAME)
    write("[/color][/H3]\n[color=#CCAA00][B]A map by ")
    write(AUTHOR)
    write("[/B][/color]\n\n")


def print_contents():
    write("[BOX=Contents]")
    if INTRODUCTION:
        write("* Introduction\n")
    if SCREENSHOTS:
        write("* Screenshots\n")
    if ABILITIES:
        write("* Abilities\n")
    if REPOSITORY_URI:
        write("* Version Control\n")
    if CHANGELOG:
        write("* Changelog\n")
    if HOSTING:
        write("* Hosting\n")
    if CONTRIBUTING:
        write("* Contributing\n")
    write("[/BOX]\n[/CENTER]\n\n")


def print_introduction():
    if INTRODUCTION:
        print_section_header("Introduction")
        for paragraph in INTRODUCTION:
            print_paragraph(paragraph)

def print_screenshots():
    if SCREENSHOTS:
        print_section_header("Screenshots")
        write("\n\n")
        for shot in SCREENSHOTS:
            write("[hidden=" + shot[0] + "]\n[img]" + shot[1] + "[/img]\n[/hidden]\n\n")


def print_abilities():
    if ABILITIES:
        print_section_header("Abilities")
        write("\n\n[table]\n")
        for race in ABILITIES:
            write("[tr]\n[td][img]" + race[0] + "[/img][/td]\n[td]")
            for paragraph in race[1][0:-1]:
                print_paragraph(paragraph)
            write(get_paragraph(race[1][-1])[0:-2])
            write("[/td]\n[/tr]\n")
        write("[/table]\n\n")


def print_repository_uri():
    if REPOSITORY_URI:
        print_section_header("Version Control")
        write("\n\n")
        print_paragraph("All iterations of this map are maintained in a public git repository at [url]" + REPOSITORY_URI + "[/url]")


def print_changelog():
    if CHANGELOG:
        print_section_header("Changelog")
        write("\n\n")
        for log in CHANGELOG[0:5]:
            write("[color=#ffcc00]" + log[0] + "[/color] [color=#999999]" + log[1] + "[/color]:\n[list]")
            for point in log[2]:
                write(get_paragraph("[*] " + point)[0:-2] + "\n")
            write("[/list]\n\n")

        if CHANGELOG[5:]:
            write("[hidden=Older Changes")
            for log in CHANGELOG[5:]:
                write("[color=#ffcc00]" + log[0] + "[/color] [color=#999999]" + log[1] + "[/color]:\n[list]")
                for point in log[2]:
                    write(get_paragraph("[*] " + point)[0:-2] + "\n")
                write("[/list]\n\n")
            write("[/hidden]")


def print_hosting():
    if HOSTING:
        print_section_header("Automatic Hosting")
        print_paragraph("Release versions of this map are uploaded to both [url=http://makemehost.com/]MMH[/url] and [url=http://entgaming.net/]ENT[/url].")


def print_contributing():
    if CONTRIBUTING:
        print_section_header("Contributing")
        print_paragraph(CONTRIBUTING)


def print_footer():
    write("[/TABLE]\n[/CENTER]\n")

print_header()
print_contents()
print_introduction()
print_screenshots()
print_abilities()
print_repository_uri()
print_changelog()
print_hosting()
print_contributing()
print_footer()
