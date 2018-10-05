#Preceptron
For this task, I created a Perceptron model that consists of four functions inside 
a class: initial, output, update weights, and train. The initial function’s purpose is 
to define the initial weight given to each data and the learning rate of the perceptron, 
which in this case is 0.1. The output function is a calculation of Weight*t and X*t for 
each data, which will return 1 if the output is greater than or equal to 0, and -1 if 
the output is smaller than 0. Update weights performs the 
following calculation: Wt = Wt + learning rate*(true label – predicted label), which adjusts 
the weight of one data based on the result of learning rate multiplied by error produced from 
the subtraction of true label – predicted label. Last is the train function, which trains every 
dataset by iterating each data per epoch set, updating their weights, and summing up the total 
Error of the dataset. It will stop only if the total error equals to 0 or has reached the number 
of epochs set.<br/>

For separable dataset, I created a random generator which would create n points (in this case n = 100), by limiting them to (2n-1/2)-/+0.5. After implementing the perceptron using the dataset the result shows that it separated the dataset with 100% accuracy. The chart is as follows:<br/>
<p align="center">
  <img width="460" height="300" src="https://github.com/AlbertSugi/Preceptron/blob/master/Seperable.JPG"><br/>
Seperable Dataset <br/>
</p><br/>

For inseparable dataset, I created a random generator which would create n points (in this case n = 100) using only (2n-1)/2 for both blue and red. After implementing the perceptron using the dataset the result shows that it is unable to separate the dataset. The chart is as follows:<br/>

<p align="center">
  <img width="460" height="300" src="https://github.com/AlbertSugi/Preceptron/blob/master/Unseperable.JPG"><br/>
Unseperable Dataset <br/>
</p><br/>
