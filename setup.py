import os
from setuptools import setup, find_packages

import menuxblock


def package_data(pkg, root_list):
    """Generic function to find package_data.
    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='menuxblock',
    version='1.0',
    description='An XBlock for creating coloured boxed content',
    license='AGPL v3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'XBlock',
        'xblock-utils'
    ],
    entry_points={
        'xblock.v1': [
            'menuxblock = menuxblock:MenuXBlock',
        ]
    },
    package_data=package_data("menuxblock", ["static", "public"]),
)
