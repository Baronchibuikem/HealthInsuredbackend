# =====================
# Utility imports
# =====================
from libs.utils import core_util_crypt

# =====================
# App imports
# =====================
from app_enrollment.models import ClientOrganization, ClientIndividual


class OrganizationBackend:
    def authenticate(self, request, **credentials):
        print(credentials)
        try:
            organization = ClientOrganization.objects.get(email=credentials["email"])
            valid_password = core_util_crypt.compare_plain_value_to_hash(credentials['password'],organization.password)
            
            if organization and valid_password:
                return organization
            return None
        except:
            return None

    
    def get_user(self, organization_id):
        try:
            return ClientOrganization.objects.get(client_id=organization_id)
        except:
            return None


class IndividualBackend:
    def authenticate(self, request, **credentials):
        try:
            individual = ClientIndividual.objects.get(email=credentials["email"])
            valid_password = core_util_crypt.compare_plain_value_to_hash(credentials['password'],individual.password)
            
            if individual and valid_password:
                return individual
            return None
        except:
            return None

    
    def get_user(self, individual_id):
        try:
            return ClientIndividual.objects.get(client_id=individual_id)
        except:
            return None