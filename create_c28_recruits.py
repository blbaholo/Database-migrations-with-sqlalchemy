from models import Recruit, session


with session as s:
    s.add_all(
        [
            Recruit(
                first_name="Palesa",
                surname="Phalane",
                rocketchat_user="Palesa",
                github_name="Palesa",
                personal_email_address="palesa.phalane@umuzi.org",
                cohort="C28 Data Eng",
            ),
            Recruit(
                first_name="Phina",
                surname="Ramalepa",
                rocketchat_user="Phina",
                github_name="Phina",
                personal_email_address="phina.ramalepa@umuzi.org",
                cohort="C28 Data Eng",
            ),
            Recruit(
                first_name="Nothando",
                surname="Mhlongo",
                rocketchat_user="Nothando",
                github_name="Nothando",
                personal_email_address="nothando.mhlongo@umuzi.org",
                cohort="C28 Data Eng",
            ),
            Recruit(
                first_name="Nomthandazo",
                surname="Mthembu",
                rocketchat_user="Nomthandazo",
                github_name="Nomthandazo",
                personal_email_address="nomthandazo.mthembu@umuzi.org",
                cohort="C28 Data Eng",
            ),
            Recruit(
                first_name="Boikanyo",
                surname="Khenzo",
                rocketchat_user="Boikanyo",
                github_name="Boikanyo",
                personal_email_address="boikanyo.khenzo@umuzi.org",
                cohort="C28 Data Eng",
            ),
        ]
    )
    s.commit()