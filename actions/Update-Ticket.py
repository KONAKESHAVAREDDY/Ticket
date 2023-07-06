from lib.actions import BaseAction

class UpdateIncidentAction(BaseAction):
    def run(self,sys_id):
        client = self.client

        endpoint = '/table/incident'
        url = client.base_url + endpoint

        # Print the constructed URL for the PUT request
        print(url)

        payload = {
            "short_description": "Updated incident description",
            "urgency": "2",
            "state": "2"
        }

        response = client.resource(api_path=endpoint).update(payload=payload, query={'sys_id':sys_id})
        return sys_id
