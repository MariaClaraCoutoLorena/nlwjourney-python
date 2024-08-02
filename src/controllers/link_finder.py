
class LinkFinder:
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def find(self, trip_id) -> dict:
        try:            
            links = self.__links_repository.find_links_from_trip(trip_id)
            
            formatted_links = []

            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "link": link[2],
                    "title": link[3],
                })

            return {
                "body": {
                    "links": formatted_links
                },
                "status_code": 200
            }
        
        except Exception as excepetion:    
            return {
                "body": { "error": "Bad Request", "message": str(excepetion) },
                "status_code": 400
            }
