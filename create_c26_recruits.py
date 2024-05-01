from models import Recruit, session


with session as s:
    s.add_all(
        [
            Recruit(
                first_name="Dibe",
                surname="Modise",
                chatname="Dibe",
                github_name="Dibe",
                id_number="9803180075083",
                personal_email_address="dibe.modise@umuzi.org",
                cohort="C26 Data Eng",
            ),
            Recruit(
                first_name="Kopano",
                surname="Ncutha",
                chatname="Kopano",
                github_name="Kopano",
                id_number="060316061086",
                personal_email_address="kopano.ncutha@umuzi.org",
                cohort="C26 Data Eng",
            ),
            Recruit(
                first_name="Mbulelo",
                surname="Dube",
                chatname="Mbulelo",
                github_name="Mbulelo",
                id_number="9607150756071",
                personal_email_address="mbulelo.dube@umuzi.org",
                cohort="C26 Data Eng",
            ),
            Recruit(
                first_name="Refiloe",
                surname="Mokoena",
                chatname="Refiloe",
                github_name="Refiloe",
                id_number="0104010457068",
                personal_email_address="refiloe.mokoena@umuzi.org",
                cohort="C26 Data Eng",
            ),
            Recruit(
                first_name="Lesego",
                surname="Moeketsi",
                chatname="Lesego",
                github_name="Lesego",
                id_number="9802190887083",
                personal_email_address="lesego.moeketsi@umuzi.org",
                cohort="C26 Data Eng",
            ),
        ]
    )
    s.commit()