from typing import List
from pyspark.sql import DataFrame
from pyspark.sql import functions as F 
from pyspark.sql.functions import lit

from datetime import datetime
from dateutil import parser

import os

## update dataframe values 
df.loc[df['country'] == 'United States', 'country'] = 'United States of America'




