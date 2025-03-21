from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """ 
    This function will return a list of requirements
    """
    
    requirement_lst = []
    try:
        with open('requirements.txt', 'r') as files:
            # Read lines from the file
            lines = files.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst                 

# Testing the function
print(get_requirements())

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Aman Kumar",
    author_email = "amancodit@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
    
)