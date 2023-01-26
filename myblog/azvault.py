from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class AzVault():

    @staticmethod
    def getSecret(name, vaulturi = "https://blog-db-secrets.vault.azure.net/"):
        try:
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url = vaulturi, credential = credential)
            secret = client.get_secret(name)
            return secret.value
        except:
            return None