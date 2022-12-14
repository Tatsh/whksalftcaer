from setuptools import setup

setup(
    name="hello_world",
    version="1.0",
    packages=["hello_world"],
    include_package_data=True,
    install_requires=['Flask'],
    extras_require={
        'dev': [
            'mypy', 'mypy-extensions', 'pylint', 'pylint-quotes', 'rope',
            'types-requests>=2.25.9'
        ]
    },
)
