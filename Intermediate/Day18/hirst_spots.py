import colorgram
import turtle as t
import random


def get_colors_from(image_path, colour_count):
    rgb_colours = []
    extracted_colors = colorgram.extract(image_path, colour_count)
    for c in extracted_colors:
        rgb_colours.append((c.rgb.r, c.rgb.g, c.rgb.b))
    
    return rgb_colours

# Extracted via get_colors_from("C:\Code\Python\Python100d\Intermediate\Day18\image.jpg", 32)
# with background colors removed.
filtered_colours = [(173, 164, 153), (229, 223, 225), 
                    (133, 88, 70), (56, 106, 134), (201, 139, 155), (134, 181, 151), (133, 166, 182), 
                    (218, 198, 142), (137, 75, 89), (61, 121, 88), (210, 87, 71), (76, 160, 106), (198, 88, 109), 
                    (33, 45, 62), (134, 145, 82), (225, 177, 166), (222, 170, 179), (72, 151, 167), 
                    (164, 207, 186), (51, 40, 44), (56, 44, 37), (39, 55, 48), (25, 90, 81), (111, 118, 156), 
                    (124, 38, 46), (17, 92, 101), (118, 43, 36), (166, 201, 210), (38, 62, 98)]

def draw_hirst_image():
    t.colormode(255)
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.speed(9)

    turtle.penup()
    turtle.goto(-250.00,-250.00)

    spacing = 50
    for _ in range(10):
        row_start_position = turtle.position()

        for _ in range(10):
            turtle.pendown()
            turtle.dot(20, random.choice(filtered_colours))
            turtle.penup()
            turtle.forward(spacing)

        turtle.penup()
        turtle.goto(row_start_position[0], row_start_position[1]+spacing)
            
    
    screen = t.Screen()
    screen.exitonclick()


draw_hirst_image()