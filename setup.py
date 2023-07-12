## will be using this file for my ML application as a package
from setuptools import find_packages,setup 

from typing import List 

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    # this function will return list of requirements
    requirements =[]
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Pritam',
author_email = 'pritamrana770@gmail.com',
packages = find_packages(),
install_requires =[
        "numpy==1.19.5",
        "pandas==1.3.2",
        "scikit-learn==0.24.2",
        "seaborn==0.12.2" 
    ],
) 