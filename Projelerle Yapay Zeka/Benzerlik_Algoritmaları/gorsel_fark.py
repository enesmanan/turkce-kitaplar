from PIL import Image ,ImageChops

def gorselFark(gorsel_1, gorsel_2):
    
    gorsel_fark = ImageChops.difference(gorsel_1, gorsel_2)
    
    if gorsel_fark.getbbox():
        gorsel_fark.show()
        gorsel_fark.save('fark.png')


if __name__ == '__main__':
    gorsel_1 = Image.open('gorsel1.png')
    gorsel_2 = Image.open('gorsel2.png')
    gorselFark(gorsel_1, gorsel_2)