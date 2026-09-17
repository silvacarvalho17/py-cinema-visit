from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        ...
