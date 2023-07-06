from lib.actions import BaseAction

class ReadIncidentAction(BaseAction):
    def run(self,sys_id):
        client = self.client

        endpoint = '/table/incident/{0}'.format(sys_id)  # Endpoint for reading an incident in ServiceNow
        response = client.resource(api_path=endpoint).get(query={})
        return sys_id  # Return the incident data
