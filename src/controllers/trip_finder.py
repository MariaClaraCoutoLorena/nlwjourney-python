from src.models.repositories.trips_repository import TripsRepository

class TripFinder():
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trip_repository = trips_repository

    def find_trip_details(self, trip_id) -> dict:
        try:            
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            
            if not trip: raise Exception("No Trip Found")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "start_date": trip[2],
                        "end_date": trip[3],
                        "status": trip[6]
                    }
                },
                "status_code": 200
            }
        
        except Exception as excepetion:    
            return {
                "body": { "error": "Bad Request", "message": str(excepetion) },
                "status_code": 400
            }
