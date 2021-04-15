from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),           # finds all the packages automatically
    include_package_data=True,          # this includes static and template directories also, which uses MANIFEST.in to describe which files are needed.
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

