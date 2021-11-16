from setuptools import setup, find_packages

setup(
    name='k8s_user',
    version='1.0.0',
    packages=find_packages(include=[
        'k8s_user', 'k8s_user.*'
    ]),
    python_requires='>=3',
    url='',
    license='',
    author='Tim Martin',
    author_email='timothy.martin@netapp.com',
    description='Kubernetes Script to create users/kubeconfigs',
    install_requires=[
        'pyyaml',
        'cryptography',
        'kubernetes'
    ],
    entry_points={
        'console_scripts': [
            'k8s-user=k8s_user.main:main'
        ]
    }
)
