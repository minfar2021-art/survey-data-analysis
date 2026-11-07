import pandas as pd

# Load the dataset
file_path = "/storage/emulated/0/Download/survey.xlsx"
df = pd.read_excel(file_path)

# Define items for each construct (dimension)
knowledge_sharing = [
    '1.  I frequently use digital platforms (e.g., Teams, Slack, Zoom, Email) to share my work expertise with my colleagues.  ',
    '2.  I find it easy to exchange professional knowledge and documents using the digital tools provided by my organization. ',
    '3.  I actively participate in online discussions, forums, or knowledge-sharing groups within my company.  ',
    '4.  Digital technology has significantly enhanced my ability to provide and receive information from my team members. ',
    '5.  I am comfortable using digital systems to document and store my work knowledge so that others can benefit from it. '
]

well_being = [
    '6.  Over the last two weeks, I have felt cheerful and in good spirits while performing my work tasks. ',
    '7.  I feel calm and relaxed, even when I have to deal with a high volume of digital information. ',
    '8.  I do not feel overwhelmed by the constant digital connection (always-on culture) required by my job. ',
    '9.  My mental energy remains high throughout the workday despite heavy use of technology. ',
    '10.  I am able to maintain a healthy and clear boundary between my digital work hours and my private life. '
]

job_performance = [
    '11.  I am able to plan my work tasks efficiently so that they are completed on time. ',
    '12.  The quality of my work has remained high (or improved) with the use of digital collaboration tools. ',
    '13.  I take the initiative to find creative solutions to problems using available technology. ',
    '14.  I consistently meet the professional goals and targets set by my organization. ',
    '15.  I work efficiently to handle my core job responsibilities in this digitalized workplace. '
]

# Likert scale mapping
likert_mapping = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

# Apply mapping to all columns
all_items = knowledge_sharing + well_being + job_performance
for col in all_items:
    df[col] = df[col].map(likert_mapping)

# Calculate composite mean scores for each construct
df['Knowledge_Sharing_Mean'] = df[knowledge_sharing].mean(axis=1)
df['Well_Being_Mean'] = df[well_being].mean(axis=1)
df['Job_Performance_Mean'] = df[job_performance].mean(axis=1)

# Select the composite columns for correlation analysis
constructs_df = df[['Knowledge_Sharing_Mean', 'Well_Being_Mean', 'Job_Performance_Mean']]

# Calculate Pearson Correlation Matrix
correlation_matrix = constructs_df.corr(method='pearson')

print("--- Pearson Correlation Matrix ---")
print(correlation_matrix)
