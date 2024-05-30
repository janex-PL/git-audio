from setuptools import setup, find_packages

setup(
    name="git-audio",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-audio=git_audio.main:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
)
