from setuptools import setup

setup(
    name='pyls',
    version='0.1.0',
    description='A Python script to list directory contents in a style similar to "ls".',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    py_modules=['pyls'],
    entry_points={
        'console_scripts': [
            'pyls=pyls:main',
        ],
    },
    python_requires='>=3.8',
)
