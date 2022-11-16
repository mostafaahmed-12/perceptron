import tkinter as tk
from tkinter import *

featuress = []
classes = []


def return_features():
    if featuress.__len__() != 2:
        if x1.get() == 1:
            x = True
            for i in featuress:
                if i == "X1":
                    x = False
                    break
            if x:
                featuress.append("X1")
        if x2.get() == 1:
            x = True
            for i in featuress:
                if i == "X2":
                    x = False
                    break
            if x:
                featuress.append("X2")
        if x3.get() == 1:
            x = True
            for i in featuress:
                if i == "X3":
                    x = False
                    break
            if x:
                featuress.append("X3")
        if x4.get() == 1:
            x = True
            for i in featuress:
                if i == "X4":
                    x = False
                    break
            if x:
                featuress.append("X4")
        if x5.get() == 1:
            x = True
            for i in featuress:
                if i == "X5":
                    x = False
                    break
            if x:
                featuress.append("X5")


def return_classes():
    if classes.__len__() != 2:
        if c1.get() == 1:
            x = True
            for i in classes:
                if i == 1:
                    x = False
                    break
            if x:
                classes.append(1)
        if c2.get() == 1:
            x = True
            for i in classes:
                if i == 2:
                    x = False
                    break
            if x:
                classes.append(2)
        if c3.get() == 1:
            x = True
            for i in classes:
                if i == 3:
                    x = False
                    break
            if x:
                classes.append(3)


def return_bias():
    if bias.get() == 1:
        return True
    else:
        return False


def ret_rate_and_epoch():
    import perceptron as per
    # p.tarin_and_test_slicing__for_gui(1,2,"X1","X2",0.1,1000,True)

    per.tarin_and_test_slicing__for_gui(int(classes[0]), int(classes[1]), str(featuress[0]), str(featuress[1]),
                                        float(e1.get()), int(e2.get()), bool(return_bias()))


root = tk.Tk()
tk.Label(root, text="Select only Two features: ").pack()
x1 = tk.BooleanVar()
x2 = tk.BooleanVar()
x3 = tk.BooleanVar()
x4 = tk.BooleanVar()
x5 = tk.BooleanVar()
tk.Checkbutton(root, text="X1", variable=x1, onvalue=1, offvalue=0, command=return_features).pack()
tk.Checkbutton(root, text="X2", variable=x2, onvalue=1, offvalue=0, command=return_features).pack()
tk.Checkbutton(root, text="X3", variable=x3, onvalue=1, offvalue=0, command=return_features).pack()
tk.Checkbutton(root, text="X4", variable=x4, onvalue=1, offvalue=0, command=return_features).pack()
tk.Checkbutton(root, text="X5", variable=x5, onvalue=1, offvalue=0, command=return_features).pack()
tk.Label(root, text="Select your class only two classes: ").pack()
c1 = tk.IntVar()
c2 = tk.IntVar()
c3 = tk.IntVar()
bias = tk.IntVar()
tk.Checkbutton(root, text="c1", variable=c1, command=return_classes).pack()
tk.Checkbutton(root, text="c2", variable=c2, command=return_classes).pack()
tk.Checkbutton(root, text="c3", variable=c3, command=return_classes).pack()
tk.Label(root, text="bias : ").pack()
tk.Checkbutton(root, text="bias", variable=bias, command=return_bias).pack()

L1 = Label(root, text="learning rate")
L1.pack()
e1 = Entry(root, bd=5)
e1.pack()
L2 = Label(root, text="num of epoch")
L2.pack()
e2 = Entry(root, bd=5)
e2.pack()

b = tk.Button(root, text='train', command=ret_rate_and_epoch)
b.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()
root.mainloop()
print(featuress)
print(classes)
