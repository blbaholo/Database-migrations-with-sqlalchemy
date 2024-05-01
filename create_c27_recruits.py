from models import Recruit, session

with session as s:
    s.add_all(
        [
            Recruit(
                first_name="Felicia",
                surname="Mosome",
                rocketchat_user="Felicia",
                github_name="Felicia",
                id_number="9526127654345",
                personal_email_address="felicia.mosome@umuzi.org",
                cohort="C27 Data Eng",
            ),
            Recruit(
                first_name="Karabo",
                surname="Ratlabala",
                rocketchat_user="Karabo",
                github_name="Karabo",
                id_number="9730129875087",
                personal_email_address="karabo.ratlabala@umuzi.org",
                cohort="C27 Data Eng",
            ),
            Recruit(
                first_name="Odirile",
                surname="Gaborone",
                rocketchat_user="Odirile",
                github_name="Odirile",
                id_number="9801067548071",
                personal_email_address="odirile.gaborone@umuzi.org",
                cohort="C27 Data Eng",
            ),
            Recruit(
                first_name="Sibongile",
                surname="Pikoli",
                rocketchat_user="Sibongile",
                github_name="Sibongile",
                id_number="9405045678081",
                personal_email_address="sibongile.pikoli@umuzi.org",
                cohort="C27 Data Eng",
            ),
            Recruit(
                first_name="Nqobile",
                surname="Mondlhane",
                rocketchat_user="Nqobile",
                github_name="Nqobile",
                id_number="9619058765089",
                personal_email_address="nqobile.mondhlane@umuzi.org",
                cohort="C27 Data Eng",
            ),
        ]
    )
    s.commit()