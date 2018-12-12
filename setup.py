from setuptools import setup, find_packages
REQUIRES = [
    'mlmorph'
]
setup(
    name='mlrandom', version='alpha-0.0.1',
    description='mlrandom is a simple random text generator for Malayalam',
    author='Sreenadh TC', author_email='kesav.tc8@gmail.com',
    packages=find_packages(),
    install_requires=REQUIRES,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'mlrandom = mlrandom.cli:cli',
        ],
    },
)
