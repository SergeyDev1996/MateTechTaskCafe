from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("not wearing mask")
        return f"Welcome to {self.name}"
