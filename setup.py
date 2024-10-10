from setuptools import setup, find_packages

setup(
    name='django-selective-email-backend',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    include_package_data=True,
    license='AGPL-3.0-or-later',
    description='A Django email backend that selects between SMTP and a default email backent based on the sender address.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/openlibhums/django-selective-email-backend',
    author='OLH Publishing Technology team',
    author_email='olh-tech@bbk.ac.uk',
)
