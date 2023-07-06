from lib.actions import BaseAction

class DeleteIncidentAction(BaseAction):
    def run(self, sys_id):
        client = self.client

        endpoint = '/table/incident'  # Remove the sys_id from the endpoint
        url = client.base_url + endpoint
        # Print the constructed URL for the DELETE request
        print(url)

        response = client.resource(api_path=endpoint).delete(query={'sys_id': sys_id})  # Add the sys_id as a query parameter
        return response
