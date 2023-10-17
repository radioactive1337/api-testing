schema = {
    "type": "object",
    "properties": {
        "detail": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "loc": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "msg": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    }
                },
                "required": [
                    "loc",
                    "msg",
                    "type"
                ]
            }
        }
    },
    "required": [
        "detail"
    ]
}
