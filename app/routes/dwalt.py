from flask import Blueprint, render_template, request

dwalt_bp = Blueprint('dwalt', __name__)

@dwalt_bp.route('/')
def dwalt_home():
    return render_template('dwalt_env.html')

@dwalt_bp.route('/smartSwap')
def smart_swap():
    'detector de id para redirecionamento interno ou externo do autorizador'