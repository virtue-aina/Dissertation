import pandas as pd

#load unfiltered dataset
unfiltered_keystrokes_df = pd.read_csv('keystrokes.csv')

#grouping the data in the DataFrame df by the SubjectID column and then counting the number of unique AssignmentIDs for each group
assignment_counts = unfiltered_keystrokes_df.groupby('SubjectID')['AssignmentID'].nunique()

# Filtered students with exactly 8 assignments
students_with_8_assignments = assignment_counts[assignment_counts == 8].index
filtered_keystrokes_df = unfiltered_keystrokes_df[unfiltered_keystrokes_df['SubjectID'].isin(students_with_8_assignments)]

# filtered DataFrame converted to CSV
filtered_keystrokes_df.to_csv('filtered_keystrokes.csv', index=False)

# filtered DataFrame converted to Excel format
filtered_keystrokes_df.to_excel('filtered_keystrokes.xlsx', index=False)

