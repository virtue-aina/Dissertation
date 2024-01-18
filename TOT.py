
import math
import pandas as pd

# Load the dataset
df = pd.read_csv('filtered_keystrokes.csv')

#SAMPLE CODE BEGINS HERE

# Given a number of minutes x since the last keystroke,
# returns the probability that the student was on task.
# Uses the model from Edwards et al., SIGCSE 2022.
def p(x):
    if x < 0.75:
        m = -(1 - 0.8072438106027864) / 0.75
        return m * x + 1
    Q, B, M, v = 6604, -4.99, 0.01, 58.32
    return 1 / (1 + Q * math.exp(-B * (x - M)))**(1 / v)

# Given a number of minutes x since the last keystroke,
# returns whether the student was on task. Uses p(x)
# to get the probability and uses that result to take
# a percentage of the time between keystrokes.
def on_task(x):
    if x <= 0 or x > 60:
        return 0
    return x * p(x)

# Filter for 'File.Edit' events
df = df[df.EventType == 'File.Edit']

# Compute the elapsed time since the last keystroke
df['elapsed'] = df.ClientTimestamp - df.shift(1).ClientTimestamp

# Create a unique ID for subject/assignment/file
df['ID'] = df.SubjectID + df.AssignmentID + df.CodeStateSection

# Any change to a new ID results in 0 elapsed
df.loc[df.ID != df.shift(1).ID, 'elapsed'] = 0

#SAMPLE CODE ENDS HERE

#ORIGINAL CODE BEGINS HERE-authored by me

# Get unique assignments for each student
unique_students = df['SubjectID'].unique()
time_on_task_data = []

for student_id in unique_students:
    student_df = df[df['SubjectID'] == student_id]
    unique_assignments = student_df['AssignmentID'].unique()
    for assignment_id in unique_assignments:
        assignment_df = student_df[student_df['AssignmentID'] == assignment_id]
        time_on_task = ((assignment_df.elapsed / (60 * 1000)).apply(on_task)/60).sum()
        new_row = {'SubjectID': student_id, 'AssignmentID': assignment_id, 'TimeOnTask': time_on_task}
        time_on_task_data.append(new_row)

# Create a DataFrame from the list
time_on_task_df = pd.DataFrame(time_on_task_data)

# Convert DataFrame to CSV
time_on_task_df.to_csv('time_on_task_summary.csv', index=False)

# Convert DataFrame to Excel
time_on_task_df.to_excel('time_on_task_summary.xlsx', index=False)



