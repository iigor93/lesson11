from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route('/')
def index_view():
    """Список всех кандидатов"""
    candidates_list = utils.get_data_from_file()
    return render_template('list.html', candidates_list=candidates_list)


@app.route('/candidate/')
def candidate_empty():
    """Страница кандидата без номера"""
    return 'Введите номер кандидата в адресную строку, например /candidate/3'


@app.route('/candidate/<string>')
def candidate_string(string):
    """Страница кандидата с набором симовлов"""
    return f'Введите номер кандидата, а не строку {string}'


@app.route('/candidate/<int:uid>/')
def candidate(uid):
    """Страница кандидата"""
    candidate_data = utils.get_candidate(uid)
    if candidate_data is False:
        return 'нет кандидата с таким номером'
    return render_template('single.html', candidate_data=candidate_data)


@app.route('/search/')
def candidate_empty_search():
    """ Если имя пустое"""
    return 'Введите имя кандидата'


@app.route('/search/<string>/')
def candidate_search_by_name(string):
    """Страница поиска кандидата по имени"""
    candidate_data = utils.get_candidates_by_name(string)
    if len(candidate_data) == 0:
        return "Нет кандидатов с таким именем"
    list_len = len(candidate_data)
    return render_template('search.html', candidate_data=candidate_data, search_num=list_len)


@app.route('/skill/')
def candidate_skill_empty_search():
    """ Если навык пустое"""
    return 'Введите навык'


@app.route('/skill/<string>/')
def candidate_search_by_skill(string):
    """Страница поиска кандидата по Навыкам"""
    candidate_data = utils.get_candidates_by_skill(string)
    if len(candidate_data) == 0:
        return "Нет кандидатов с таким Навыком"
    list_len = len(candidate_data)
    return render_template('skill.html', candidate_data=candidate_data, search_num=list_len, skill=string.title())
