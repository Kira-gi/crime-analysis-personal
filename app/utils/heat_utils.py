from sklearn.cluster import DBSCAN
import numpy as np
from geopy.distance import geodesic
from shapely.geometry import MultiPoint
import folium
from folium.plugins import HeatMap

def get_filtered_crimes(Crime, filters):
    query = Crime.query.filter(Crime.lat.isnot(None), Crime.lon.isnot(None))

    if filters.get('max_vict_age') and filters['max_vict_age'].isdigit():
        query = query.filter(Crime.vict_age <= int(filters['max_vict_age']))
    if filters.get('min_vict_age') and filters['min_vict_age'].isdigit():
        query = query.filter(Crime.vict_age >= int(filters['min_vict_age']))
    if filters.get('vict_sex'):
        query = query.filter(Crime.vict_sex.ilike(f"%{filters['vict_sex']}%"))
    if filters.get('vict_descent'):
        query = query.filter(Crime.vict_descent.ilike(f"%{filters['vict_descent']}%"))
    if filters.get('min_date'):
        query = query.filter(Crime.date_occ >= filters['min_date'])
    if filters.get('max_date'):
        query = query.filter(Crime.date_occ <= filters['max_date'])
    if filters.get('area_name'):
        query = query.filter(Crime.area_name.ilike(f"%{filters['area_name']}%"))
    if filters.get('crm_cd_desc'):
        query = query.filter(Crime.crm_cd_desc.ilike(f"%{filters['crm_cd_desc']}%"))
    if filters.get('weapon_type'):
        query = query.filter(Crime.weapon_type.ilike(f"%{filters['weapon_type']}%"))
    if filters.get('status'):
        query = query.filter(Crime.status == filters['status'])
    return query.all() # Use .limit(XXX) to limit map display

def run_dbscan(coords, eps=0.005, min_samples=5):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)
    return db.labels_


def build_heatmap_map(coords, labels):
    m = folium.Map(location=[34.05, -118.25], zoom_start=11)
    core_points = coords[labels != -1]
    HeatMap(core_points).add_to(m)

    unique_labels = set(labels)

    for label in unique_labels:
        if label == -1:
            continue
        cluster_points = coords[labels == label]
        center_lat = cluster_points[:, 0].mean()
        center_lon = cluster_points[:, 1].mean()
        center = (center_lat, center_lon)
        radius = max(geodesic(center, (lat, lon)).meters for lat, lon in cluster_points)

        folium.Marker(
            location=[center_lat, center_lon],
            icon=folium.Icon(color='red', icon='info-sign'),
            popup=f'Cluster {label}'
        ).add_to(m)

        folium.Circle(
            location=center,
            radius=radius,
            color='black',
            fill=True,
            fill_opacity=0.10,
            popup=f'Cluster {label}, Radius ≈ {int(radius)}m'
        ).add_to(m)

    return m
