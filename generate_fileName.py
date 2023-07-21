import datetime

# Function to generate a unique file name for each note/invoice


def generate_file_name(prefix):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return f'{prefix}_{timestamp}.txt'
