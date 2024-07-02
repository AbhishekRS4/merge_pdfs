from setuptools import setup, find_packages


setup(
    name="merge-pdfs",
    version="0.0.1",
    description="merge multiple PDFs into a single PDF file",
    install_requires=["click>=8.1.7", "pypdf2>=3.0.1"],
    entry_points="""
    [console_scripts]
    merge-pdfs=merge_pdfs.merge_pdfs:main
    """,
    author="Abhishek R. S.",
    author_email="abhishek.r.satyanarayana.4@gmail.com",
    packages=find_packages(),
)

# name_of_the_cli_tool = module.script:main_function_name