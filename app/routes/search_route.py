from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models import Crime
from app.utils.search_utils import build_crime_query

search_bp = Blueprint('search', __name__)

@search_bp.route('/search',methods=['GET','POST'])
def search():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # Save filters to session
        session['filters'] = {
            'max_vict_age': request.form.get('max_vict_age'),
            'min_vict_age': request.form.get('min_vict_age'),
            'vict_sex': request.form.get('vict_sex'),
            'vict_descent': request.form.get('vict_descent'),
            'min_date': request.form.get('min_date'),
            'max_date': request.form.get('max_date'),
            'area_name': request.form.get('area_name'),
            'crm_cd_desc': request.form.get('crm_cd_desc'),
            'weapon_type': request.form.get('weapon_type'),
            'status': request.form.get('status'),
        }
        return redirect(url_for('search.search'))  # Redirect to GET for pagination

    # For GET: Retrieve filters from session
    filters = session.get('filters', {})

    # Extract page number from URL
    page = request.args.get('page', 1, type=int)
    per_page = 25

    
    query = build_crime_query(Crime, filters)
    results = query.paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('search.html', results=results, filters=filters, page=page, per_page=per_page)
