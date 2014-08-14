##Identify a relationship that you would like to approximate with simple linear regression. 
You could regress the heights of dogs onto their weights, the average price of an entree onto average Yelp scores, etc. Submit a few sentences describing the explanatory variable, response variable, and the relationship between them.

##Collect (or fabricate) toy training and test sets. 
These sets both require only 5-10 instances. Submit the training and test sets.

###Training Data
I made 100% made this up.

| Training Instance | Length Of Hair (inches) | Happiness Level |
|:-----------------:|:-----------------------:|:---------------:|
|         1         |            10           |        20       |
|         2         |            19           |        35       |
|         3         |             1           |        7        |
|         5         |            39           |        65       |
|         6         |            53           |       122       |
|         7         |             4           |        13       |


###Testing Data
I also 110% made this up. Scared to see the results.

| Testing Instance  | Length Of Hair (inches) | Happiness Level |
|:-----------------:|:-----------------------:|:---------------:|
|         1         |           12            |        28       |
|         2         |           15            |        65       |
|         3         |           19            |        77       |
|         5         |           79            |        165      |
|         6         |           6             |        12       |
|         7         |           15            |        35       |

## Calculate the values of the model parameters that minimize the cost function. 
Refer to the lab or the lecture's slides to calculate the variance of your explanatory variable and the covariance of your explanatory and response variables. Submit your model parameters.

###[HERE IS THE SPREADSHEET I DID EVERYTHING IN](https://docs.google.com/spreadsheets/d/1UDDXwMpb7gP-1wYCwe2JiTtb-VRY4VhYFc3QeYarKhI/edit?usp=sharing)



## Predict the values of the response variable for the test instances. 
Calculate your model's r-squared score on the test set, and interpret it in a sentence or two. Submit the r-squared score.



###The Predictions
It seemed ok(ish?). Still working through what is "acceptable" for predicting things. :)

| Testing Instance  | Length Of Hair (inches) | Happiness Level | Happiness PREDICTION |
|:-----------------:|:-----------------------:|:---------------:|:---------------:|
|         1         |           12            |        28       |25.25454826|
|         2         |           15            |        65       |31.39192106|
|         3         |           19            |        77       |39.5750848|
|         5         |           79            |        165      |162.3225409|
|         6         |           6             |        12       |12.97980265|
|         7         |           15            |        35       |31.39192106|


###R2 Score : 0.8317825445
This seemed acceptable as a modle but still want to talk it through more...