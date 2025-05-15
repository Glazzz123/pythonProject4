from setuptools import setup, find_packages

setup(
    name="salary_report",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "salary-report=salary_report.main:main",
        ],
    },
    author="Your Name",
    author_email="you@example.com",
    description="CLI tool for generating salary reports from CSV",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
