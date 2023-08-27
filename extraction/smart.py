import pandas as pd
import requests
import json


class invoke_smart:
    def __init__(self, moniter_json='stock_moniter_links.json'):
        self.moniter_json=moniter_json
        
    def load_json(self) -> {}:
        with open(self.moniter_json,'r') as file:
            links=json.load(file)
        self.staging_path=links['staging_path']
        return links
    
    #Download csv files in staging area for further operations
    def stage_file(self,path,staging_path):
        file_name=path.rsplit('/',1)[1]
        try:
            response = requests.get(path)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful            
            with open(staging_path+file_name, 'wb+') as file:
                file.write(response.content)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))



def main():
    smart=invoke_smart()
    links=smart.load_json()

    for type,link in links.items():
        if type != "staging_path":
            smart.stage_file(link,links['staging_path'])

if __name__ == '__main__':
    main()
        