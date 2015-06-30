##Class 8
###24 June 2015

*Reproducibility*
- Openly providing data and computer code in order to make it practical for others to reproduce their entire data analysis
- Not replication (another study group that uses different methods and data)
- Why does this matter?
	- Transparency

*scikit learn*

'''
mylist = ['species', 'species_num']
iris[mylist] # will output just species and species_num column
iris[['species', 'species_num']]
	# inner brackets: use these columns
	# outer brackets: only show listed columns

iris[['species']]	# dataframe with one feature
iris.species		# series

# I should have just created a python notebook...
'''

Step 1: Import the class you plan to use
- Don't import scikit-learn... it's massive. Better to just call the things you need from scikit-learn.
- scikit-learn is well organized into modules

Step 2: Create an instance of the model (the estimator)
'''
knn = KNeighborsClassifier(n_neighbors=1)
# argument: n_neighbors = 1 aka k = 1
# if you leave out the model parameters, that's fine. It will just inherit default parameters of the model.
'''

Step 3: Fit the model with data (aka learning)
- knn learns the relationship between x and y
- not much happens
- occurs in-place

Step 4: Predict the response for a new observation!

Can't assign weights, but can ask the model to place greater importance on closer neighbors.

*Exploring the Bias-Variance Tradeoff*


