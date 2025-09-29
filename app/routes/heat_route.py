from flask import Blueprint, render_template, redirect, url_for, session
from app.models import Crime
from app.utils.heat_utils import get_filtered_crimes, run_dbscan, build_heatmap_map
import numpy as np
import folium

heat_bp = Blueprint('heat', __name__)

@heat_bp.route('/heatmap', methods=['GET', 'POST'])
def heatmap():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    filters = session.get('filters', {})
    crimes = get_filtered_crimes(Crime, filters)
    coords = np.array([[c.lat, c.lon] for c in crimes if c.lat and c.lon])

    if len(coords) == 0:
        m = folium.Map(location=[34.05, -118.25], zoom_start=11)
    else:
        labels = run_dbscan(coords)
        m = build_heatmap_map(coords, labels)

    return render_template("heatmap.html", map_html=m._repr_html_())