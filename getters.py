import config
import pandas as pd


class DataGetter:
    def __init__(self):
        if config.DATA_FILE.endswith(".xlsx"):
            self.config_data = pd.read_excel(config.DATA_FILE, sheet_name=['Team', 'Database-Records'],keep_default_na=False)
        else:
            raise("Wrong data file. Needs to be excel and in the format described in the README.")


    def get_team(self) -> dict:
        team = dict()
        names = self.config_data["Team"]
        names = names.replace('nan','')
        for name, apellido1, apellido2 in zip(names.Nombre, names.Apellido_1, names.Apellido_2):
            
            if apellido2 == '':
                full_name = " ".join([name, apellido1])
                apellido2 = apellido1
            else:
                full_name = " ".join([name, apellido1, apellido2])
            
            key_initials = name[0].upper()+ apellido1[0].upper() + apellido2[0].upper()
            team[key_initials] = full_name

        return team
