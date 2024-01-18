import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('time_on_task_summary.csv')


# Calculate IQR for each AssignmentID
Q1 = df.groupby('AssignmentID')['TimeOnTask'].quantile(0.25)
Q3 = df.groupby('AssignmentID')['TimeOnTask'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bound for each AssignmentID
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create boxplot
plt.figure(figsize=(10,6))
sns.boxplot(x='AssignmentID', y='TimeOnTask', data=df)

# Annotate Outliers
for assignment in df['AssignmentID'].unique():
    assignment_outliers = df[(df['AssignmentID'] == assignment) &
                             ((df['TimeOnTask'] < lower_bound[assignment]) |
                              (df['TimeOnTask'] > upper_bound[assignment]))]
    for index, outlier in assignment_outliers.iterrows():
        plt.annotate(outlier['SubjectID'],
                     xy=(outlier['AssignmentID'], outlier['TimeOnTask']),
                     xytext=(0,5),
                     textcoords='offset points',
                     ha='center',
                     va='bottom')

# Labeling
plt.title('Boxplot of Time on Task by Assignment with Outliers')
plt.xlabel('Assignment ID')
plt.ylabel('Time on Task (hours)')

# Show plot
plt.show()

