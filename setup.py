from setuptools import setup
from source.conf import release

setup(
    name="ztools",
    version=release,
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

