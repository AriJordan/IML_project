from setuptools import setup, find_packages

setup(
    name="rllib",
    version="0.0.1",
    author="Sebastian Curi",
    author_email="sebascuri@gmail.com",
    license="MIT",
    packages=find_packages(exclude=['docs']),
    install_requires=['numpy>=1.0,<2',
                      'scipy>=1.3.0,<1.4.0',
                      'torch==1.4.0',
                      'gym>=0.13,<0.15',
                      'tqdm>=4.0.0,<5.0',
                      'matplotlib>=3.1.0',
                      'gpytorch==1.0.1',
                      ],
    extras_require={
        'test': [
            'pytest>=5.0,<5.1',
            'flake8>=3.7.8,<3.8',
            'pydocstyle==4.0.0',
            'pytest_cov>=2.7,<3',
            'mypy>=0.740',
        ],
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
