import os
from flask import Flask, render_template, request, redirect, url_for, Response, jsonify

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
    return jsonify(output)


@app.route('/analyze_context', methods=['GET'])
def analyze_context():
    output = {
        "probabilidad":0.91,
        "Soborno": {
            "probabilidad": 0.89,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":20, "unidades":"unidad", "porcentaje":0.15}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":131, "unidades":"unidad", "porcentaje":1.00}}
        },
        "Desvio de Recursos": {
            "probabilidad": 0.25,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":80, "unidades":"unidad", "porcentaje":0.4}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":200, "unidades":"unidad", "porcentaje":1.0}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":120, "unidades":"unidad", "porcentaje":0.6}}
        },
        "Abuso de funciones": {
            "probabilidad": 0.85,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":100, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":34, "unidades":"unidad", "porcentaje":0.33}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":67, "unidades":"unidad", "porcentaje":0.66}},
            "indicador_4": {"tipo":"kpi", "datos":{"valor":67, "unidades":"unidad", "porcentaje":0.66}}
        },
        "Colusión": {
            "probabilidad": 0.51,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":250, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":200, "unidades":"unidad", "porcentaje":0.8}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":125, "unidades":"unidad", "porcentaje":0.5}},
            "indicador_4": {"tipo":"kpi", "datos":{"valor":75, "unidades":"unidad", "porcentaje":0.3}},
            "indicador_5": {"tipo":"kpi", "datos":{"valor":175, "unidades":"unidad", "porcentaje":0.7}}
        },
        "Conspiración para cometer actos de corrupción": {
            "probabilidad": 0.23,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":150, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":61, "unidades":"unidad", "porcentaje":0.41}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":20, "unidades":"unidad", "porcentaje":0.13}}
        },
        "Tráfico de influencia": {
            "probabilidad": 0.60,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":1000, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":600, "unidades":"unidad", "porcentaje":0.60}},
        },
        "Enriquecimiento Oculto": {
            "probabilidad": 0.90,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":800, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":430, "unidades":"unidad", "porcentaje":0.54}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":240, "unidades":"unidad", "porcentaje":0.3}}
        },
        "Obstrucción de Justicia": {
            "probabilidad": 0.95,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":130, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":96, "unidades":"unidad", "porcentaje":0.74}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":58, "unidades":"unidad", "porcentaje":0.45}}
        },
        "Uso ilegal de información falsa o confidencial": {
            "probabilidad": 0.91,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":250, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":200, "unidades":"unidad", "porcentaje":0.8}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":125, "unidades":"unidad", "porcentaje":0.5}},
            "indicador_4": {"tipo":"kpi", "datos":{"valor":75, "unidades":"unidad", "porcentaje":0.3}},
            "indicador_5": {"tipo":"kpi", "datos":{"valor":175, "unidades":"unidad", "porcentaje":0.7}}
        },
        "Nepotismo": {
            "probabilidad": 0.85,
            "indicador_1": {"tipo":"kpi", "datos":{"valor":100, "unidades":"unidad", "porcentaje":1.00}},
            "indicador_2": {"tipo":"kpi", "datos":{"valor":34, "unidades":"unidad", "porcentaje":0.33}},
            "indicador_3": {"tipo":"kpi", "datos":{"valor":67, "unidades":"unidad", "porcentaje":0.66}},
            "indicador_4": {"tipo":"kpi", "datos":{"valor":67, "unidades":"unidad", "porcentaje":0.66}}
        },
    }
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)