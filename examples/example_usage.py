from astropy.coordinates import SkyCoord
from decalsquery import DECaLSQuery

# Define coordinates of the galaxy
coordinates = SkyCoord(ra=173.145238,  dec=53.06792, unit='deg')

# Initialize DECaLSQuery object
query = DECaLSQuery(output_dir='downloads')

# Query and download both JPG and FITS images
query.query_region(coordinates, size=100, download_type='both', galid="example_galaxy")
