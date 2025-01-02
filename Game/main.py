import pygame as pg

pg.init()

screen = pg.display.set_mode((1280,720))

clock = pg.time.Clock()

# load SR
SR_jpg = pg.image.load("summoners_rift.jpg").convert()


while True:
    # Process player inputs.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    pg.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)


    


