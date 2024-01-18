import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt

# Load datasets
students_df = pd.read_csv('students.csv')
time_on_task_df = pd.read_csv('time_on_task_summary.csv')

# Merge datasets on SubjectID
merged_df = pd.merge(students_df, time_on_task_df, on='SubjectID')

merged_df['AverageScore'] = merged_df[['Assign6', 'Assign7', 'Assign8', 'Assign9', 'Assign10', 'Assign11', 'Assign12', 'Assign13']].mean(axis=1)


# Correlation Analysis
correlation, p_value = scipy.stats.pearsonr(merged_df['TimeOnTask'], merged_df['AverageScore'])
print("Correlation Coefficient:", correlation)
print("P-value:", p_value)


# Scatter Plot
plt.scatter(merged_df['TimeOnTask'], merged_df['AverageScore'])
plt.title('Scatter Plot: Time on Task vs. Average Score')
plt.xlabel('Time on Task')
plt.ylabel('Average Score')
plt.show()
