#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate_analysis.py - Creates a Python script and Jupyter notebook template

Usage:
Run this script and enter a base filename when prompted.
It will generate both a .py and .ipynb file with starter code.
"""

import json
import os
from datetime import datetime

def create_python_script(filename):
    """Create a basic Python script with common imports and structure"""
    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
{filename}.py - A Python script generated on {datetime.now().strftime('%Y-%m-%d')}

Description:
This is an automatically generated Python script with common imports and structure.
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional

# Constants
CONSTANT_EXAMPLE = 42

def main():
    """Main function that runs when the script is executed"""
    print("Hello from Python script!")
    print(f"Current working directory: {{os.getcwd()}}")
    
    # Example numpy operation
    arr = np.array([1, 2, 3])
    print(f"Numpy array sum: {{arr.sum()}}")
    
    # Example pandas DataFrame
    df = pd.DataFrame({{'A': [1, 2], 'B': [3, 4]}})
    print("\\nSample DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
'''

    with open(f"{filename}.py", "w") as f:
        f.write(content)
    print(f"Created Python script: {filename}.py")

def create_jupyter_notebook(filename):
    """Create a basic Jupyter Notebook with common cells"""
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {filename}.ipynb",
                    "\n",
                    "## Jupyter Notebook Analysis\n",
                    f"*Generated on {datetime.now().strftime('%Y-%m-%d')}*\n",
                    "\n",
                    "This is an automatically generated Jupyter Notebook with common analysis setup."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Common imports\n",
                    "import numpy as np\n",
                    "import pandas as pd\n",
                    "import matplotlib.pyplot as plt\n",
                    "%matplotlib inline\n",
                    "\n",
                    "print(\"Jupyter Notebook ready for analysis!\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example data analysis\n",
                    "data = pd.DataFrame({\n",
                    "    'Values': np.random.randn(100),\n",
                    "    'Category': np.random.choice(['A', 'B', 'C'], 100)\n",
                    "})\n",
                    "\n",
                    "data.head()"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example visualization\n",
                    "plt.figure(figsize=(8, 4))\n",
                    "data['Values'].hist(bins=20)\n",
                    "plt.title('Distribution of Values')\n",
                    "plt.xlabel('Value')\n",
                    "plt.ylabel('Frequency')\n",
                    "plt.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Next Steps\n",
                    "\n",
                    "1. Add your analysis code in new cells\n",
                    "2. Document your process with markdown cells\n",
                    "3. Save your work regularly"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with open(f"{filename}.ipynb", "w") as f:
        json.dump(notebook_content, f)
    print(f"Created Jupyter notebook: {filename}.ipynb")

if __name__ == "__main__":
    base_name = input("Enter base name for files (without extension): ").strip()
    if not base_name:
        base_name = "analysis"
    
    create_python_script(base_name)
    create_jupyter_notebook(base_name)
    
    print("\nFiles created successfully!")
    print(f"- Python script: {base_name}.py")
    print(f"- Jupyter notebook: {base_name}.ipynb")