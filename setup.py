from setuptools import find_packages,setup
from typing import List


HYPEN_E='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' this function return the list of requirements '''
  
    requiremnt=[]
    with open(file_path) as file_obj:
        requiremnt=file_obj.readlines()
        requiremnt=[req.replace("\n","") for req in requiremnt]
        
        if HYPEN_E in requiremnt:
            requiremnt.remove(HYPEN_E)
            
    return requiremnt   
    
setup(
    name="Ml Project",
    version='0.0.1',
    author='Mansi',
    author_email='vermamansi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)