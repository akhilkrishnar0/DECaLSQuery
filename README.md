<<<<<<< HEAD
# DECaLSQuery
=======
# DECaLSQuery

A Python utility to query and download DECaLS (Dark Energy Camera Legacy Survey) image cutouts in JPG or FITS format.

## Features
- Download JPG or FITS cutouts by RA, Dec, and size.
- Save outputs in structured directories.

## Installation
Clone the repository:
```bash
git clone <repo-url>



Install required dependencies:

pip install -r requirements.txt


Usage
from decals_query import DECaLSQuery
from astropy.coordinates import SkyCoord

coords = SkyCoord(ra=10.684, dec=41.269, unit="deg")
query = DECaLSQuery(output_dir="downloads")
query.query_region(coords, size=256, download_type='both', galid="example")

>>>>>>> 85587ca (Initial commit with DECaLSquery)
