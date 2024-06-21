from opal_client.policy import PolicyStoreClient
from opal_client.config import opal_client_config
import json

policy_store_client = PolicyStoreClient(config=opal_client_config)
policy_store_client.setup()

def enforce_access_control(user_role, action):
    query = {
        "input": {
            "user_role": user_role,
            "action": action
        }
    }
    result = policy_store_client.query("data.authz.allow", query)
    return result['result']
