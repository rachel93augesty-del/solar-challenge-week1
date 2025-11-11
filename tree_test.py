import os

# Function to print the directory tree
def print_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

# Set the path to current folder
print_tree('.')

# Optional: try importing your module to check structure
try:
    from src.data_processing import load_clean_data
    print("\nModule import successful!")
except Exception as e:
    print(f"\nModule import failed: {e}")