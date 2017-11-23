class Config:
    display_width = 800
    display_height = 600
    white = (255,255,255)
    apple_x = display_width * 0.7
    apple_y = display_height * 0.2
    banana_x = display_width * 0.5
    banana_y = display_height * 0.5
    head_x = display_width * 0.5
    head_y = display_height * 0.5
    body_x = []
    body_y = []
    directions = {"Left":0,"Up":1,"Right":2,"Down":3}
    direction =directions["Right"]
    speed = 1
    boost_lenght = 150