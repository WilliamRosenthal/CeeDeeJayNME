import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset_file_path = 'Employee Attrition.csv'
data = pd.read_csv(dataset_file_path)

data_cleaned = data.dropna(how = 'all')
data_cleaned['Work_accident'] = data_cleaned['Work_accident'].astype(int)
data_cleaned['promotion_last_5years'] = data_cleaned['promotion_last_5years'].astype(int)

numeric_data_cleaned = data_cleaned.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_data_cleaned.corr()


# Function to plot and save box plots for continuous variables
def plot_box_plots(data_cleaned):
  plt.figure(figsize = (15, 10))
  plt.subplot(2, 3, 1)
  sns.boxplot(data = data_cleaned['satisfaction_level'])
  plt.subplot(2, 3, 2)
  sns.boxplot(data = data_cleaned['last_evaluation'])
  plt.subplot(2, 3, 3)
  sns.boxplot(data = data_cleaned['number_project'])
  plt.subplot(2, 3, 4)
  sns.boxplot(data = data_cleaned['average_montly_hours'])
  plt.subplot(2, 3, 5)
  sns.boxplot(data = data_cleaned['time_spend_company'])
  plt.tight_layout()
  plt.savefig('box_plots.png')

# Function to plot and save categorical variable visualizations
def plot_categorical_variables(data_cleaned):
  plt.figure(figsize = (15, 7))
  plt.subplot(1, 2, 1)
  sns.countplot(y = 'dept', data = data_cleaned, order = data_cleaned['dept'].value_counts().index)
  plt.title('Department Distribution')
  plt.subplot(1, 2, 2)
  sns.countplot(x = 'salary', data = data_cleaned, order = data_cleaned['salary'].value_counts().index)
  plt.title('Salary Level Distribution')
  plt.tight_layout()
  plt.savefig('categorical_variables.png')

# Function to plot and save relationships between 'salary' and other continuous variables
def plot_salary_relationships(data_cleaned):
  plt.figure(figsize = (18, 12))
  plt.subplot(2, 2, 1)
  sns.boxplot(x = 'salary', y = 'satisfaction_level', data = data_cleaned)
  plt.title('Salary vs Satisfaction Level')
  plt.subplot(2, 2, 2)
  sns.boxplot(x = 'salary', y = 'last_evaluation', data = data_cleaned)
  plt.title('Salary vs Last Evaluation')
  plt.subplot(2, 2, 3)
  sns.boxplot(x = 'salary', y = 'average_montly_hours', data = data_cleaned)
  plt.title('Salary vs Average Monthly Hours')
  plt.subplot(2, 2, 4)
  sns.boxplot(x = 'salary', y = 'time_spend_company', data = data_cleaned)
  plt.title('Salary vs Time Spent Company')
  plt.tight_layout()
  plt.savefig('salary_relationships.png')

# Function to plot and save the correlation matrix heatmap
def plot_correlation_matrix(corr_matrix):
  plt.figure(figsize = (10, 8))
  sns.heatmap(corr_matrix, annot = True, fmt = ".2f", cmap = 'coolwarm', cbar_kws = {'shrink': .5})
  plt.title('Correlation Matrix')
  plt.savefig('correlation_matrix.png')

# Function to plot and save the scatter plot: Satisfaction Level vs Last Evaluation by Salary
def plot_scatter_plot(data_cleaned):
  plt.figure(figsize = (12, 6))
  sns.scatterplot(x = 'satisfaction_level', y = 'last_evaluation', hue = 'salary', data = data_cleaned, alpha = 0.5)
  plt.title('Satisfaction Level vs Last Evaluation by Salary')
  plt.savefig('satisfaction_vs_evaluation.png')

# Call the functions to plot and save the images
plot_box_plots(data_cleaned)
plot_categorical_variables(data_cleaned)
plot_salary_relationships(data_cleaned)
plot_correlation_matrix(corr_matrix)
plot_scatter_plot(data_cleaned)

# Scatter Plot with Trend Line for 'log(last_evaluation)' vs 'log(average_montly_hours)' on the sampled data
sampled_data = transformed_data.sample(frac=0.1, random_state=42)

plt.figure(figsize=(10, 6))
sns.regplot(x='last_evaluation_log', y='average_montly_hours_log', data=sampled_data, line_kws={"color":"red"})
plt.title('Log of Last Evaluation vs Log of Average Monthly Hours with Trend Line (Sampled Data)')
plt.xlabel('Log of Last Evaluation')
plt.ylabel('Log of Average Monthly Hours')
plt.savefig('log_evaluation_vs_log_hours_trend_sampled.png')
plt.close() 
