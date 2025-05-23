from typing import Dict, Any
from arklex.exceptions import AuthenticationError

HUBSPOT_AUTH_ERROR: str = "Missing some or all required hubspot authentication parameters: access_token. Please set up 'fixed_args' in the config file. For example, {'name': <unique name of the tool>, 'fixed_args': {'token': <shopify_access_token>, 'shop_url': <shopify_shop_url>, 'api_version': <Shopify API version>}}"


def authenticate_hubspot(kwargs: Dict[str, Any]) -> str:
    access_token: str = kwargs.get("access_token")
    if not access_token:
        raise AuthenticationError(HUBSPOT_AUTH_ERROR)

    return access_token
