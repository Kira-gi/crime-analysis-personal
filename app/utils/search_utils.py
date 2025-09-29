def build_crime_query(Crime, filters):
    query = Crime.query

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

    return query