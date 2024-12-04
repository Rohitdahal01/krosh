import pygame
import random

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Helicopter vs Mythical Creature")
clock = pygame.time.Clock()

# Game variables
PLAYER_HEALTH = 50
ENEMY_HEALTH = 100
BULLET_DAMAGE = 1
ENEMY_BULLET_DAMAGE = 2

# Load assets
player_image = pygame.image.load("assets/hellicopter.jpg")
enemy_image = pygame.image.load("assets/download.jpg")
background_image = pygame.image.load("assets/bc.jpg")
player_bullet_image = pygame.image.load("assets/bullet.jpg")
enemy_bullet_image = pygame.image.load("assets/bullet.jpg")

# Load sound effects
try:
    player_fire_sound = pygame.mixer.Sound("Sounds/PlayerBullet.wav")
    enemy_fire_sound = pygame.mixer.Sound("Sounds/PlayerBullet.wav")
except pygame.error as e:
    print(f"Error loading sound: {e}")

# Load background music (make sure the path is correct)
pygame.mixer.music.load("Sounds/background.wav")  # Add the correct music file path here
pygame.mixer.music.set_volume(0.1)  # Set the volume level of the background music (0.0 to 1.0)
pygame.mixer.music.play(-1, 0.0)  # Play the music indefinitely

# Resize assets
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.transform.scale(enemy_image, (70, 70))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_bullet_image = pygame.transform.scale(player_bullet_image, (10, 5))
enemy_bullet_image = pygame.transform.scale(enemy_bullet_image, (10, 5))

# Player class
class Player:
    def __init__(self):
        self.image = player_image
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.health = PLAYER_HEALTH
        self.speed = 5
        self.bullets = []

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(screen.get_rect())  # Keep player within screen bounds

    def shoot(self):
        if len(self.bullets) < 5:  # Limit bullets on screen
            if 'player_fire_sound' in globals():
                player_fire_sound.play()  # Play the bullet firing sound
            bullet = pygame.Rect(self.rect.centerx, self.rect.centery, 10, 5)
            self.bullets.append(bullet)

    def draw(self):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            pygame.draw.rect(screen, WHITE, bullet)

# Enemy class
class Enemy:
    def __init__(self):
        self.image = enemy_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2))
        self.health = ENEMY_HEALTH
        self.speed = 2
        self.bullets = []

    def move(self, player_rect):
        # Basic AI to move toward the player
        if self.rect.y < player_rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player_rect.y:
            self.rect.y -= self.speed

    def shoot(self):
        if len(self.bullets) < 5 and random.randint(0, 20) == 0:  # Random shooting
            if 'enemy_fire_sound' in globals():
                enemy_fire_sound.play()  # Play the enemy shooting sound
            bullet = pygame.Rect(self.rect.centerx - 10, self.rect.centery, 10, 5)
            self.bullets.append(bullet)

    def draw(self):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            pygame.draw.rect(screen, RED, bullet)

# Health bar function
def draw_health_bar(x, y, current_health, max_health, color_fg, color_bg):
    pygame.draw.rect(screen, color_bg, (x, y, 100, 10))  # Background
    health_width = 100 * (current_health / max_health)
    pygame.draw.rect(screen, color_fg, (x, y, health_width, 10))

# Initialize player and enemy
player = Player()
enemy = Enemy()

# Main game loop
running = True
while running:
    screen.blit(background_image, (0, 0))  # Draw the background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Player movement controls
    keys = pygame.key.get_pressed()
    dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    player.move(dx, dy)

    # Enemy movement and shooting
    enemy.move(player.rect)
    enemy.shoot()

    # Update bullets and check collisions
    for bullet in player.bullets[:]:
        bullet.x += 10
        if bullet.colliderect(enemy.rect):
            enemy.health -= BULLET_DAMAGE
            player.bullets.remove(bullet)
        elif bullet.x > SCREEN_WIDTH:
            player.bullets.remove(bullet)

    for bullet in enemy.bullets[:]:
        bullet.x -= 10
        if bullet.colliderect(player.rect):
            player.health -= ENEMY_BULLET_DAMAGE
            enemy.bullets.remove(bullet)
        elif bullet.x < 0:
            enemy.bullets.remove(bullet)

    # Check game-over conditions
    if player.health <= 0 or enemy.health <= 0:
        running = False
        print("Game Over!")  # Replace with a game-over screen if needed

    # Draw game elements
    player.draw()
    enemy.draw()
    draw_health_bar(10, 10, player.health, PLAYER_HEALTH, GREEN, RED)
    draw_health_bar(SCREEN_WIDTH - 110, 10, enemy.health, ENEMY_HEALTH, GREEN, RED)

    pygame.display.flip()
    clock.tick(30)  # Limit to 30 FPS

pygame.quit()
