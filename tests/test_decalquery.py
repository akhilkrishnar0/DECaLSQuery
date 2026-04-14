import unittest
from astropy.coordinates import SkyCoord
from decalsquery import DECaLSQuery

class TestDECaLSQuery(unittest.TestCase):
    def setUp(self):
        self.query = DECaLSQuery(output_dir="test_downloads", layer="ls-dr9")
        self.coordinates = SkyCoord(ra=150.116, dec=2.205, unit='deg')

    def test_download_image(self):
        self.query.download_image(
            "test_galaxy",
            self.coordinates.ra.deg,
            self.coordinates.dec.deg,
            100
        )

    def test_download_fits(self):
        self.query.download_fits(
            "test_galaxy",
            self.coordinates.ra.deg,
            self.coordinates.dec.deg,
            100
        )

    def test_download_psf(self):
        self.query.download_psf(
            "test_galaxy",
            self.coordinates.ra.deg,
            self.coordinates.dec.deg
        )

    def test_download_invvar(self):
        self.query.download_invvar(
            "test_galaxy",
            self.coordinates.ra.deg,
            self.coordinates.dec.deg,
            100
        )

    def test_query_region_all(self):
        self.query.query_region(
            self.coordinates,
            size=100,
            download_type='all',
            galid="test_galaxy"
        )

    def test_query_region_individual_types(self):
        for dtype in ['jpg', 'fits', 'psf', 'invvar']:
            with self.subTest(download_type=dtype):
                self.query.query_region(
                    self.coordinates,
                    size=100,
                    download_type=dtype,
                    galid=f"test_{dtype}"
                )

if __name__ == "__main__":
    unittest.main()
