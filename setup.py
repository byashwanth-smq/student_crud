from setuptools import setup, find_packages

setup(
    name="student_crud",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'pg8000',
        'python-dotenv',
    ],
)