import cv2
import warnings

warnings.filterwarnings('ignore')

def pixel_difference(pixel1, pixel2, tolerance):
    return all(abs(p1 - p2) <= tolerance for p1, p2 in zip(pixel1, pixel2))

def image_similarity(image1, image2, tolerance):
    if image1.shape != image2.shape:
        raise ValueError('Goruntuler ayni boyutta olmalidir.')
    
    height, width = image1.shape[:2]
    total_pixels = height * width
    matched_pixels = 0

    for i in range(height):
        for j in range(width):
            if pixel_difference(image1[i, j], image2[i, j], tolerance):
                matched_pixels += 1

    similarity_ratio = matched_pixels * 100 / total_pixels
    return similarity_ratio

if __name__ == '__main__':
    gorsel_1 = cv2.imread('gorsel1.png')
    gorsel_2 = cv2.imread('gorsel2.png')

    tolerance_value = 20 #max=255

    similarity = image_similarity(gorsel_1, gorsel_2, tolerance_value)
    print(f'Iki gorsel arasindaki benzerlik orani: {similarity:.2f}%')
