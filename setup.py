from setuptools import setup

setup(
    name='ratemarkt',
    py_modules=['ratemarkt'],
    version='0.0.1',
    description='Python client library for Ratemarkt API',
    author='Kadir Pekel',
    author_email='kadirpekel@gmail.com',
    url='https://github.com/ratemarkt/ratemarkt-python-client',
    install_requires=[
        'requests>=2.13.0'
    ],
    tests_require=['httpretty==0.5.4'],
)
