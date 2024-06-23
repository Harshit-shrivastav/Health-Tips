from opal_client.data.updater import DataUpdater

# data source URL
data_source_url = "http://localhost:7002/data"

# DataUpdater instance
data_updater = DataUpdater(data_source_url=data_source_url)

# data to synchronize
data_to_sync = {
    "roles": {
        "admin": ["view", "edit", "delete"],
        "guest": ["view"]
    }
}

# Synchronize the data
data_updater.update_data(data_to_sync)
