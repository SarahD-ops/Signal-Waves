import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())

# Initialize the repository
run_command('git init')

# Add all files to staging
run_command('git add .')

# Commit changes with a message
run_command('git commit -m "Initial commit"')

# Add remote repository
run_command('git remote add origin https://github.com/SarahD-ops/Signal-Waves.git')

# Push changes to the remote repository
run_command('git push -u origin master')
