import numpy as np
import matplotlib.pyplot as plt
import preprocessing as ps
import pandas as pd

data = ps.data
c1 = data[data["target"] == 1]
c2 = data[data["target"] == 2]
c3 = data[data["target"] == 3]


def get_class(class_no):
    if class_no == 1:
        return c1
    elif class_no == 2:
        return c2
    elif class_no == 3:
        return c3


def split_data_train_test(class_no1, class_no2, f1_name, f2_name):
    class1 = get_class(class_no1)
    class2 = get_class(class_no2)
    data = pd.concat([class1, class2])
    data["target"] = data["target"].replace([class_no1], 1)
    data["target"] = data["target"].replace([class_no2], -1)
    features = [f1_name, f2_name, "target"]
    selected_features = [f1_name, f2_name]
    data = data.loc[:, features]
    dat_train = pd.concat([data.iloc[0:30], data.iloc[50:80]]).sample(frac=1).reset_index()
    dat_train.pop("index")
    dat_test = pd.concat([data.iloc[30:50], data.iloc[80:100]]).reset_index()
    dat_test.pop("index")
    x_train = np.array(dat_train.loc[:, selected_features])
    y_train = np.array(dat_train.loc[:, "target"])
    y_test = np.array(dat_test.loc[:, "target"])
    x_test = np.array(dat_test.loc[:, selected_features])
    return x_train, y_train, y_test, x_test


def build_input_matrix(train_data_test, bias_boolean, for_testing_2_for_traing_1):
    modeling_data = train_data_test
    rows = 60
    colums = 3
    bias = 0
    if for_testing_2_for_traing_1 == 2:
        rows = 40
    input_matrix = np.empty([rows, colums])
    if bias_boolean == True:
        bias = 1
    for i in range(0, rows):
        input_matrix[i][0] = bias
        input_matrix[i][1] = modeling_data[i][0]
        input_matrix[i][2] = modeling_data[i][1]
    return input_matrix


def build_weights_matrix():
    weights = np.random.rand(1, 3)
    return weights


def sigum(net):
    if net >= 0:
        return 1
    return -1


def perceptron(x_training__, y_training__, weights__, learning_rate, epochs):
    w = weights__
    x = x_training__
    d = y_training__
    for j in range(0, epochs):
        for i in range(0, 60):
            v_net = np.dot(x[i], np.transpose(w))
            net = v_net[0]
            y_ = sigum(net)
            error = d[i] - y_
            if y_ != d[i]:
                w = w + error * learning_rate * x[i]
    return w


def test(x_test_ing, y_test_ing, ws):
    counter = 0
    counter_c1_true = 0
    counter_c1_false = 0
    counter_c2_true = 0
    counter_c2_false = 0
    matrix = np.empty([2, 2])
    w = ws
    x = x_test_ing
    y = y_test_ing
    for i in range(0, 40):
        v_net = np.dot(x[i], np.transpose(w))
        net = v_net[0]
        y_ = sigum(net)
        if y_ == y[i]:
            counter += 1
            if y_ == 1:
                counter_c1_true += 1
            elif y_ == -1:
                counter_c2_true += 1
        else:
            if y_ == -1 and y[i] == 1:
                counter_c1_false += 1
            elif y_ == 1 and y[i] == -1:
                counter_c2_false += 1
    matrix[0][0] = counter_c1_true
    matrix[0][1] = counter_c1_false
    matrix[1][0] = counter_c2_false
    matrix[1][1] = counter_c2_true

    acc = (counter / 40) * 100
    print("Accuracy =" + str(acc))
    print(matrix)


def draw_line(x_test_ing, y_test_ing, final_weights, f1_name, f2_name):
    feature_one_first_class = list()
    feature_two_first_class = list()
    feature_one_second_class = list()
    feature_two_second_class = list()

    for i in range(0, 20):
        if y_test_ing[i] == 1:
            feature_one_first_class.append(x_test_ing[i][1])
            feature_two_first_class.append(x_test_ing[i][2])
    for i in range(20, 40):
        if y_test_ing[i] == -1:
            feature_one_second_class.append(x_test_ing[i][1])
            feature_two_second_class.append(x_test_ing[i][2])
    minx = min(x_test_ing[:, 1])
    maxx = max(x_test_ing[:, 1])
    ymin = -1 * (final_weights[0][1] / final_weights[0][2]) * minx - final_weights[0][0] / final_weights[0][2]
    ymax = -1 * (final_weights[0][1] / final_weights[0][2]) * maxx - (final_weights[0][0] / final_weights[0][2])
    plt.scatter(feature_one_first_class, feature_two_first_class, alpha=0.5)
    plt.scatter(feature_one_second_class, feature_two_second_class, alpha=0.5)
    plt.plot((minx, maxx), (ymin, ymax))
    plt.grid()
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.title("")
    plt.legend(["class1", "class2"])
    plt.show()


def tarin_and_test_slicing__for_gui(class_no1, class_no2, f1_name, f2_name, learning_rate, epochs, boolean_bias):
    ps.plot_class(class_no1, class_no2, f1_name, f2_name)
    x_train, y_train, y_test, x_test = split_data_train_test(class_no1, class_no2, f1_name, f2_name)
    x_training = build_input_matrix(x_train, boolean_bias, 1)
    weights = build_weights_matrix()
    y_training = y_train
    x_testing = build_input_matrix(x_test, boolean_bias, 2)
    y_testing = y_test
    final_weights = perceptron(x_training, y_training, weights, learning_rate, epochs)
    draw_line(x_testing, y_testing, final_weights, f1_name, f2_name)
    test(x_testing,y_testing,final_weights)
# x_test
# y_test
