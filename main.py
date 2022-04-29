from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
import data_manager

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city = request.args.get('city-name')
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_city(city)
    else:
        mentor_details = data_manager.get_mentors()
    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')
    return render_template('mentors.html', mentors=mentor_details)


@app.route('/applicants', methods=['GET', 'POST'])
def applicants_list():
    if request.method == 'POST':
        data_manager.delete_applicant_by_email(request.form['email-ending'])
        return redirect(url_for('applicants_list'))
    applicants_details = data_manager.get_applicants()
    return render_template('applicants.html', applicants=applicants_details)


@app.route('/applicants-phone', methods=['GET', 'POST'])
def applicants_phone():
    applicant_name = request.form.get('applicant-name')
    applicant_email_ending = request.form.get('email-ending')
    if applicant_name:
        applicant_details = data_manager.get_applicant_data_by_name(applicant_name)
    else:
        applicant_details = data_manager.get_applicant_data_by_email_ending(applicant_email_ending)
    return render_template('applicant.html', applicants=applicant_details)


@app.route('/applicants/<code>', methods=['GET', 'POST'])
def edit_applicant_data(code):
    if request.method == 'POST':
        data_manager.update_applicant_phone_number(request.form['new-phone'], code)
        return redirect(url_for('edit_applicant_data', code=code))
    applicant_details = data_manager.get_applicant_data_by_code(code)
    return render_template('edit-applicant-data.html', code=code, applicants=applicant_details)


@app.route('/applicants/<code>/delete')
def delete_applicant(code):
    data_manager.delete_applicant_data(code)
    return redirect(url_for('applicants_list'))




if __name__ == '__main__':
    app.run(debug=True,
            port=8000)
