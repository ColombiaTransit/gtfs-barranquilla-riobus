#!/usr/bin/env python3
"""Generate a provisional static GTFS feed for RíoBus Karakalí."""
import csv, datetime as dt, io, json, math, sys, zipfile
from pathlib import Path
import holidays

ROOT = Path(__file__).resolve().parents[1]

def table(header, rows):
    stream = io.StringIO()
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(header.split(","))
    writer.writerows(rows)
    return stream.getvalue()

def build(start, end):
    src = json.loads((ROOT / "data/riobus-osm.json").read_text())
    points = src["geometry"]
    terminal = src["terminal"]
    assert len(points) == 55 and points[0] == points[-1]
    assert points[0] == [terminal["lat"], terminal["lon"]]
    if end < start: raise ValueError("Invalid calendar interval")
    out = {}
    out["agency.txt"] = table("agency_id,agency_name,agency_url,agency_timezone,agency_lang", [
        ["puerta_de_oro","Puerta de Oro Empresa de Desarrollo Caribe","https://visit.barranquilla.gov.co/planes/karakali","America/Bogota","es"]])
    out["stops.txt"] = table("stop_id,stop_name,stop_lat,stop_lon", [
        ["puerta_de_oro_pier","RíoBus - Muelle Puerta de Oro",terminal["lat"],terminal["lon"]]])
    out["routes.txt"] = table("route_id,agency_id,route_short_name,route_long_name,route_type", [
        ["karakali","puerta_de_oro","RíoBus","Karakalí sightseeing loop",4]])
    shapes=[]; distance=0
    for i,(lat,lon) in enumerate(points):
        if i:
            plat,plon=points[i-1]
            a=math.sin(math.radians(lat-plat)/2)**2+math.cos(math.radians(plat))*math.cos(math.radians(lat))*math.sin(math.radians(lon-plon)/2)**2
            distance+=12742000*math.asin(min(1,math.sqrt(a)))
        shapes.append(["riobus_osm_1499062007",lat,lon,i+1,round(distance/1000,5)])
    out["shapes.txt"]=table("shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled",shapes)
    date=lambda d:d.strftime("%Y%m%d")
    out["calendar.txt"]=table("service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date",[
        ["regular",0,1,1,1,1,1,1,date(start),date(end)],
        ["weekend_1100",0,0,0,0,0,1,1,date(start),date(end)]])
    holiday_set=holidays.country_holidays("CO",years=range(start.year,end.year+1))
    exceptions=[]; d=start
    while d<=end:
        if d in holiday_set and d.weekday()==0:
            exceptions.extend([["regular",date(d),1],["weekend_1100",date(d),1]])
            tomorrow=d+dt.timedelta(days=1)
            if tomorrow<=end:exceptions.append(["regular",date(tomorrow),2])
        elif d in holiday_set and d.weekday()<5:
            exceptions.append(["weekend_1100",date(d),1])
        d+=dt.timedelta(days=1)
    out["calendar_dates.txt"]=table("service_id,date,exception_type",exceptions)
    trips=[]; times=[]
    for service,departures in (("regular",["14:00:00","17:00:00"]),("weekend_1100",["11:00:00"])):
        for depart in departures:
            trip=service+"_"+depart[:2]
            trips.append(["karakali",service,trip,"riobus_osm_1499062007"])
            h,m=map(int,depart[:5].split(":"))
            arrive=f"{h+(m+45)//60:02d}:{(m+45)%60:02d}:00"
            times.extend([[trip,depart,depart,"puerta_de_oro_pier",1,0],
                          [trip,arrive,arrive,"puerta_de_oro_pier",2,round(distance/1000,5)]])
    out["trips.txt"]=table("route_id,service_id,trip_id,shape_id",trips)
    out["stop_times.txt"]=table("trip_id,arrival_time,departure_time,stop_id,stop_sequence,shape_dist_traveled",times)
    out["feed_info.txt"]=table("feed_publisher_name,feed_publisher_url,feed_lang,feed_start_date,feed_end_date",[
        ["ColombiaTransit","https://github.com/ColombiaTransit/gtfs-barranquilla-riobus","es",date(start),date(end)]])
    target=ROOT/"dist/gtfs-barranquilla-riobus.zip"
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target,"w",zipfile.ZIP_DEFLATED) as archive:
        for name,data in sorted(out.items()):archive.writestr(name,data)
    print(f"Generated {target}; {len(points)} points, {distance/1000:.2f} km")
if __name__=="__main__":
    today=dt.date.today()
    build(dt.date.fromisoformat(sys.argv[1]) if len(sys.argv)>1 else today,
          dt.date.fromisoformat(sys.argv[2]) if len(sys.argv)>2 else today+dt.timedelta(days=365))
