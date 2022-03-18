from setuptools import setup

setup(
    name="ztools",
    version='0.1.0',
    description='Useful tools',
    author='zhaisilong',
    author_email='zhaisilong@outlook.com',
    packages=['cli'],
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    keywords=["deep learning", "tools", "AI"],
    python_requires=">=3.6",
    setup_requires=[
        'recommonmark',
        'sphinx_rtd_theme',
    ],
    entry_points={
        "console_scripts": [
            "new=cli.new:new_entry",
        ],
    }
)

