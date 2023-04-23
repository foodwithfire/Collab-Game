import os  # Not used yet
import json

if os.path.exists("saves/save.json"):
    exists = True
else:
    exists = False

if exists:
    inventory = "prout"
else:
    hotbar = {
        "hotbar1": None,
        "hotbar2": None,
        "hotbar3": None,
        "hotbar4": None,
        "hotbar5": None,
        "hotbar6": None,
        "hotbar7": None,
        "hotbar8": None,
        "hotbar9": None
    }
    inventory_slots = {
        "slot1": None,
        "slot2": None,
        "slot3": None,
        "slot4": None,
        "slot5": None,
        "slot6": None,
        "slot7": None,
        "slot8": None,
        "slot9": None,
        "slot10": None,
        "slot11": None,
        "slot12": None,
        "slot13": None,
        "slot14": None,
        "slot15": None,
        "slot16": None,
        "slot17": None,
        "slot18": None,
        "slot19": None,
        "slot20": None,
        "slot21": None,
        "slot22": None,
        "slot23": None,
        "slot24": None,
        "slot25": None,
        "slot26": None,
        "slot27": None,
    }