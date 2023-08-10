from colorthief import ColorThief


def get_dominant_colour(image_path):
    colour = ColorThief(image_path)

    dominant_colour = colour.get_color(quality=1)
    
    return dominant_colour

def main():
    dominant_colour = get_dominant_colour("img/DeepSeaPoncho.png")

    print("Colour:", dominant_colour)

main()
