from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        require = file_obj.readlines()
        require = [req.replace('\n', '') for req in require]
        
        if HYPEN_E_DOT in require:
            require.remove(HYPEN_E_DOT)
        return require

setup(
    name='mlproject1',
    version='0.0.1',
    author='Fame_Patcharapol',
    author_email='patcharapol.yasamut@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('get_requirements.txt')
    
)