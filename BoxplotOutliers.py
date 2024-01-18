import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('time_on_task.xlsx')

# Convert 'TimeOnTask' from HH:MM:SS format to total minutes
df['TimeOnTask'] = pd.to_timedelta(df['TimeOnTask']).dt.total_seconds() / 60

# Creating a box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='AssignmentID', y='TimeOnTask', data=df)
plt.title('Box Plot of Time On Task for Each Assignment')
plt.xlabel('Assignment')
plt.ylabel('Time On Task (minutes)')
plt.show()
