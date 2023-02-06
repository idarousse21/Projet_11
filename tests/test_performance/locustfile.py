from locust import HttpUser, task, between


class TestPerformanceProject(HttpUser):
    wait_time = between(1, 5)

    club = {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    }
    competition = {
        "name": "Spring Festival",
        "date": "2023-05-27 10:00:00",
        "numberOfPlaces": "25"
    }
    purchase = {
        "club": club["name"],
        "competition": competition["name"],
        "places": 5,
    }

    def on_start(self):
        self.client.get("/")
        self.client.post("/showSummary", data={"email": self.club["email"]})

    @task
    def display_board_for_points(self):
        self.client.get("/displayPoints")

    @task
    def get_places_for_competition(self):
        self.client.get(f"/book/{self.competition['name']}/{self.club['name']}")

    def post_purchases_competition_tickets(self):
        self.client.get("/purchasesPlaces", data=self.purchase)

    