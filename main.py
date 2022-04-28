from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route("/")
def list_candidates():
    """Главная страница приложения"""
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """Страница одного кандидата"""
    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template("card.html", candidate=candidate)
    else:
        abort(404)


@app.route("/skill/<string:skill_name>")
def get_candidates_by_skill(skill_name):
    """Поиск кандидатов по скилу"""
    candidates = utils.get_candidates_by_skill(slill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))


@app.route("/search/<string:candidate_name>")
def get_candidates_by_name(candidate_name):
    """Поиск кандидатов по имени"""
    candidates = utils.get_candidates_by_name(candidates_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


app.run()

