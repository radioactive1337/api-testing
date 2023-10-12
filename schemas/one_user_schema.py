one_user_schema = {
    "type": "object",
    "properties": {
        "first_name": {
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "null"
                }
            ]
        },
        "last_name": {
            "type": "string"
        },
        "company_id": {
            "anyOf": [
                {
                    "type": "integer"
                },
                {
                    "type": "null"
                }
            ]
        },
        "user_id": {
            "type": "integer"
        }
    },
    "required": [
        "last_name",
        "user_id"
    ]
}
