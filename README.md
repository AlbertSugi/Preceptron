# Overview
The task is to implement a [Perceptron Model](https://en.wikipedia.org/wiki/Perceptron#Learning_algorithm) from scratch to further understand how artificial neural network works.<br/>
A ***Perceptron*** is used to define a hyperplane which divides the input space into two half-spaces and can be used to make binary classification.
<p align="center">
  <img width="460" height="300" src="https://github.com/AlbertSugi/Preceptron/blob/master/Perceptron.png"><br/>
</p><br/>

# Learning Boolean Functions 
A boolean function is a two-class classification problem- the inputs are binary and the output is 1 if the corresponding function value is true and 0 otherwise. <br/>
Functions like AND and OR are linearly separable and are solvable using the perceptron.<br/>
<p align="center">
  <img src="https://github.com/AlbertSugi/Preceptron/blob/master/AND%20Function.jpg"><br/>
</p><br/>
Functions like XOR cannot be solved with the simple perceptron because their graphs are not linearly separable. Hence, there is no single line/hyperplane that can divide the input space into two classes. Note that a multilayer perceptron (MLP) can be used to solve problems like the XOR.<br/>
<p align="center">
  <img src="https://github.com/AlbertSugi/Preceptron/blob/master/XOR%20Function.jpg"><br/>
</p><br/>

# Perceptron Model
In this task, I created a Perceptron class which consists of four methods:<br/>
* ***initial***        : defines the initial weight and the learning rate (adjust the learning rate here)
* ***output***         : calculates wTxT within each sample
* ***update weights*** : updates the weight of each sample based on learning rate and error produced (Wt = Wt + learning rate*(true label – predicted label))
* ***train***          : trains dataset by iterating each data, updating their weights, and reaching the minimum error.<br/> 

There are 3 other methods outside the Perceptron class:
* ***UnSepGenerateData*** :generates random unseparable data
* ***SepGenerateData***   :generates random seperable data
* ***plotgraph***         :a graph generated by running the Perceptron class, showing whether a dataset is linearly separable 

# Running The Application
Open Perceptron.py in your selected python IDE. Use command ***plotGraph(Dataset,train,test,epoch)*** 
* Dataset: Type of desired dataset: UnSepGenerateData or SepGenerateData
* train  : number of training data desired
* test   : number of testing data desired
* epoch  : number of epoch training the Perceptron

# Output
### Seperable Dataset
The output of a seperable dataset will have a graph with similar to the following graph shown:
<p align="center">
  <img  src="https://github.com/AlbertSugi/Preceptron/blob/master/Seperable1.png"><br/>
</p><br/>

### Unseperable Dataset
The output of an unseperable dataset will have a graph with similar to the following graph shown:
<p align="center">
  <img  src="https://github.com/AlbertSugi/Preceptron/blob/master/Unseperable.png"><br/>
</p><br/>
