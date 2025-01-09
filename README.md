# DECaLSQuery
=======

DECaLSQuery is a Python package that allows users to query the DECaLS catalog for image cutouts. This package provides an easy-to-use interface for downloading JPG and FITS images of galaxies from the DECaLS survey.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akhilkrishnar0/DECaLSQuery.git
   cd DECaLSQuery



2. Install dependencies:
pip install -r requirements.txt



3. Usage:
   ```bash
   from astropy.coordinates import SkyCoord
   from decalsquery import DECaLSQuery # Define coordinates of the galaxy
   coordinates = SkyCoord(ra=173.145238,  dec=53.06792, unit='deg') # Initialize DECaLSQuery object
   query = DECaLSQuery(output_dir='downloads') # Query and download both JPG and FITS images
   query.query_region(coordinates, size=100, download_type='both', galid="example_galaxy")




4. Add `requirements.txt`:
This file contains the necessary dependencies.

```txt
   astroquery
   astropy
   requests

