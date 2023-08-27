import pandas as pd
import requests
import json
import os


class invoke_smart:
    def __init__(self, moniter_json='stock_moniter_links.json'):
        self.working_directory='/workspaces/freelance/'
        self.code_directory=self.working_directory+'extraction/'
        self.staging_directory=self.working_directory+'staging/'
        self.moniter_json=self.code_directory+moniter_json
        self.data_path=self.working_directory+'/data/'
        
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
    
    def _bulk_csv(self,df):
        #this will hold all the securities name along with symbol for now.
        #It's look redundant yet useful information for future.
        df_security_name    =   df[['Symbol','Security Name']].drop_duplicates()
        df_security_name.reset_index(drop=True).to_csv(self.data_path+'securities.csv')
        
        df_trade    =   df.drop(columns=['Security Name']).drop_duplicates()
        return df_trade
        
        
    
    def data_analyzer(self):
        for files in os.listdir(self.staging_directory):
            df=pd.read_csv(files)
            if files.split('.')[0] == "bulk":
                bulk_trade_df = self._bulk_csv(df)
        
        print(bulk_trade_df.head())


def main():
    smart=invoke_smart()
    links=smart.load_json()

    for type,link in links.items():
        if type != "staging_path":
            smart.stage_file(link,links['staging_path'])
    
    smart.data_analyzer()

if __name__ == '__main__':
    main()
        