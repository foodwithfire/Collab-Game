class Player:

    def __init__(self, player_health, player_damage, mana, player_level, placeholder, player_pos, player_weapon):
        self.player_health = player_health
        self.player_damage = player_damage
        self.mana = mana
        self.player_level = player_level
        self.player_inventory = placeholder  # Awaiting to create the inventory class which will consist of a dictionary
        self.player_pos = player_pos
        self.player_weapon = player_weapon
        
