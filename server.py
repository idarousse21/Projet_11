import json
from flask import Flask, render_template, request, redirect, flash, url_for
from http import HTTPStatus
from collections import defaultdict


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


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()
clubs_purchase = purchases_initialization_por_club(clubs, competitions)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = [club for club in clubs if club["email"] == request.form["email"]][0]
    return render_template(
        "welcome.html",
        club=club,
        competitions=competitions,
        club_competition_purchases=clubs_purchase,
    )


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
    new_purchases_club = int(purchases_club) + placesRequired
    if new_purchases_club <= 12:
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - placesRequired
        )
        clubs_purchase[club["email"]][competition["name"]] += placesRequired
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            club_competition_purchases=clubs_purchase,
        )

    else:
        flash("You cannot buy more than 12 places for this competition.")
        return (
            render_template(
                "booking.html",
                club=club,
                competition=competition,
                club_competition_purchases=clubs_purchase,
            ),
            HTTPStatus.BAD_REQUEST,
        )


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
