from setuptools import find_packages, setup

setup(
    name="zsl-tools",
    version='0.1.0',
    description='Useful tools',
    author='zhaisilong',
    author_email='zhaisilong@outlook.com',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    keywords=["deep learning", "tools", "AI"],
    python_requires=">=3.6",
    setup_requires=[
        'recommonmark',
        'sphinx_rtd_theme',
    ],
)
