from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """This imports each package from requiremtns.txt as a list. It will have \n 
    for each line, we need to replace \n with null to install correct package
    """
    requirements = []
    requirements = [req.replace("\n","") for req in requirements]

    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

setup(
    name='Machine Learning Project',
    version = '0.0.1',
    author = 'Vivek Vardhan',
    author_email='vivekvardhan1512@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)