from allauth.socialaccount import providers
from allauth.account.models import EmailAddress
from allauth.socialaccount.app_settings import QUERY_EMAIL
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class FourtyTwoAccount(ProviderAccount):
    pass
    # def get_profile_url(self):
    #     return self.account.extra_data.get("url")

    # def get_avatar_url(self):
    #     return self.account.extra_data.get("image", {}).get("versions",{}).get("small")
    
    # def to_str(self):
    #     default = super(FourtyTwoAccount, self).to_str()
    #     return self.account.extra_data.get("displayname", default)


class FourtyTwoProvider(OAuth2Provider):
    id = "fourtytwo"
    name = "FourtyTwo"
    account_class = FourtyTwoAccount

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
                    user=data['login'],
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    )

    def extract_email_addresses(self, data):
        ret = []
        email = data.get("email")
        if email:
            # verified = bool(data.get("email_verified") or data.get("verified_email"))
            ret.append(EmailAddress(email=email, verified=True, primary=True))
        return ret

    # def get_default_scope(self):
    #     pass


# providers.registry.register(FourtyTwoProvider)
provider_classes = [FourtyTwoProvider]	