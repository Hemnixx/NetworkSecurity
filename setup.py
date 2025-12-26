from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirements_list:list[str]=[]
    try:
       with open('requirements.txt', 'r') as file:
            lines=file.readlines()
            for line in lines:        
                requirements = line.strip()
                if requirements and requirements !='-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return requirements_list
setup(
    name='Network_Security_ETOE_Project',
    version='0.0.1',
    author='Neeraj Gupta',
    author_email="Neeraj210302@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )
