import numpy as np

# 1'den 1000'e kadar olan sayilardan olusan numpy array
array = np.arange(1, 1001)

# 18 ile tam bolunen sayilari sec
secim = array[array % 18 == 0]

print(secim)
#[ 18  36  54  72  90 108 126 144 162 180 198 216 234 252 270 288 306 324
# 342 360 378 396 414 432 450 468 486 504 522 540 558 576 594 612 630 648
# 666 684 702 720 738 756 774 792 810 828 846 864 882 900 918 936 954 972
# 990]