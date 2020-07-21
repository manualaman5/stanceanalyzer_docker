Stance Analyzer
This is a dockerized version of the basic structure for the Stance Analyzer application. I did not include the heavy data processing/connection with Twitter for agility reasons.
To create the docker image: docker build -t yourusername/stanceanalyzer . 
To run the web application: docker run -p 8888:5000 yourusername/stanceanalyzer

Brief description of the web application
Social media offers a huge amount of information about the users, specially Twitter where people publish their bare opinions. This data could be used to analyze the position of users regarding several topics. It comes more interesting when those topics can be some sensitive topics and the analysis is contrasted with some organizations that are widely known for representing a stance either pro or against one topic. 

The objective of this project is the development of a web application where the user inputs a Twitter account and selects one or several possible issues such as “environment” or “inmigration”. Using the Twitter API, the most recent tweets of the user are going to be accessed and using a pre-trained model, the tweets of the user are going the be scored on the selected issues. The most pro and anti issue tweets will be displayed.

