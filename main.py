import os
import shutil
import zipfile
import subprocess

# Prompt user for dependencies
dependencies = []
while True:
    dependency = input("Enter a dependency (or 'done' to finish): ")
    if dependency.lower() == "done":
        break
    dependencies.append(dependency)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)

# Initialize Node.js environment
subprocess.check_call('npm init -y', shell=True, cwd=script_dir)

# Install the dependencies
subprocess.check_call(['npm', 'install'] + dependencies, shell=True, cwd=script_dir)

# Create a zip file
zip_filename = 'dependencies.zip'
shutil.make_archive(os.path.join(script_dir, 'node_modules'), 'zip', 'node_modules')

print('Zip file created successfully!')

# Remove unnecessary files
shutil.rmtree(os.path.join(script_dir, 'node_modules'))
os.remove(os.path.join(script_dir, 'package-lock.json'))
