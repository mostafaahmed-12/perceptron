# perceptron
single layer perceptron implementation in python
Task 1 – Dataset (Penguins)
The data set consists of 50 samples from each of three species of Penguins (Adelie, Gentoo and Chinstrap).  

Five features were measured from each sample: bill_length, bill_depth, flipper_length, gender and body_mass, (in millimeter)
Task 1 - GUI
User Input:
 Select two features
 Select two classes (C1 & C2 or C1 & C3 or C2 & C3)
 Enter learning rate (eta)
 Enter number of epochs (m)
 Add bias or not (Checkbox)

Initialization:
Number of features = 2.
Number of classes = 2.
Weights + Bias = small random numbers

Classification:
 Sample (single sample to be classified).
![image](https://user-images.githubusercontent.com/77200939/202291182-83672fbf-14bb-45f6-a1c9-c236a8dcbc84.png)
Visualize Penguins dataset
Penguins' dataset contains 150 samples (50 samples/class). Each sample consists of 5 features.
The first part of task(1) is analyzing the data and making a simple report to know the linear/non-linear separable features. HINT: Drawing all possible combinations of features like (X1, X2), (X1, X3), (X1, X4), (X2, X3), (X2, X4), etc as shown in the following figure and determine which features are discriminative between which classes
![image](https://user-images.githubusercontent.com/77200939/202291239-c15a4c9e-8491-4ff3-aaaf-f1bd7bb44e22.png)
Implement the Perceptron learning algorithm
Single layer neural networks which can be able to classify a stream of input data to one of a set of predefined classes.

Use the penguins data in both your training and testing processes. (Each class has 50 samples: train NN with 30 non-repeated samples randomly selected, and test it with the remaining 20 samples)
![image](https://user-images.githubusercontent.com/77200939/202291287-614bebfe-e483-4247-a2c6-7c7abeefe3f2.png)
After training
Draw a line that can discriminate between the two learned classes. You should also scatter the points of both classes to visualize the behavior of the line.
Test the classifier with the remaining 20 samples of each selected classes and find confusion matrix and compute overall accuracy.
![image](https://user-images.githubusercontent.com/77200939/202291339-838617ff-4ded-4f71-84b1-360705cf718f.png)



