class Player:

    def __init__(self, player_name, player_health, player_damage, mana, player_level, placeholder, player_pos, player_weapon):
        self.player_name = player_name
        self.player_health = player_health
        self.player_damage = player_damage
        self.mana = mana
        self.player_level = player_level
        self.player_inventory = placeholder  # Awaiting to create the inventory class which will consist of a dictionary
        self.player_pos = player_pos
        self.player_weapon = player_weapon

    def get_player_name(self):
        return self.player_name

    def get_player_health(self):
        return self.player_health

    def get_player_damage(self):
        return self.player_damage

    def get_mana(self):
        return self.mana

    def get_player_level(self):
        return self.player_level

    def get_player_pos(self):
        return self.player_pos

    def get_player_weapon(self):
        return self.player_weapon
    
