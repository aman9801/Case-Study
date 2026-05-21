# Technical assignment Heineken - Data Science

This repo contains three exercises for the technical round of the interview process and one conclusion slide. These exercises 
will be reviewed by two of our data scientists and then discussed during a technical interview with them.

The process for this round is as follows:
1. You will receive these exercises and perform them
  We recommend you to start with the pull request exercise since it contains helper functions for the other exercises.

2. The answers should be sent 3 days before the interview such that we can review them
  - We think it will take you at least three hours of work to answer the questions. The below times are indicative how to distribute your work time.
    - ~30 minutes on the PR exercise
    - ~60 minutes on the EDA exercise
    - ~60 minutes on the modelling exercise
    - ~15 minutes on making one slide to present conclusions.
  - Feel free to spend more time. But it is totally fine to not do so. We will assess the exercises based on the time you said you spend.

3. The interview will take place (~1 hour)
 - First, present your main conclusion slide to us.
 - Then, you will walk us through your findings and solution, highlighting your reasons for the approach.

4. If you want to receive comments based on our assessment you can request it after the interview.

## Business question
The technical assignment follows the business question that you already discussed during your first interview.

_We, as Global Analytics, are the go-to department for when there is a data challenge anywhere in the organization. For this case, our colleague from the Demand Planning department in the Dutch branch came to us with some serious concern. Here is what he said:_

> “Historically, our beer production has always been close to what the market needed: out-of-stocks rarely happened, and we hardly ever had to get rid of excess production. However, our senior demand planner retired last year and since then we've seen both stock-outs increase for some products and surging write-offs for other products.  

> Our department is struggling to make better forecasting and we are worried about the impact this can have on our image as a brand towards our clients and the consumers.” 


__In summary,  the business wants you to "predict the demand of a product eight weeks in advance"?__

![Prediction window](prediction_window.png)


## Data description
There are two datasets provided. The file demand.csv contains the daily demand from a supermarket and a specific product (SKU). The file promotions.csv contains all days when a promotion started for a specific product and supermarket. The duration of a promotion is one week.
 
## 1. Pull request exercies
This exercise tests your communication towards technical colleagues and ability to understand code. The exercise consists of writing a docstring, giving feedback on code, and optionally improving an implementation. The reviewer only expects that you spend around 30 minutes on this task to limit the effort for you. 

### Exercise question
The exercise consists of reviewing the `utils.py` file and performing the following steps:

1. Write a docstring for the `utils.py/clean_demand_per_group` function
2. Give comments on `utils.py` in the subsection below. Consider it as a pull request by a colleague towards a production grade codebase. It does not need to be an exhaustive list of comments but the ones you find the most important to address.
3. Optional: Give comments on better test cases for the function `utils.py/merge` or find an unexpected behavior in one of the functions. 

### Comments on utils.py

_your answer here_


## 2. Exploratory data analysis

The EDA exercise tests your basic understanding of performing an exploratory data analysis to understand the data quality, make a basic analysis of historic data relevant to the business questions, and find possible features for a model. 

### Exercise question
You can find the exercise and further description in `EDA_exercise.ipynb`. You can use the notebook for you analysis or, if you prefer, create a script to run the EDA. 

## 3. Modelling 

The Modelling exercise tests your ability to develop/create a model suited for the business task at hand. We would look at how you go about making decisions regarding the data preparation, choice of algorithm and evaluation for the same. Please note that you don't have to optimize the score, we are not expecting a really complex optimized model for the task.

### Exercise question
You can find the exercise and further description in `Modelling_exercise.ipynb`. You can use the notebook for your analysis or, if you prefer, create a script to make a model. 

## 4. Conclusion slide

Please prepare **one slide** that summarizes your findings and conclusions from the analysis. Imagine you would need to present this to a business stakeholder. Don't forget to connect your findings to the business question ("predict demand eight weeks in advance").