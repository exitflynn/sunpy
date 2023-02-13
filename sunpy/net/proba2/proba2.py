import astropy.table

from sunpy.net import attr
from sunpy.net.base_client import BaseClient, QueryResponseTable


class Proba2Response(QueryResponseTable):
    query_args = astropy.table.TableAttribute()
    requests = astropy.table.TableAttribute()
    display_keys = ['calibrated', 'extension', 'file_date', 'file_name', 'file_oid', 'file_path', 'file_size', 'file_type', 'instrument_name', 'instrument_oid', 'processing_level']
    # This variable is used to detect if the result has been sliced before it is passed
    # to fetch and issue a warning to the user about not being able to post-filter JSOC searches.
    _original_num_rows = astropy.table.TableAttribute(default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_num_rows = len(self)


class Proba2Client(BaseClient):
    """
    Provides access to the Proba-2 in-situ DSLP data.

    The HEK stores solar feature and event data generated by algorithms and
    human observers.
    will insert description here
    """
    @property
    def info_url(self):
        return 'http://p2sa.esac.esa.int/p2sa/'

    def search(self, *query, **kwargs):
        response = Proba2Response(client=self)
        query = attr.and_(*query)
