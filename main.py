import os
import shutil
import subprocess
import time

# Prompt user for dependencies
dependencies = []
print('Enter the dependencies you want to install in the Lambda layer. Please make sure that ')

while True:
    count_dependencies = len(dependencies)
    if count_dependencies != 0:
        print(f'Current dependencies: {dependencies}')
    dependency = input("Enter a dependency (or 'n' to finish): ")
    if dependency.lower() == "n":
        break
    dependencies.append(dependency)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)
os.mkdir('nodejs')
#subprocess.check_call('mkdir nodejs', shell=True, cwd=script_dir)
new_dir = os.chdir(os.path.join(script_dir, 'nodejs'))



os.system('cls')
print('Starting creating project...')
# Initialize Node.js environment
subprocess.check_call('npm init -y', shell=True, cwd=new_dir)

os.system('cls')
print('Installing dependencies...')
# Install the dependencies
subprocess.check_call(['npm', 'install'] + dependencies, shell=True, cwd=new_dir)

os.system('cls')
print('Finish dependencies...')
print('Creating Zip file...')

# Create a zip file
zip_filename = f'layer-{dependencies}'

nj_folder= os.path.join(script_dir, 'nodejs')
os.remove(os.path.join(nj_folder, 'package-lock.json'))
os.remove(os.path.join(nj_folder, 'package.json'))

shutil.make_archive(os.path.join(script_dir, zip_filename), 'zip',new_dir)

os.system('cls')


print('Zip file created successfully!')
print('Removing unnecessary files...')

# Remove unnecessary files
time.sleep(1)
os.chdir(script_dir)
shutil.rmtree(os.path.join(script_dir, 'nodejs'))


os.system('cls')
print(f'All done!, your layer has been zipped and is ready to be uploaded to AWS Lambda. Zip file: {zip_filename}')
