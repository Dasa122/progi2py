class VideoGameCharacter:
    def __init__(self, name, game, health, strength, stamina):
        self.name = name
        self.game = game
        self.health = health
        self.strength = strength
        self.stamina = stamina 
        self.level = 1  # New property
        self.experience = 0  # New property

    def __str__(self):
        return f"A {self.name} tulajdonsagai: game={self.game}, health={self.health}, strength={self.strength}, stamina={self.stamina}, level={self.level}, experience={self.experience}"

    def is_strong(self):
        return self.strength > 75
    
    def is_stamina_high(self):
        return self.stamina > 80

    def level_up(self):
        self.level += 1
        self.experience = 0  # Reset experience on level up

    def gain_experience(self, points):
        self.experience += points
        if self.experience >= 100:  # Example threshold for leveling up
            self.level_up()

    def save_info(self, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(self) + '\n')
    

characters = []

def strongest(character):
    if not characters:
        return False
    max_strength = max(c.strength for c in characters)
    return max_strength


def create_characters():
    char1 = VideoGameCharacter("Arthas", "Warcraft", 100, 80, 70)
    char2 = VideoGameCharacter("Master Chief", "Halo", 120, 90, 85)
    char3 = VideoGameCharacter("Lara Croft", "Tomb Raider", 90, 70, 95)
    char4 = VideoGameCharacter("Mario", "Super Mario", 80, 60, 80)
    char5 = VideoGameCharacter("Link", "The Legend of Zelda", 110, 75, 90)
    characters.append(char1)
    characters.append(char2)
    characters.append(char3)
    characters.append(char4)
    characters.append(char5)
    

def main():
    create_characters()
    print("Erős karakterek (strength > 75):")
    for character in characters:
        if character.is_strong():
            print(character)
    
    print("\nMagas állóképességű karakterek (stamina > 80):")
    for character in characters:
        if character.is_stamina_high():
            print(character)

    print("\nErősebb karakterek (strength > 75):")
    for character in characters:
        if character.is_strong():
            print(character)
    

    print("\nLegerősebb karakterek:")
    for character in characters:
        if strongest(character):
            print(character)

    for character in characters:
        character.save_info("character_info.txt")


main()