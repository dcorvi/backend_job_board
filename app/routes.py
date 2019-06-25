from app import app, db
from flask import request, jsonify
from app.models import Job

@app.route('/')
def index():
    return ''


@app.route('/api/save', methods=['GET', 'POST'])
def save():
    try:
        # get headers first
        # save through headers
        # jobtitle = request.headers.get('jobtitle')
        # company = request.headers.get('company')
        # city = request.headers.get('city')
        # state = request.headers.get('state')
        # zip = request.headers.get('zip')
        # descr = request.headers.get('descr')
        # jstatus = request.headers.get('jstatus')
        # link = request.headers.get('link')
        # duties = request.headers.get('duties')
        # requi = request.headers.get('requi')
        # post_date = request.headers.get('post_date')

        # save through parameters
        jobtitle = request.args.get('jobtitle')
        company = request.args.get('company')
        city = request.args.get('city')
        state = request.args.get('state')
        zip = request.args.get('zip')
        descr = request.args.get('descr')
        jstatus = request.args.get('jstatus')
        link = request.args.get('link')
        duties = request.args.get('duties')
        requi = request.args.get('requi')
        post_date = request.args.get('post_date')


        if not jobtitle and not company and not city and not state and not zip and not descr and not jstatus and not link and not duties and not requi and not post_date:
            return jsonify({ 'error #301': 'Invalid params' })

        # create an event
        job = Job(jobtitle=jobtitle, company=company, city=city, state=state, zip=zip, descr=descr, jstatus=jstatus, link=link, duties=duties, requi=requi, post_date=post_date)

        # add to stage and commit to db
        db.session.add(job)
        db.session.commit()

        return jsonify({ 'success': 'job saved' })
    except:
        return jsonify({ 'error #303': 'job could not be saved' })



@app.route('/api/retrieve', methods=['GET', 'POST'])
def retrieve():
    # try:
    jobtitle = request.headers.get('jobtitle')
    company = request.headers.get('company')
    city = request.headers.get('city')
    state = request.headers.get('state')
    zip = request.headers.get('zip')
    descr = request.headers.get('descr')
    jstatus = request.headers.get('jstatus')
    link = request.headers.get('link')
    duties = request.headers.get('duties')
    requi = request.headers.get('requi')
    post_date = request.headers.get('post_date')

    if jobtitle and company:
        results = Job.query.filter_by(jobtitle=jobtitle, company=company).all()
    elif not company and jobtitle:
        results = Job.query.filter_by(jobtitle=jobtitle).all()
    elif not jobtitle and company:
        results = Job.query.filter_by(company=company).all()
    elif not jobtitle and not company:
        results = Job.query.all()
    else:
        return jsonify({ 'error#304': 'Required params not included' })

    if not results:
        return jsonify({ 'success': 'No job matching that description.' })

    # remember that results is a list of db.Model objects
    parties = []

    for job in results:
        party = {
            'id': job.id,
            'jobtitle': job.jobtitle,
            'company': job.company,
            'city': job.city,
            'state': job.state,
            'zip': job.zip,
            'descr': job.descr,
            'jstatus': job.jstatus,
            'link': job.link,
            'duties': job.duties,
            'requi': job.requi,
            'post_date': job.post_date
        }

        parties.append(party)

    return jsonify(parties)

    # except:
    #     return jsonify({ 'error#305': 'something went wrong' })



@app.route('/api/delete', methods=['GET', 'POST'])
def delete():
    try:
        job_id = request.headers.get('job_id')

        job = Job.query.filter_by(id=job_id).first()

        if not job:
            return jsonify({ 'error#306': 'Job does not exist.'})

        db.session.delete(job)
        db.session.commit()

        return jsonify({ 'success': f'Item {job_id} deleted.'})

    except:
        return jsonify({ 'error#307': 'Could not delete job.' })
