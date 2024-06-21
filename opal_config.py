import os
from opal_client.config import opal_client_config
from opal_client.client import OPALClient

opal_client_config.SERVER_URL = os.getenv("OPAL_SERVER_URL")

opal_client = OPALClient(config=opal_client_config)
opal_client.setup()
