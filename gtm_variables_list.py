from ga3_credentials import get_service
from googleapiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
from oauth2client.service_account import ServiceAccountCredentials

def list_variables(service, parent):
    """This Returns the GTM properties (Id, Name) that the user has read access.

    Args:
    service: service object for authorising the operation.

    Returns:
        A dict with the accounts: (Id, Name).
    """
    
    try:
        variables = service.accounts().containers().workspaces().variables().list(
            parent=parent).execute()
        

        return variables

    except TypeError as error:
      # Handle errors in constructing a query.
      print('There was an error in constructing your query : ', error)

    except HttpError as error:
        # Handle API errors.
        print ('There was an API error : ', error.status_code, error.reason)
  
    except AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run' 
        'the application to re-authorize')  


if __name__ == '__main__':
    # Define the auth scopes to request.
    scope = ['https://www.googleapis.com/auth/tagmanager.readonly', 'https://www.googleapis.com/auth/tagmanager.edit.containers']
    key_file_location = 'google_credentials.json'
    # Authenticate and construct service.
    service = get_service('tagmanager', 'v2', scope, key_file_location)
    account_id = '123467890'
    container_id = '0987654321'
    workspace_id = '1'
    variable_id = '666'
    parent = "accounts/" + account_id + "/containers/" + container_id + "/workspaces/" + workspace_id
    result = list_variables(service, parent)
    print(result)

