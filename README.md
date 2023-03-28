# Classification-method-with-the-Decision-Tree-Method-Based-on-the-Diabetes-Dataset

This project is an implementation of the classification method, where the method used is the decision tree method. The dataset used is the dataset that has been given before, namely the diabetes dataset and its causal factors. Before processing the data, the value of the target or dependent variable, namely the diabetes test result variable (tested_positive and tested_negative), is labeled by an encoder to convert its value to numeric, which in this case is binary (1 and 0). The feature variables of the classification above are preg, plas, pres, skin, insu, mass, and pedi, while the target variable is the class column containing the test results. Then, the data is divided into training and test data, where in this method, a test size ratio of 0.3 is used, or 70% training and 30%.

<p align="center">
<img width=400px height=auto alt="image" src="https://user-images.githubusercontent.com/78911479/228196988-28d5d274-ae2c-4a3a-a60b-103e8d49b442.png">
</p>

The result or output of this program is the percentage of the accuracy of the decision tree model for the classifier or training and test objects. The accuracy value is 0.63157… or 63%, so it can be said that this decision tree model is quite accurate. In addition, the output also produces a visualization of the decision tree model in the form of a tree diagram which is plotted using the plot_tree syntax and saved locally in the form of PNG.

<p align="center">
<img width=400px height=auto alt="image" src="https://user-images.githubusercontent.com/78911479/228197176-e595f48b-b64e-4c72-b1d4-21012e384894.png">
</p>
