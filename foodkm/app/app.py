import responder


cors_params = {
    'allow_origins': ['*'],
    'allow_methods': ['*'],
    'allow_headers': ['*']
}

api = responder.API(cors=True, cors_params=cors_params)


@api.route("/upper")
async def upper(req, resp):
    req_json = await req.media()
    name = req_json['data']['name'].upper()
    resp_json = {'data': {'name': name}}
    resp.media = resp_json


def run():
    api.run()
