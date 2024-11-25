import config
import pandas as pd


class DataGetter:
    def __init__(self):
        if config.DATA_FILE.endswith(".xlsx"):
            self.setup_data = pd.read_excel(config.DATA_FILE, sheet_name=['Team', 'Database-Records'])

        else:
            raise("Wrong data file. Needs to be excel and in the format described in the README.")


    def get_team(self) -> dict:
        team = dict()
        names = self.setup_data["Team"]
        names = names.fillna('')
        for name, apellido1, apellido2 in zip(names.Nombre, names.Apellido_1, names.Apellido_2):
            
            if apellido2 == '':
                full_name = " ".join([name, apellido1])
                apellido2 = apellido1
            else:
                full_name = " ".join([name, apellido1, apellido2])
            
            key_initials = name[0].upper()+ apellido1[0].upper() + apellido2[0].upper()
            team[key_initials] = full_name

        return team
    
    def get_db(self) -> list:
        db_fields = self.setup_data["Database-Records"].columns.to_list()

        return db_fields
        
    def get_records(self) -> list:
        test_func = lambda x: x != ''
        filtered_fields = list(filter(test_func, self.setup_data["Database-Records"].iloc[0].to_list()))

        return filtered_fields
    
    def get_record_db_relation(self) -> dict:
        
        # Dict like {"DB Field": "Field_record_field"}
        # No empty field record fields.

        relations = self.setup_data["Database-Records"].dropna(axis=1, how='all') # remove all columns that have no data.
        record_db = relations.to_dict(orient='records')[0] #record returns a list of dicts, so access the first one.
        inverted_records = dict((v, k) for k, v in record_db.items())

        return inverted_records