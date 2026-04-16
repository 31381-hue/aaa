from models.cachorro_model import Cachorro
from config import db
import json
from flask import make_response, request

# 📋 GET - listar todos os cachorros
def get_cachorros():
    cachorros = Cachorro.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de cachorros cadastrados.',
            'dados': [c.to_dict() for c in cachorros]
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


 GET por ID
def get_cachorro_by_id(cachorro_id):
    cachorro = Cachorro.query.get(cachorro_id)

    if cachorro:
        response = make_response(
            json.dumps({
                'mensagem': 'Cachorro encontrado com sucesso.',
                'dados': cachorro.to_dict()
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Cachorro não encontrado.',
                'dados': {}
            }, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response


# POST - criar cachorro
def create_cachorro(cachorro_data):
    novo_cachorro = Cachorro(
        nome=cachorro_data['nome'],
        raca=cachorro_data['raca'],
        idade=cachorro_data['idade']
    )

    db.session.add(novo_cachorro)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Cachorro cadastrado com sucesso!',
            'cachorro': novo_cachorro.to_dict()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# PUT - atualizar cachorro
def update_cachorro(cachorro_id, data):
    cachorro = Cachorro.query.get(cachorro_id)

    if not cachorro:
        response = make_response(
            json.dumps({'mensagem': 'Cachorro não encontrado'}),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    cachorro.nome = data.get('nome', cachorro.nome)
    cachorro.raca = data.get('raca', cachorro.raca)
    cachorro.idade = data.get('idade', cachorro.idade)

    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Cachorro atualizado com sucesso!',
            'cachorro': cachorro.to_dict()
        })
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# DELETE - deletar cachorro
def delete_cachorro(cachorro_id):
    cachorro = Cachorro.query.get(cachorro_id)

    if not cachorro:
        response = make_response(
            json.dumps({'mensagem': 'Cachorro não encontrado'}),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(cachorro)
    db.session.commit()

    response = make_response(
        json.dumps({'mensagem': 'Cachorro deletado com sucesso!'})
    )
    response.headers['Content-Type'] = 'application/json'
    return response