import uuid
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.drivers.emails_sender import send_email

class TripCreator():
    def __init__(self, trips_repository: TripsRepository, emails_repository: EmailsToInviteRepository) -> None:
        self.__trip_repository = trips_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> dict:
        try:
            trip_id = str(uuid.uuid4())
            trip_infos = { **body, "id": trip_id }
            self.__trip_repository.create_trip(trip_infos)

            emails = body.get("emails_to_invite")
            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "id": str(uuid.uuid4()),
                        "trip_id": trip_id,
                        "email": email
                    })
            
            send_email([body["owner_email"]], f"http://localhost:3000/trips/{trip_id}/confirm" )

            return {
                "body": { "id": trip_id },
                "status_code": 201
            }
        
        except Exception as excepetion:    
            return {
                "body": { "error": "Bad Request", "message": str(excepetion) },
                "status_code": 400
            }
