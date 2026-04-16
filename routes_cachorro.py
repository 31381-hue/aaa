from flask import Blueprint, request
from controllers.cachorro_controller import (
    get_cachorros,
    create_cachorro,
    get_cachorro_by_id,
    update_cachorro,
    delete_cachorro
)

# Blueprint no tema cachorro
cachorro_routes = Blueprint('cachorro_routes', __name__)

# GET - listar todos os cachorros
@cachorro_routes.route('/cachorros', methods=['GET'])
def cachorros_get():
    return get_cachorros()


# GET por ID
@cachorro_routes.route('/cachorros/<int:cachorro_id>', methods=['GET'])
def cachorro_get_by_id(cachorro_id):
    return get_cachorro_by_id(cachorro_id)


# POST - cadastrar cachorro
@cachorro_routes.route('/cachorros', methods=['POST'])
def cachorros_post():
    return create_cachorro(request.json)


# PUT - atualizar cachorro
@cachorro_routes.route('/cachorros/<int:cachorro_id>', methods=['PUT'])
def cachorros_put(cachorro_id):
    return update_cachorro(cachorro_id, request.json)


# DELETE - deletar cachorro
@cachorro_routes.route('/cachorros/<int:cachorro_id>', methods=['DELETE'])
def cachorros_delete(cachorro_id):
    return delete_cachorro(cachorro_id)
