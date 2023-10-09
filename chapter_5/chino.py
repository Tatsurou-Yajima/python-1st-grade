import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy as np

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    resizedGrayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    displayImage = PIL.ImageTk.PhotoImage(resizedGrayImage.resize((300, 300), resample=0))
    imageLabel.configure(image=displayImage)
    imageLabel.image = displayImage
    numImage = np.asarray(resizedGrayImage, dtype=float)
    formattedNumImage = 16 - np.floor(17 * numImage / 256)
    return formattedNumImage.flatten()

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    textLabel.configure(text="この画像は"+str(n)+"です。")

def openFile():
    filePath = fd.askopenfilename()
    if filePath:
        data = imageToData(filePath)
        predictDigits(data)

root = tk.Tk()
root.geometry("400x400")

button = tk.Button(root, text="画像ファイルを選択", command=openFile)
imageLabel = tk.Label()

button.pack()
imageLabel.pack()

textLabel = tk.Label(text="手書きの数字を認識します！")
textLabel.pack()

tk.mainloop()
