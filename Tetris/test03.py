import sys
import pygame as pg


class Player(pg.sprite.Sprite):

    def __init__(self, pos, color):
        super().__init__()
        self.image = pg.Surface((50, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    player = Player((100, 100), pg.Color('dodgerblue2'))
    enemy = Player((300, 100), pg.Color('sienna2'))
    enemy2 = Player((200, 300), pg.Color('sienna2'))
    all_sprites = pg.sprite.Group(player, enemy, enemy2)
    enemies = pg.sprite.Group(enemy, enemy2)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEMOTION:
                player.rect.center = event.pos

        all_sprites.update()

        collided_enemies = pg.sprite.spritecollide(player, enemies, False)
        for collided_enemy in collided_enemies:
            print(collided_enemy.rect)

        screen.fill((50, 50, 50))
        all_sprites.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()