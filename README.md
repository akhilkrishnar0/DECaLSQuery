# DECaLSQuery
=======

DECaLSQuery is a Python package that allows users to query the DECaLS catalog for image cutouts. This package provides an easy-to-use interface for downloading JPG and FITS images of galaxies from the DECaLS survey.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akhilkrishnar0/DECaLSQuery.git
   cd DECaLSQuery
   pip install .
   

Unable to Install DECaLSQuery via pip see this: https://github.com/akhilkrishnar0/DECaLSQuery/issues/1

2. Install dependencies:
pip install -r requirements.txt



3. Usage:
   ```bash
   from astropy.coordinates import SkyCoord
   from decals_query import DECaLSQuery
   coordinates = SkyCoord(ra=173.145238, dec=53.06792, unit='deg')

   query = DECaLSQuery(output_dir='downloads', layer='ls-dr9')

   query.query_region(
    coordinates,
    size=100,
    download_type='all',  # options: jpg, fits, psf, invvar, all
    galid="example_galaxy")




4. Add `requirements.txt`:
This file contains the necessary dependencies.

```txt
   astroquery
   astropy
   requests

