import json


def get_data_from_file():
    """загрузка данных из файла"""
    file_name = 'candidates.json'
    with open(file_name, 'r', encoding='utf-8') as file:
        file_data = json.load(file)
    return file_data


def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    file_data = get_data_from_file()
    return file_data


def get_candidate(candidate_id):
    """ возвращает одного кандидата по его id"""
    file_data = get_data_from_file()
    for candidate in file_data:
        if candidate_id == candidate['id']:
            return candidate
    return False


def get_candidates_by_name(candidate_name):
    file_data = get_data_from_file()
    candidate_list = []
    """возвращает кандидатов по имени"""
    for candidate in file_data:
        if candidate_name.strip().lower() in candidate['name'].strip().lower():
            candidate_list.append(candidate)
    return candidate_list


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    file_data = get_data_from_file()
    list_to_return = []
    for candidate in file_data:
        skills_list = candidate['skills'].split(',')
        for item in skills_list:
            if skill_name.strip().lower() == item.strip().lower():
                list_to_return.append(candidate)

    return list_to_return

