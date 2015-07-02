##Class 6
###17 June 2015

**Machine Learning**

What is machine learning?
- does not have to be explicitly programmed
- automatic (semi-automatic) extraction of knowledge from data
	- still requires smart decisions by humans!

Types of machine learning
- Supervised vs unsupervised
- will largely focus on supervised

Supervised
- "predictive modeling": predict an outcome based on input data
- goal: generalizatioin
	- build a model that is good at predicting the future
- two categories: all about what we're trying to predict!
	- regression: outcome we are trying to predict is continuous
		- class of supervised learning problems (linear being one of them)
		- price, BP
	- classification: outcome we are trying to predict is categorical (values in a finite, unordered set)
		- includes binary (regardless of number of categories)
		- also includes probabilities of categorical outcomes
- data sets are not inherently regression/classification; depends on your question

Terminology
- observations: n 
	- aka samples, examples, instances, records
- features: inputs
	- aka predictors, IV, inputs, regressors, covariates, attributes
- response: what you're trying to predict
	- aka outcome, label, target, DV
- feature matrix: n x p table (X, indicates more than one dimension)
- response vector: y (single dimension object), has length n

How does it work?
1) Train a machine learning model using labeled data (data with response variable)
	- goal is to learn the relationship between the features and the response
2) Make predictions on new data for whcih the response is unknown
- Want to build a model that "generalizes"
	- predicts the future rather than the past, but based on the past
	- model learns the relationship

Unsupervised learning
- extracting structure from data
- not predictive modeling
- example: segment grocery store shoppers in "clusters" that exhibit similar behaviors
- there is no "true" label --> you're adding a label
- goal is representation
- no clear objective
- no "right" answer and hard to tell how you're doing
- no response variable, just observations with features

How does it work?
1) Perform unsupervised learning
	- cluster images based on "similarity"
	- might find a "dog cluster", might not
	- tada you're done
- sometimes unsupervised learning is used as a "preprocessing" step for supervised learning






