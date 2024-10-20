from setuptools import find_packages,setup
from typing import List

HYPHEN_E_Dot ="-e ."

def get_requirements(file_path:str)->list[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_Dot in requirements:
            requirements.remove(HYPHEN_E_Dot)
    return requirements

setup(
    name="Device Usage",
    version='0.0.1',
    author='Danson Macharia',
    author_email='writingcode2022@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)