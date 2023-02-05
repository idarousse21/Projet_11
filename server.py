import json
from flask import Flask, render_template, request, redirect, flash, url_for
from http import HTTPStatus
from collections import defaultdict
from datetime import datetime


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def purchases_initialization_por_club(clubs, competitions):
    clubs_purchase = defaultdict(lambda: defaultdict(int))
    for club in clubs:
        for competition in competitions:
            clubs_purchase[club["email"]][competition["name"]]
    return clubs_purchase

def get_future_competitions():
    today_date = datetime.now()
    return [
        competition
        for competition in loadCompetitions()
        if datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S") > today_date
    ]

app = Flask(__name__)
app.secret_key = "something_special"

clubs = loadClubs()
clubs_purchase = purchases_initialization_por_club(clubs, get_future_competitions())
competitions = get_future_competitions()



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            club_competition_purchases=clubs_purchase,
        )
    except IndexError:
        flash("The email is incorrect.")
        return redirect(url_for("index"))


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            "booking.html",
            club=foundClub,
            competition=foundCompetition,
            club_competition_purchases=clubs_purchase,
        )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            club_competition_purchases=clubs_purchase,
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    purchases_club = clubs_purchase[club["email"]][competition["name"]]
    purchase_valid = valid_purchase(
        placesRequired,
        int(competition["numberOfPlaces"]),
        int(club["points"]),
        int(purchases_club),
    )
    if purchase_valid[0]:
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - placesRequired
        )
        club["points"] = int(club["points"]) - placesRequired
        clubs_purchase[club["email"]][competition["name"]] += placesRequired
        flash(purchase_valid[1])
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            club_competition_purchases=clubs_purchase,
        )
    else:
        flash(purchase_valid[1])
        return render_template(
            "booking.html",
            club=club,
            competition=competition,
            club_competition_purchases=clubs_purchase,
        )


@app.route("/displayPoints")
def display_clubs_points():
    clubs_sort_by_alphabet = sorted(clubs, key=lambda club: club["name"])
    return render_template("display_clubs_points.html", clubs=clubs_sort_by_alphabet)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


def valid_purchase(
    places_required, number_places_competition, number_places_club, places_club
):
    if places_required > number_places_club:
        message = "The club points balance is lower than the places bought."
        return False, message
    elif (places_required + places_club) > 12:
        message = "You cannot buy more than 12 places for this competition."
        return False, message
    elif places_required <= 0:
        message = "The number of seats purchased cannot be less than 1"
        return False, message
    elif places_required > number_places_competition:
        message = "The places to ask for are superior to the places available in the competition."
        return False, message
    else:
        message = "Great-booking complete!"
        return True, message
