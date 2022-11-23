from app.cafe import Cafe
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    total = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            total += 1
    if total:
        return f"Friends should buy {total} masks"
    return f"Friends can go to {cafe.name}"
