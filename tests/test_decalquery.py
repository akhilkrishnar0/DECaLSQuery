import unittest
from astropy.coordinates import SkyCoord
from decalsquery import DECaLSQuery

class TestDECaLSQuery(unittest.TestCase):
    def setUp(self):
        self.query = DECaLSQuery(output_dir="test_downloads")
        self.coordinates = SkyCoord(ra=150.116, dec=2.205, unit='deg')

    def test_download_image(self):
        self.query.download_image("test_galaxy", self.coordinates.ra.deg, self.coordinates.dec.deg, 100)

    def test_download_fits(self):
        self.query.download_fits("test_galaxy", self.coordinates.ra.deg, self.coordinates.dec.deg, 100)

    def test_query_region(self):
        self.query.query_region(self.coordinates, size=100, download_type='both', galid="test_galaxy")

if __name__ == "__main__":
    unittest.main()
