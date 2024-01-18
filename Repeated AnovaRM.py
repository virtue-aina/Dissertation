import pandas as pd

from statsmodels.stats.anova import AnovaRM


# Load  data
df = pd.read_csv('time_on_task_summary.csv')

# Conduct Repeated Measures ANOVA
anova_results = AnovaRM(data=df, depvar='TimeOnTask', subject='SubjectID', within=['AssignmentID']).fit()

# Print the results
print(anova_results.summary())

