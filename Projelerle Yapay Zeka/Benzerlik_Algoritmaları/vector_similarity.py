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
    
    

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 128, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
purple = [128, 0, 128]


similarity_calculator = VectorSimilarity()

black_normalized = similarity_calculator.arrange(black)
white_normalized = similarity_calculator.arrange(white)
red_normalized = similarity_calculator.arrange(red)
green_normalized = similarity_calculator.arrange(green)
blue_normalized = similarity_calculator.arrange(blue)
yellow_normalized = similarity_calculator.arrange(yellow)
purple_normalized = similarity_calculator.arrange(purple)


similarity = similarity_calculator.calculate_similarity(red_normalized, purple_normalized)
print(similarity)