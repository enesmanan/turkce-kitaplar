from PIL import Image
import numpy as np

def jaccard_similarity(matrix1, matrix2):
    intersection = np.logical_and(matrix1, matrix2)
    union = np.logical_or(matrix1, matrix2)
    return intersection.sum() / union.sum()

def png_to_matrix(file_path):
    img = Image.open(file_path).convert('L')
    img_arr = np.array(img)
    return img_arr

file1 = 'gorsel1.png'
file2 = 'gorsel2.png'


matrix1 = png_to_matrix(file1)
matrix2 = png_to_matrix(file2)

similarity = jaccard_similarity(matrix1, matrix2)

print(f'Benzerlik orani: {similarity}')