import os
import shutil
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
os.mkdir('nodejs')
#subprocess.check_call('mkdir nodejs', shell=True, cwd=script_dir)
new_dir =  os.chdir(os.path.join(script_dir, 'nodejs'))




# Initialize Node.js environment
subprocess.check_call('npm init -y', shell=True, cwd=new_dir)

# Install the dependencies
subprocess.check_call(['npm', 'install'] + dependencies, shell=True, cwd=new_dir)

# Create a zip file
zip_filename = f'layer-{dependencies}'
shutil.make_archive(os.path.join(script_dir, zip_filename), 'zip',new_dir)

print('Zip file created successfully!')

# Remove unnecessary files
#shutil.rmtree(os.path.join(script_dir, 'node_modules'))
#os.remove(os.path.join(script_dir, 'package-lock.json'))
