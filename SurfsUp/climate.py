# Import the dependencies.

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.sql import exists  
import datetime as dt
import numpy as np
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Save references to each table
Station=Base.classes.station
Measurement=Base.classes.measurement

# Create our session (link) from Python to the DB
session=Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    """List of all available api routes."""
    return (
        f"Welcome to the Climate API! "      
        f"Please check out the available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/start/end "

    )

# ####################################################################################
@app.route("/api/v1.0/precipitation") 

def precipitation():

# Query precipitation
    results = (session.query(Measurement.date, Measurement.tobs)
                      .order_by(Measurement.date))

#creating  dictionary
    prcp_date_tobs = []
    for row in results:
        date_dict = {}
        date_dict["date"] = row.date
        date_dict["tobs"] = row.tobs
        prcp_date_tobs.append(date_dict)

    return jsonify(prcp_date_tobs)

# #######################################################################################

@app.route("/api/v1.0/stations") 

def stations():

# Query Stations
    results = session.query(Station.name).all()

    station_details = list(np.ravel(results))

    return jsonify(station_details)


if __name__ == "__main__":
    app.run(debug=True)
