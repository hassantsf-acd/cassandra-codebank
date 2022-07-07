import pandas as pd

from collection.api import get_codeforces_problems
from collection.scrap import get_spoj_problems

fieldnames = ['id', 'title', 'type', 'difficulty', 'company', 'submits', 'solved', 'tags', 'time_step']

codeforces_df = pd.DataFrame(get_codeforces_problems())
spoj_df = pd.DataFrame(get_spoj_problems())

df = pd.concat([codeforces_df, spoj_df], ignore_index=True, sort=False)

df.to_csv('../data.csv', index=False)