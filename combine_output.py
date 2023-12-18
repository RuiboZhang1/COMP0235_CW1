import os
import glob

def combine_hhr_parse_files(input_dir, output_file):
    header_written = False
    with open(output_file, 'w') as outfile:
        # Iterate over all 'hhr_parse.out' files in the directory
        for filename in glob.glob(os.path.join(input_dir, '**/hhr_parse.out'), recursive=True):
            with open(filename, 'r') as infile:
                header = infile.readline()
                # Write the header line only once
                if not header_written:
                    outfile.write(header)
                    header_written = True
                # Write the rest of the file
                for line in infile:
                    outfile.write(line)

# Directory where 'hhr_parse.out' files are stored
input_directory = '/home/ec2-user/coursework/collected_hhr_parse/'
# Output file path
output_file_path = '/home/ec2-user/coursework/combined_hhr_parse.out'

# Run the function
combine_hhr_parse_files(input_directory, output_file_path)
