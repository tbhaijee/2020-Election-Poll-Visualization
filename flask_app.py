import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("postgresql://postgres:superuser@localhost:5432/election_db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


poll_data = Base.classes.poll_data

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"Below route list Election 2020 Poll Data <br/>"        
        f"/api/v1.0/Poll_Data<br/>"
        f"<br/>"
        f"Below route takes state name and list election 2020 poll for the state <br/>"
        f"/api/v1.0/statename/<state_name><br/>"
        f"<br/>"
        f"Below route takes state abbrevation and list election 2020 poll for the state <br/>"
        f"/api/v1.0/stateabbrevation/<state_abbv><br/>"
        f"<br/>"
        f"Below route takes state abbrevation and list election 2020 poll for the state <br/>"
        f"/api/v1.0/party/<party><br/>"
      

    )

@app.route("/api/v1.0/Poll_Data")
def data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all date as the key and prcp as the value."""
    # Query all dates
    result = session.query(poll_data.id,poll_data.name, poll_data.abbv, poll_data.candidate_name,poll_data.candidate_party,poll_data.pct).all()

    session.close()

    return jsonify(result) 


@app.route("/api/v1.0/statename/<state_name>")
def filter_data(state_name):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(poll_data.abbv, poll_data.candidate_name,poll_data.candidate_party,poll_data.pct).filter(poll_data.name == state_name).all()
    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/stateabbrevation/<state_abbv>")
def filter_data_abbv(state_abbv):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(poll_data.name, poll_data.candidate_name,poll_data.candidate_party,poll_data.pct).filter(poll_data.abbv == state_abbv).all()
    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/party/<party>")
def filter_data_party(party):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results= session.query(poll_data.name, poll_data.candidate_name,poll_data.candidate_party,poll_data.pct).filter(poll_data.candidate_party == party).all()
    session.close()
    
    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)