import pandas as pd

# Path to the input file
input_file_path = '/home/ec2-user/coursework/combined_hhr_parse.out'

# Read the data into a DataFrame
df = pd.read_csv(input_file_path)

# Extract 'query_id' and 'best_hit' and save to a new csv file
hits_output = df[['query_id', 'best_hit']]
hits_output.columns = ['fasta_id', 'best_hit_id']
hits_output.to_csv('/home/ec2-user/coursework/hits_output.csv', index=False)

# Replace NaN values with 0 in 'score_std' and 'score_gmean'
df['score_std'] = df['score_std'].fillna(0)
df['score_gmean'] = df['score_gmean'].fillna(0)

# Calculate mean Standard Deviation and mean Geometric means
mean_std = round(df['score_std'].mean(), 2)
mean_gmean = round(df['score_gmean'].mean(), 2)

print("Mean Standard Deviation: ", mean_std)
print("Mean Geometric Mean: ", mean_gmean)

# Create a DataFrame for the profile output
profile_output = pd.DataFrame({'ave_std': [mean_std], 'ave_gmean': [mean_gmean]})

# Save the profile output to a CSV file
profile_output.to_csv('/home/ec2-user/coursework/profile_output.csv', index=False, header=True)
