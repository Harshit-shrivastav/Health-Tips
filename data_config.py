from opal_client.data.updater import DataUpdater

data_source_url = "http://localhost:8000/data"

data_updater = DataUpdater(data_source_url=data_source_url)

data_to_sync = {
    "roles": {
        "admin": ["view", "edit", "delete"],
        "guest": ["view"]
    }
}

data_updater.update_data(data_to_sync)
