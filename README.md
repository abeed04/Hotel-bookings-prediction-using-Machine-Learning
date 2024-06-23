<h1 align="center">Hotel Bookings Prediction with Machine Learning

</h1>
<h2 align="center">Introduction</h2>

- 👨‍💻This project demonstrates the prediction of hotel booking cancellations using a Random Forest classifier trained on historical data. It outlines the model training process and provides a basic structure for a potential web application.

- ⚡This project demonstrates proficiency in machine learning, data analysis, data visualization, and model building for real-world  applications.
<br/>
<img  align="right" src="https://media.licdn.com/dms/image/C4D12AQERGi4BRBVf5A/article-cover_image-shrink_720_1280/0/1592071903807?e=2147483647&v=beta&t=oQO6fXk2vhJhTDUOm9uluYHYyTyin8C4976DEt1704w" />
<br/><br/>

<h2 align="center">Requirements</h2>

- Python 3.x
- pandas
- numpy
- Scikit-learn
- Flask

  
<h2 align="center">Data Cleaning and Feature Engineering</h2>

- Performed data cleaning techniques like finding Null values, Outliers, Imputations and then performed EDA over the data in google colab using python.

- In Feature engineering performed Chi square test, Anova test, VIF, Multicollinearity, Label Model seencoding, One hot encoding and Data wrangling by which some of the columns were removed which were not useful for further process of model building.

- After performing all necessary actions, created a new csv file named 'Clean_hotel_data' which was used further in deployment of model.

<h2 align="center">Training the Model</h2>
<img  align="right" height=350 width=330 src="https://www.ijraset.com/images/text_version_uploads/imag%201_10253.png" />

- To deploy this model we used pycharm platform and flask framework.
-  Loads the data from the CSV file "Clean_hotel_data".
- Encode categorical features using LabelEncoder from scikit-learn.
- Split the data into training and testing sets (8:2).
- Random Forest Algorithm, Desicion tree algorithm and logistic regression algorithms were used on training data as it was a task of classification.
-  Random Forest classifier with 201 decision trees gave the best results of classification report .

- Evaluate the model's performance on the testing set.

- Save the trained model using pickle as "model.pkl".
  
<h2 align="center">Deployment</h2>

-  To deploy this model we used pycharm platform and flask framework .
-  Run deploy.py to start the Flask application.. This script defines two routes:
-  1) Renders the index.html template (if provided).
   2) Handles user input, makes predictions using the loaded model, and displays the result (either in the template or directly).

<h2 align="center">Customization</h2>

- You can modify the model training (in main.py) to explore different machine learning algorithms, hyperparameter tuning, and feature engineering techniques.
- You can customize the Flask application (in deploy.py) to create a more user-friendly interface with forms and informative output.
- Consider using a templating engine like Jinja2 for more complex layouts in index.html.
- For production deployment, explore options like containerization with Docker or cloud platforms like Heroku.

<h2 align="center">Use Cases</h2>

- Reduced Revenue Loss: By identifying bookings with a high cancellation risk, hotels can proactively implement strategies to prevent them. This could involve offering incentives for early booking or reaching out to high-risk guests with targeted promotions
- Optimized Resource Allocation: Knowing which bookings are less likely to be cancelled allows hotels to better allocate resources like staff and housekeeping.
- Improved Revenue Management: Predictions can inform pricing strategies and dynamically adjust room rates based on cancellation likelihood and demand fluctuations.
- Improved Resource Management: Platforms can optimize their resources, such as customer support staff, by anticipating potential cancellation inquiries based on predictions.
- Informed Decision-Making: Travelers can use predicted cancellation risks to make more informed booking choices, especially when considering non-refundable options.
