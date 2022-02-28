import pandas as pd
import io
from js import fetch

from .utils import get_contents

import warnings 
warnings.filterwarnings("ignore")

# Via: https://github.com/jupyterlite/jupyterlite/issues/119#issuecomment-854495013
async def read_csv_local(fn, sep=","):
    """"""
    return pd.read_csv(io.StringIO((await get_contents(fn))["content"]), sep = sep)

#df = await read_csv_jupyterlite("iris.csv", "\t")
#df

async def read_csv_url(url, sep=",", dummy_fn="_data.csv"):
    """Load CSV file from URL into pandas dataframe."""
    res = await fetch(url)
    text = await res.text()


    with open(dummy_fn, 'w') as f:
        f.write(text)

    data = pd.read_csv(dummy_fn, sep=sep)
    return data

#URL = "https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv"
#df = await read_csv_url(URL, "\t")
#df