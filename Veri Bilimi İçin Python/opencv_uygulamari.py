import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    root = tk.Tk()
    root.withdraw()

    image_file = filedialog.askopenfilename()
    r1 = cv2.imread(image_file)

    cv2.imshow('r_tusuna_bas', r1)
    messagebox.showinfo('Bilgilendirme', 'Resmi dondurmek icin r tusuna, gri yapmak icin g tusuna, blur efekti icin b tusuna basiniz!')

    griMi = False
    blurMu = False

    while True:
        key = cv2.waitKey(1)
        if key == ord('r'):
            dondur = cv2.rotate(r1, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow('r_tusuna_bas', dondur)
            cv2.waitKey(0)
            dondur = cv2.rotate(dondur, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow('r_tusuna_bas', dondur)
            cv2.waitKey(0)
            dondur = cv2.rotate(dondur, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow('r_tusuna_bas', dondur)
            cv2.waitKey(0)
            dondur = cv2.rotate(dondur, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow('r_tusuna_bas', dondur)
        elif key == ord('g'):
            if griMi:
                cv2.imshow('r_tusuna_bas', r1)
                griMi = False
            else:
                gri = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)
                cv2.imshow('r_tusuna_bas', gri)
                griMi = True
        elif key == ord('b'):
            if blurMu:
                cv2.imshow('r_tusuna_bas', r1)
                blurMu = False
            else:
                blur = cv2.blur(r1, (15,15))
                cv2.imshow('r_tusuna_bas', blur)
                blurMu = True
        elif key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()