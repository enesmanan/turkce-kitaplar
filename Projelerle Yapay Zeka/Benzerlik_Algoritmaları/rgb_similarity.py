class VectorSimilarity:
    def __init__(self, min_val=0, max_val=255):
        self.min_val = min_val
        self.max_val = max_val

    def arrange(self, item):
        item_count = len(item)
        normalized_item = []
        for i in range(item_count):
            if i <= item_count:
                normalized_value = item[i] / ((self.max_val - self.min_val) / 100)
                normalized_item.append(normalized_value)
            else:
                normalized_value = 50 / ((self.max_val - self.max_val) / 100)
        
        return normalized_item
    
    @staticmethod
    def sqrt(value):
        return value ** (1/2)
    
    @staticmethod
    def power(value, level=2):
        return value ** level
    
    def calculate_similarity(self, A, B):
        if len(A) != len(B):
            return -1
        
        len_ = len(A)
        total = 0

        for i in range(len_):
            total += self.power(B[i] - A[i])

        distance = self.sqrt(total)
        max_dist = self.sqrt(self.power(100) * len_)

        return 1 - (distance / max_dist)
    
    @staticmethod
    def normalized(color):
        return VectorSimilarity().arrange(color)
    

# RGBCodes_normalized.txt
def read_normalized_txt(file_name):
    normalized_colors = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                color, rgb_values = line.split(':')
                rgb_values = [float(val) for val in rgb_values.strip().strip('[]').split(',')]
                normalized_colors[color] = rgb_values
    return normalized_colors


def get_most_similar_colors(input_colors, normalized_colors):
    vector_similarity = VectorSimilarity()
    similarity_scores = {}
    
    for color, normalized_values in normalized_colors.items():
        similarity = 0
        for input_color in input_colors:
            similarity += vector_similarity.calculate_similarity(input_color, normalized_values)
        similarity_scores[color] = similarity
    
    sorted_colors = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors[:3]


normalized_colors = read_normalized_txt('RGBCodes_normalized.txt')

user_input = []
for i in range(1):
    r = int(input('Enter the value of R: '))
    g = int(input('Enter the value of G: '))
    b = int(input('Enter the value of B: '))
    user_input.append(VectorSimilarity.normalized([r, g, b]))

most_similar_colors = get_most_similar_colors(user_input, normalized_colors)

print('Most similar colors:')
for color, similarity in most_similar_colors:
    print(color, similarity)
