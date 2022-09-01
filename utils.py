import json

from candidate import Candidate


def load_candidates_from_json(path: str) -> list[Candidate]:
    arr = []
    data = None

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        id_ = item['id']
        name = item['name']
        picture = item['picture']
        position = item['position']
        gender = item['gender']
        age = item['age']
        skills = item['skills']
        arr.append(Candidate(id_, name, picture, position, gender, age, skills))

    return arr

def get_candidate(candidate_id: int, arr: list[Candidate]) -> Candidate:

    for item in arr:
       if item.id == condidate_id:
            return item

def get_candidates_by_name(candidate_name: str, arr: list[Candidate]) -> list[Candidate]:
    ret_arr = []

    for item in arr:
        if candidate_name in item.name:
            ret_arr.append(item)
    return ret_arr

def get_candidates_by_skill(skill_name: str, arr: list[Candidate]) -> list[Candidate]:

    ret_arr = []

    for item in arr:
        if skill_name in item.skills:
            ret_arr.append ( item )
    return ret_arr
