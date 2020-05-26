import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities


start_session = pd.Timestamp('2015-5-15', tz='utc')
end_session = pd.Timestamp('2020-5-15', tz='utc')


register(
    'eod-yahoofinance',
    csvdir_equities(
        ['daily'],
        'AI-Alpha/data',
    ),
    calendar_name='XBOM', 
    start_session=start_session,
    end_session=end_session
)
