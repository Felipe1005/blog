from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = ''
    account_key = ''
    azure_container = ''
    expiration_secs = None
