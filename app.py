import os
from flask import Flask, render_template, request, redirect, url_for, Response, json

app = Flask(__name__)


def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE,  \
          GET,POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response

app.after_request(add_cors_headers)

@app.route('/analyze_utterance', methods=['GET'])
def anticorruption_analysis():
    output = {
        "caso": 213141,
        "status": "caso_completo",
        "corrupcion" : [
                { "tipo_corrupción_1": 0.99 },
                { "tipo_corrupción_2": 0.99 },
                { "tipo_corrupción_3": 0.99 },
                { "tipo_corrupción_4": 0.99 },
                { "tipo_corrupción_5": 0.99 },
                { "tipo_corrupción_6": 0.99 },
                { "tipo_corrupción_7": 0.99 },
                { "tipo_corrupción_8": 0.99 },
                { "tipo_corrupción_9": 0.99 },
                { "tipo_corrupción_10": 0.99 }
            ],
            "contrato": "identificador_OpenContracting",
            "entidades_identificadas": [
                { "tipo": "institución", "texto": "texto" },
                { "tipo": "institución", "texto": "texto" },
                { "tipo": "proveedor", "texto": "texto" },
                { "tipo": "proveedoor", "texto": "texto" }
            ],
            "preguntas_pendientes" : [
                { "persona": [] },
                { "empresa": [] },
                { "contrato": [] },
                { "institución": [] },
            ],
            "sustantivos_pendientes": [
                "sustantivo_1",
                "sustantivo_2",
                "sustantivo_3"
            ]
    }
    return response = app.response_class( response=json.dumps(output), mimetype='application/json' )


@app.route('/analyze_context', methods=['GET'])
def anticorruption_analysis():
    output = {
        "probabilidad":0.91,
        "tipo corrupción 1": {
            "probabilidad": 0.89,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 2": {
            "probabilidad": 0.25,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 3": {
            "probabilidad": 0.85,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 4": {
            "probabilidad": 0.51,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 5": {
            "probabilidad": 0.23,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 6": {
            "probabilidad": 0.60,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 7": {
            "probabilidad": 0.90,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 8": {
            "probabilidad": 0.95,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 9": {
            "probabilidad": 0.91,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
        "tipo corrupción 10": {
            "probabilidad": 0.85,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad"}}
        },
    }
    return response = app.response_class( response=json.dumps(output), mimetype='application/json' )
