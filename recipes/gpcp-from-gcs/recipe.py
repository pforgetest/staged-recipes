import pandas as pd
from pangeo_forge_recipes.patterns import ConcatDim, FilePattern
from pangeo_forge_recipes.recipes import XarrayZarrRecipe

dates = pd.date_range("1996-10-01", "2022-02-01", freq="D")


def make_url(date):
    url_base = "https://storage.googleapis.com/pforge-test-data"
    return f"{url_base}/gpcp/v01r03_daily_d{date.strftime('%Y%m%d')}.nc"


concat_dim = ConcatDim("time", dates, nitems_per_file=1)
pattern = FilePattern(make_url, concat_dim)

recipe = XarrayZarrRecipe(
    pattern,
    inputs_per_chunk=200,
    xarray_open_kwargs={"decode_coords": "all"}
)
