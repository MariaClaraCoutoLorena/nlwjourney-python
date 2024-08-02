from sqlite3 import Connection

class ParticipantsRepository:

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO participants
                id TEXT PRIMARY KEY,
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"],
            )
        )
        self.__conn.commit()

    def confirm_participant(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                    SET is_confirmed = 1
                WHERE 
                    id = ?
            ''', (
                participant_id,
            )
        )
        cursor.commit()

    def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                from participant as p 
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''', (
                trip_id,
            ) 
        )
        participants = cursor.fetchall()
        return participants