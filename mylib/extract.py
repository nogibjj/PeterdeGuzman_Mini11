"""
Extracting dataset from CSV files hosted online
"""

import requests
import os
import zipfile
import chardet
import io


def extract(
    url,
    filepath,
    directory,
):
    """Extract to file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url, timeout=5) as r:
        with open(filepath, "wb") as f:
            f.write(r.content)
    return filepath




